# -*- coding: utf-8 -*-
"""course_learn_content 服务单测 — 预置 (seeded) 数据路径.

覆盖:
- _build_from_seeded: 预置 lecture.concepts / lecture.exercises 优先于启发式
- _normalize_exercises: 题型/答案归一化与脏数据过滤
- _convert_nodes_to_tree: nodes/edges -> {name, children} 树
- get_subchapter_content: 父章节有预置内容时走快速通道, 不调 LLM
"""
from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Any

import pytest

from app.services import course_learn_content as svc


@pytest.fixture(autouse=True)
def _clear_cache():
    """服务层的进程内缓存会跨测试串结果, 每个用例前清空."""
    svc._CACHE.clear()
    yield
    svc._CACHE.clear()


# ── 测试用的轻量 ORM 替身 ──

@dataclass
class FakeSub:
    id: str = "sub-1"
    title: str = "变量与数据类型"
    transcript: str = ""
    bvid: str = ""
    cid: int = 0


@dataclass
class FakeChapter:
    id: str = "ch-1"
    title: str = "变量与数据类型"
    lecture: dict | None = None
    mindmap: dict | None = None


@dataclass
class FakeCourse:
    id: str = "course-1"
    title: str = "Java编程入门"
    description: str = ""


def _seeded_lecture() -> dict[str, Any]:
    return {
        "blocks": [
            {"kind": "h2", "text": "本节概览：变量"},
            {"kind": "p", "text": "变量是内存中的存储空间。"},
            {"kind": "list", "items": ["int", "double"]},
            {"kind": "code", "lang": "java", "text": "int age = 18;"},
            {"kind": "callout", "tone": "tip", "text": "先敲代码再看解析。"},
            {"kind": "summary", "text": "掌握八大基本类型。"},
        ],
        "concepts": [
            {"term": "变量", "level": "core", "definition": "存储空间",
             "example": "int age = 18;"},
            {"term": "隐式转换", "level": "bad-level", "definition": "小转大"},
        ],
        "exercises": [
            {"type": "choice", "question": "哪个是合法标识符?",
             "options": ["2name", "userName"], "answer": 1, "explanation": "数字不能开头。"},
            {"type": "bool", "question": "int i = (int) 3.99 后 i 为 3。",
             "answer": True},
            {"type": "fill", "question": "long 字面量后缀是?", "answer": "L"},
        ],
    }


def _seeded_mindmap() -> dict[str, Any]:
    return {
        "nodes": [
            {"id": "root", "label": "变量", "level": 0},
            {"id": "n1", "label": "基本类型", "level": 1},
            {"id": "n1a", "label": "int", "level": 2},
            {"id": "n2", "label": "转换", "level": 1},
        ],
        "edges": [
            {"from": "root", "to": "n1"},
            {"from": "n1", "to": "n1a"},
            {"from": "root", "to": "n2"},
        ],
    }


class TestBuildFromSeeded:
    def test_curated_concepts_and_exercises_win(self):
        out = svc._build_from_seeded(_seeded_lecture(), _seeded_mindmap(), "变量")
        # 预置 concepts 生效 (而不是从 h2 标题启发式抽取)
        assert [c["term"] for c in out["concepts"]] == ["变量", "隐式转换"]
        # level 非法值被归一化为 basic
        assert out["concepts"][1]["level"] == "basic"
        # 预置 exercises 生效且被归一化
        assert len(out["exercises"]) == 3
        choice = out["exercises"][0]
        assert choice["answer"] == 1 and isinstance(choice["answer"], int)
        assert out["exercises"][1]["answer"] is True
        assert out["exercises"][2]["answer"] == "L"

    def test_transcript_renders_blocks(self):
        out = svc._build_from_seeded(_seeded_lecture(), _seeded_mindmap(), "变量")
        html = out["transcript"]
        assert "<h4>本节概览：变量</h4>" in html
        assert "<p>变量是内存中的存储空间。</p>" in html
        assert "<ul><li>int</li><li>double</li></ul>" in html
        assert "<pre><code" in html and "int age = 18;" in html
        assert "callout callout-tip" in html
        assert "<strong>小结：</strong>" in html

    def test_mindmap_tree_conversion(self):
        out = svc._build_from_seeded(_seeded_lecture(), _seeded_mindmap(), "变量")
        mm = out["mindMap"]
        assert mm["name"] == "变量"
        l1 = {c["name"]: c["children"] for c in mm["children"]}
        assert l1["基本类型"] == [{"name": "int", "children": []}]
        assert l1["转换"] == []

    def test_fallback_to_heuristic_without_curated(self):
        lecture = {"blocks": [{"kind": "h2", "text": "变量"}]}
        out = svc._build_from_seeded(lecture, None, "变量")
        # 无预置 concepts -> 从标题抽取
        assert out["concepts"] and out["concepts"][0]["term"] == "变量"
        # 无预置 exercises -> 启发式合成 (至少 1 道)
        assert out["exercises"]
        assert out["mindMap"] in (None, {})


class TestNormalizeExercises:
    def test_dirty_items_are_dropped_or_fixed(self):
        raw = [
            {"type": "choice", "question": "ok?", "options": ["a", "b"], "answer": "1"},
            {"type": "choice", "question": "no options"},   # choice 缺选项 -> 丢弃
            {"type": "weird", "question": "q"},             # 非法题型 -> 回退 choice 后仍缺选项 -> 丢弃
            {"question": ""},
            "not-a-dict",
        ]
        out = svc._normalize_exercises(raw)
        assert len(out) == 1
        assert out[0]["answer"] == 1          # "1" -> int


class TestGetSubchapterContentFastPath:
    def test_seeded_chapter_short_circuits_llm(self, monkeypatch):
        async def _boom(*a, **kw):  # LLM 不应被调用
            raise AssertionError("LLM should not be called on seeded path")

        monkeypatch.setattr(svc, "_generate_all", _boom)
        course = FakeCourse()
        chapter = FakeChapter(lecture=_seeded_lecture(), mindmap=_seeded_mindmap())
        sub = FakeSub()

        out = asyncio.run(svc.get_subchapter_content(course, chapter, sub))
        assert out["source"] == "demo_seeder"
        assert out["is_skeleton"] is False
        assert "变量是内存中的存储空间" in out["transcript"]
        assert out["mindMap"]["name"] == "变量"
        assert len(out["concepts"]) == 2

    def test_subchapter_transcript_used_as_base_text_without_seed(self, monkeypatch):
        """无预置章节内容时, 小节自带 transcript 作为 LLM 的 base_text."""
        captured = {}

        async def _fake_generate(**kw):
            captured.update(kw)
            return {"transcript": "<p>gen</p>", "concepts": [], "mindMap": None,
                    "exercises": []}

        monkeypatch.setattr(svc, "_generate_all", _fake_generate)
        course = FakeCourse()
        chapter = FakeChapter(lecture=None, mindmap=None)
        sub = FakeSub(transcript="小节自带文字稿")

        out = asyncio.run(svc.get_subchapter_content(course, chapter, sub,
                                                     force_refresh=True))
        assert captured["base_text"] == "小节自带文字稿"
        assert out["source"] == "transcript"

    def test_seeded_chapter_beats_subchapter_transcript(self, monkeypatch):
        """文档化的优先级: 父章节预置内容 (0) 高于小节 transcript (1)."""
        async def _boom(*a, **kw):
            raise AssertionError("LLM should not be called on seeded path")

        monkeypatch.setattr(svc, "_generate_all", _boom)
        course = FakeCourse()
        chapter = FakeChapter(lecture=_seeded_lecture(), mindmap=_seeded_mindmap())
        sub = FakeSub(transcript="小节自带文字稿")

        out = asyncio.run(svc.get_subchapter_content(course, chapter, sub))
        assert out["source"] == "demo_seeder"
        assert "变量是内存中的存储空间" in out["transcript"]


if __name__ == "__main__":
    pytest.main([__file__, "-q"])
