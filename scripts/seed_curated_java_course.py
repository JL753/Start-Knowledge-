# -*- coding: utf-8 -*-
"""为 course_58507604_fcd8_4fcd_9746_ (Java编程入门, B站 BV17F411T7Ao) 写入
预置的 AI 讲义 / 概念 / 思维导图 / 练习, 并把每个小节对齐到真实视频分 P.

为什么需要这个脚本
==================
`course-learn.html` 的四件套 (transcript/concepts/mindMap/exercises) 依赖
``/api/courses/courses/{cid}/subchapters/{sid}/content``. 服务层优先走
"父章节已预置 lecture/mindmap" 的快速通道 (不调 LLM, ~5ms).

之前的问题:
  1. seeder 导入的小节 cid=0/page=1, 前端检测到空 cid 会用 B 站 200 个分 P
     重排目录, 小节 id 变成 sub-N, 后端 404 → 讲义/导图全部空白.
  2. 通用脚本 seed_course_learn_content.py 生成的讲义/导图是模板套话
     ("核心概念/关键步骤" + "XX 的定义"), 演示效果差.

本脚本写入手工整理的 Java 课程内容:
  - chapters.lecture  = {blocks, concepts, exercises}   (concepts/exercises
    由 app.services.course_learn_content._build_from_seeded 优先采用)
  - chapters.mindmap  = {nodes, edges}                   (真实 Java 知识树)
  - subchapters       = bvid/cid/page/duration 对齐真实分 P

用法:
    python scripts/seed_curated_java_course.py           # 幂等, 已写则跳过
    python scripts/seed_curated_java_course.py --force   # 强制重写
"""
from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_PROJECT_ROOT))

from sqlalchemy import select  # noqa: E402
from sqlalchemy.orm import selectinload  # noqa: E402

from app.core.database import get_sessionmaker  # noqa: E402
from app.models.course import Chapter, Course, SubChapter  # noqa: E402

COURSE_ID = "course_58507604_fcd8_4fcd_9746_"
BVID = "BV17F411T7Ao"
CURATED_VERSION = "curated-java-v2"

# 每章: 小节对齐的分 P + 讲义 + 概念 + 练习 + 思维导图
# page/cid/duration 来自 /api/bilibili/parse 的真实数据 (2026-09 抓取)
CHAPTERS: dict[str, dict] = {

    # ── 第 1 章 Java世界初探 ──────────────────────────────────────────
    "ch_58507604_fcd8_4f_0": {
        "video": {"page": 1, "cid": 25761288170, "duration": 500,
                  "title": "Java入门-01-Java学习介绍"},
        "lecture": {
            "blocks": [
                {"kind": "h2", "text": "本节概览：Java 是什么"},
                {"kind": "p", "text":
                    "Java 是 1995 年由 Sun 公司（后被 Oracle 收购）推出的面向对象编程语言。"
                    "它以「一次编写，到处运行」著称：源代码编译成与平台无关的字节码"
                    "（.class 文件），由各平台上的 Java 虚拟机（JVM）解释执行。"},
                {"kind": "h2", "text": "三个关键角色：JDK / JRE / JVM"},
                {"kind": "list", "items": [
                    "JVM（Java Virtual Machine）：虚拟机，负责执行字节码，是跨平台的核心。",
                    "JRE（Java Runtime Environment）：运行环境 = JVM + 核心类库，只想运行程序装它即可。",
                    "JDK（Java Development Kit）：开发工具包 = JRE + 编译器 javac + 调试工具，写代码必装。",
                ]},
                {"kind": "h2", "text": "第一个程序：HelloWorld"},
                {"kind": "code", "lang": "java", "text":
                    "public class HelloWorld {\n"
                    "    public static void main(String[] args) {\n"
                    "        System.out.println(\"Hello, World!\");\n"
                    "    }\n"
                    "}"},
                {"kind": "p", "text":
                    "编译执行两步：javac HelloWorld.java 生成字节码，java HelloWorld 由 JVM 运行。"
                    "文件名必须与 public 类名完全一致（含大小写）。"},
                {"kind": "h2", "text": "学习路线建议"},
                {"kind": "list", "ordered": True, "items": [
                    "基础语法：变量、数据类型、运算符、流程控制。",
                    "面向对象：类与对象、封装、继承、多态。",
                    "常用 API：字符串、集合、异常、I/O。",
                    "实战项目：学生管理系统 → 打通前面所有知识点。",
                ]},
                {"kind": "callout", "tone": "tip", "text":
                    "本节视频时长 8 分 20 秒，先看完再往下学，环境装好后亲手敲一遍 HelloWorld。"},
                {"kind": "summary", "text":
                    "Java 通过「字节码 + JVM」实现跨平台；JDK ⊃ JRE ⊃ JVM；"
                    "开发第一步是配置 JDK 并跑通 HelloWorld。"},
            ],
            "concepts": [
                {"term": "JVM", "level": "core",
                 "definition": "Java 虚拟机，负责加载并执行字节码，是 Java 跨平台能力的核心。",
                 "example": "同一份 .class 文件可在 Windows / Linux / macOS 的 JVM 上运行。"},
                {"term": "JDK", "level": "core",
                 "definition": "Java 开发工具包，= JRE + javac 编译器等开发工具，编写 Java 程序的必备环境。",
                 "example": "javac HelloWorld.java 中的 javac 就来自 JDK。"},
                {"term": "JRE", "level": "basic",
                 "definition": "Java 运行环境，= JVM + 核心类库，只运行不开发时装它即可。"},
                {"term": "字节码", "level": "core",
                 "definition": "Java 源码编译产生的中间代码（.class 文件），与操作系统无关，由 JVM 解释执行。",
                 "example": "HelloWorld.java --javac--> HelloWorld.class --JVM--> 输出结果"},
                {"term": "跨平台", "level": "basic",
                 "definition": "同一份程序无需修改即可在不同操作系统运行，原理是各平台提供各自的 JVM。",
                 "example": "Write once, run anywhere."},
            ],
            "exercises": [
                {"type": "choice",
                 "question": "下列关于 JDK、JRE、JVM 的包含关系，正确的是？",
                 "options": ["JRE ⊃ JDK ⊃ JVM", "JDK ⊃ JRE ⊃ JVM",
                             "JVM ⊃ JDK ⊃ JRE", "三者互相独立"],
                 "answer": 1,
                 "explanation": "JDK = JRE + 开发工具，JRE = JVM + 核心类库，所以 JDK ⊃ JRE ⊃ JVM。"},
                {"type": "bool",
                 "question": "Java 实现跨平台的原因是源代码可以直接在任意操作系统上运行。",
                 "answer": False,
                 "explanation": "跨平台靠的是字节码 + 各平台 JVM，源代码必须先编译成 .class 字节码。"},
                {"type": "fill",
                 "question": "Java 源文件编译后生成的中间代码文件扩展名是 .______。",
                 "answer": "class",
                 "explanation": "javac 编译生成 HelloWorld.class 字节码文件。"},
                {"type": "choice",
                 "question": "只想在自己的电脑上运行别人写好的 Java 程序，最少需要安装？",
                 "options": ["JDK", "JRE", "JVM", "Eclipse"],
                 "answer": 1,
                 "explanation": "运行只需要 JRE（含 JVM 与核心类库）；开发才需要 JDK。"},
            ],
        },
        "mindmap": {
            "nodes": [
                {"id": "root", "label": "Java 世界初探", "level": 0},
                {"id": "n1", "label": "语言定位", "level": 1},
                {"id": "n1a", "label": "面向对象", "level": 2},
                {"id": "n1b", "label": "1995 年诞生", "level": 2},
                {"id": "n2", "label": "跨平台原理", "level": 1},
                {"id": "n2a", "label": "字节码 .class", "level": 2},
                {"id": "n2b", "label": "各平台 JVM", "level": 2},
                {"id": "n3", "label": "环境搭建", "level": 1},
                {"id": "n3a", "label": "JDK 下载安装", "level": 2},
                {"id": "n3b", "label": "环境变量配置", "level": 2},
                {"id": "n3c", "label": "IDEA 编辑器", "level": 2},
                {"id": "n4", "label": "HelloWorld", "level": 1},
                {"id": "n4a", "label": "javac 编译", "level": 2},
                {"id": "n4b", "label": "java 运行", "level": 2},
                {"id": "n4c", "label": "类名=文件名", "level": 2},
            ],
            "edges": [
                {"from": "root", "to": "n1"}, {"from": "n1", "to": "n1a"},
                {"from": "n1", "to": "n1b"},
                {"from": "root", "to": "n2"}, {"from": "n2", "to": "n2a"},
                {"from": "n2", "to": "n2b"},
                {"from": "root", "to": "n3"}, {"from": "n3", "to": "n3a"},
                {"from": "n3", "to": "n3b"}, {"from": "n3", "to": "n3c"},
                {"from": "root", "to": "n4"}, {"from": "n4", "to": "n4a"},
                {"from": "n4", "to": "n4b"}, {"from": "n4", "to": "n4c"},
            ],
        },
    },

    # ── 第 2 章 变量与数据类型 ────────────────────────────────────────
    "ch_58507604_fcd8_4f_1": {
        "video": {"page": 19, "cid": 585584311, "duration": 459,
                  "title": "Java基础概念-04-变量-基本用法"},
        "lecture": {
            "blocks": [
                {"kind": "h2", "text": "本节概览：变量是内存中的一块存储空间"},
                {"kind": "p", "text":
                    "变量用来在程序运行过程中存储数据。定义格式：数据类型 变量名 = 初始化值。"
                    "变量名属于标识符，要遵守命名规范。"},
                {"kind": "h2", "text": "八大基本数据类型"},
                {"kind": "list", "items": [
                    "整数（4 种）：byte(1字节) < short(2) < int(4, 默认) < long(8, 字面量加 L)。",
                    "浮点（2 种）：float(4, 字面量加 F) < double(8, 默认)。",
                    "字符：char(2 字节)，单引号单个字符，本质是无符号整数。",
                    "布尔：boolean，只有 true / false 两个取值。",
                ]},
                {"kind": "h2", "text": "类型转换"},
                {"kind": "code", "lang": "java", "text":
                    "int i = 10;\n"
                    "double d = i;            // 隐式转换: 小 -> 大, 自动\n"
                    "int j = (int) 3.99;      // 强制转换: 大 -> 小, 可能丢精度, j = 3\n"
                    "byte b = 10; b = (byte)(b + 1);  // 运算时先提升为 int"},
                {"kind": "h2", "text": "常见误区"},
                {"kind": "list", "items": [
                    "long 类型字面量不加 L，整数默认按 int 处理，大数会编译报错。",
                    "float f = 13.14 直接写会报错——13.14 是 double，需写成 13.14F。",
                    "变量未初始化就使用，编译不通过。",
                ]},
                {"kind": "callout", "tone": "warning", "text":
                    "字符串 String 是引用类型不是基本类型，但用起来和基本类型一样频繁。"},
                {"kind": "summary", "text":
                    "8 种基本类型按取值范围从小到大可自动隐式转换；反向必须强转并承担精度损失风险。"},
            ],
            "concepts": [
                {"term": "变量", "level": "core",
                 "definition": "内存中的一块存储空间，存储的数据可以在程序运行中改变。",
                 "example": "int age = 18;"},
                {"term": "八大基本类型", "level": "core",
                 "definition": "byte/short/int/long/float/double/char/boolean 共 8 种，其余全是引用类型。",
                 "example": "整数默认 int，小数默认 double。"},
                {"term": "隐式转换", "level": "basic",
                 "definition": "取值范围小的类型赋给大的类型时自动完成，如 int → double。",
                 "example": "double d = 100;"},
                {"term": "强制转换", "level": "core",
                 "definition": "取值范围大的类型赋给小的类型必须强转，可能丢失精度。",
                 "example": "int i = (int) 3.99; // i = 3"},
                {"term": "标识符", "level": "basic",
                 "definition": "给类、变量、方法起名的规则：字母数字下划线美元符组成，数字不开头，不能用关键字。",
                 "example": "userName 合法；2name、class 非法。"},
            ],
            "exercises": [
                {"type": "choice",
                 "question": "下列哪个变量定义是合法的？",
                 "options": ["float f = 13.14;", "long l = 10000000000;",
                             "double d = 13.14;", "char c = \"a\";"],
                 "answer": 2,
                 "explanation": "A 应写 13.14F；B 超过 int 范围应加 L；D 字符用单引号；C 正确。"},
                {"type": "bool",
                 "question": "int i = (int) 3.99; 执行后 i 的值是 3，体现了强制转换会丢失精度。",
                 "answer": True,
                 "explanation": "浮点强转整数直接截断小数部分，不做四舍五入。"},
                {"type": "fill",
                 "question": "定义 long 类型变量并赋一个大整数时，字面量末尾要加字母 ______。",
                 "answer": "L",
                 "explanation": "long l = 10000000000L; 整数字面量默认是 int。"},
                {"type": "choice",
                 "question": "byte b = 10; b = b + 1; 会编译报错，原因是？",
                 "options": ["byte 不能参与运算", "b + 1 的结果是 int，赋回 byte 需要强转",
                             "1 只能赋给 int", "b 没有初始化"],
                 "answer": 1,
                 "explanation": "byte/short/char 参与运算会先提升为 int，需写成 b = (byte)(b + 1)。"},
            ],
        },
        "mindmap": {
            "nodes": [
                {"id": "root", "label": "变量与数据类型", "level": 0},
                {"id": "n1", "label": "变量", "level": 1},
                {"id": "n1a", "label": "定义与赋值", "level": 2},
                {"id": "n1b", "label": "标识符规范", "level": 2},
                {"id": "n2", "label": "基本类型", "level": 1},
                {"id": "n2a", "label": "整数 byte~long", "level": 2},
                {"id": "n2b", "label": "浮点 float/double", "level": 2},
                {"id": "n2c", "label": "char / boolean", "level": 2},
                {"id": "n3", "label": "引用类型", "level": 1},
                {"id": "n3a", "label": "String 字符串", "level": 2},
                {"id": "n3b", "label": "数组/类/接口", "level": 2},
                {"id": "n4", "label": "类型转换", "level": 1},
                {"id": "n4a", "label": "隐式: 小→大", "level": 2},
                {"id": "n4b", "label": "强制: 大→小", "level": 2},
                {"id": "n4c", "label": "运算时提升 int", "level": 2},
            ],
            "edges": [
                {"from": "root", "to": "n1"}, {"from": "n1", "to": "n1a"},
                {"from": "n1", "to": "n1b"},
                {"from": "root", "to": "n2"}, {"from": "n2", "to": "n2a"},
                {"from": "n2", "to": "n2b"}, {"from": "n2", "to": "n2c"},
                {"from": "root", "to": "n3"}, {"from": "n3", "to": "n3a"},
                {"from": "n3", "to": "n3b"},
                {"from": "root", "to": "n4"}, {"from": "n4", "to": "n4a"},
                {"from": "n4", "to": "n4b"}, {"from": "n4", "to": "n4c"},
            ],
        },
    },

    # ── 第 3 章 流程控制逻辑 ──────────────────────────────────────────
    "ch_58507604_fcd8_4f_2": {
        "video": {"page": 39, "cid": 25761351515, "duration": 261,
                  "title": "判断和循环-01-流程控制语句-顺序结构"},
        "lecture": {
            "blocks": [
                {"kind": "h2", "text": "本节概览：顺序 / 分支 / 循环"},
                {"kind": "p", "text":
                    "流程控制决定程序「按什么顺序执行代码」。最基本的是顺序结构（从上到下逐行执行），"
                    "在此基础上通过分支和循环改变执行路径。"},
                {"kind": "h2", "text": "分支结构"},
                {"kind": "list", "items": [
                    "if 三种格式：单分支 / if-else / if-else if-else，适合区间判断。",
                    "switch：适合等值匹配；JDK 14 起支持箭头语法，case 不再默认穿透。",
                    "三元运算符可看作 if-else 的表达式简写：int max = a > b ? a : b;",
                ]},
                {"kind": "h2", "text": "循环结构"},
                {"kind": "code", "lang": "java", "text":
                    "for (int i = 1; i <= 100; i++) { sum += i; }   // 已知次数\n"
                    "while (scanner.hasNext()) { ... }               // 未知次数\n"
                    "do { menu(); } while (choice != 0);             // 至少执行一次"},
                {"kind": "h2", "text": "跳转控制"},
                {"kind": "list", "items": [
                    "break：结束整个循环（整个 for / while）。",
                    "continue：跳过本次循环体剩余代码，直接进入下一次。",
                    "死循环 while(true) + break 是「菜单式程序」的标准写法。",
                ]},
                {"kind": "callout", "tone": "tip", "text":
                    "经典练习：逢七过、求水仙花数、猜数字小游戏——都是分支 + 循环的组合。"},
                {"kind": "summary", "text":
                    "区间判断用 if，等值匹配用 switch；循环次数已知用 for，未知用 while；"
                    "break 终止整层循环，continue 只跳过本轮。"},
            ],
            "concepts": [
                {"term": "分支结构", "level": "core",
                 "definition": "根据条件选择执行路径：if 适合区间判断，switch 适合离散等值匹配。"},
                {"term": "循环结构", "level": "core",
                 "definition": "重复执行某段代码：for 适合已知次数，while 适合未知次数，do-while 至少执行一次。"},
                {"term": "break", "level": "basic",
                 "definition": "终止当前所在整层循环，跳到循环后的代码。",
                 "example": "找到目标后立即 break 退出查找循环。"},
                {"term": "continue", "level": "basic",
                 "definition": "跳过本次循环体剩余部分，直接进入下一次条件判断。",
                 "example": "逢七过：if (i % 7 == 0) continue;"},
                {"term": "死循环", "level": "advanced",
                 "definition": "while(true) 配合 break 使用，是菜单驱动程序的标准骨架。",
                 "example": "do { showMenu(); } while (choice != 0);"},
            ],
            "exercises": [
                {"type": "choice",
                 "question": "需要在「数字星期」与「中文星期」之间做一一对应匹配，最合适的是？",
                 "options": ["多个 if-else", "switch 语句", "while 循环", "三元运算符"],
                 "answer": 1,
                 "explanation": "switch 天然适合有限个离散值的等值匹配，结构清晰。"},
                {"type": "bool",
                 "question": "do...while 循环的循环体至少会执行一次。",
                 "answer": True,
                 "explanation": "do-while 先执行循环体再判断条件，即使条件一开始就不成立。"},
                {"type": "fill",
                 "question": "想立即结束整个循环（而不是跳过本轮），应使用关键字 ______。",
                 "answer": "break",
                 "explanation": "break 结束整层循环；continue 只结束本轮。"},
                {"type": "choice",
                 "question": "以下代码输出什么？for(int i=1;i<=5;i++){ if(i%2==0) continue; System.out.print(i);}",
                 "options": ["12345", "135", "24", "无输出"],
                 "answer": 1,
                 "explanation": "偶数被 continue 跳过，只打印 1、3、5。"},
            ],
        },
        "mindmap": {
            "nodes": [
                {"id": "root", "label": "流程控制逻辑", "level": 0},
                {"id": "n1", "label": "分支", "level": 1},
                {"id": "n1a", "label": "if 三种格式", "level": 2},
                {"id": "n1b", "label": "switch 匹配", "level": 2},
                {"id": "n1c", "label": "三元运算符", "level": 2},
                {"id": "n2", "label": "循环", "level": 1},
                {"id": "n2a", "label": "for 已知次数", "level": 2},
                {"id": "n2b", "label": "while 未知次数", "level": 2},
                {"id": "n2c", "label": "do-while 至少一次", "level": 2},
                {"id": "n3", "label": "跳转控制", "level": 1},
                {"id": "n3a", "label": "break 结束循环", "level": 2},
                {"id": "n3b", "label": "continue 跳过本轮", "level": 2},
                {"id": "n4", "label": "经典练习", "level": 1},
                {"id": "n4a", "label": "逢七过", "level": 2},
                {"id": "n4b", "label": "水仙花数", "level": 2},
                {"id": "n4c", "label": "猜数字", "level": 2},
            ],
            "edges": [
                {"from": "root", "to": "n1"}, {"from": "n1", "to": "n1a"},
                {"from": "n1", "to": "n1b"}, {"from": "n1", "to": "n1c"},
                {"from": "root", "to": "n2"}, {"from": "n2", "to": "n2a"},
                {"from": "n2", "to": "n2b"}, {"from": "n2", "to": "n2c"},
                {"from": "root", "to": "n3"}, {"from": "n3", "to": "n3a"},
                {"from": "n3", "to": "n3b"},
                {"from": "root", "to": "n4"}, {"from": "n4", "to": "n4a"},
                {"from": "n4", "to": "n4b"}, {"from": "n4", "to": "n4c"},
            ],
        },
    },

    # ── 第 4 章 基础语法测验 ──────────────────────────────────────────
    "ch_58507604_fcd8_4f_3": {
        "video": {"page": 30, "cid": 831408595, "duration": 1525,
                  "title": "运算符-01-03-算术运算符详解和综合练习"},
        "lecture": {
            "blocks": [
                {"kind": "h2", "text": "本节概览：运算符综合测验前的知识点盘点"},
                {"kind": "p", "text":
                    "本章以运算符为主线，串联前面学的变量与数据类型，作为基础语法阶段的小测验。"},
                {"kind": "h2", "text": "算术运算符"},
                {"kind": "list", "items": [
                    "+ - * / %：整数相除结果仍是整数（10 / 3 = 3），想得到小数先转成 double。",
                    "% 取模：结果的符号与被除数一致，常用于判奇偶、逢七过。",
                    "字符串参与 + 时变成拼接：\"1\" + 1 = \"11\"；char 参与 + 时按码表值算术相加。",
                ]},
                {"kind": "h2", "text": "自增自减与赋值"},
                {"kind": "code", "lang": "java", "text":
                    "int a = 5;\n"
                    "int b = a++;   // 先用后加: b=5, a=6\n"
                    "int c = ++a;   // 先加后用: a=7, c=7\n"
                    "// 扩展赋值隐含强转: byte x=10; x += 1; 合法, 等价 x=(byte)(x+1)"},
                {"kind": "h2", "text": "逻辑与短路"},
                {"kind": "list", "items": [
                    "& 与 |：两边都会执行（不短路）。",
                    "&& 与 ||：短路版，左边已能决定结果时右边不再执行——生产代码首选。",
                    "关系运算符结果都是 boolean；三元运算符 a ? b : c 可嵌套但别滥用。",
                ]},
                {"kind": "callout", "tone": "warning", "text":
                    "测验高频坑：整数除法截断、字符串 + 拼接顺序、短路求值的执行顺序。"},
                {"kind": "summary", "text":
                    "算术 / 自增自减 / 赋值 / 关系 / 逻辑 / 三元六类运算符，重点掌握整数除法、"
                    "++ 前后缀区别与短路逻辑。"},
            ],
            "concepts": [
                {"term": "整数除法", "level": "core",
                 "definition": "两个整数相除结果仍是整数，小数部分直接截断。",
                 "example": "10 / 3 = 3；10 / 3.0 = 3.333…"},
                {"term": "短路求值", "level": "core",
                 "definition": "&& 左边为 false 或 || 左边为 true 时，右边表达式不再执行。",
                 "example": "if (s != null && s.length() > 0) 避免 NPE。"},
                {"term": "自增自减", "level": "basic",
                 "definition": "++/-- 让变量加 1 或减 1；前缀先运算后取值，后缀先取值后运算。",
                 "example": "a=5: a++ 表达式值为 5，++a 表达式值为 6。"},
                {"term": "三元运算符", "level": "basic",
                 "definition": "条件 ? 值1 : 值2，是 if-else 的表达式形式。",
                 "example": "int max = a > b ? a : b;"},
                {"term": "取模 %", "level": "advanced",
                 "definition": "求余数，结果符号跟随被除数，常用于周期性与奇偶判断。",
                 "example": "i % 2 == 0 判偶数；i % 7 == 0 判七的倍数。"},
            ],
            "exercises": [
                {"type": "choice",
                 "question": "表达式 10 / 3 的值是？",
                 "options": ["3.33", "3", "4", "编译报错"],
                 "answer": 1,
                 "explanation": "整数相除结果取整截断；写成 10 / 3.0 才是 3.33。"},
                {"type": "bool",
                 "question": "int a = 5; int b = a++; 执行后 b 的值是 6。",
                 "answer": False,
                 "explanation": "后缀 ++ 先取值后自增，b = 5，a 变 6。"},
                {"type": "fill",
                 "question": "System.out.println(\"1\" + 1 + 1); 的输出结果是 ______。",
                 "answer": "111",
                 "explanation": "字符串参与 + 变拼接，从左到右依次拼接成 \"111\"。"},
                {"type": "choice",
                 "question": "boolean r = (5 > 3) || (++x < 10); 已知 x 初值为 0，执行后 x 是？",
                 "options": ["0", "1", "取决于 x 类型", "编译报错"],
                 "answer": 0,
                 "explanation": "|| 左边为 true 发生短路，右边 ++x 不会执行，x 保持 0。"},
            ],
        },
        "mindmap": {
            "nodes": [
                {"id": "root", "label": "基础语法测验", "level": 0},
                {"id": "n1", "label": "算术运算符", "level": 1},
                {"id": "n1a", "label": "整数除法截断", "level": 2},
                {"id": "n1b", "label": "取模判奇偶", "level": 2},
                {"id": "n1c", "label": "字符串拼接", "level": 2},
                {"id": "n2", "label": "自增自减", "level": 1},
                {"id": "n2a", "label": "前缀先加", "level": 2},
                {"id": "n2b", "label": "后缀后加", "level": 2},
                {"id": "n3", "label": "逻辑运算", "level": 1},
                {"id": "n3a", "label": "&& 短路与", "level": 2},
                {"id": "n3b", "label": "|| 短路或", "level": 2},
                {"id": "n3c", "label": "结果为 boolean", "level": 2},
                {"id": "n4", "label": "三元运算符", "level": 1},
                {"id": "n4a", "label": "条件?值1:值2", "level": 2},
                {"id": "n4b", "label": "替代简单 if", "level": 2},
            ],
            "edges": [
                {"from": "root", "to": "n1"}, {"from": "n1", "to": "n1a"},
                {"from": "n1", "to": "n1b"}, {"from": "n1", "to": "n1c"},
                {"from": "root", "to": "n2"}, {"from": "n2", "to": "n2a"},
                {"from": "n2", "to": "n2b"},
                {"from": "root", "to": "n3"}, {"from": "n3", "to": "n3a"},
                {"from": "n3", "to": "n3b"}, {"from": "n3", "to": "n3c"},
                {"from": "root", "to": "n4"}, {"from": "n4", "to": "n4a"},
                {"from": "n4", "to": "n4b"},
            ],
        },
    },

    # ── 第 5 章 数组操作实战 ──────────────────────────────────────────
    "ch_58507604_fcd8_4f_4": {
        "video": {"page": 54, "cid": 585591161, "duration": 893,
                  "title": "数组-01-数组的概述和静态初始化"},
        "lecture": {
            "blocks": [
                {"kind": "h2", "text": "本节概览：数组 = 同类型数据的容器"},
                {"kind": "p", "text":
                    "数组用来存储同一类型的多个数据，长度在创建后不可改变。数组的地址存在栈上，"
                    "真正的元素连续存放在堆中——所以数组是引用类型。"},
                {"kind": "h2", "text": "两种初始化"},
                {"kind": "code", "lang": "java", "text":
                    "int[] a = {1, 2, 3};              // 静态: 直接给出元素\n"
                    "int[] b = new int[3];             // 动态: 只给长度, 元素取默认值\n"
                    "// 默认值: int->0, double->0.0, boolean->false, 引用->null"},
                {"kind": "h2", "text": "访问与遍历"},
                {"kind": "list", "items": [
                    "通过 索引 访问：下标从 0 开始，最大下标 = length - 1。",
                    "越界访问抛 ArrayIndexOutOfBoundsException。",
                    "遍历首选 for-each：for (int x : arr) {...}；需要下标时用普通 for。",
                ]},
                {"kind": "h2", "text": "常见操作模板"},
                {"kind": "list", "ordered": True, "items": [
                    "遍历求和 / 求最值：用 max 变量打擂台。",
                    "反转：双指针 left/right 相向交换。",
                    "统计：满足条件的元素计数。",
                ]},
                {"kind": "callout", "tone": "tip", "text":
                    "arr.length 是属性不是方法（没有括号），这是与字符串 str.length() 最容易混的点。"},
                {"kind": "summary", "text":
                    "数组定长、下标从 0 开始；静态初始化给元素，动态初始化给长度；"
                    "引用在栈、实体在堆。"},
            ],
            "concepts": [
                {"term": "数组", "level": "core",
                 "definition": "存储同一种类型多个数据的容器，长度创建后不可变。",
                 "example": "int[] scores = new int[5];"},
                {"term": "静态初始化", "level": "basic",
                 "definition": "定义时直接列出所有元素，系统自动推算长度。",
                 "example": "int[] a = {1, 2, 3};"},
                {"term": "动态初始化", "level": "basic",
                 "definition": "只指定长度，元素先取类型默认值，之后再赋值。",
                 "example": "int[] b = new int[3]; // [0,0,0]"},
                {"term": "索引越界", "level": "core",
                 "definition": "访问下标 < 0 或 >= length 时抛出 ArrayIndexOutOfBoundsException。",
                 "example": "int[] a={1,2,3}; a[3] // 抛异常"},
                {"term": "栈与堆", "level": "advanced",
                 "definition": "数组变量（引用）存在栈上，数组实体（元素连续空间）存在堆上。",
                 "example": "int[] a = b; 只是复制引用，两个变量指向同一块堆内存。"},
            ],
            "exercises": [
                {"type": "choice",
                 "question": "int[] arr = new int[5]; arr[arr.length] 会发生什么？",
                 "options": ["返回 0", "返回最后一个元素", "抛数组越界异常", "自动扩容"],
                 "answer": 2,
                 "explanation": "合法下标 0~length-1，length 处越界抛 ArrayIndexOutOfBoundsException。"},
                {"type": "bool",
                 "question": "数组一旦创建，它的长度就不能再改变。",
                 "answer": True,
                 "explanation": "数组定长；需要动态增删时使用集合 ArrayList。"},
                {"type": "fill",
                 "question": "获取数组长度的写法是 arr.______（属性，不带括号）。",
                 "answer": "length",
                 "explanation": "数组用 length 属性，字符串用 length() 方法。"},
                {"type": "choice",
                 "question": "动态初始化 int[] a = new int[3] 后，a[0] 的默认值是？",
                 "options": ["null", "0", "未定义", "随机值"],
                 "answer": 1,
                 "explanation": "int 数组默认值是 0；double 是 0.0，boolean 是 false，引用是 null。"},
            ],
        },
        "mindmap": {
            "nodes": [
                {"id": "root", "label": "数组操作实战", "level": 0},
                {"id": "n1", "label": "初始化", "level": 1},
                {"id": "n1a", "label": "静态 {1,2,3}", "level": 2},
                {"id": "n1b", "label": "动态 new int[3]", "level": 2},
                {"id": "n1c", "label": "元素默认值", "level": 2},
                {"id": "n2", "label": "访问", "level": 1},
                {"id": "n2a", "label": "下标从 0 开始", "level": 2},
                {"id": "n2b", "label": "越界异常", "level": 2},
                {"id": "n3", "label": "遍历", "level": 1},
                {"id": "n3a", "label": "for-each", "level": 2},
                {"id": "n3b", "label": "普通 for 带下标", "level": 2},
                {"id": "n4", "label": "经典操作", "level": 1},
                {"id": "n4a", "label": "求最值(打擂台)", "level": 2},
                {"id": "n4b", "label": "反转(双指针)", "level": 2},
                {"id": "n4c", "label": "求和与统计", "level": 2},
            ],
            "edges": [
                {"from": "root", "to": "n1"}, {"from": "n1", "to": "n1a"},
                {"from": "n1", "to": "n1b"}, {"from": "n1", "to": "n1c"},
                {"from": "root", "to": "n2"}, {"from": "n2", "to": "n2a"},
                {"from": "n2", "to": "n2b"},
                {"from": "root", "to": "n3"}, {"from": "n3", "to": "n3a"},
                {"from": "n3", "to": "n3b"},
                {"from": "root", "to": "n4"}, {"from": "n4", "to": "n4a"},
                {"from": "n4", "to": "n4b"}, {"from": "n4", "to": "n4c"},
            ],
        },
    },

    # ── 第 6 章 面向对象编程 ──────────────────────────────────────────
    "ch_58507604_fcd8_4f_5": {
        "video": {"page": 82, "cid": 585599258, "duration": 1543,
                  "title": "面向对象-02-类和对象"},
        "lecture": {
            "blocks": [
                {"kind": "h2", "text": "本节概览：从「做事」到「找对象」"},
                {"kind": "p", "text":
                    "面向对象把数据和行为封装成对象。类是对象的模板（描述属性和行为），"
                    "对象是类的具体实例。Java 面向对象三大特性：封装、继承、多态。"},
                {"kind": "h2", "text": "类与对象"},
                {"kind": "code", "lang": "java", "text":
                    "class Student {                 // 类 = 模板\n"
                    "    private String name;        // 成员变量(属性)\n"
                    "    public void study() {...}   // 成员方法(行为)\n"
                    "}\n"
                    "Student s = new Student();      // 对象 = 实例, 在堆中开辟空间"},
                {"kind": "h2", "text": "封装"},
                {"kind": "list", "items": [
                    "属性私有化（private），对外提供 getter / setter 访问。",
                    "好处：数据可控（在 setter 里校验）、调用方无需关心内部实现。",
                    "this 指向当前对象，用于区分成员变量与局部变量同名的情况。",
                ]},
                {"kind": "h2", "text": "继承与多态"},
                {"kind": "list", "items": [
                    "继承 extends：子类复用父类成员，只能单继承；方法重写要求签名一致。",
                    "多态：父类引用指向子类对象，编译看左边、运行看右边。",
                    "构造方法：与类同名、无返回值、可重载；子类构造默认先 super()。",
                ]},
                {"kind": "callout", "tone": "tip", "text":
                    "记口诀：成员变量编译运行都看左边；成员方法编译看左边、运行看右边——这就是多态。"},
                {"kind": "summary", "text":
                    "类是模板对象是实例；封装隐藏细节保护数据；继承复用代码；"
                    "多态让同一调用产生不同行为。"},
            ],
            "concepts": [
                {"term": "类与对象", "level": "core",
                 "definition": "类是描述属性和行为的模板；对象是按模板在堆中创建的实例。",
                 "example": "Student 是类，new Student() 是对象。"},
                {"term": "封装", "level": "core",
                 "definition": "属性私有 + 公共 getter/setter，隐藏实现细节并校验数据。",
                 "example": "private int age; public void setAge(int a){ if(a>0) age=a; }"},
                {"term": "继承", "level": "core",
                 "definition": "子类通过 extends 获得父类的属性和方法，Java 只支持单继承。",
                 "example": "class Dog extends Animal {}"},
                {"term": "多态", "level": "advanced",
                 "definition": "父类引用指向子类对象，运行时调用的是子类重写后的方法。",
                 "example": "Animal a = new Dog(); a.eat(); // 执行 Dog 的 eat"},
                {"term": "构造方法", "level": "basic",
                 "definition": "与类同名且无返回值的方法，创建对象时初始化，可重载；不写则默认有一个空构造。",
                 "example": "public Student(String name){ this.name = name; }"},
                {"term": "this 与 super", "level": "basic",
                 "definition": "this 指向当前对象；super 指向父类部分，用于访问父类成员和构造。",
                 "example": "this.name 区分成员变量；super.study() 调用父类方法。"},
            ],
            "exercises": [
                {"type": "choice",
                 "question": "实现类之间的继承关系，使用的关键字是？",
                 "options": ["implements", "extends", "inherits", "super"],
                 "answer": 1,
                 "explanation": "类继承类用 extends；类实现接口用 implements。"},
                {"type": "bool",
                 "question": "方法重写（Override）要求子类方法的声明与父类完全一致（方法名和参数列表相同）。",
                 "answer": True,
                 "explanation": "方法名、参数列表一致才是重写；只有方法名相同而参数不同是重载（Overload）。"},
                {"type": "fill",
                 "question": "封装后，外界访问私有属性需要通过 ______ 和 setter 方法。",
                 "answer": "getter",
                 "explanation": "getter 读取属性，setter 设置（并校验）属性。"},
                {"type": "choice",
                 "question": "Animal a = new Dog(); a.eat(); 编译和运行时的说法正确的是？",
                 "options": ["编译看 Dog，运行看 Animal", "编译看 Animal，运行看 Dog",
                             "编译运行都看 Animal", "编译运行都看 Dog"],
                 "answer": 1,
                 "explanation": "口诀：编译看左边（引用类型 Animal），运行看右边（对象类型 Dog）。"},
            ],
        },
        "mindmap": {
            "nodes": [
                {"id": "root", "label": "面向对象编程", "level": 0},
                {"id": "n1", "label": "类与对象", "level": 1},
                {"id": "n1a", "label": "类是模板", "level": 2},
                {"id": "n1b", "label": "对象是实例", "level": 2},
                {"id": "n1c", "label": "成员变量/方法", "level": 2},
                {"id": "n2", "label": "封装", "level": 1},
                {"id": "n2a", "label": "private 私有", "level": 2},
                {"id": "n2b", "label": "getter/setter", "level": 2},
                {"id": "n2c", "label": "this 关键字", "level": 2},
                {"id": "n3", "label": "继承", "level": 1},
                {"id": "n3a", "label": "extends 单继承", "level": 2},
                {"id": "n3b", "label": "方法重写", "level": 2},
                {"id": "n3c", "label": "super 调父类", "level": 2},
                {"id": "n4", "label": "多态", "level": 1},
                {"id": "n4a", "label": "父类引用指子类", "level": 2},
                {"id": "n4b", "label": "编译左运行右", "level": 2},
                {"id": "n4c", "label": "构造方法重载", "level": 2},
            ],
            "edges": [
                {"from": "root", "to": "n1"}, {"from": "n1", "to": "n1a"},
                {"from": "n1", "to": "n1b"}, {"from": "n1", "to": "n1c"},
                {"from": "root", "to": "n2"}, {"from": "n2", "to": "n2a"},
                {"from": "n2", "to": "n2b"}, {"from": "n2", "to": "n2c"},
                {"from": "root", "to": "n3"}, {"from": "n3", "to": "n3a"},
                {"from": "n3", "to": "n3b"}, {"from": "n3", "to": "n3c"},
                {"from": "root", "to": "n4"}, {"from": "n4", "to": "n4a"},
                {"from": "n4", "to": "n4b"}, {"from": "n4", "to": "n4c"},
            ],
        },
    },

    # ── 第 7 章 学生管理系统 ──────────────────────────────────────────
    "ch_58507604_fcd8_4f_6": {
        "video": {"page": 116, "cid": 585675330, "duration": 1575,
                  "title": "学生管理系统-01-业务分析并搭建主菜单"},
        "lecture": {
            "blocks": [
                {"kind": "h2", "text": "本节概览：用面向对象 + 集合做一个完整系统"},
                {"kind": "p", "text":
                    "学生管理系统是 Java 基础阶段的综合实战：用 Student 类描述数据、"
                    "ArrayList 存储所有学生、菜单循环驱动增删改查，把前面六章的知识串起来。"},
                {"kind": "h2", "text": "整体架构"},
                {"kind": "list", "ordered": True, "items": [
                    "数据层：Student 类（id、姓名、年龄、成绩），全私有 + getter/setter。",
                    "容器层：ArrayList<Student>，在内存中保存所有学生对象。",
                    "界面层：while(true) 菜单循环，switch 分发到 1 查询 / 2 添加 / 3 删除 / 4 修改 / 0 退出。",
                    "逻辑层：每个功能封装成独立方法，方法之间只传 list 与学号。",
                ]},
                {"kind": "h2", "text": "关键技术点"},
                {"kind": "code", "lang": "java", "text":
                    "ArrayList<Student> list = new ArrayList<>();\n"
                    "for (Student s : list) {                       // 遍历查询\n"
                    "    if (s.getId().equals(targetId)) { list.remove(s); break; }\n"
                    "}\n"
                    "// 删除/修改前都要先「根据学号找索引」, 找不到要给出友好提示"},
                {"kind": "list", "items": [
                    "equals 比较字符串内容（== 比较地址），学号匹配必须用 equals。",
                    "遍历中删除元素后立即 break，避免并发修改异常。",
                    "添加时校验学号唯一；删除时校验存在性。",
                ]},
                {"kind": "callout", "tone": "tip", "text":
                    "先画功能清单再动手：菜单 → 实体类 → 容器 → 一个功能一个方法，步步为营。"},
                {"kind": "summary", "text":
                    "系统 = Student 实体 + ArrayList 容器 + 菜单循环 + 四个独立业务方法；"
                    "完成后可再扩展文件存储与登录。"},
            ],
            "concepts": [
                {"term": "分层设计", "level": "core",
                 "definition": "按数据层/容器层/界面层/逻辑层组织代码，每层职责单一，便于维护扩展。"},
                {"term": "ArrayList", "level": "core",
                 "definition": "长度可变的集合容器，常用方法 add / remove / get / size / 遍历。",
                 "example": "ArrayList<Student> list = new ArrayList<>();"},
                {"term": "菜单循环驱动", "level": "basic",
                 "definition": "while(true) + switch 让程序持续响应菜单输入，选择退出时 break。",
                 "example": "do { showMenu(); } while (choice != 0);"},
                {"term": "equals 与 ==", "level": "core",
                 "definition": "== 比较两个引用是否同一对象，equals 比较字符串内容是否相同。",
                 "example": "s.getId().equals(inputId)"},
                {"term": "方法封装", "level": "basic",
                 "definition": "每个业务（查询/添加/删除/修改）独立成方法，主流程只做分发。",
                 "example": "case 2 -> addStudent(list);"},
            ],
            "exercises": [
                {"type": "choice",
                 "question": "存储多个学生对象并需要频繁增删，最合适的容器是？",
                 "options": ["定长数组 int[]", "ArrayList<Student>", "String", "多个变量"],
                 "answer": 1,
                 "explanation": "ArrayList 长度可变且提供 add/remove，适合动态增删对象。"},
                {"type": "bool",
                 "question": "比较两个字符串学号是否相同，应该使用 == 运算符。",
                 "answer": False,
                 "explanation": "== 比较地址；内容比较要用 equals 方法。"},
                {"type": "fill",
                 "question": "在遍历 ArrayList 找到目标并删除后，应立即使用 ______ 跳出循环，避免并发修改异常。",
                 "answer": "break",
                 "explanation": "遍历中删除元素后继续遍历会触发 ConcurrentModificationException。"},
                {"type": "choice",
                 "question": "「输入 0 退出系统」对应的程序骨架最合理的是？",
                 "options": ["for(int i=0;i<100;i++) 菜单();", "while(true){ menu(); if(choice==0) break; }",
                             "if(choice==0) menu();", "try{ menu(); }catch(Exception e){}"],
                 "answer": 1,
                 "explanation": "死循环 + 条件 break 是菜单驱动程序的标准写法。"},
            ],
        },
        "mindmap": {
            "nodes": [
                {"id": "root", "label": "学生管理系统", "level": 0},
                {"id": "n1", "label": "整体架构", "level": 1},
                {"id": "n1a", "label": "Student 实体类", "level": 2},
                {"id": "n1b", "label": "ArrayList 容器", "level": 2},
                {"id": "n1c", "label": "菜单循环驱动", "level": 2},
                {"id": "n2", "label": "核心功能", "level": 1},
                {"id": "n2a", "label": "查询遍历", "level": 2},
                {"id": "n2b", "label": "添加校验唯一", "level": 2},
                {"id": "n2c", "label": "删除先找索引", "level": 2},
                {"id": "n2d", "label": "修改整体替换", "level": 2},
                {"id": "n3", "label": "关键技术", "level": 1},
                {"id": "n3a", "label": "equals 比内容", "level": 2},
                {"id": "n3b", "label": "遍历中删除+break", "level": 2},
                {"id": "n3c", "label": "方法分装", "level": 2},
                {"id": "n4", "label": "拓展方向", "level": 1},
                {"id": "n4a", "label": "文件持久化", "level": 2},
                {"id": "n4b", "label": "异常处理", "level": 2},
            ],
            "edges": [
                {"from": "root", "to": "n1"}, {"from": "n1", "to": "n1a"},
                {"from": "n1", "to": "n1b"}, {"from": "n1", "to": "n1c"},
                {"from": "root", "to": "n2"}, {"from": "n2", "to": "n2a"},
                {"from": "n2", "to": "n2b"}, {"from": "n2", "to": "n2c"},
                {"from": "n2", "to": "n2d"},
                {"from": "root", "to": "n3"}, {"from": "n3", "to": "n3a"},
                {"from": "n3", "to": "n3b"}, {"from": "n3", "to": "n3c"},
                {"from": "root", "to": "n4"}, {"from": "n4", "to": "n4a"},
                {"from": "n4", "to": "n4b"},
            ],
        },
    },
}


async def run(force: bool) -> None:
    sm = get_sessionmaker()
    async with sm() as session:
        res = await session.execute(
            select(Course).where(Course.id == COURSE_ID)
            .options(selectinload(Course.chapters).selectinload(Chapter.subchapters))
        )
        course = res.scalar_one_or_none()
        if not course:
            sys.exit(f"course {COURSE_ID} not found")

        updated = skipped = 0
        for ch in sorted(course.chapters, key=lambda c: c.sort_order):
            data = CHAPTERS.get(ch.id)
            if not data:
                print(f"[SKIP] {ch.id} 无预置内容")
                continue
            if ch.demo_version == CURATED_VERSION and not force:
                skipped += 1
                continue

            ch.lecture = data["lecture"]
            ch.mindmap = data["mindmap"]
            ch.is_demo = False              # 学生导入的课程, 不参与 demo 版本清理
            ch.demo_version = CURATED_VERSION

            video = data["video"]
            if ch.subchapters:
                sc = ch.subchapters[0]
                sc.bvid = BVID
                sc.cid = video["cid"]
                sc.page = video["page"]
                sc.duration = video["duration"]
                sc.is_demo = False
                sc.demo_version = CURATED_VERSION
            updated += 1
            print(f"[OK  ] {ch.id} {ch.title} -> P{video['page']} {video['title']}")

        if updated:
            course.total_lessons = sum(len(c.subchapters) for c in course.chapters)
            course.total_duration = sum(
                sc.duration or 0 for c in course.chapters for sc in c.subchapters
            )
        await session.commit()
        print(f"\n汇总: 更新 {updated} 章, 跳过 {skipped} 章"
              + (" (--force 可重写)" if skipped else ""))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--force", action="store_true", help="覆盖已写入的预置内容")
    args = ap.parse_args()
    asyncio.run(run(args.force))
