# -*- coding: utf-8 -*-
"""校验数据集：python validate_dataset.py —— 全部通过输出 OK"""
import json, sys
from collections import Counter
from pathlib import Path

DS = Path(__file__).resolve().parent / "dataset" / "star_eval_v1.jsonl"
EXPECT = {"知识问答": 12, "逻辑推理": 13, "代码生成": 12, "安全合规": 10, "中文特性": 12, "多轮上下文": 5}
cnt, errs, ids = Counter(), [], set()

for ln, line in enumerate(DS.read_text(encoding="utf-8").splitlines(), 1):
    if not line.strip():
        continue
    try:
        it = json.loads(line)
    except Exception as e:
        errs.append(f"第{ln}行 JSON 解析失败: {e}")
        continue
    if it["id"] in ids:
        errs.append(f"第{ln}行 id 重复: {it['id']}")
    ids.add(it["id"])
    cnt[it["dimension"]] += 1
    if "multi_round" not in it:
        for k in ("instruction", "reference_answer", "scoring", "evaluator"):
            if k not in it:
                errs.append(f"第{ln}行 {it.get('id')} 缺字段 {k}")
        try:
            json.loads(it["scoring"])
        except Exception:
            errs.append(f"第{ln}行 {it['id']} 的 scoring 不是合法 JSON（多半是引号没转义）")
    if it["evaluator"] in ("exec", "judge+exec"):
        for k in ("language", "test_code"):
            if k not in it:
                errs.append(f"第{ln}行 {it['id']} 代码题缺 {k}")

for d, n in EXPECT.items():
    if cnt[d] != n:
        errs.append(f"{d} 题数 {cnt[d]}，应为 {n}")

print("\n".join(errs) if errs else f"OK 共 {sum(cnt.values())} 题 " + str(dict(cnt)))
sys.exit(1 if errs else 0)
