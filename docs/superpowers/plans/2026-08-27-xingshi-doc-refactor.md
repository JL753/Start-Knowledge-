# 星识 Star-Learn 文档重构 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 按主题分层重写 `docs/`，输出 14 篇新主题文档 + 3 篇走查 + 1 篇索引 + 1 篇占位 + 1 篇归档说明（20 个新 Markdown 文件），并把 22 份旧文档搬进 `_archive/`。

**Architecture:** 不动任何代码；纯 `docs/` 目录变更。每篇文档按 6 段模板（摘要/前置/内容/代码定位/常见坑/相关链接）撰写。先建立 `_archive/` 骨架，再按依赖图自顶向下写作，最后写 `README.md` 总索引。

**Tech Stack:** Markdown、Git、Mermaid（图表）、bash（grep/wc 做验证）。

---

## File Structure

### 新文件（20 个）

```
docs/
├── README.md                              # Task 19
├── 项目说明.md                            # Task 2
├── 架构设计.md                            # Task 3
├── 后端服务.md                            # Task 4
├── 前端架构.md                            # Task 5
├── 智能体与流水线.md                      # Task 6
├── 子系统详解.md                          # Task 7
├── 数据层与迁移.md                        # Task 8
├── 可观测性与安全.md                      # Task 9
├── 外部服务依赖.md                        # Task 10
├── 部署与运维.md                          # Task 11
├── 演示现场手册.md                        # Task 12
├── 测试体系.md                            # Task 13
├── 脚本索引.md                            # Task 14
├── 评测体系.md                            # Task 15（占位）
└── walkthrough/
    ├── 01-首次运行.md                     # Task 16
    ├── 02-新增智能体.md                   # Task 17
    └── 03-新增前端页面.md                 # Task 18

docs/_archive/                             # Task 1
├── README.md                              # Task 1
└── (现有 22 份文档)
```

### 不修改的文件

- 任何 `.py`、`.js`、`.html`、`.css` 文件
- `package.json`、`requirements.txt`、`mkdocs.yml`（如有）
- `alembic/`、`tests/`、`scripts/`
- 仓库根目录 `main.py`、`agents.py`、`db.py`、`state.py`
- `docs/sql/` 子目录

---

## Task 1: 建立 `_archive/` 骨架并搬迁 22 份旧文档

**Files:**
- Create: `docs/_archive/README.md`
- Move: 22 个现有 `docs/*.md` / `*.txt` 到 `docs/_archive/`

- [ ] **Step 1: 创建 `_archive/` 目录**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
mkdir -p docs/_archive
```

- [ ] **Step 2: 用 `git mv` 搬迁现有文档**

执行以下命令序列（每条独立运行；如文件不存在则跳过该条）：

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git mv docs/项目完善建议.md         docs/_archive/项目完善建议.md || true
git mv docs/项目结构说明.md         docs/_archive/项目结构说明.md || true
git mv docs/项目功能地图.md         docs/_archive/项目功能地图.md || true
git mv docs/代码百科.md             docs/_archive/代码百科.md || true
git mv docs/运行指南.md             docs/_archive/运行指南.md || true
git mv docs/部署文档.md             docs/_archive/部署文档.md || true
git mv docs/比赛架构图说明.md        docs/_archive/比赛架构图说明.md || true
git mv docs/演示数据流图.md         docs/_archive/演示数据流图.md || true
git mv docs/技术问答准备.md         docs/_archive/技术问答准备.md || true
git mv docs/P1运维手册.md           docs/_archive/P1运维手册.md || true
git mv docs/P1收尾总结.md           docs/_archive/P1收尾总结.md || true
git mv docs/P1合并请求说明.md       docs/_archive/P1合并请求说明.md || true
git mv docs/缺口分析与实施记录.md   docs/_archive/缺口分析与实施记录.md || true
git mv docs/实施报告-v1.0.md        docs/_archive/实施报告-v1.0.md || true
git mv docs/数据库迁移切片状态.md    docs/_archive/数据库迁移切片状态.md || true
git mv docs/演示内容注入执行报告.md   docs/_archive/演示内容注入执行报告.md || true
git mv docs/代码同步操作手册.md      docs/_archive/代码同步操作手册.md || true
git mv docs/记忆系统完整框架.txt     docs/_archive/记忆系统完整框架.txt || true
git mv docs/消息链路.txt            docs/_archive/消息链路.txt || true
git mv docs/防幻觉机制架构流程图.txt docs/_archive/防幻觉机制架构流程图.txt || true
git mv docs/PROJECT_STRUCTURE.md    docs/_archive/PROJECT_STRUCTURE.md || true
git mv docs/PROJECT_MAP.md          docs/_archive/PROJECT_MAP.md || true
```

预期输出：每行打印形如 `rename docs/X.md => docs/_archive/X.md (100%)`。

- [ ] **Step 3: 验证搬迁结果**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
ls docs/_archive/ | wc -l
```

预期：22（22 个旧文档已搬入，README.md 还没建）。

- [ ] **Step 4: 写 `_archive/README.md`**

创建文件 `docs/_archive/README.md`，内容如下：

```markdown
# 文档归档（_archive）

本目录是项目文档重构（2026-08-27）前的旧版本，仅供历史回溯。
新文档请参考：[docs/README.md](../README.md)。

## 归档策略

本次重构按"主题分层"重写 `docs/`。旧文档有 3 种去向：

1. **内容被吸收**：[运行指南.md](运行指南.md)、[部署文档.md](部署文档.md)、[P1运维手册.md](P1运维手册.md)、[数据库迁移切片状态.md](数据库迁移切片状态.md) 等的内容已整合进对应新文档（部署与运维、数据层与迁移）。
2. **主题被取代**：[项目结构说明.md](项目结构说明.md)、[项目功能地图.md](项目功能地图.md)、[代码百科.md](代码百科.md)、[比赛架构图说明.md](比赛架构图说明.md) 等已被新文档取代（架构设计、子系统详解、智能体与流水线）。
3. **过程性文档**：[P1收尾总结.md](P1收尾总结.md)、[P1合并请求说明.md](P1合并请求说明.md)、[缺口分析与实施记录.md](缺口分析与实施记录.md)、[实施报告-v1.0.md](实施报告-v1.0.md)、[演示内容注入执行报告.md](演示内容注入执行报告.md) 等仅作历史参考。

## 规则

如旧文档与新文档有出入，**以新文档为准**。新文档编写时已尽量吸收旧文档的有效内容，但旧文档不会主动修正；如发现旧文档中存在重大错误，请直接在 `_archive/` 对应文件中以注释形式标注。
```

- [ ] **Step 5: 自检**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
ls docs/_archive/ | wc -l
```

预期：23（22 个旧文档 + 1 个 README）。

- [ ] **Step 6: 提交**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add docs/_archive/
git commit -m "docs(archive): 搬迁 22 份旧文档到 _archive/ 并加归档说明

- git mv 22 个 *.md / *.txt 到 docs/_archive/
- 新增 _archive/README.md，说明归档策略
- 不修改任何代码文件

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Task 2: 写 `docs/项目说明.md`

**Files:**
- Create: `docs/项目说明.md`

- [ ] **Step 1: 写文档**

创建 `docs/项目说明.md`，按 6 段模板：

```markdown
# 项目说明

## 摘要

星识 Star-Learn 是面向学生的 AI 智能学习中枢，基于多智能体编排、苏格拉底式教学、个性化学习路径规划、AI 课堂对话、代码练习、心流监测、知识图谱等能力。融合 10+ 个 Agent、6 套主题、35 张数据表，支持本地 SQLite 与生产 MySQL 双部署、Windows 一键安装包与 Docker Compose 开发环境。本文档是项目入口的"一句话定位 + 能力清单"。

## 前置知识

无（这是入口文档）。

## 内容

### 一句话定位

> 个人智能学习中枢 = 多智能体编排 × 苏格拉底教学 × 个性化路径 × 心流监测

### 核心能力

- 🧠 **多智能体编排**：MasterController 调度 Profiler、Planner、Document/Mindmap/Exercise/Video Generator、ResourcePush、Evaluation、Socratic 等 10+ Agent
- 💬 **AI 课堂对话**：5 种教师 Persona（patient_tutor / socratic_questioner / energetic_lecturer / expert_mentor / caring_counselor），按 `socratic_intensity` 注入反问强度
- 🎯 **学习路径规划**：每日学习路线、SM2 间隔重复、知识节点图谱
- 💻 **代码工坊**：Monaco IDE、实时运行、AI 评审、批量出题、错题本
- 📚 **课程中心**：学科 → 课程 → 章节 → 子章节 四级结构，B 站视频导入
- 🌱 **生态养成**：星宝宠物、植物林场、成就系统
- 🎙 **多媒体**：TTS（MiniMax / OpenAI 兼容）、ASR（百度 / Whisper WASM）、视频生成（可灵 / CogVideo）
- 📊 **心流共振仪**：专注度监测 + 遥测数据可视化
- 🎨 **主题系统**：6 套主题（dawn/forest/sakura/midnight/nebula/...） + 液态玻璃 + 3D 加载动画

### 技术栈

| 层级 | 技术 |
|---|---|
| 后端框架 | FastAPI 0.104 + Uvicorn 0.24 |
| ORM | SQLAlchemy 2.0(async) + Alembic 1.13 |
| 数据校验 | Pydantic 2.x + pydantic-settings |
| 数据库 | MySQL 5.7+ / SQLite 3（asyncmy / aiosqlite） |
| Agent 编排 | LangGraph 0.2 + langgraph-checkpoint-mysql |
| 缓存 / 队列 | Redis 7（可选）|
| 向量库 | Qdrant 1.9（可选）|
| LLM | MiniMax（默认）/ 讯飞大模型 |
| TTS | MiniMax TTS / OpenAI 兼容 |
| ASR | 百度短语音 / Whisper WASM |
| 视频生成 | 可灵 Kling / CogVideo（本地）|
| 前端 | 原生 HTML/CSS/JS（无构建），Monaco Editor（CDN），Alpine.js + Tailwind CDN |
| 测试 | pytest（后端）+ Vitest / Playwright（前端）|
| 打包 | Inno Setup + 嵌入 CPython → 单 exe 安装包 |

### 用户类型

- 学生：登录后使用 AI 课堂、学习路径、代码工坊、心流监测等功能
- 教师：通过 `/teacher-*` 系列页面查看班级、批改、内容管理、考试管理

## 代码定位

- 后端入口：`main.py:172`（FastAPI app）、`main.py:322-410`（路由注册）
- 后端 ORM：`app/models/user.py:User`、`app/models/course.py:Course`、`app/models/classroom.py:ClassroomSession`
- 后端 Agent：`app/agents/audit.py`、`app/agents/critic.py`、`app/agents/recommend.py`、`app/agents/io_schema.py`
- 前端：`static/html/index.html`（营销页）、`static/html/hub.html`（个人中枢）
- 配置：`config/config.py`（LLM 密钥）、`app/core/config.py`（DB + 特性开关）

## 常见坑

- **v1 / v2 双层并存**：根目录 `main.py / agents.py / db.py / state.py` 是 V1 legacy；`app/` 是 V2。`state.py` 是 Pydantic 状态，`db.py` 是数据访问；不要混用
- **环境变量冲突**：`APP_DEBUG` 同时被 V1 和 V2 读取；改它会触发两个启动分支
- **数据库连接**：默认 SQLite 在 `xingshi_v2.db`；切 MySQL 必须改 `DATABASE_URL` 并跑 `alembic upgrade head`

## 相关链接

- [架构设计.md](架构设计.md) — 总体架构图 + v1/v2 双层结构
- [部署与运维.md](部署与运维.md) — dev / prod / docker / Windows 安装包
- [演示现场手册.md](演示现场手册.md) — 评委用文档
```

- [ ] **Step 2: 自检**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
grep -c "^## " docs/项目说明.md       # 应 ≥6
wc -m docs/项目说明.md                # 字数（不含空白）应 800-2500
```

预期：第一条命令输出 ≥6（6 段都在），第二条 wc -m 输出在 2000-5000 之间（中文为主，字数略大）。

- [ ] **Step 3: 提交**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add docs/项目说明.md
git commit -m "docs: 新增 项目说明.md（入口定位 + 能力清单 + 技术栈）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Task 3: 写 `docs/架构设计.md`

**Files:**
- Create: `docs/架构设计.md`

- [ ] **Step 1: 写文档**

创建 `docs/架构设计.md`：

```markdown
# 架构设计

## 摘要

本文档描述星识 Star-Learn 的总体架构：双层代码组织（V1 legacy + V2 app/）、多智能体编排图（6 个 Agent + MasterController + tutor_engine 流水线）、仓储双写与灰度切流、外部服务依赖关系。理解本文档后，可以从任意子系统入手快速定位代码。

## 前置知识

- [项目说明.md](项目说明.md) — 一句话定位与能力清单

## 内容

### 总体架构图

```mermaid
graph TD
    Browser[浏览器<br/>HTML/JS/Alpine] --> FastAPI
    FastAPI[main.py<br/>FastAPI 单体] --> Legacy[Legacy V1<br/>db.py / agents.py / state.py]
    FastAPI --> App[app/ V2]
    App --> API[app/api/* 路由]
    API --> Services[app/services/* 业务]
    Services --> Repos[app/repositories/* 仓储]
    Repos --> ORM[SQLAlchemy ORM<br/>app/models/*]
    Repos --> Legacy
    Services --> Tutor[tutor_engine/<br/>新流水线]
    Tutor --> Agents[app/agents/*<br/>命名实体化]
    Services --> KB[services/kb/<br/>Qdrant]
    Services --> LLM[services/llm/<br/>MiniMax/讯飞]
    Services --> TTS[services/tts/<br/>MiniMax]
    Services --> ASR[services/asr/<br/>百度/Whisper]
    ORM --> SQLite[(SQLite/MySQL)]
    Legacy --> SQLite
    Browser --> Mascot[小星 mascot<br/>mascot.js]
    Mascot --> Services
```

### 双层代码组织（V1 / V2）

| 层 | 路径 | 状态 | 用途 |
|---|---|---|---|
| V1 Legacy | 根目录 `main.py / agents.py / db.py / state.py` + `agent_utils.py / llm_stream.py / proactive_tutor.py / task_manager.py` | 仍在运行 | 单体入口、Pydantic 状态、传统数据访问、MasterController 编排 |
| V2 重构 | `app/`（api/core/models/schemas/services/agents/repositories/prompts）| 主线开发 | 模块化路由、SQLAlchemy ORM、仓储抽象、新 Agent 命名空间 |

**迁移策略**：V2 通过 `app/repositories/dual_write.py` + `app/core/repository_factory.py` 同时写 V1（legacy 仓储）和 V2（ORM），读路径按 feature flag 灰度切流。

### 6 个 Agent

| Agent | 文件 | 角色 |
|---|---|---|
| ProfilerAgent | `agents.py:62` | 画像分析（更新6 维雷达）|
| PlannerAgent | `agents.py:316` | 任务规划 |
| DocumentGeneratorAgent | `agents.py:396` | 文档生成 |
| MindmapGeneratorAgent | `agents.py:447` | 思维导图 |
| ExerciseGeneratorAgent | `agents.py:514` | 练习题生成 |
| VideoContentAgent | `agents.py:569` | 视频内容 |
| ResourcePushAgent | `agents.py:599` | 资源推送 |
| EvaluationAgent | `agents.py:629` | 评估 |
| SocraticEvaluatorAgent | `agents.py:667` | 苏格拉底式问答 |
| RecommendAgent | `app/agents/recommend.py` | 可解释推荐（M2.1）|
| AuditAgent | `app/agents/audit.py` | 越狱 + 防幻觉（M2.2）|
| CriticAgent | `app/agents/critic.py` | L3 独立评审（M4.4）|

MasterController（`agents.py:1116`）调度：`Echo → Profiler → Planner → DocumentGenerator/MindmapGenerator/ExerciseGenerator/VideoContent（并行）→ ResourcePush → Evaluation`

### 仓储双写与灰度切流

- 读路径：`get_repository_for_user(user_id, type)`（`app/core/repository_factory.py:97`）→ 若 `is_orm_enabled()` 且 `user_in_orm_read_path(user_id, pct)`（md5 hash 桶分）→ ORM；否则 legacy
- 写路径：`get_write_repository(user_id, type)` → 主 ORM；若 `is_dual_write_enabled()` → `DualWriteRepository(primary=ORM, shadow=legacy)`
- Feature flags：`app/core/feature_flags.py` — `ORM_ENABLED` / `READ_BACKEND_PERCENTAGE` / `DUAL_WRITE_LEGACY` / `GUARD_V2_MODE` / `MEMORY_V2` / `SELF_CHECK_ENABLED` / `EMBEDDING_PROVIDER`

### 路由前缀总表（部分）

| 前缀 | 文件 | 主要端点 |
|---|---|---|
| `/api/v2` | `app/api/__init__.py` | tts/asr/grading/teacher_chat/ppt |
| `/api` | `main.py:330-350` | memory/profile/evaluation/mascot |
| `/api/learning-path` | `main.py:326` | learning_path |
| `/api/auth` | `app/api/auth.py` | login/register/refresh |
| `/api/bilibili` | `app/api/bilibili.py` | B 站视频解析 |
| `/api/courses` | `app/api/courses.py` | 课程 CRUD |
| `/api/teacher` | `app/api/teacher.py` | 教师工作台 |
| `/api/datacenter` | `app/api/datacenter.py` | 教师数据中心 |
| `/api/agent-orchestration` | `app/api/agent_orchestration.py` | MasterController HTTP |
| `/api/kb` | `app/api/kb.py` | KB 摄取 |
| `/api/health` | `app/api/health.py` | 健康检查 |

完整路由表见 [后端服务.md](后端服务.md)。

### 中间件栈（`main.py:286-316`）

- TraceMiddleware（W3C trace context，stdlib-only）
- SecurityHeadersMiddleware（CSP、X-Frame-Options 等）
- SlowAPIMiddleware（限流）
- OriginCheckMiddleware（CSRF via Origin/Referer）
- RequestSizeLimitMiddleware（DoS 防护，SSE 路由白名单放大）

## 代码定位

- 总入口：`main.py:172`（FastAPI app）、`main.py:184-217`（异常处理）、`main.py:286-316`（中间件）
- 路由注册：`main.py:322-410`
- 双层数据：`app/repositories/dual_write.py`、`app/core/repository_factory.py`
- Agent 注册：`agents.py:1116`（MasterController）、`agents.py:1698`（create_default_controller）
- 新 Agent：`app/agents/{audit,critic,recommend,io_schema}.py`
- 健康检查：`app/api/health.py`

## 常见坑

- **V1 仍在写状态**：`main.py` 内联 ~200 路由 + 调用 legacy 助手函数；切勿假设所有数据走 V2 ORM
- **Agent 单例**：`MasterController` 通过 `main.py:3745 get_controller()` 懒构建，全局唯一；不要重复 `create_default_controller()`
- **In-memory 状态**：`app/api/agent_orchestration.py` 的 `_PIPELINE_STATUS` 字典不持久化；重启或多 worker 部署会丢
- **配置两套**：`config/config.py`（LLM 密钥）+ `app/core/config.py`（DB/特性开关）共用 `.env`；改配置要意识到两个文件

## 相关链接

- [项目说明.md](项目说明.md) — 入口
- [后端服务.md](后端服务.md) — 路由详细表 + 单体结构
- [智能体与流水线.md](智能体与流水线.md) — 6 Agent + tutor_engine 流水线
- [数据层与迁移.md](数据层与迁移.md) — 35 表 + 双写 + 迁移
```

- [ ] **Step 2: 自检**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
grep -c "^## " docs/架构设计.md    # 应 ≥6
grep -c "mermaid" docs/架构设计.md  # 应 ≥1（架构图）
```

预期：第一个 ≥6，第二个 ≥1。

- [ ] **Step 3: 提交**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add docs/架构设计.md
git commit -m "docs: 新增 架构设计.md（双层架构图 + 6 Agent + 路由总表）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Task 4: 写 `docs/后端服务.md`

**Files:**
- Create: `docs/后端服务.md`

- [ ] **Step 1: 写文档**

创建 `docs/后端服务.md`：

```markdown
# 后端服务

## 摘要

本文档描述星识 Star-Learn 后端：`main.py` FastAPI 单体（10,544 行）+ `app/api/*` 模块化路由（23 个文件）。理解入口结构、路由注册模式、依赖注入与异常处理，可以快速定位任意端点的代码与行为。

## 前置知识

- [架构设计.md](架构设计.md) — 总架构图与双层结构

## 内容

### 入口：`main.py` 结构

`main.py` 是 FastAPI 单体应用，按"配置 → lifespan → 异常处理 → 中间件 → 路由注册 → 内联路由 → 启动"组织。

| 区段 | 行号 | 作用 |
|---|---|---|
| 导入与路径 | 1-100 | `load_dotenv(config/.env)`、`import db as database`、`from state import ...`、`from agents import MasterController, ...` |
| Lifespan | 100-180 | 启动期做 backend 一致性检查、`init_db()`、KB `_COUNTER` hydrate、demo/course 种子、`HealthWorker`、每日 cron（记忆整合 03:00、drift 04:00）|
| FastAPI 实例 | 172 | `app = FastAPI(lifespan=lifespan)` |
| 异常处理 | 184-217 | 全局 `Exception` handler 返回 `{code, message, data}` + trace_id；404 与 RateLimitExceeded 单独处理 |
| 中间件栈 | 286-316 | Trace / SecurityHeaders / SlowAPI / OriginCheck / RequestSizeLimit |
| 路由注册 | 322-410 | 18 个 `app.include_router(...)` 调用；每条 try/except 包裹以容忍单路由失败 |
| 内联路由 | 411-10520 | 约 200+ `@app.get/post/...` 直接定义在 `main.py` 中，覆盖用户、进度、苏格拉底、聊天、v2 智能体、课程管线、媒体、课堂、HTML 页面、静态资源 |
| 启动 banner | 10539 | `if __name__ == "__main__": ...` |

### 路由组织（`app/api/*`）

23 个 FastAPI `APIRouter` 模块按职责拆分：

| 文件 | 前缀 | 一行职责 |
|---|---|---|
| `__init__.py` | `/api/v2` | 伞路由，挂 tts/asr/grading/teacher_chat/ppt |
| `agent_orchestration.py` | （无）| MasterController HTTP 控制塔 |
| `asr.py` | `/asr` | 语音识别（Baidu + Whisper 代理）|
| `auth.py` | `/api/auth` | 登录/注册/刷新令牌 |
| `bilibili.py` | `/api/bilibili` | B 站视频解析、播放流、字幕导入 |
| `classroom.py` | `/api/classroom` | Demo 课堂会话读取/流式 |
| `courses.py` | `/api/courses` | 课程 CRUD + B 站 playlist 导入 |
| `datacenter.py` | `/api/datacenter` | 教师工作台汇总 |
| `demo_path.py` | `/api/demo` | P0 Task 12 演示路径触发 |
| `evaluation.py` | `/evaluation` | 学习评估指标 |
| `grading.py` | `/grade` | 代码/测验评分 |
| `health.py` | （根）| `/health`、`/healthz`、`/ready` |
| `kb.py` | `/api/kb` | KB 摄取 + 内容层 |
| `learning_path.py` | `/api/learning-path` | 实时学习路径生成/更新 |
| `mascot.py` | `/mascot` | "小星" AI 助手 SSE 端点 |
| `memory.py` | `/memories` | 长期记忆 CRUD |
| `ppt.py` | `/ppt` | PPT 生成/流式 |
| `profile.py` | `/profile` | 学习画像读写 |
| `seed_media.py` | `/api/seed` | 火山方舟 image/video 生成 |
| `teacher.py` | `/api/teacher` | 教师端点（班级、考试、内容）|
| `teacher_chat.py` | `/teacher` | 教师 AI 对话 |
| `telemetry.py` | （无）| 前端批量遥测上报 |
| `tts.py` | `/tts` | 文本转语音 |

### 启动期副作用

`lifespan` 启动时会做（按顺序）：

1. backend 一致性检查（`verify_backend_consistency`，legacy/ORM 同表对比）
3. `init_db()`（`app/core/database.py:42`，异步创建所有表）
4. KB `_COUNTER` hydrate（`app/models/knowledge_node.py`，节点 ID 自增）
5. Demo 种子（`app/services/demo_seeder.py` + `course_seeder.py`）
6. `HealthWorker` 启动（`app/core/health_worker.py`，Qdrant + Redis 健康探测）
7. APScheduler 每日任务（记忆整合 03:00、drift 04:00）

任何一步失败仅记日志，不阻塞启动。

### 关键 SSE 端点

| 端点 | 用途 | 流式事件类型 |
|---|---|---|
| `/api/teacher/chat` | 教师 AI 对话 | text_delta / action / function_call / function_result / done |
| `/api/agents/execute` | MasterController 执行 | heartbeat / memory_card / agent_step / profile_updated / product_ready / error / pipeline_complete |
| `/api/v2/course/chat/stream` | 课程对话 | text_delta / action / done |
| `/api/v2/course/discussion/stream` | 课堂讨论 | text_delta / done |
| `/api/v2/course/bundle/generate/stream` | 课程包生成 | progress / slide / done |
| `/api/v2/classroom/stream` | 课堂流 | text_delta / action / done |
| `/mascot/chat/stream` | 小星对话 | text_delta / action / done |

所有 SSE 路由在 `RequestSizeLimitMiddleware` 的 `STREAMING_ENDPOINTS` 白名单内，允许较大 body。

### 异常响应格式

```json
{
  "code": 1001,
  "message": "user not found",
  "data": null,
  "trace_id": "00-aabbcc...-1234-01"
}
```

`code` 由全局 `Exception` handler（`main.py:184`）赋值；`trace_id` 来自 W3C trace context。

### 启动方式

```bash
# 方式 1：直接跑 main.py
python main.py

# 方式 2：uvicorn + reload（开发）
uvicorn main:app --reload --port 8000

# 方式 3：包装脚本
python scripts/start_server.py
```

Windows 安装包使用 `packaging/launcher.py`（嵌入 CPython + uvicorn）启动。

## 代码定位

- FastAPI 实例：`main.py:172`
- Lifespan：`main.py:100-180`
- 异常处理：`main.py:184-217`
- 中间件：`main.py:286-316`
- 路由注册：`main.py:322-410`
- 内联路由起点：`main.py:411`
- 启动 banner：`main.py:10539`

## 常见坑

- **单体增长护栏**：CI 中 `agents-size-net` job 限制 `agents.py` 单次增长 ≤ 50 行；`main.py` 无此护栏，但仍是 P1 收敛目标
- **路由注册 try/except**：每个 `app.include_router` 包在 try 里，单路由失败不阻塞应用启动；调试时要看日志
- **HTML 页面硬编码**：`main.py` 内含 30+ 静态 HTML 路由（`@app.get("/login.html")` 等）；新增页面优先放 `static/html/` + `app.mount("/static")`）

## 相关链接

- [架构设计.md](架构设计.md) — 总架构
- [数据层与迁移.md](数据层与迁移.md) — 仓储与数据库
- [可观测性与安全.md](可观测性与安全.md) — Trace + 中间件
- [部署与运维.md](部署与运维.md) — 启动命令与 systemd
```

- [ ] **Step 2: 自检**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
grep -c "^## " docs/后端服务.md       # 应 ≥6
grep -c "main.py:" docs/后端服务.md    # 应 ≥10（多个代码定位）
```

- [ ] **Step 3: 提交**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add docs/后端服务.md
git commit -m "docs: 新增 后端服务.md（main.py 单体结构 + 路由组织 + 启动副作用）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Task 5: 写 `docs/前端架构.md`

**Files:**
- Create: `docs/前端架构.md`

- [ ] **Step 1: 写文档**

创建 `docs/前端架构.md`：

```markdown
# 前端架构

## 摘要

本文档描述星识 Star-Learn 前端：原生 HTML/CSS/JS（无构建工具）、Alpine.js + Tailwind CDN、6 套 OKLCH 主题、32 个 HTML 页面、76 个 JS 文件、60 个 CSS 文件。理解页面加载顺序、CSS 分层、主题系统，可以快速定位 UI 行为。

## 前置知识

- [项目说明.md](项目说明.md) — 入口

## 内容

### 设计原则

- **零构建**：HTML/CSS/JS 全部由 FastAPI `app.mount("/static", ...)` 直接服务；不引入 webpack/vite
- **Alpine.js 为主框架**：`alpinejs.min.js` 本地副本 + CDN `<script defer>` 双轨
- **Tailwind CDN**：JIT runtime 加载；CSS 也提供预生成副本
- **设计令牌优先**：所有颜色/阴影/饱和度源自 `tokens.css`（HCL 三元组 → OKLCH 标度 → 语义令牌）

### 文件组织

```
static/
├── html/       32 个 HTML 页面（登录 → 教师管理）
├── js/         76 个 plain JS 文件
│   └── pages/  7 个页面级 JS（教师 / 数据大屏 / 登录等）
├── css/        60 个 CSS 文件（tokens → app-base → theme → components → page）
├── audio/      20 首免版税背景音乐 .mp3
├── video/      （空，README 说明格式）
├── wallpaper/
│   ├── dynamic/  2 个 .webm 循环视频
│   └── static/   3 个 .png / .webp 静态图
└── demo/       5 个课程封面 SVG
```

### 32 个 HTML 页面

| 类别 | 页面 |
|---|---|
| 公共 | `index.html`（营销）/ `login.html` / `register.html` |
| 学习中枢 | `hub.html`（主面板）/ `personal.html` / `settings.html` |
| 课程 | `courses.html` / `my-courses.html` / `course-learn.html` / `generated-courses.html` / `generation-preview.html` |
| 课堂 | `classroom.html` / `classroom-premium-preview.html` |
| 学习数据 | `calendar.html` / `progress.html` / `data-dashboard.html` / `flow-meter.html` / `plant.html` / `assessment.html` |
| 代码 | `code.html`（Monaco IDE）/ `ai-pair-programming.html` |
| 智能体 | `socratic-ai.html` / `concept-analyzer.html` / `architecture-blueprint.html` / `agent-orchestration.html` |
| 展示 | `stellar-showcase.html` / `pixel-pet-game.html` |
| 教师 | `teacher-dashboard.html` / `teacher-class.html` / `teacher-content.html` / `teacher-exam.html` / `teacher-manage.html` |

### CSS 分层

```
tokens.css                ← 单一来源：HCL → OKLCH 标度 → 语义令牌
tailwind.css              ← Tailwind 工具类（CDN + 预生成副本）
tailwind-input.css        ← Tailwind 输入侧
app-base.css              ← 全局 reset + 排版 + 布局原语
app-bg.css                ← 页面背景
theme-bg.css              ← 主题背景（[data-theme] 选择器）
theme-modal.css           ← 模态框主题
animations.css            ← 关键帧 + 过渡
loading.css               ← 加载态
components.css            ← 主聚合（components-* 一并引入）
components-{navbar,cards,buttons,forms,glass,modals,badges,kanban,toast,utilities,theme-settings,slide-player}.css
<page>.css                ← 页面级样式
scheme-{star,bamboo,sakura,ocean,twilight}.css
```

加载顺序（被 `audit_compound_selectors.py` + `fix_css_load_order.py` 强制）：tokens → tailwind → app-base → bg → components → animations → page → theme。

### 主题系统（6 套）

- 默认：`star`（scheme-star.css）
- 备选：`bamboo` / `sakura` / `ocean` / `twilight`
- 切换方式：HTML 根元素 `data-theme="<id>"`，由 `theme.js` 持久化到 localStorage
- 设计令牌：`tokens.css` 定义 `--_brand-h/c/l`、`--_success-*`、`--_shadow-strength` 等，通过 `oklch()` + `color-mix()` 派生 6 套

### Alpine.js 用法

每个 HTML 页面通过 `x-data="..."` 绑定 Alpine 组件；组件逻辑写在同名 `.js` 中，挂 `window.<Name>`：

```html
<div x-data="loginPage">
  <form @submit.prevent="submit()">
    <input x-model="username" />
    <button :disabled="loading">登录</button>
  </form>
</div>
<script src="/js/pages/login.js"></script>
```

`alpinejs.min.js` 是 vendored 副本（local first），CDN 是 fallback。

### Tailwind CDN

```html
<script src="https://cdn.tailwindcss.com"></script>
```

JIT 模式按需生成工具类；同时提供 `tailwind.css`（预生成）兜底。

### 测试

- **Vitest（unit）**：`tests/frontend/unit/*.test.js`，jsdom 环境
- **Playwright（e2e）**：`tests/frontend/e2e/*.spec.js`，chromium + mobile-chrome
- **Playwright a11y**：`tests/frontend/a11y/a11y.spec.js`，axe-core
- 视觉快照：`tests/frontend/e2e/visual.spec.js-snapshots/`（16 PNG）

## 代码定位

- 静态资源挂载：`main.py:319`（`app.mount("/static", StaticFiles(...))`）
- HTML 路由：`main.py:859-...`（30+ 内联路由）
- CSS 入口：`static/css/components.css`（主聚合）
- 设计令牌：`static/css/tokens.css`
- 主题切换：`static/js/theme.js`
- Alpine 组件：每个 HTML 的同名 `.js`

## 常见坑

- **加载顺序错乱**：CSS 写错顺序会被 `audit_compound_selectors.py` 警告；新页面必须按 tokens → app-base → bg → components → animations → page → theme
- **Tailwind 工具类 vs 令牌**：能用 CSS 变量（`var(--_brand-h)`）就优先用，避免 Tailwind 工具类冲突主题切换
- **Alpine 全局命名空间**：组件必须挂 `window.<NamePascalCase>`；同名组件会冲突

## 相关链接

- [项目说明.md](项目说明.md)
- [测试体系.md](测试体系.md) — Vitest + Playwright
- [部署与运维.md](部署与运维.md) — Nginx 与静态资源代理
```

- [ ] **Step 2: 自检**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
grep -c "^## " docs/前端架构.md        # 应 ≥6
grep -c "tokens.css\|alpine" docs/前端架构.md  # 应 ≥2
```

- [ ] **Step 3: 提交**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add docs/前端架构.md
git commit -m "docs: 新增 前端架构.md（HTML/CSS/JS 组织 + Alpine/Tailwind + 6 主题）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Task 6: 写 `docs/智能体与流水线.md`

**Files:**
- Create: `docs/智能体与流水线.md`

- [ ] **Step 1: 写文档**

创建 `docs/智能体与流水线.md`：

```markdown
# 智能体与流水线

## 摘要

本文档描述星识 Star-Learn 的多智能体层：9 个 V1 legacy Agent（agents.py）+ 3 个 V2 命名实体 Agent（app/agents/）+ MasterController 编排链 + tutor_engine 新流水线（InputGateway → IntentRouter → SocraticEngine → OutputGateway）。理解 Agent 注册、编排图、消息契约（AgentEnvelope），可以扩展新 Agent 或修改编排。

## 前置知识

- [架构设计.md](架构设计.md) — 总架构图
- [后端服务.md](后端服务.md) — main.py 单体与路由

## 内容

### V1 Agent 注册（agents.py）

`agents.py:33 BaseAgent(ABC)` 是抽象基类，提供 `name` / `description` / `enabled` 属性与 `async def run(state, **kwargs)` 接口。9 个具体 Agent：

| Agent | 行号 | 角色 |
|---|---|---|
| `ProfilerAgent` | `agents.py:62` | 画像分析（更新 6 维雷达：knowledge_mastery / weakness / cognitive_style / focus_level / learning_goals） |
| `PlannerAgent` | `agents.py:316` | 任务规划，输出 `PlannerOutput(content_types)` |
| `DocumentGeneratorAgent` | `agents.py:396` | 富文本讲义生成 |
| `MindmapGeneratorAgent` | `agents.py:447` | Mermaid 思维导图生成 |
| `ExerciseGeneratorAgent` | `agents.py:514` | 练习题变体生成 |
| `VideoContentAgent` | `agents.py:569` | 视频内容推荐 |
| `ResourcePushAgent` | `agents.py:599` | 学习资源推送 |
| `EvaluationAgent` | `agents.py:629` | 学习效果评估 |
| `SocraticEvaluatorAgent` | `agents.py:667` | 苏格拉底式问答（5 种 persona × socratic_intensity） |
| `EchoAgent` | `agents.py:1276` | 入门回显 |
| `FlashcardAgent` | `agents.py:1379` | 闪卡（注册但默认不在流水线）|

### MasterController 编排

`agents.py:1116 MasterController` 是链式编排器，`create_default_controller()`（`agents.py:1698`）工厂方法构建默认实例。`main.py:3745 get_controller()` 懒加载单例。

执行图：

```mermaid
graph LR
    Echo[EchoAgent<br/>仅 on_login] --> Profiler[ProfilerAgent]
    Profiler --> Planner[PlannerAgent]
    Planner --> Router{route_generators<br/>按 content_types}
    Router --> DocGen[DocumentGenerator]
    Router --> MindmapGen[MindmapGenerator]
    Router --> ExerciseGen[ExerciseGenerator]
    Router --> VideoGen[VideoContent]
    DocGen & MindmapGen & ExerciseGen & VideoGen --> ResourcePush[ResourcePushAgent]
    ResourcePush --> Evaluation[EvaluationAgent]
```

`route_generators` 路由规则（`agents.py` 内）：

- `ContentType.TEXT / DOCUMENT` → DocumentGenerator
- `ContentType.MERMAID / MINDMAP` → MindmapGenerator
- `ContentType.EXERCISE / CODE` → ExerciseGenerator
- `ContentType.VIDEO` → VideoContent
- `dialogue_type == "confusion"` → DocumentGenerator 强制前置
- 默认 → DocumentGenerator

并行执行（`asyncio.gather`）但**所有生成器共享同一个 `state` 对象**（通过 `state.__dict__.update(state_local.__dict__)`），依赖 `_GENERATOR_OUTPUT_KEYS` 查找表避免键冲突。

### V2 命名实体 Agent（app/agents/）

| Agent | 文件 | 角色 |
|---|---|---|
| `RecommendAgent` | `app/agents/recommend.py` | 可解释推荐（M2.1，离线、确定性） |
| `AuditAgent` | `app/agents/audit.py` | 越狱 + 防幻觉 4 层防御（M2.2） |
| `CriticAgent` | `app/agents/critic.py` | L3 独立评审（M4.4） |

`io_schema.py` 定义消息契约：

```python
class AgentRole(str, Enum):
    PROFILER = "profiler"
    PLANNER = "planner"
    SOCRATIC = "socratic"
    RECOMMEND = "recommend"
    CRITIC = "critic"
    AUDIT = "audit"

@dataclass
class AgentEnvelope:
    trace_id: str
    role: AgentRole
    payload: dict
    latency_ms: int = 0
    fallback: bool = False   # LLM/KB 不可用时为 True
    provider: str = ""       # 调用来源（ark/qwen/human）
    error: str = ""
```

`wrap_agent_call` 装饰器在 `io_schema.py` 末尾，可在不修改 `agents.py` 的情况下为旧 Agent 注入 Envelope。

### tutor_engine 新流水线

`app/services/tutor_engine/` 是替代旧 MasterController 的新流水线（M3 起逐步上线）：

| 文件 | 角色 |
|---|---|
| `pipeline_gate.py` | 主流程 `InputGateway → IntentRouter → SocraticEngine → OutputGateway` |
| `engine.py` | `TutorDecisionEngine` 主类 |
| `hallucination_guard.py` | 防幻觉守门（v2 模式由 `GUARD_V2_MODE` 控制） |
| `context_aggregator.py` | 上下文聚合（5 维画像 + 记忆 + 知识） |
| `capability_aggregator.py` | 能力画像聚合 |
| `link_recommender.py` | 链接推荐 |
| `mascot_adapter.py` | 适配 mascot（小星）SSE 协议 |
| `proactive_advisor.py` | 主动推送建议 |
| `response_composer.py` | 响应组装 |
| `action_ledger.py` | 动作账本（追踪 UI action） |

切换控制：环境变量 `GUARD_V2_MODE = off | shadow | enforce`（默认 `enforce`）。

### 5 种教师 Persona（app/services/teacher/personas.py）

| ID | 名称 | socratic_intensity | 默认 |
|---|---|---|---|
| `patient_tutor` | 陈默 | 0.4 | — |
| `socratic_questioner` | 林问 | 1.0 | — |
| `energetic_lecturer` | 周燃 | 0.1 | — |
| `expert_mentor` | 严铮 | 0.7 | **✓** `DEFAULT_PERSONA_ID` |
| `caring_counselor` | 苏语 | 0.0 | —（含 crisis_keywords：自残/自杀/想死 等） |

`PersonaManager.build_system_prompt(intensity)` 按强度动态注入苏格拉底规则（强度带：0.0 / ≤0.2 / ≤0.5 / ≤0.8 / >0.8）。

### 安全：4 层防御

| 层 | 模块 | 触发 |
|---|---|---|
| L0 越狱 | `app/services/safety/jailbreak_detector.py` | 正则扫描 < 50ms |
| L1 引用锚定 | `app/agents/audit.py:_check_hallucination` | 检查知识源存在 |
| L2 长度/模板 | 同上 | 输出形态检测 |
| L3 综合评分 | `AuditAgent.run` 聚合 | 返回 `AuditResult` |

L0 阈值：jailbreak_score ≥ 0.7 拦截；hallucination_score ≥ 0.6 拦截。

## 代码定位

- V1 抽象基类：`agents.py:33`
- MasterController：`agents.py:1116`
- 工厂方法：`agents.py:1698`
- 全局单例：`main.py:3745`
- V2 Agent：`app/agents/{recommend,audit,critic}.py`
- 消息契约：`app/agents/io_schema.py`
- 新流水线：`app/services/tutor_engine/pipeline_gate.py`
- Persona 注册：`app/services/teacher/personas.py`
- 安全：`app/services/safety/jailbreak_detector.py`

## 常见坑

- **并行生成器共享 state**：Document / Mindmap / Exercise / Video 并行写 `state`，依赖 `_GENERATOR_OUTPUT_KEYS` 表保证键不冲突；扩展新生成器时必须更新该表
- **Agent 名 vs class 名**：前端 `_AGENT_DISPLAY` 字典（`app/api/agent_orchestration.py`）独立维护一份"显示名 ↔ icon ↔ content_type"映射；改名要同步
- **`SocraticEvaluatorAgent` 在 catalog 但不在默认流水线**：通过 `app/api/agent_orchestration.py:GET /api/agents/catalog` 暴露，但 MasterController 默认不调用；要手动加
- **V1/V2 混用**：`main.py` 内联路由直接 `from agents import ProfilerAgent`（V1），`app/services/tutor_engine/` 调用 `app/agents/audit.py`（V2）；切勿假设一个端点走的是哪条路
- **`PersonaManager.auto_select()` 不选 `caring_counselor`**：仅 `app/services/teacher/persona_selector.py::auto_select_persona()`（带 emotion 分支）可选 `caring_counselor`

## 相关链接

- [架构设计.md](架构设计.md)
- [后端服务.md](后端服务.md)
- [子系统详解.md](子系统详解.md)
- [可观测性与安全.md](可观测性与安全.md)
```

- [ ] **Step 2: 自检**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
grep -c "^## " docs/智能体与流水线.md       # 应 ≥6
grep -c "MasterController\|tutor_engine" docs/智能体与流水线.md  # 应 ≥4
```

- [ ] **Step 3: 提交**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add docs/智能体与流水线.md
git commit -m "docs: 新增 智能体与流水线.md（9 V1 + 3 V2 + MasterController + tutor_engine）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Task 7: 写 `docs/子系统详解.md`

**Files:**
- Create: `docs/子系统详解.md`

- [ ] **Step 1: 写文档**

创建 `docs/子系统详解.md`：

```markdown
# 子系统详解

## 摘要

本文档按子系统维度梳理星识 Star-Learn 的核心能力：课程中心、课堂会话、代码工坊、知识图谱、心流共振仪、生态养成（宠物/植物/成就）、学习路径、记忆系统、演示路径。理解每个子系统的入口端点、关键服务、数据表，可以快速进入对应模块二次开发。

## 前置知识

- [架构设计.md](架构设计.md)
- [智能体与流水线.md](智能体与流水线.md)

## 内容

### 1. 课程中心

| 项 | 定位 |
|---|---|
| 入口 | `/api/courses`、`/api/v2/course/...` |
| 页面 | `courses.html` / `my-courses.html` / `course-learn.html` / `generated-courses.html` / `generation-preview.html` |
| 服务 | `app/services/course_*.py`（brainstorm / bundle / import / learn_content / schemas / seeder / service） |
| 库 | `libs/course.py`（CourseGenerator，124KB，LLM 驱动课程生成） |
| 模型 | `Subject` → `Course` → `Chapter` → `SubChapter` → `KnowledgePoint`；`SceneOutline` → `Slide` |
| 关键能力 | 9 组件 bundle 生成（outline / plan / PPT / graph / radar / project / case / exercises / survey）；B 站视频导入 |

### 2. 课堂会话

| 项 | 定位 |
|---|---|
| 入口 | `/api/classroom`、`/api/v2/classroom/stream`、`/api/v2/course/discussion/stream` |
| 页面 | `classroom.html` / `classroom-premium-preview.html` |
| 服务 | `app/services/teacher/`（personas / pipeline / grading / ensemble_grading / discussion_roles） |
| 模型 | `ClassroomSession`（含 `teacher_persona`） / `QuizRecord`（含 4 维评分：knowledge / ability / process / innovation） / `AgentTurnRecord` |
| 关键能力 | 5 种教师 Persona 实时对话；课堂闪卡；测验评分（单评 + 集成评） |

### 3. 代码工坊

| 项 | 定位 |
|---|---|
| 入口 | `/api/run_code`、`/api/quiz/grade`、`/api/v2/grade/batch` |
| 页面 | `code.html`（Monaco IDE）/ `ai-pair-programming.html`（AI 结对编程舱）|
| 服务 | `app/services/sandbox/`（代码执行沙箱）；`libs/course.py:grade_quiz_answers()` |
| 前端 | `code.js` / `code-ide.js` / `code-monaco.js` / `code-coach.js` / `code-output-tabs.js` / `slide-v2-adapter.js` / `openmaic-slide-player.js` |
| 关键能力 | Monaco 编辑器、实时运行、AI 评审、批量出题、错题本；`openmaic-slide-player` 全息视界播放器 |

### 4. 知识图谱

| 项 | 定位 |
|---|---|
| 入口 | `/api/knowledge/nodes`、`/api/knowledge/review`、`/api/knowledge/analyze-relations` |
| 服务 | `app/services/kb/`（ingestion / semantic_kb / qdrant_client / citation_retriever / source_ref / splitter / fallback_queue） |
| 模型 | `KnowledgeNode`（含 `M2 KB-CON-XXXX` 编号，KB `_COUNTER` hydrate）/ `KnowledgeRelation`（src/dst）/ `KnowledgeReview` / `KnowledgeRecord` |
| 外部 | Qdrant 1.9（向量库，可选）|
| 关键能力 | 摄取 + 向量化 + 关系分析 + 复习调度（SM2 间隔重复） |

### 5. 心流共振仪

| 项 | 定位 |
|---|---|
| 入口 | `/api/focus/save`、`/api/focus/record`、`/api/focus/quiz`、`/api/focus/analysis/{user_id}` |
| 页面 | `flow-meter.html` / `calendar.html` |
| 前端 | `flow-meter.js` / `focus-calendar.js` / `focus-sync.js` / `focus-quiz-intervention.js` / `focus-analysis.js` |
| 模型 | `FocusSession` → `FocusEvent`；`UserFocusHistory` |
| 关键能力 | 专注度实时监测 + 测验中断 + 日历视图 |

### 6. 生态养成

| 项 | 定位 |
|---|---|
| 入口 | `/api/pet/save`、`/api/garden/save`、`/api/achievements/save` |
| 页面 | `plant.html`（植物林场）/ `pixel-pet-game.html`（星宝宠物）|
| 前端 | `plant.js` / `pixel-pet-game.js` / `achievement-manager.js` / `achievements-data.js` |
| 模型 | `UserGarden` / `UserPet` / `UserAchievement` / `UserEcoData`（均 1:1 per user）|
| 关键能力 | 专注→植物生长；学习→宠物升级；累积成就 |

### 7. 学习路径与每日路线

| 项 | 定位 |
|---|---|
| 入口 | `/api/learning-path`、`/api/daily-route/generate`、`/api/daily-route/complete`、`/api/daily-route/status` |
| 服务 | `app/services/learning_path/`（forgetting_curve / llm_analyzer / review_scheduler / rule_engine） |
| 模型 | `LearningPath` → `LearningPathNode`；`DailyRoute`；`CourseDeadline`；`DeadlineTracker` |
| 关键能力 | 每日学习路线、SM2 间隔重复、目标差距分析 |

### 8. 记忆系统

| 项 | 定位 |
|---|---|
| 入口 | `/memories`、`/api/memory/...` |
| 服务 | `app/services/memory/`（extractor / retriever / search / scheduler / clustering / consolidator / episodic / lifecycle / llm_extractor） |
| 模型 | `SemanticMemory` / `EpisodicMemory` / `MemoryConsolidationJob` |
| 关键能力 | 双路召回（语义 + 情节）+ RRF 融合；每日 03:00 cron 整合 |
| 特性开关 | `MEMORY_V2 = on/off`（默认 `on`；`off` 时回退旧版 200 条全量扫）|

### 9. 演示路径

| 项 | 定位 |
|---|---|
| 入口 | `/api/demo`、`/api/v2/course/bundle/generate/stream` |
| 服务 | `app/services/demo_runner/` |
| 触发器 | `app/api/demo_path.py` |
| 关键能力 | P0 Task 12 直播演示路径一键触发（5 分钟内展示完整学习闭环）|

### 10. 小星（Mascot）

| 项 | 定位 |
|---|---|
| 入口 | `/mascot/chat/stream`、`/mascot/checkin`、`/mascot/stats/{user_id}`、`/mascot/capability/{user_id}` |
| 服务 | `app/services/mascot/`（persona / dialogue） |
| 前端 | `mascot-core.js` / `mascot-panel.js` / `mascot-services.js` |
| 关键能力 | 页面级 AI 伙伴，warm + emoji + 苏格拉底倾向；输出含 `[navigate:...]` `[expression:...]` 命令 |
| 引擎 | `TutorDecisionEngine`（v2）/ `mascot/llm_service`（v1）双路径 |

## 代码定位

- 子系统服务总览：`app/services/`（50+ 文件 / 15 子包）
- 模型表清单：[数据层与迁移.md](数据层与迁移.md)
- 路由前缀表：[架构设计.md](架构设计.md)
- 智能体注册：[智能体与流水线.md](智能体与流水线.md)

## 常见坑

- **子系统边界模糊**："课堂" 与 "课程" 都用 `classroom.html` / `course.html`；前者是会话、后者是聚合
- **`_run_*` 内联路由**：`main.py` 内含 `/api/focus/record` 等内联路由；不在 `app/api/` 中
- **记忆 v1/v2 切换**：通过 `MEMORY_V2` env 控制；线上默认 v2，回滚需重启

## 相关链接

- [架构设计.md](架构设计.md)
- [智能体与流水线.md](智能体与流水线.md)
- [数据层与迁移.md](数据层与迁移.md)
- [演示现场手册.md](演示现场手册.md)
```

- [ ] **Step 2: 自检**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
grep -c "^### " docs/子系统详解.md       # 应 ≥10（10 个子系统）
grep -c "^## " docs/子系统详解.md        # 应 ≥6
```

- [ ] **Step 3: 提交**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add docs/子系统详解.md
git commit -m "docs: 新增 子系统详解.md（10 个子系统：课程/课堂/代码/知识图谱/心流/生态/路径/记忆/演示/小星）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Task 8: 写 `docs/数据层与迁移.md`

**Files:**
- Create: `docs/数据层与迁移.md`

- [ ] **Step 1: 写文档**

创建 `docs/数据层与迁移.md`：

```markdown
# 数据层与迁移

## 摘要

本文档描述星识 Star-Learn 的数据层：35 张数据表（含 30+ ORM 模型 + 5 个 legacy 表）、仓储双写（DualWriteRepository）、灰度切流（feature flags）、Alembic 迁移 + 8 个临时 migrate_*.py 脚本。理解数据模型、迁移策略与回滚路径，可以安全做 schema 变更。

## 前置知识

- [架构设计.md](架构设计.md) — 双层架构 + 仓储工厂
- [后端服务.md](后端服务.md) — main.py 与 lifespan

## 内容

### 数据库后端

| 后端 | 适用场景 | 连接驱动 |
|---|---|---|
| SQLite 3（默认）| 开发 / 单机 / 演示 | `sqlite+aiosqlite` |
| MySQL 5.7+ | 生产环境 | `mysql+asyncmy` / `mysql+aiomysql` |

切换方式：`.env` 中 `DATABASE_URL=sqlite+aiosqlite:///xingshi_v2.db` 或 `mysql+asyncmy://user:pwd@host/db`。

### 35 张数据表（按子包分组）

**用户与认证**（`app/models/user.py`）：`users` / `student_profiles` / `user_login_records` / `user_profile`

**聊天与消息**（`app/models/chat.py` + `app/models/message.py`）：`chat_messages` / `chat_summaries` / `chat_turn_records` / `user_memories` / `messages` / `conversation_summaries`

**课程**（`app/models/course.py`）：`subjects` / `courses` / `chapters` / `sub_chapters` / `knowledge_points` / `scene_outlines` / `slides`

**课程进度**（`app/models/course_progress.py`）：`course_progress` / `learning_paths` / `learning_path_nodes` / `user_evaluations` / `course_generation_status` / `course_deadlines` / `daily_routes`

**课堂**（`app/models/classroom.py`）：`classroom_sessions` / `quiz_records` / `agent_turn_records`

**学习统计**（`app/models/learning.py`）：`study_sessions` / `learning_records` / `user_stats` / `learning_goals` / `weekly_summaries` / `user_learning_profile` / `user_evaluation_metrics`

**知识图谱**（`app/models/knowledge.py` + `knowledge_node.py`）：`knowledge_nodes` / `knowledge_relations` / `knowledge_reviews` / `knowledge_records` / `knowledge_pending` / `review_history`

**专注度**（`app/models/focus.py`）：`focus_sessions` / `focus_events` / `user_focus_histories`

**生态养成**（`app/models/gamification.py`）：`user_gardens` / `user_pets` / `user_achievements` / `user_eco_data`

**偏好**（`app/models/preferences.py`）：`user_preferences` / `user_settings` / `user_themes`

**记忆**（`app/models/semantic_memory.py` + `episodic_memory.py` + `memory_consolidation_job.py`）：`semantic_memories` / `episodic_memories` / `memory_consolidation_jobs`

**审计**（`app/models/drift_report.py` + `weakness_timeline.py` + `deadline.py` + `supervision.py` + `agent_behavior_log.py`）：`drift_reports` / `weakness_timelines` / `deadline_trackers` / `supervision_rules` / `supervision_events` / `agent_behavior_logs`

### 仓储双写（DualWriteRepository）

`app/repositories/dual_write.py` 实现"primary + shadow"装饰器：

- **写路径**：所有调用先走 primary（ORM），成功后异步尝试 shadow（legacy）；primary 失败立即抛错，shadow 失败仅记日志
- **读路径**：由 `app/core/repository_factory.py:get_repository_for_user(user_id, type)` 按 feature flag 选择 ORM 或 legacy
- **失败语义**：primary 失败 → 抛错（生产真源）；shadow 失败 → 日志（不重试，TODO: Redis 队列）

### Feature Flags（`app/core/feature_flags.py`）

| Flag | 类型 | 默认 | 作用 |
|---|---|---|---|
| `ORM_ENABLED` | bool | true | 主开关；false → 全走 legacy |
| `READ_BACKEND_PERCENTAGE` | 0-100 | 0 | 读路径灰度（md5 bucket 稳定分桶）|
| `DUAL_WRITE_LEGACY` | bool | false | 双写开关 |
| `GUARD_V2_MODE` | off/shadow/enforce | enforce | 防幻觉守门模式 |
| `MEMORY_V2` | bool | true | 记忆 v2 开关 |
| `SELF_CHECK_ENABLED` | bool | true | 置信度边界 [0.55, 0.75) 二次校验 |
| `EMBEDDING_PROVIDER` | auto/local/api/hash | auto | Embedding 服务降级链 |

所有非法值静默回退默认。

### Alembic 迁移

```
alembic.ini
alembic/
├── env.py             # 异步 runner（auto-detect +async / aiomysql / asyncpg）
├── script.py.mako     # 标准模板
└── versions/
    ├── b01b4224a404_initial_users_student_profiles_courses_.py
    ├── 20260529_add_subjects_chapters_subchapters.py
    └── 20260720_add_demo_flags_and_lecture_fields.py
```

执行：

```bash
alembic upgrade head      # 应用所有迁移
alembic downgrade -1      # 回滚一步
alembic current           # 当前版本
```

### 临时迁移脚本（`scripts/`）

- `migrate_add_subject_columns.py` — Subject/Chapter 列补齐
- `migrate_add_user_memories.py` — user_memories 表创建
- `migrate_local_storage_to_v2.py` — JSON 本地存储 → DB
- `migrate_messages_metadata.py` — messages.metadata 列
- `migrate_user_id_to_varchar.py` — INT → VARCHAR(64)
- `migrate_user_table.py` — users 表统一
- `reconcile_databases.py` — ORM ↔ legacy 一致性
- `init_xingshi_v2_mysql.sql` — 原始 MySQL DDL bootstrap

这些脚本在 Alembic 不可用时使用（如旧 DB）；新表改 schema 优先走 Alembic。

### 健康检查与一致性

`db.py:verify_backend_consistency` 在 lifespan 启动期运行：抽样关键表，对比 legacy 与 ORM 行数 / 字段。`BackendUnavailable` 异常表示不一致，不再静默 fallback（生产真源语义）。

### 修复工具

- `scripts/fix_database.py` — 自动检测/修复缺表缺列
- `scripts/fix_db_schema.py` — ALTER TABLE 补丁（legacy SQLite）
- `scripts/fix_p0_tech_debt.py` — 数据驱动 P0 修复（CSS 变量回填等）

## 代码定位

- ORM 模型：`app/models/*.py`（22 个文件）
- Base：`app/models/base.py`
- 数据库连接：`app/core/database.py`
- 仓储抽象：`app/repositories/base.py`
- 仓储实现：`app/repositories/{legacy,orm}/*.py`
- 工厂：`app/core/repository_factory.py`
- 双写：`app/repositories/dual_write.py`
- 特性开关：`app/core/feature_flags.py`
- 启动建表：`app/core/database.py:42 init_db()`

## 常见坑

- **Schema 漂移**：ORM 模型与 legacy 字段不完全一致；`verify_backend_consistency` 启动期会告警
- **迁移幂等**：Alembic migration 必须可重复跑；运行前检查 `alembic current`
- **数据双写未做**：legacy DB 不在 dual_write 范围内的表（如新加的 v2 表）只走 ORM；切 MySQL 时这些表自动迁移
- **`_COUNTER` hydrate**：`app/models/knowledge_node.py:KnowledgeNode` 的 M2 编号 `KB-CON-XXXX` 在 lifespan 启动期 hydrate；不能跨重启保持，依赖 max(id) 推算

## 相关链接

- [架构设计.md](架构设计.md)
- [后端服务.md](后端服务.md)
- [部署与运维.md](部署与运维.md) — 迁移命令 + MySQL 切换
- [脚本索引.md](脚本索引.md) — 38 个脚本功能
```

- [ ] **Step 2: 自检**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
grep -c "^## " docs/数据层与迁移.md       # 应 ≥6
grep -c "DualWrite\|feature_flags\|Alembic" docs/数据层与迁移.md  # 应 ≥3
```

- [ ] **Step 3: 提交**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add docs/数据层与迁移.md
git commit -m "docs: 新增 数据层与迁移.md（35 表清单 + 仓储双写 + Feature Flags + 迁移）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Task 9: 写 `docs/可观测性与安全.md`

**Files:**
- Create: `docs/可观测性与安全.md`

- [ ] **Step 1: 写文档**

创建 `docs/可观测性与安全.md`：

```markdown
# 可观测性与安全

## 摘要

本文档描述星识 Star-Learn 的可观测性（W3C trace context、health 探针、Sentry 占位）与安全层（CSP / Origin / 越狱检测 / 防幻觉 / 审计）。理解 trace 流、越狱拦截逻辑、Agent 行为日志，可以快速定位线上问题与安全事件。

## 前置知识

- [架构设计.md](架构设计.md) — 中间件栈
- [智能体与流水线.md](智能体与流水线.md) — Agent 安全层

## 内容

### Trace（W3C Context，stdlib-only）

`app/core/trace.py` 实现 W3C Trace Context（`00-<32hex trace_id>-<16hex span_id>-<2hex flags>`）。无 OpenTelemetry 依赖，纯 `contextvars`。

- `TraceContext` dataclass：`trace_id` / `span_id` / `flags`
- `SpanRecorder`：记录当前 root span 的属性与状态（**有意不支持子 span**）
- `TraceMiddleware`（`app/core/middleware/trace.py`）：提取或生成 `traceparent`，写入 contextvar，响应回写 header

异常响应（`main.py:184`）中 `trace_id` 字段即来自此。

### Health 探针

- `/api/health`（`app/api/health.py`）：聚合 4 个子系统（llm / kb / db / qdrant），各仅做 import 检测（≤2s budget）
  - 规则：任一 `down` → `down`；任一 `degraded` → `degraded`；否则 `ok`
  - `qdrant` 默认跳过，需 `STARLEARN_REQUIRE_QDRANT=1` 才检查
- `/healthz`、`/ready`（`app/api/health.py`）：标准化端点（比赛模式）
- 后台 `HealthWorker`（`app/core/health_worker.py`）：Qdrant + Redis 主动探测，10 s 间隔

### 中间件安全层

| 中间件 | 文件 | 作用 |
|---|---|---|
| `SecurityHeadersMiddleware` | `app/core/middleware/security_headers.py` | CSP / X-Frame-Options / X-Content-Type-Options / HSTS（HTTPS only）|
| `OriginCheckMiddleware` | `app/core/middleware/origin_check.py` | CSRF via Origin/Referer（POST/PUT/DELETE/PATCH）|
| `RequestSizeLimitMiddleware` | `app/core/middleware/request_size.py` | DoS 防护 + SSE 路由白名单放大 |
| `SlowAPIMiddleware` | `main.py:308` | 限流 |

### 越狱检测（L0）

`app/services/safety/jailbreak_detector.py` `JailbreakDetector`：

- L0 正则扫描 < 50 ms
- L1 LLM 复核（`ENABLE_L1_JAILBREAK=1` 启用）
- 返回 `JailbreakResult(risk_score, pattern, matched_text)`
- 阈值：jailbreak_score ≥ 0.7 拦截

### 防幻觉（4 层）

`app/agents/audit.py` `AuditAgent` 4 层防御：

1. L0 越狱（已上）
2. L1 引用锚定（基于知识源是否存在）
3. L2 输出长度/模板检测
4. L3 综合评分

阈值：hallucination_score ≥ 0.6 拦截。

新流水线 `app/services/tutor_engine/hallucination_guard.py` 在 `GUARD_V2_MODE = enforce` 时生效（v2 证据融合守门）。

### 审计日志

- `app/services/audit_log.py`：append-only NDJSON 审计（输入拦截、输出替换、intent 路由、agent 决策、越狱尝试）
- `app/models/agent_behavior_log.py:AgentBehaviorLog`：Agent 执行日志表（KB 摄取）
- `app/models/supervision.py`：监督规则与事件（rules + events）

### 用户消息层

- `ChatMessage` / `Message`：聊天历史持久化
- `MemoryCardLoader`（`app/services/agent/memory_card_loader.py`）：token 预算内的每 Agent 记忆卡

### 配置安全

- 密钥：`config/config.py` 的 `Settings`（XUNFEI_API_KEY / MINIMAX_API_KEY / BAIDU_ASR_* / KLING_*）
- `.env` 文件不入 git（`.gitignore`）
- Windows 安装包：`packaging/launcher.py` 首次启动写 `%APPDATA%\StarLearn\.env`（`templates/starter.env` 模板）

## 代码定位

- Trace：`app/core/trace.py`、`app/core/middleware/trace.py`
- 中间件注册：`main.py:286-316`
- 健康检查：`app/api/health.py`
- 后台探测：`app/core/health_worker.py`
- 越狱：`app/services/safety/jailbreak_detector.py`
- 防幻觉：`app/agents/audit.py`、`app/services/tutor_engine/hallucination_guard.py`
- 审计：`app/services/audit_log.py`

## 常见坑

- **`SpanRecorder` 不支持子 span**：复杂链路 trace_id 会"折叠"；只保留根 span
- **`/api/health` 假阳性**：仅做 import 检测，无法捕获运行时错误（DB 连接中断等）；后台 `HealthWorker` 才是真实健康度
- **CSP 严格**：`SecurityHeadersMiddleware` 默认较严；新加第三方脚本（CDN）需更新 `SECURITY_HEADERS` 配置
- **`OriginCheckMiddleware` 仅 state-changing 方法**：GET 不检查；GET 路由 XSS 由 CSP 兜底
- **`jailbreak_score` 阈值漂移**：阈值写在常量里，不在配置；调阈值要改代码并回归测试

## 相关链接

- [架构设计.md](架构设计.md)
- [后端服务.md](后端服务.md)
- [智能体与流水线.md](智能体与流水线.md)
- [部署与运维.md](部署与运维.md)
```

- [ ] **Step 2: 自检**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
grep -c "^## " docs/可观测性与安全.md    # 应 ≥6
grep -c "trace\|Jailbreak\|CSP" docs/可观测性与安全.md  # 应 ≥4
```

- [ ] **Step 3: 提交**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add docs/可观测性与安全.md
git commit -m "docs: 新增 可观测性与安全.md（Trace + 中间件 + 越狱 + 防幻觉 + 审计）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Task 10: 写 `docs/外部服务依赖.md`

**Files:**
- Create: `docs/外部服务依赖.md`

- [ ] **Step 1: 写文档**

创建 `docs/外部服务依赖.md`：

```markdown
# 外部服务依赖

## 摘要

本文档列出星识 Star-Learn 依赖的所有外部服务：MiniMax（LLM / TTS 默认）、讯飞大模型（LLM 备选）、可灵 Kling（视频生成）、CogVideo（本地视频，可选）、百度 ASR、Whisper WASM（浏览器端 ASR）、Qdrant（向量库）、Redis（缓存 / 队列）。理解每个服务的用途、配置、降级路径，可以规划成本与高可用。

## 前置知识

- [架构设计.md](架构设计.md) — 总架构
- [部署与运维.md](部署与运维.md) — 环境变量

## 内容

### LLM（大模型）

| 厂商 | 服务 | 配置 | 用途 |
|---|---|---|---|
| MiniMax | MiniMax LLM | `MINIMAX_API_KEY` + `MINIMAX_GROUP_ID` | 默认 LLM，提供对话、规划、生成 |
| 讯飞 | Xunfei 大模型 | `XUNFEI_API_KEY` | 备选 LLM |

切换：当前在 `llm_stream.py` 中硬编码 MiniMax；可扩展 `config/config.py` 添加 `LLM_PROVIDER` 字段。

代码：`app/services/llm/xunfei_chat_model.py`（讯飞适配器）；`agents.py`、`libs/course.py`（通用 LLM 调用）

### TTS（文本转语音）

| 厂商 | 配置 | 用途 |
|---|---|---|
| MiniMax TTS | `MINIMAX_API_KEY` + `MINIMAX_GROUP_ID`（与 LLM 共用）| 默认 TTS，speech-2.8-hd 高清模型 |
| OpenAI 兼容 | 任意兼容端点 | 备选 |

代码：`app/services/tts/`（provider 抽象）、`app/api/tts.py`、`main.py:9876 /api/v2/generate/tts`

### ASR（语音识别）

| 厂商 | 配置 | 用途 |
|---|---|---|
| 百度短语音 | `BAIDU_ASR_API_KEY` + `BAIDU_ASR_SECRET_KEY` | 服务端 ASR |
| Whisper WASM | `@picovoice/picovoice-web` + `@timur00kh/whisper.wasm`（前端依赖） | 浏览器端 ASR，离线 |

代码：`app/services/asr/providers/{whisper,baidu}.py`、`app/api/asr.py`、`static/js/voice-input.js`

### 视频生成

| 厂商 | 配置 | 用途 |
|---|---|---|
| 可灵 Kling | `KLING_ACCESS_KEY` + `KLING_SECRET_KEY` | 文本/图像→视频（`libs/kling_api.py`，HMAC-SHA256 签名）|
| CogVideo | 本地模型 | 本地兜底（README 说明）|

代码：`libs/kling_api.py`（可灵）、`app/services/seedance_service.py` / `seedream_service.py`（火山方舟 Seedance / Seedream）

### B 站（数据源）

| 项 | 说明 |
|---|---|
| 用途 | 视频解析、CC 字幕抓取、收藏夹/合集导入课程 |
| 配置 | 无需密钥（部分 API 需登录 Cookie）；`scripts/bind_bilibili_playlists.py` 维护 |

代码：`app/services/bilibili.py`（WBI 签名 + 解析）、`app/services/bilibili_audio_asr.py`（yt-dlp + faster-whisper 兜底字幕）、`app/api/bilibili.py`、`scripts/bind_bilibili_playlists.py`、`scripts/verify_bilibili_cookie.py`

### 向量库

| 厂商 | 配置 | 用途 |
|---|---|---|
| Qdrant 1.9 | Docker（`docker-compose.dev.yml`）：master + replica | KB 内容层向量检索 |

代码：`app/services/kb/qdrant_client.py`、`app/core/health_worker.py`（探活）

### 缓存 / 队列

| 厂商 | 配置 | 用途 |
|---|---|---|
| Redis 7 | Docker（`docker-compose.dev.yml`） | agent log buffer、缓存 |

代码：`app/services/agent_log/buffer.py`

### Embedding Provider

由 `EMBEDDING_PROVIDER` env 控制：`auto | local | api | hash`（默认 `auto`）。按可用性降级链：`api → local → hash`。

### 火山方舟

| 项 | 说明 |
|---|---|
| 用途 | Seedream 图像生成、Seedance 视频生成 |
| 配置 | `ARK_API_KEY`（如需）|
| 代码 | `app/services/seedream_service.py`、`app/services/seedance_service.py`、`app/api/seed_media.py`、`libs/ark_client.py` |

## 代码定位

- 配置：`config/config.py`（LLM/ASR/Kling 密钥）
- LLM：`app/services/llm/xunfei_chat_model.py`、`llm_stream.py`（根）
- TTS：`app/services/tts/`
- ASR：`app/services/asr/providers/`
- 视频：`libs/kling_api.py`、`app/services/seedance_service.py`
- 向量：`app/services/kb/qdrant_client.py`
- B 站：`app/services/bilibili.py`、`app/api/bilibili.py`
- Ark：`libs/ark_client.py`

## 常见坑

- **密钥冗余**：LLM 与 TTS 共用 `MINIMAX_API_KEY`；单独禁用 TTS 需额外配置
- **可灵鉴权**：HMAC-SHA256 时间戳容忍 ±5 min；本地时钟漂移会导致 401
- **Qdrant 健康**：默认 `/api/health` 不检查 Qdrant（启动慢）；要 `STARLEARN_REQUIRE_QDRANT=1`
- **Embedding 降级链**：hash fallback 会显著降低 KB 召回质量；线上慎用
- **B 站 Cookie**：依赖外部登录态；定期 `verify_bilibili_cookie.py` 检查

## 相关链接

- [架构设计.md](架构设计.md)
- [部署与运维.md](部署与运维.md) — Docker Compose
- [数据层与迁移.md](数据层与迁移.md) — KB 数据模型
```

- [ ] **Step 2: 自检**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
grep -c "^## " docs/外部服务依赖.md      # 应 ≥6
grep -c "MiniMax\|Xunfei\|Kling\|Qdrant" docs/外部服务依赖.md  # 应 ≥4
```

- [ ] **Step 3: 提交**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add docs/外部服务依赖.md
git commit -m "docs: 新增 外部服务依赖.md（LLM/TTS/ASR/视频/向量/缓存/B 站/火山方舟）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Task 11: 写 `docs/部署与运维.md`

**Files:**
- Create: `docs/部署与运维.md`

- [ ] **Step 1: 写文档**

创建 `docs/部署与运维.md`：

```markdown
# 部署与运维

## 摘要

本文档描述星识 Star-Learn 的部署选项：本地开发、uvicorn 生产、MySQL 切换、Docker Compose（Qdrant + Redis）、Windows Inno Setup 一键安装包。理解启动命令、环境变量、Nginx 反代配置与故障排查路径，可以独立运维一个实例。

## 前置知识

- [项目说明.md](项目说明.md)
- [数据层与迁移.md](数据层与迁移.md)

## 内容

### 开发环境

```bash
# 1. 克隆
git clone <repo-url> && cd xingshi

# 2. 装依赖
pip install -r requirements.txt

# 3. 配置环境变量
cp config/.env.example config/.env
# 必填 MINIMAX_API_KEY + MINIMAX_GROUP_ID
# 也可填 XUNFEI_API_KEY（讯飞 LLM 备选）

# 4. 初始化数据库（默认 SQLite，无需额外依赖）
python Navicat/setup_database.py --backend=sqlite

# 5. 启动
python main.py
# 或
uvicorn main:app --reload --port 8000
# 或
python scripts/start_server.py
```

打开浏览器访问：**http://127.0.0.1:8000**

API 文档：**http://127.0.0.1:8000/docs**

### 生产环境（推荐）

```bash
# 1. 虚拟环境
python3 -m venv .venv && source .venv/bin/bin/activate
pip install -r requirements.txt

# 2. 配置
cp config/.env.example config/.env && vim config/.env
# 必改：DATABASE_URL=MySQL URL，APP_DEBUG=False

# 3. 初始化 MySQL
export MYSQL_USER=starlearn MYSQL_PASSWORD=secret
python Navicat/setup_database.py --backend=mysql
# 或跑迁移
alembic upgrade head

# 4. Systemd unit（示例）
# /etc/systemd/system/starlearn.service
[Unit]
Description=Star-Learn FastAPI
After=network.target

[Service]
User=starlearn
WorkingDirectory=/opt/xingshi
ExecStart=/opt/xingshi/.venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
Restart=always

[Install]
WantedBy=multi-user.target

# 5. 启动
sudo systemctl enable --now starlearn
```

### Nginx 反代（关键配置）

```nginx
location / {
    proxy_pass http://127.0.0.1:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}

# SSE 必须关闭缓冲
location /api/ {
    proxy_pass http://127.0.0.1:8000;
    proxy_buffering off;
    proxy_cache off;
    proxy_read_timeout 300s;
}
```

**SSE 流断开**通常是因为 `proxy_buffering on`；必须显式 `off`。

### 数据库

| 后端 | 适用场景 | 命令 |
|---|---|---|
| SQLite（默认） | 开发 / 单机 / 演示 | `python Navicat/setup_database.py --backend=sqlite` |
| MySQL 5.7+ | 生产环境 | `python Navicat/setup_database.py --backend=mysql` |
| SQL 文件 | 离线 / K8s / Docker | `mysql < docs/sql/init_mysql.sql` |
| Alembic | ORM 模型变更 | `alembic upgrade head` |

### Docker Compose（开发用，仅 Qdrant + Redis）

```bash
docker compose -f docker-compose.dev.yml up -d
```

服务：
- `qdrant-master`（port 6333）+ `qdrant-replica`（port 6334）
- `redis`（port 6379）

应用本身仍在宿主机跑 uvicorn；`docker-compose.yml` 不含 app 容器。

### Windows 一键安装包（Inno Setup）

打包流水线：

```
源码树 → packaging/stage_payload.py → packaging/app_payload/
                              ↓
            packaging/install_deps.py（嵌入 CPython）
                              ↓
                  packaging/installer.iss → Star-Learn-Setup-1.0.0.exe
```

构建命令：

```bat
packaging\build.bat
:: 或
python packaging\build_portable.py
```

安装后行为（`packaging/launcher.py`）：

1. 首次启动创建 `%APPDATA%\StarLearn\{logs,cache/audio,cache/storage,cache/agent_log_spool}`
2. 写 `starter.env` → `.env`（pinned：`STARLEARN_DB_BACKEND=sqlite`、`SQLITE_PATH`、`DATABASE_URL`、`LOCAL_STORAGE_PATH`、`XINSHI_AUDIT_LOG`、`KB_BEHAVIOR_LOG_SPOOL_DIR`）
3. 后台线程轮询 `http://127.0.0.1:8000/login.html`，30 s 后打开浏览器
4. uvicorn 进程内启动

卸载可清 `%APPDATA%\StarLearn\`（用户数据，需确认）。

### 演示内容注入（比赛专用）

```bash
python scripts/seed_demo.py --reset     # 重置 demo
python scripts/seed_demo.py --check    # 检查状态
```

Demo 课程源：`storage/seed/demo/*.json` + `manifest.json`（含 `demo_version`，升级 bump）。用户私有数据完全不受影响。

### 常见运维命令

| 目的 | 命令 |
|---|---|
| 健康检查 | `curl http://127.0.0.1:8000/api/health` |
| 看 trace 流 | 看 `trace_id` 字段跨服务串联 |
| 数据库迁移 | `alembic upgrade head` / `alembic downgrade -1` |
| Legacy ↔ ORM 对齐 | `python scripts/reconcile_databases.py` |
| 备份 | `bash scripts/backup.sh` |
| 恢复 | `bash scripts/restore.sh` |
| 健康巡检 | `bash scripts/health_check.sh` |
| 现场重置 | `bash scripts/reset_demo.sh` |
| 比赛启动 | `bash scripts/start_competition.sh` |

### 故障排查

| 现象 | 排查 |
|---|---|
| 启动 `ModuleNotFoundError` | `pip install -r requirements.txt` |
| DB 连接失败 | 检查 `.env` 的 `DATABASE_URL`；或切 SQLite |
| LLM 401 / 超时 | 检查 API Key 与网络 |
| SSE 流断开 | Nginx 必须 `proxy_buffering off` |
| 静态资源 404 | 检查 Nginx `location` 路径 |
| Windows 安装包启动失败 | 看 `%APPDATA%\StarLearn\logs\` |
| 双库不一致 | `scripts/reconcile_databases.py` 跑对齐 |

### 备份与恢复

`scripts/backup.sh`：打包 SQLite + storage 目录到 `backups/<timestamp>.tar.gz`
`scripts/restore.sh`：从 tar 解压到原路径

## 代码定位

- 启动入口：`main.py`
- 启动脚本：`scripts/start_server.py`、`scripts/start_competition.sh`
- 打包：`packaging/{stage_payload,install_deps,launcher,build_portable}.py`、`packaging/installer.iss`
- 数据库：`Navicat/setup_database.py`、`docs/sql/init_mysql.sql`
- 健康检查：`app/api/health.py`、`scripts/health_check.sh`
- 备份：`scripts/{backup,restore}.sh`

## 常见坑

- **Nginx SSE**：必须 `proxy_buffering off` + `proxy_read_timeout 300s`；否则 SSE 流立刻断开
- **`.env` 路径**：V1/V2 共用 `config/.env`；改一个文件两个 config 都受影响
- **MySQL 8 vs 5.7**：项目测试基于 5.7；MySQL 8 默认 caching_sha2_password 需 `asyncmy` 支持
- **Windows 安装包大小**：嵌入 CPython + LZMA2/ultra64 → 安装包 ~150 MB
- **APP_DEBUG**：`config/config.py` 和 `app/core/config.py` 都读；生产务必 `False`

## 相关链接

- [项目说明.md](项目说明.md)
- [数据层与迁移.md](数据层与迁移.md)
- [外部服务依赖.md](外部服务依赖.md)
- [脚本索引.md](脚本索引.md)
```

- [ ] **Step 2: 自检**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
grep -c "^## " docs/部署与运维.md        # 应 ≥6
grep -c "uvicorn\|Nginx\|Docker\|Inno" docs/部署与运维.md  # 应 ≥4
```

- [ ] **Step 3: 提交**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add docs/部署与运维.md
git commit -m "docs: 新增 部署与运维.md（dev/prod/Docker/Windows 安装包 + 故障排查）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Task 12: 写 `docs/演示现场手册.md`

**Files:**
- Create: `docs/演示现场手册.md`

- [ ] **Step 1: 写文档**

创建 `docs/演示现场手册.md`：

```markdown
# 演示现场手册

## 摘要

本文档面向答辩评委与现场演示操作员：5 分钟闭环演示路径、关键页面截图点、风险预案、网络/硬件失败回退方案。理解演示节奏与"看什么"，可以 5 分钟内展示"个人智能学习中枢"的核心亮点。

## 前置知识

- [项目说明.md](项目说明.md)
- [部署与运维.md](部署与运维.md) — 启动 + demo 重置

## 内容

### 演示 5 分钟闭环（推荐路径）

```mermaid
sequenceDiagram
    participant J as 评委
    participant U as 现场操作员
    participant App as 星识应用
    participant AI as LLM 后端

    J->>U: 1. 登录（演示账号 / 游客登录）
    U->>App: 打开 http://127.0.0.1:8000/login.html
    U->>App: 点击"游客登录" / 用 demo 账号
    App-->>U: 跳转 hub.html（个人中枢）

    U->>App: 2. 展示"AI 眼中的你"画像（personal.html）
    App-->>U: 渲染 6 维雷达 + 记忆卡

    U->>App: 3. 触发课程生成（courses.html → generated-courses.html）
    App->>AI: /api/v2/course/bundle/generate/stream
    AI-->>App: 流式输出大纲 / PPT / 思维导图
    App-->>U: 实时渲染进度条 + 章节卡片

    U->>App: 4. 进入课堂（classroom.html）
    App->>AI: /api/v2/classroom/stream
    AI-->>App: text_delta + action（spotlight / wb_draw_svg）
    App-->>U: 苏格拉底式对话 + 板书

    U->>App: 5. 展示小星（任意页面右下角 mascot）
    App->>AI: /mascot/chat/stream
    AI-->>App: 鼓励语 + 链接
    App-->>U: 表情 + 跳转建议
```

### 演示路径详细步骤

**准备**：

```bash
bash scripts/reset_demo.sh    # 重置 demo 数据
python main.py &              # 启动应用
```

**第 1 步 · 登录（30 s）**：

- 打开 http://127.0.0.1:8000
- 点"游客登录"或 demo 账号（`demo` / `demo123` 或 seed 数据中的测试账号）
- 跳转到 hub.html（个人中枢），展示液态玻璃 + 6 主题切换

**第 2 步 · 画像（30 s）**：

- 进入 personal.html
- "AI 眼中的你"卡片：6 维雷达图 + 4 张记忆卡
- 强调"基于历史记忆聚合"——`profile_aggregator.py` + `portrait_aggregator.py`

**第 3 步 · 课程生成（60 s）**：

- 进入 generated-courses.html
- 输入主题（如"图神经网络"），点生成
- 展示 `/api/v2/course/bundle/generate/stream` SSE 流：进度条 → 大纲 → PPT → 思维导图
- 强调"9 组件 bundle：outline / plan / PPT / graph / radar / project / case / exercises / survey"

**第 4 步 · 课堂（90 s）**：

- 进入 classroom.html
- 选生成的课程 → 进入会话
- 展示苏格拉底式对话：5 种 persona 切换（右上角）、socratic_intensity 实时调整
- 板书（`wb_draw_svg` action）+ 重点高亮（`spotlight`）

**第 5 步 · 小星陪伴（30 s）**：

- 任意页面右下角"小星"浮动
- 点击 → "今天学了 90 分钟，专注度 87%！要不要复习一下昨天的递归？"
- 强调 `[navigate:...]` `[expression:...]` 命令标记

### 关键看点（评委常问）

| 问题 | 看点 / 答案 |
|---|---|
| "多智能体在哪？" | classroom 步骤 + agent_orchestration.html（5 阶段流水线）|
| "防幻觉？" | AuditAgent 4 层防御（截图 backend 日志）；`audit_*.py` 巡检 |
| "数据安全？" | 演示账号无登录；JWT + bcrypt 密码（`app/api/auth.py`）；CSP + OriginCheck 中间件 |
| "能离线吗？" | SQLite 默认本地；演示不依赖外网（除 LLM）|
| "多 LLM 切换？" | 默认 MiniMax；XUNFEI_API_KEY 配置即可切换 |

### 风险预案

| 风险 | 预案 |
|---|---|
| LLM 调用超时 | 提前缓存 demo 课程（SSE 流录屏）；预生成 `storage/courses/<demo_id>/` 内容 |
| 网络断开 | 切离线 SQLite + 预录 demo；展示 UI 静态部分 |
| 投影不显示 | 备用 USB-C 转 HDMI；提前测试分辨率 |
| 评委追问未准备问题 | 引导到 architecture-blueprint.html / stellar-showcase.html（"看看其他能力"）|
| 现场启动失败 | `scripts/health_check.sh` + `bash scripts/reset_demo.sh` |

### 演示数据管理

- 演示账号：`scripts/seed_demo.py` 注入
- 演示课程：`storage/seed/demo/*.json` + `manifest.json`（含 `demo_version`）
- 升级：`demo_version` bump（如 2.0.0 → 2.0.1），下次启动自动替换
- 用户私有数据完全不受影响（`storage/state_storage/<user_id>/` 与 demo 路径分离）

### 演示后清理

```bash
bash scripts/reset_demo.sh    # 重置 demo
bash scripts/backup.sh        # 备份日志
```

## 代码定位

- Demo 种子：`app/services/demo_seeder.py`、`scripts/seed_demo.py`
- 演示路径触发：`app/services/demo_runner/`、`app/api/demo_path.py`
- 课程生成：`libs/course.py`
- 课堂流：`app/api/classroom.py`、`app/services/teacher/pipeline.py`
- 小星：`app/api/mascot.py`、`app/services/mascot/`
- 主题切换：`static/js/theme.js`、`static/css/tokens.css`

## 常见坑

- **首次启动慢**：lifespan 跑 demo 种子 + KB _COUNTER hydrate；首次启动 30-60 s
- **SSE 流断**：Nginx 反代场景下必须 `proxy_buffering off`；本地无影响
- **缓存冲突**：演示后不清缓存，下次可能显示旧数据；用 `reset_demo.sh`
- **LLM 限流**：高频切换 persona 可能触发 MiniMax 限流；演示前预热

## 相关链接

- [项目说明.md](项目说明.md)
- [架构设计.md](架构设计.md) — 总图
- [智能体与流水线.md](智能体与流水线.md) — 6 Agent
- [子系统详解.md](子系统详解.md) — 课堂/小星
- [部署与运维.md](部署与运维.md) — demo 重置
- [脚本索引.md](脚本索引.md)
```

- [ ] **Step 2: 自检**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
grep -c "^## " docs/演示现场手册.md     # 应 ≥6
grep -c "mermaid\|sequenceDiagram" docs/演示现场手册.md  # 应 ≥1
```

- [ ] **Step 3: 提交**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add docs/演示现场手册.md
git commit -m "docs: 新增 演示现场手册.md（5 分钟闭环 + 风险预案 + 看点）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Task 13: 写 `docs/测试体系.md`

**Files:**
- Create: `docs/测试体系.md`

- [ ] **Step 1: 写文档**

创建 `docs/测试体系.md`：

```markdown
# 测试体系

## 摘要

本文档描述星识 Star-Learn 的测试体系：后端 pytest（~70+ 文件，覆盖 agent/api/contracts/cognitive/course/db/exercise/integration 等）+ 前端 Vitest（15 个 unit）+ Playwright（11 个 e2e + 1 个 a11y）+ 视觉快照（16 PNG）+ CI 5 个 GitHub Actions job。理解测试组织、契约测试（dual-backend 一致性）、agents.py 行数护栏，可以快速贡献测试。

## 前置知识

- [架构设计.md](架构设计.md)
- [后端服务.md](后端服务.md)

## 内容

### 后端测试（pytest）

```bash
pytest tests/                          # 全跑
pytest tests/ -k "unit"                # 仅单元
pytest tests/ -k "integration"         # 仅集成
pytest tests/contracts/                # 仅契约（dual-backend 一致性）
pytest --cov=app --cov=agents --cov=scripts  # 带覆盖率
```

#### 测试目录结构

```
tests/
├── agents/                  # 5 个：critic / master_controller_on_product / registration / recommend_audit / socratic_threshold
├── api/                     # 8 个：agent_orchestration / kb_ingest / learning_path_uses_repo / mascot_*(4) / teacher_ai_suggestions
├── cognitive/               # 1 个：style_recognizer
├── contracts/               # 11 个：auth / chat / classroom / course_progress / dual_write_consistency / focus / gamification / knowledge / learning_dual_write / learning_read / preferences
├── course/                  # 1 个：brainstorm_persistence
├── db/                      # 1 个：backend_consistency
├── exercise/                # 1 个：variant_generator
├── fixtures/                # seed_data.py + real_legacy_schema.sql（实测 DDL）+ normalize.py
├── integration/             # 6 个：anti_hallucination / engine_to_mascot / mascot_data_unified / socratic_card_flow / socratic_card_perf / supervision_e2e
├── kb/                      # 4 个：deposition / embedding_nonzero / fallback_queue / ingest_retry
├── learning_path/           # 2 个：forgetting_curve / review_scheduler
├── orchestrator/            # MasterController 编排测试
├── parity/langchain_parity.py   # LangChain 路径对齐
├── repositories/            # 仓储测试
├── safety/                  # 越狱检测测试
├── scripts/                 # 10 个脚本测试
├── services/                # ~45 个服务层测试
├── tutor_engine/            # 新流水线测试
└── (顶层 ~70 个 test_*.py)
```

#### 契约测试（`tests/contracts/`）

11 个契约测试是本项目的核心创新：同一请求在 legacy 与 ORM 两个后端分别跑，归一化响应后断言相等。

- `ContractRunner`（`tests/conftest.py`）：提供 `dual_db_environment` fixture（tmp legacy + tmp ORM）
- `normalize.py`：归一化字段（剥离 trace_id、时间戳）
- `tests/fixtures/seed_data.py`：`SEED_USERS`、`init_legacy_schema`、`init_orm_schema`、`populate_legacy`、`populate_orm`
- `tests/fixtures/real_legacy_schema.sql`：从生产 `storage/xingshi.db` 导出的真实 DDL（修复了"测试想象 schema"的问题）

### 前端测试（Vitest + Playwright）

```bash
npm install
npm run test:unit          # Vitest
npm run test:e2e           # Playwright
npm run test:e2e:smoke     # 仅 smoke
npm run test:e2e:visual    # 仅视觉快照
npm run test:e2e:visual:update  # 更新视觉快照
npm run test:a11y          # axe-core 无障碍
npm run test:all           # 全部
npm run test:ci            # CI 模式（junit 报告）
```

#### Vitest（unit，`tests/frontend/unit/`）

15 个 `.test.js`：agent-bus / agent-orchestration / agent-tower-render / auth / code-coach / code-ide / code-monaco / code-output-tabs / is-socratic-resolver / login / persona-switcher / profile-real-time / teacher-ai-suggestions / toast / why-this

环境：jsdom + `vitest.config.js`。

#### Playwright（e2e，`tests/frontend/e2e/`）

11 个 `.spec.js`：smoke / visual / login-rebuild / code-ide-skeleton / code-ide-theme-regression / css-conflict-resolution / agent-tower / classroom-token-verify / openmaic-token-verify / tech-debt-inventory / think-block-bug / ui-inspect

视觉快照：`visual.spec.js-snapshots/`（16 PNG，chromium + mobile-chrome，多主题）。

#### Playwright a11y

`tests/frontend/a11y/a11y.spec.js`，用 `@axe-core/playwright`。

### CI（`.github/workflows/test.yml`）

5 个 job：

1. **python-tests**（Ubuntu 15 min）— pytest + coverage on `app/` `agents/` `scripts/`；上传 htmlcov
2. **frontend-unit**（Ubuntu 10 min）— Vitest + coverage
3. **e2e-tests**（Ubuntu 15 min）— 启动 uvicorn + Playwright，失败时截图
4. **static-audit**（Ubuntu 5 min）— `audit_undefined_css_vars.py` / `audit_frontend_smells.py` / `audit_compound_selectors.py`
5. **agents-size-net**（Ubuntu 3 min）— P1 收敛护栏：`agents.py` 单次增长 > 50 行则 fail PR

### 测试覆盖率

后端：~70+ 文件覆盖 agent / api / services / repositories；前端 unit + e2e + a11y。**强单元与契约，弱 E2E**（仅 ~6 真正端到端）。

## 代码定位

- Pytest 配置：`pytest.ini`
- Vitest 配置：`vitest.config.js`
- Playwright 配置：`playwright.config.js`
- 契约测试：`tests/contracts/` + `tests/conftest.py`（ContractRunner）
- 真实 DDL fixture：`tests/fixtures/real_legacy_schema.sql`
- CI：`.github/workflows/test.yml`

## 常见坑

- **契约测试的归一化**：响应中 trace_id / 时间戳会变；`normalize.py` 强制剥离
- **DB 双 fixture 慢**：每测试构建 legacy + ORM 两套数据库；并发跑可缓解
- **视觉快照更新**：`npm run test:e2e:visual:update` 后必须 review diff，避免静默回退
- **`agents-size-net` 失败**：单 PR `agents.py` 增长 > 50 行会 fail；应拆分到多 PR

## 相关链接

- [架构设计.md](架构设计.md)
- [后端服务.md](后端服务.md)
- [前端架构.md](前端架构.md)
- [脚本索引.md](脚本索引.md) — audit/fix/verify 脚本
```

- [ ] **Step 2: 自检**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
grep -c "^## " docs/测试体系.md         # 应 ≥6
grep -c "pytest\|Vitest\|Playwright" docs/测试体系.md  # 应 ≥5
```

- [ ] **Step 3: 提交**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add docs/测试体系.md
git commit -m "docs: 新增 测试体系.md（pytest 70+ 文件 + Vitest + Playwright + CI 5 job）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Task 14: 写 `docs/脚本索引.md`

**Files:**
- Create: `docs/脚本索引.md`

- [ ] **Step 1: 写文档**

创建 `docs/脚本索引.md`：

```markdown
# 脚本索引

## 摘要

本文档列出 `scripts/` 下 38 个 Python/Bash 脚本的功能与使用时机：DB 迁移、种子、审计、修复、验证、构建/分发、运维。理解每个脚本的用途，可以避免误跑或漏跑。

## 前置知识

- [部署与运维.md](部署与运维.md)
- [数据层与迁移.md](数据层与迁移.md)
- [测试体系.md](测试体系.md)

## 内容

### 数据库迁移

| 脚本 | 用途 |
|---|---|
| `init_xingshi_v2_mysql.sql` | MySQL 全量 DDL bootstrap（约 27 KB）|
| `migrate_add_subject_columns.py` | Subject/Chapter 列补齐 |
| `migrate_add_user_memories.py` | user_memories 表创建 |
| `migrate_local_storage_to_v2.py` | JSON 本地存储 → DB |
| `migrate_messages_metadata.py` | messages.metadata 列 |
| `migrate_user_id_to_varchar.py` | INT → VARCHAR(64) |
| `migrate_user_table.py` | users 表统一 |
| `reconcile_databases.py` | ORM ↔ legacy 对齐（DualWriteRepository 影子失败恢复）|

### 种子

| 脚本 | 用途 |
|---|---|
| `seed_demo.py` | demo 账号与内容注入（比赛专用）|
| `seed_course_learn_content.py` | 课程学习样例内容 |
| `bind_bilibili_playlists.py` | B 站 playlist 关联到课程 |
| `fill_parity_answers.py` | parity answer 回填 |

### 审计（`audit_*.py`）

| 脚本 | 检查 |
|---|---|
| `audit_compound_selectors.py` | 复合 CSS 选择器 |
| `audit_foreign_keys.py` | FK 引用 user.id vs users.id 计数 |
| `audit_frontend_smells.py` | 前端代码异味 |
| `audit_global_selectors.py` | 全局选择器泄漏 |
| `audit_tailwind.py` | Tailwind 误用 / 旧类检测 |
| `audit_undefined_css_vars.py` | 未定义 CSS 变量（驱动 `fix_p0_tech_debt.py`）|

### 修复（`fix_*.py`）

| 脚本 | 修复 |
|---|---|
| `fix_css_load_order.py` | 强制 CSS 加载顺序（tokens → tailwind → app-base → bg → components → animations → page → theme）|
| `fix_database.py` | 自动检测/修复缺表缺列 |
| `fix_db_schema.py` | ALTER TABLE 补丁（legacy SQLite `user_evaluations` 列等）|
| `fix_p0_tech_debt.py` | 数据驱动 P0 修复（212 缺失 CSS 变量回填 + 5 文件溢出规则剥离）；备份 `tokens.css` 为 `.bak-pre-p0-fix` |

### 验证（`verify_*.py|js|mjs`）

| 脚本 | 验证 |
|---|---|
| `verify_bilibili_cookie.py` | B 站 cookie 有效性 |
| `verify_css_load_order.py` | CSS 加载顺序（CI 用）|
| `verify_css_vars.py` | CSS 变量审计 |
| `verify_ppt_diversity.py` | PPT 生成多样性 |
| `verify_ppt_templates.py` | PPT 模板 |
| `verify_knowledge_tree.js` | KB 树完整性 |
| `verify-demo-data.js` | demo 页面数据 sanity |
| `verify-dashboard-demo.js` | 数据大屏 demo |
| `verify-plant-demo.js` | 植物林场 demo |
| `verify-dd.mjs` | 设计依赖 / 依赖漂移检查 |
| `visual_verify_static.py` | 静态资源渲染验证 |

### 构建 / 分发

| 脚本 | 用途 |
|---|---|
| `build_tech_debt_inventory.py` | 聚合器：跑 3 个新 JSON-output audits + 6 legacy 脚本（subprocess）→ 写 `docs/superpowers/notes/frontend-tech-debt-YYYY-MM-DD.md` |
| `drift_detector.py` | dual-backend 漂移检测 |
| `chaos_drill.py` | 故障注入演练 |
| `inference_rules.py` | 缺失 CSS 变量值推断 |
| `_inventory_db_imports.py` | 静态导入清单 |
| `_recreate_classrooms.py` / `_recreate_extra_courses.py` | DB 重置助手 |

### 运维

| 脚本 | 用途 |
|---|---|
| `start_server.py` | 启动 uvicorn |
| `start_competition.sh` | 比赛模式启动 |
| `playback.sh` / `backup.sh` / `restore.sh` | 备份恢复 |
| `reset_demo.sh` | 重置 demo |
| `health_check.sh` | 健康巡检 |
| `check_db.py` | DB 连接检查 |
| `walkthrough_course_learn.md` | 课程学习手动走查 |

### 文档生成

| 脚本 | 用途 |
|---|---|
| `preview-demo-pages.js` | demo 页面预览 |
| `preview-login.js` | 登录页预览 |
| `preview-progress.js` | 进度页预览 |
| `theme-modal-debug.png` | 主题调试截图 |

## 代码定位

- 脚本目录：`scripts/`
- 打包：`packaging/`（与 scripts 平级，独立）

## 常见坑

- **`audit_*.py` 输出 JSON vs 文本**：新旧版本输出格式不同；CI 调用注意版本
- **`fix_p0_tech_debt.py` 会改 `tokens.css`**：自动备份 `.bak-pre-p0-fix`；不要重复跑（会覆盖备份）
- **`reconcile_databases.py` 双向**：可 ORM → legacy 或 legacy → ORM；执行前确认方向
- **`scripts/*.sh` 不可移植**：依赖 bash + 某些 unix 工具；Windows 用 WSL 或 Git Bash

## 相关链接

- [数据层与迁移.md](数据层与迁移.md)
- [部署与运维.md](部署与运维.md)
- [测试体系.md](测试体系.md)
- [可观测性与安全.md](可观测性与安全.md)
```

- [ ] **Step 2: 自检**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
grep -c "^## " docs/脚本索引.md        # 应 ≥6
grep -c "audit_\|fix_\|verify_\|migrate_" docs/脚本索引.md  # 应 ≥10
```

- [ ] **Step 3: 提交**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add docs/脚本索引.md
git commit -m "docs: 新增 脚本索引.md（38 个脚本按功能分组 + 使用时机）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Task 15: 写 `docs/评测体系.md`（占位）

**Files:**
- Create: `docs/评测体系.md`

- [ ] **Step 1: 写占位文档**

创建 `docs/评测体系.md`，内容只有占位说明：

```markdown
# 评测体系

## 摘要

⚠️ **占位章节**：本章节将在后续独立 brainstorming 会话中重写，本轮文档重构仅作占位。

## 前置知识

无（占位章节）。

## 内容

本章节目标内容：

- **评测数据集设计**：覆盖知识问答、逻辑推理、代码生成、安全合规、中文特性 5 个维度
- **自动化测试**：评测脚本与基线 LLM（MiniMax / 讯飞 等）批量跑分
- **人工评估**：抽样案例的人工评分与一致性校准
- **量化报告**：模型性能差异的可视化报告（响应时间 / 准确率 / 安全性 / 中文质量）

启动方式——本轮重构完成后，另启 brainstorming 会话。

## 代码定位

暂无（本章节尚未实施）。

## 常见坑

暂无（本章节尚未实施）。

## 相关链接

- [架构设计.md](架构设计.md)
- [智能体与流水线.md](智能体与流水线.md)
- [外部服务依赖.md](外部服务依赖.md)
```

- [ ] **Step 2: 自检**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
grep -c "占位" docs/评测体系.md   # 应 ≥1
```

- [ ] **Step 3: 提交**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add docs/评测体系.md
git commit -m "docs: 新增 评测体系.md（占位；后续独立 brainstorming 重写）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Task 16: 写 `docs/walkthrough/01-首次运行.md`

**Files:**
- Create: `docs/walkthrough/01-首次运行.md`

- [ ] **Step 1: 写文档**

创建 `docs/walkthrough/01-首次运行.md`：

```markdown
# Walkthrough 01: 首次运行（git clone → 主页）

## 摘要

本文档是新人首次运行星识 Star-Learn 的端到端操作指南：从 `git clone` 到看到 http://127.0.0.1:8000 的登录页。预期耗时：30 分钟（不含依赖下载）。

## 前置知识

- Python 3.9+
- pip / virtualenv
- Git
- （可选）Node 16+（前端测试 / 演示页预览）

## 内容

### 步骤 1：克隆与依赖

```bash
git clone <repo-url> xingshi
cd xingshi
pip install -r requirements.txt
```

预期：`requirements.txt` 安装约 1-3 分钟（视网络）。关键包：fastapi、sqlalchemy、alembic、langgraph、pymysql、aiosqlite、python-pptx、pdfplumber、bcrypt、PyJWT、qdrant-client、redis、apscheduler。

### 步骤 2：环境配置

```bash
cp config/.env.example config/.env
# 编辑 config/.env，必填：
#   MINIMAX_API_KEY=<your-key>
#   MINIMAX_GROUP_ID=<your-group-id>
# 可选填：
#   XUNFEI_API_KEY=<讯飞 key>（LLM 备选）
#   KLING_ACCESS_KEY=<可灵>（视频生成）
#   BAIDU_ASR_API_KEY / BAIDU_ASR_SECRET_KEY（ASR）
```

不填 LLM 密钥也能启动；调用 LLM 时会 401。

### 步骤 3：初始化数据库

```bash
python Navicat/setup_database.py --backend=sqlite
```

预期：`xingshi_v2.db` 文件创建，约 5-10 MB（含 demo 种子）。SQLite 默认在项目根目录。

或：

```bash
alembic upgrade head
```

### 步骤 4：启动服务

```bash
# 方式 1：直接跑 main.py
python main.py

# 方式 2：uvicorn + reload（开发）
uvicorn main:app --reload --port 8000

# 方式 3：包装脚本
python scripts/start_server.py
```

预期：日志输出：

```
[init_db] schema created (or already existed): sqlite+aiosqlite:///xingshi_v2.db
[seed] demo seeded: 5 courses
[HealthWorker] started
[Scheduler] daily jobs: memory_consolidation@03:00, drift@04:00
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
```

### 步骤 5：访问主页

打开浏览器：

- http://127.0.0.1:8000 — 首页（营销）
- http://127.0.0.1:8000/login.html — 登录
- http://127.0.0.1:8000/hub.html — 个人中枢（需登录）
- http://127.0.0.1:8000/docs — API 文档（FastAPI 自动生成）

### 步骤 6：游客登录

点"游客登录"或访问 http://127.0.0.1:8000/api/login/guest（POST）。

跳转到 hub.html，看到液态玻璃 + 6 主题切换（右上角）。

### 步骤 7：（可选）切换主题

点击右上角主题切换按钮，选 sakura 或 bamboo。预期：整站换色（背景 / 卡片 / 文本），设计令牌驱动。

### 步骤 8：（可选）探索 demo 课程

进入 generated-courses.html → 看 5 门预置 demo 课程（Python 入门 / Web 前端 / 数据结构 / AI 导论 / 线性代数）。

## 代码定位

- 启动入口：`main.py:172`
- Demo 种子：`app/services/demo_seeder.py`
- 路由前缀：[架构设计.md](../架构设计.md)

## 常见坑

- **首次启动慢**：lifespan 跑 demo 种子 + KB _COUNTER hydrate，30-60 s
- **Nginx 反代场景下 SSE 流断**：开发环境无影响；生产见 [部署与运维.md](../部署与运维.md)
- **依赖冲突**：langgraph-checkpoint-mysql 与 langgraph 版本要对齐 requirements.txt
- **Windows 安装**：用 Inno Setup 单 exe，参考 [部署与运维.md](../部署与运维.md)

## 相关链接

- [项目说明.md](../项目说明.md)
- [架构设计.md](../架构设计.md)
- [部署与运维.md](../部署与运维.md)
```

- [ ] **Step 2: 自检**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
grep -c "^## " docs/walkthrough/01-首次运行.md  # 应 ≥6
grep -c "git clone\|pip install\|main.py" docs/walkthrough/01-首次运行.md  # 应 ≥3
```

- [ ] **Step 3: 提交**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add docs/walkthrough/01-首次运行.md
git commit -m "docs(walkthrough): 新增 01-首次运行.md（git clone → 主页，30 分钟）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Task 17: 写 `docs/walkthrough/02-新增智能体.md`

**Files:**
- Create: `docs/walkthrough/02-新增智能体.md`

- [ ] **Step 1: 写文档**

创建 `docs/walkthrough/02-新增智能体.md`：

```markdown
# Walkthrough 02: 新增一个智能体（V2 命名空间）

## 摘要

本文档演示如何添加一个新的 V2 命名实体 Agent：以 `FactCheckAgent` 为例（虚构的"事实核查 Agent"），覆盖命名空间注册、消息契约、注册到编排、暴露 HTTP 端点、添加测试。本 walkthrough 完成后，FactCheckAgent 将出现在 `/api/agents/catalog` 并可在 MasterController 中调用。

## 前置知识

- [智能体与流水线.md](../智能体与流水线.md)
- [架构设计.md](../架构设计.md)

## 内容

### 步骤 1：定义 Agent 类

创建 `app/agents/factcheck.py`：

```python
"""FactCheckAgent: 事实核查 Agent（示例）。

从知识源列表中检查输出文本中的事实声明是否可锚定。
演示新 Agent 接入的完整流程。
"""
from __future__ import annotations

from dataclasses import dataclass
from app.agents.io_schema import AgentRole


@dataclass
class FactCheckResult:
    user_id: str
    verified_count: int
    unverified_claims: list[str]
    confidence: float


class FactCheckAgent:
    """事实核查 Agent。"""

    name = "fact_check_agent"

    CONFIDENCE_THRESHOLD = 0.6

    async def run(
        self,
        user_id: str,
        output_text: str,
        knowledge_source: list[str] | None = None,
    ) -> FactCheckResult:
        knowledge_source = knowledge_source or []

        # 简化版：检查每个句子是否出现在知识源中
        sentences = [s.strip() for s in output_text.split("。") if s.strip()]
        verified = sum(
            1 for s in sentences
            if any(k in s for k in knowledge_source)
        )
        unverified = [s for s in sentences if not any(k in s for k in knowledge_source)]

        confidence = verified / max(len(sentences), 1)

        return FactCheckResult(
            user_id=user_id,
            verified_count=verified,
            unverified_claims=unverified,
            confidence=confidence,
        )
```

### 步骤 2：注册 AgentRole 枚举

编辑 `app/agents/io_schema.py`，在 `AgentRole` 枚举中加一行：

```python
class AgentRole(str, enum.Enum):
    PROFILER = "profiler"
    PLANNER = "planner"
    SOCRATIC = "socratic"
    RECOMMEND = "recommend"
    CRITIC = "critic"
    AUDIT = "audit"
    FACTCHECK = "factcheck"   # ← 新增
```

### 步骤 3：在 `app/agents/__init__.py` 导出

```python
from app.agents.audit import AuditAgent, AuditResult
from app.agents.critic import CriticAgent, CritiqueResult
from app.agents.recommend import RecommendationResult, RecommendAgent
from app.agents.factcheck import FactCheckAgent, FactCheckResult  # ← 新增

__all__ = [
    "RecommendAgent",
    "RecommendationResult",
    "AuditAgent",
    "AuditResult",
    "CriticAgent",
    "CritiqueResult",
    "FactCheckAgent",           # ← 新增
    "FactCheckResult",          # ← 新增
]
```

### 步骤 4：注册到 MasterController（可选）

编辑 `agents.py`，添加：

```python
class FactCheckV1Adapter(BaseAgent):
    """V1 适配器：把 V2 FactCheckAgent 包成 BaseAgent。"""
    name = "fact_check_agent"
    description = "事实核查 Agent（V2 命名空间）"

    def __init__(self):
        from app.agents.factcheck import FactCheckAgent
        self._agent = FactCheckAgent()

    async def run(self, state, **kwargs):
        result = await self._agent.run(
            user_id=state.user_id,
            output_text=state.last_output,
            knowledge_source=state.knowledge_source,
        )
        state.fact_check_result = result
        return state
```

在 `MasterController.__init__` 中注册：

```python
self.fact_check = FactCheckV1Adapter()
self._registry["fact_check_agent"] = self.fact_check
```

### 步骤 5：暴露 HTTP 端点（可选）

编辑 `app/api/agent_orchestration.py`，在 `GET /api/agents/catalog` 的 agent 列表加：

```python
{
    "id": "fact_check_agent",
    "name": "事实核查",
    "role": "factcheck",
    "tools": ["knowledge_search"],
    "stage": "post",                # 在 ResourcePush 之后
    "class": "validator",
},
```

### 步骤 6：写测试

创建 `tests/agents/test_factcheck.py`：

```python
import pytest
from app.agents.factcheck import FactCheckAgent


@pytest.mark.asyncio
async def test_factcheck_with_matching_source():
    agent = FactCheckAgent()
    result = await agent.run(
        user_id="u1",
        output_text="Python 是一种编程语言。它广泛用于数据科学。",
        knowledge_source=["Python", "数据科学"],
    )
    assert result.verified_count == 2
    assert result.confidence == 1.0


@pytest.mark.asyncio
async def test_factcheck_with_no_source():
    agent = FactCheckAgent()
    result = await agent.run(
        user_id="u1",
        output_text="完全无关的声明。",
        knowledge_source=[],
    )
    assert result.verified_count == 0
    assert result.confidence == 0.0
```

### 步骤 7：跑测试

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
pytest tests/agents/test_factcheck.py -v
```

预期：

```
tests/agents/test_factcheck.py::test_factcheck_with_matching_source PASSED
tests/agents/test_factcheck.py::test_factcheck_with_no_source PASSED
```

### 步骤 8：提交

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add app/agents/factcheck.py app/agents/io_schema.py app/agents/__init__.py \
        agents.py app/api/agent_orchestration.py tests/agents/test_factcheck.py
git commit -m "feat(agents): 新增 FactCheckAgent（V2 命名空间示例）

- app/agents/factcheck.py: FactCheckAgent + FactCheckResult
- io_schema.py: AgentRole.FACTCHECK
- agents.py: FactCheckV1Adapter 接入 MasterController
- agent_orchestration.py: catalog 新增 fact_check_agent
- tests/agents/test_factcheck.py: 2 个测试

Co-Authored-By: Claude <noreply@anthropic.com>"
```

## 代码定位

- 新 Agent 类：`app/agents/factcheck.py`
- 消息契约：`app/agents/io_schema.py`
- 命名空间：`app/agents/__init__.py`
- MasterController：`agents.py:1116`
- HTTP 暴露：`app/api/agent_orchestration.py`
- 测试：`tests/agents/test_factcheck.py`

## 常见坑

- **V1/V2 双层**：新 Agent 默认放 `app/agents/`（V2 命名空间），如要接入 MasterController V1 流水线需写 V1 适配器
- **`AgentRole` 枚举值**：用小写 snake_case；`value` 序列化用
- **catalog 同步**：HTTP catalog 与 V2 namespace 不同步；改 V2 时记得改 catalog
- **测试 fixture**：`tests/conftest.py` 的 `dual_db_environment` 仅契约测试需要；单 Agent 测试不依赖

## 相关链接

- [智能体与流水线.md](../智能体与流水线.md)
- [架构设计.md](../架构设计.md)
- [测试体系.md](../测试体系.md)
```

- [ ] **Step 2: 自检**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
grep -c "^## " docs/walkthrough/02-新增智能体.md  # 应 ≥6
grep -c "app/agents\|FactCheckAgent" docs/walkthrough/02-新增智能体.md  # 应 ≥5
```

- [ ] **Step 3: 提交**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add docs/walkthrough/02-新增智能体.md
git commit -m "docs(walkthrough): 新增 02-新增智能体.md（FactCheckAgent 完整流程）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Task 18: 写 `docs/walkthrough/03-新增前端页面.md`

**Files:**
- Create: `docs/walkthrough/03-新增前端页面.md`

- [ ] **Step 1: 写文档**

创建 `docs/walkthrough/03-新增前端页面.md`：

```markdown
# Walkthrough 03: 新增一个前端页面

## 摘要

本文档演示如何添加一个新的前端页面：以 `/my-quizzes.html`（"我的测验"页面）为例，覆盖 HTML 模板、CSS 加载顺序、Alpine.js 组件、API 接入、Playwright 测试。完成后，新页面可通过 http://127.0.0.1:8000/my-quizzes.html 访问。

## 前置知识

- [前端架构.md](../前端架构.md)
- [子系统详解.md](../子系统详解.md)

## 内容

### 步骤 1：创建 HTML 页面

创建 `static/html/my-quizzes.html`：

```html
<!DOCTYPE html>
<html lang="zh-CN" data-theme="star">
<head>
  <meta charset="UTF-8">
  <title>我的测验 — 星识</title>

  <!-- CSS 加载顺序：tokens → tailwind → app-base → bg → components → animations → page → theme -->
  <link rel="stylesheet" href="/css/tokens.css">
  <link rel="stylesheet" href="/css/tailwind.css">
  <link rel="stylesheet" href="/css/app-base.css">
  <link rel="stylesheet" href="/css/app-bg.css">
  <link rel="stylesheet" href="/css/components.css">
  <link rel="stylesheet" href="/css/animations.css">
  <link rel="stylesheet" href="/css/my-quizzes.css">
  <link rel="stylesheet" href="/css/theme-bg.css">
  <link rel="stylesheet" href="/css/theme-modal.css">

  <script src="/js/auth.js" defer></script>
  <script src="/js/http-intercept.js" defer></script>
  <script src="/js/theme.js" defer></script>
  <script src="/js/data-layer.js" defer></script>
  <script src="/js/my-quizzes.js" defer></script>
  <script src="/js/alpinejs.min.js" defer></script>
</head>
<body>
  <div x-data="myQuizzesPage">
    <!-- 顶部导航 -->
    <nav class="navbar">
      <a href="/hub.html">← 返回中枢</a>
      <h1>我的测验</h1>
      <button @click="refresh()">刷新</button>
    </nav>

    <!-- 加载态 -->
    <div x-show="loading" class="loading">加载中…</div>

    <!-- 测验列表 -->
    <template x-for="quiz in quizzes" :key="quiz.id">
      <div class="quiz-card">
        <h3 x-text="quiz.title"></h3>
        <p>得分：<span x-text="quiz.score"></span> / <span x-text="quiz.total"></span></p>
        <p>时间：<span x-text="quiz.created_at"></span></p>
        <span x-show="quiz.passed" class="badge badge-success">通过</span>
        <span x-show="!quiz.passed" class="badge badge-warning">未通过</span>
      </div>
    </template>

    <!-- 空状态 -->
    <div x-show="!loading && quizzes.length === 0" class="empty">
      还没有测验记录。
    </div>
  </div>
</body>
</html>
```

### 步骤 2：创建页面级 CSS

创建 `static/css/my-quizzes.css`：

```css
/* 我的测验页 — 卡片网格 */
.quiz-card {
  background: var(--_surface-1, oklch(98% 0.01 240));
  border: 1px solid var(--_border-subtle, oklch(85% 0.02 240));
  border-radius: 12px;
  padding: 16px;
  margin-bottom: 12px;
  box-shadow: 0 2px 8px var(--_shadow-strength, 0.05);
  transition: transform 0.2s ease;
}

.quiz-card:hover {
  transform: translateY(-2px);
}

.empty {
  text-align: center;
  color: var(--_text-secondary, oklch(50% 0.02 240));
  padding: 48px;
}
```

### 步骤 3：创建 Alpine 组件

创建 `static/js/my-quizzes.js`：

```javascript
window.myQuizzesPage = function () {
  return {
    quizzes: [],
    loading: true,

    async init() {
      await this.refresh();
    },

    async refresh() {
      this.loading = true;
      try {
        const userId = window.auth?.userId || 'guest';
        const resp = await window.http.get(`/api/v2/quiz/list/${userId}`);
        this.quizzes = resp.data?.quizzes || [];
      } catch (e) {
        console.error('加载测验失败', e);
        window.toast?.error('加载失败');
      } finally {
        this.loading = false;
      }
    },
  };
};
```

### 步骤 4：注册 HTML 路由

编辑 `main.py`，在内联 HTML 路由区（约 line 880-920）加：

```python
@app.get("/my-quizzes.html", response_class=HTMLResponse)
async def my_quizzes_page():
    html_path = HTML_DIR / "my-quizzes.html"
    if not html_path.exists():
        raise HTTPException(404, "my-quizzes.html not found")
    return html_path.read_text(encoding="utf-8")
```

或更简洁——FastAPI 自动从 `static/html/` 提供 HTML（已 `app.mount("/static")`），可直接 http://127.0.0.1:8000/static/html/my-quizzes.html 访问（不推荐 URL 中带 `/static/`）。

**推荐方式**：把 HTML 拷贝或符号链接到 `static/html/` 根目录，并通过 `@app.get("/my-quizzes.html")` 提供；URL 友好。

### 步骤 5：写 Playwright 测试

创建 `tests/frontend/e2e/my-quizzes.spec.js`：

```javascript
import { test, expect } from '@playwright/test';

test.describe('我的测验页', () => {
  test.beforeEach(async ({ page }) => {
    // 假设已登录
    await page.context().addCookies([
      { name: 'auth_token', value: 'test-token', domain: '127.0.0.1', path: '/' },
    ]);
  });

  test('展示空状态', async ({ page }) => {
    await page.route('**/api/v2/quiz/list/**', (route) =>
      route.fulfill({ json: { success: true, data: { quizzes: [] } } })
    );

    await page.goto('http://127.0.0.1:8000/my-quizzes.html');
    await expect(page.locator('.empty')).toBeVisible();
    await expect(page.locator('.empty')).toContainText('还没有测验记录');
  });

  test('展示测验列表', async ({ page }) => {
    await page.route('**/api/v2/quiz/list/**', (route) =>
      route.fulfill({
        json: {
          success: true,
          data: {
            quizzes: [
              {
                id: 'q1',
                title: '递归测验',
                score: 80,
                total: 100,
                passed: true,
                created_at: '2026-08-27',
              },
            ],
          },
        },
      })
    );

    await page.goto('http://127.0.0.1:8000/my-quizzes.html');
    await expect(page.locator('.quiz-card h3')).toContainText('递归测验');
    await expect(page.locator('.badge-success')).toBeVisible();
  });
});
```

### 步骤 6：跑测试

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
npm run test:e2e -- my-quizzes.spec.js
```

预期：2 个 test pass。

### 步骤 7：浏览器手动验证

启动应用后，访问 http://127.0.0.1:8000/my-quizzes.html，确认：

- 顶部导航显示
- 加载状态 → 测验列表 / 空状态切换
- 主题切换（右上角）即时生效

### 步骤 8：提交

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add static/html/my-quizzes.html static/css/my-quizzes.css static/js/my-quizzes.js \
        main.py tests/frontend/e2e/my-quizzes.spec.js
git commit -m "feat(ui): 新增 我的测验 页（my-quizzes.html）

- static/html/my-quizzes.html: 页面模板
- static/css/my-quizzes.css: 卡片样式（CSS 变量驱动主题）
- static/js/my-quizzes.js: Alpine 组件
- main.py: HTML 路由
- tests/frontend/e2e/my-quizzes.spec.js: 2 个 e2e 测试

Co-Authored-By: Claude <noreply@anthropic.com>"
```

## 代码定位

- HTML 模板：`static/html/my-quizzes.html`
- 页面 CSS：`static/css/my-quizzes.css`
- Alpine 组件：`static/js/my-quizzes.js`
- 路由：`main.py`
- E2E 测试：`tests/frontend/e2e/my-quizzes.spec.js`

## 常见坑

- **CSS 加载顺序错乱**：被 `audit_compound_selectors.py` + `fix_css_load_order.py` 强制；新页面必须按 tokens → tailwind → app-base → bg → components → animations → page → theme
- **Alpine 全局命名空间**：组件必须挂 `window.<NamePascalCase>`，同名组件会冲突
- **`data-layer.js` 必须先加载**：`my-quizzes.js` 依赖 `window.http`，必须 `http-intercept.js` + `data-layer.js` 先加载
- **测试夹具**：Playwright 测试需登录态；用 `addCookies` 或走 `api/login/guest` 端点

## 相关链接

- [前端架构.md](../前端架构.md)
- [测试体系.md](../测试体系.md)
```

- [ ] **Step 2: 自检**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
grep -c "^## " docs/walkthrough/03-新增前端页面.md  # 应 ≥6
grep -c "static/\|alpinejs" docs/walkthrough/03-新增前端页面.md  # 应 ≥4
```

- [ ] **Step 3: 提交**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add docs/walkthrough/03-新增前端页面.md
git commit -m "docs(walkthrough): 新增 03-新增前端页面.md（my-quizzes.html 完整流程）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Task 19: 写 `docs/README.md`（总索引）

**Files:**
- Create: `docs/README.md`

- [ ] **Step 1: 写文档**

创建 `docs/README.md`：

````markdown
# 星识 Star-Learn 文档中心

> 个人智能学习中枢 — 基于多智能体架构的智能教学辅助系统

---

## 🎯 我是谁？3 角色速读路径

### 👨‍💻 开发者（接手 / 二次开发 / 交接新人）

读完这 3 篇 → [项目说明](项目说明.md) · [架构设计](架构设计.md) · [智能体与流水线](智能体与流水线.md)

再深入： [后端服务](后端服务.md) · [前端架构](前端架构.md) · [数据层与迁移](数据层与迁移.md) · [子系统详解](子系统详解.md) · [测试体系](测试体系.md)

动手： [Walkthrough 01-首次运行](walkthrough/01-首次运行.md) · [Walkthrough 02-新增智能体](walkthrough/02-新增智能体.md) · [Walkthrough 03-新增前端页面](walkthrough/03-新增前端页面.md)

---

### 🔧 运维（部署 / 迁移 / 故障排查）

读完这 3 篇 → [项目说明](项目说明.md) · [部署与运维](部署与运维.md) · [数据层与迁移](数据层与迁移.md)

再深入： [可观测性与安全](可观测性与安全.md) · [脚本索引](脚本索引.md)

---

### 🎤 评委（架构理解 / 答辩 / 演示）

读完这 3 篇 → [项目说明](项目说明.md) · [架构设计](架构设计.md) · [演示现场手册](演示现场手册.md)

再深入： [智能体与流水线](智能体与流水线.md) · [子系统详解](子系统详解.md)

---

## 📑 主题地图（按编号）

| # | 文档 | 一句话 |
|---|---|---|
| - | [项目说明](项目说明.md) | 一句话定位 + 核心能力清单 + 技术栈 |
| - | [架构设计](架构设计.md) | 总架构图 + v1/v2 双层结构 + 6 Agent + 路由总表 |
| - | [后端服务](后端服务.md) | FastAPI + main.py 单体 + 路由组织 + 启动副作用 |
| - | [前端架构](前端架构.md) | HTML/JS/CSS 组织 + Alpine/Tailwind + 6 套主题 |
| - | [智能体与流水线](智能体与流水线.md) | 9 V1 + 3 V2 Agent + MasterController + tutor_engine |
| - | [子系统详解](子系统详解.md) | 课程/课堂/代码/知识图谱/心流/生态/路径/记忆/演示/小星 |
| - | [数据层与迁移](数据层与迁移.md) | 35 表 + 仓储双写 + Feature Flags + 迁移 |
| - | [可观测性与安全](可观测性与安全.md) | Trace + 中间件 + 越狱 + 防幻觉 + 审计 |
| - | [外部服务依赖](外部服务依赖.md) | LLM/TTS/ASR/视频/向量/缓存/B 站/火山方舟 |
| - | [部署与运维](部署与运维.md) | dev / prod / docker / Windows 安装包 + 故障排查 |
| - | [演示现场手册](演示现场手册.md) | 5 分钟闭环 + 风险预案 + 看点 |
| - | [测试体系](测试体系.md) | pytest 70+ 文件 + Vitest + Playwright + CI 5 job |
| - | [脚本索引](脚本索引.md) | 38 个 scripts 功能索引 + 使用时机 |
| - | [评测体系](评测体系.md) | ⚠️ 占位（后续独立 brainstorming 重写）|

## 🚶 新人走查

| # | 文档 | 用途 |
|---|---|---|
| 01 | [Walkthrough 01-首次运行](walkthrough/01-首次运行.md) | 从 git clone 到 http://127.0.0.1:8000（30 分钟） |
| 02 | [Walkthrough 02-新增智能体](walkthrough/02-新增智能体.md) | 添加一个新 V2 Agent 完整流程 |
| 03 | [Walkthrough 03-新增前端页面](walkthrough/03-新增前端页面.md) | 添加一个新 HTML/CSS/JS 页面完整流程 |

## 🗄️ 历史归档

22 份重构前文档已搬迁至 [_archive/](_archive/README.md)。如发现旧文档与新文档有出入，**以新文档为准**。

---

最后更新：2026-08-27
````

- [ ] **Step 2: 自检**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
grep -c "^## " docs/README.md             # 应 ≥3（3 角色卡 + 主题地图 + 走查）
grep -c "\[.*\](.*\.md)" docs/README.md   # 应 ≥30（大量相对路径链接）
```

- [ ] **Step 3: 提交**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add docs/README.md
git commit -m "docs: 新增 README.md（3 角色速读路径 + 主题地图 + 走查索引）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Task 20: 全局验证（链接 + 字数 + 6 段结构）

**Files:**
- 无新增文件；只跑验证脚本

- [ ] **Step 1: 验证 6 段结构**

每篇文档必须有 6 段：摘要 / 前置知识 / 内容 / 代码定位 / 常见坑 / 相关链接。

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
for f in docs/{项目说明,架构设计,后端服务,前端架构,智能体与流水线,子系统详解,数据层与迁移,可观测性与安全,外部服务依赖,部署与运维,演示现场手册,测试体系,脚本索引}.md; do
  count=$(grep -c "^## " "$f")
  echo "$f: $count sections"
done
```

预期：每行输出 ≥6（占位章节 `评测体系.md` 跳过）。

- [ ] **Step 2: 验证相对路径链接可达**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
# 抽出所有 [text](path.md) 形式，检查目标文件存在
grep -hoE "\[[^\]]+\]\(([^\)]+\.md)\)" docs/*.md docs/walkthrough/*.md | \
  sed -E 's/.*\(([^)]+)\).*/\1/' | \
  sort -u | while read link; do
    # 仅验证同目录或上一级相对路径
    case "$link" in
      ../*) target="docs/${link#../}" ;;
      *) target="docs/${link}" ;;
    esac
    if [ ! -f "$target" ] && [ ! -f "$link" ]; then
      echo "BROKEN: $link"
    fi
done
```

预期：无 BROKEN 输出。如有，逐条修复。

- [ ] **Step 3: 验证 walkthrough 链接**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
grep -hoE "\([^)]+\.md\)" docs/walkthrough/*.md | tr -d '()' | sort -u | while read link; do
  case "$link" in
    ../*) target="docs/${link#../}" ;;
    *) target="docs/walkthrough/${link}" ;;
  esac
  if [ ! -f "$target" ]; then
    echo "BROKEN: $link"
  fi
done
```

预期：无 BROKEN。

- [ ] **Step 4: 验证代码定位路径存在**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
# 抽出 main.py:行号、app/、static/ 引用做轻量检查
grep -hoE "(main\.py|app/agents/[a-z_]+\.py|app/services/[a-z_/]+\.py|app/models/[a-z_]+\.py|app/api/[a-z_]+\.py|static/[a-z/_]+\.(css|js|html))" docs/*.md docs/walkthrough/*.md | \
  awk -F: '{print $1}' | sort -u | while read p; do
    if [ ! -e "$p" ]; then
      echo "MISSING: $p"
    fi
done
```

预期：无 MISSING。

- [ ] **Step 5: 验证 `_archive/README.md` 存在**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
ls docs/_archive/README.md
ls docs/_archive/ | wc -l  # 应 = 23（22 旧文档 + README）
```

预期：两个命令均成功，第二条输出 23。

- [ ] **Step 6: 验证 20 个新文档 + 22 个旧文档搬运**

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
# 新文档
ls docs/{README,项目说明,架构设计,后端服务,前端架构,智能体与流水线,子系统详解,数据层与迁移,可观测性与安全,外部服务依赖,部署与运维,演示现场手册,测试体系,脚本索引,评测体系}.md 2>/dev/null | wc -l
# 应 = 15（其中评测体系.md 是占位）

# walkthrough
ls docs/walkthrough/*.md | wc -l  # 应 = 3

# 归档
ls docs/_archive/*.md docs/_archive/*.txt 2>/dev/null | wc -l  # 应 ≥22
```

预期：15 + 3 + ≥22。

- [ ] **Step 7: 最终提交（无变更时跳过）**

如有任何修复：

```bash
cd "c:/Users/ZWC/Desktop/软件杯大赛/星识-小星伴学/xingshi"
git add docs/
git commit -m "docs(refactor): 全局验证修复（链接 / 路径 / 结构）

Co-Authored-By: Claude <noreply@anthropic.com>"
```

如无变更则跳过此步。

---

## Self-Review（计划提交前）

| 项 | 状态 |
|---|---|
| Spec 覆盖率 | 14 篇新主题文档（Tasks 2-14）+ 1 占位（Task 15）+ 3 走查（Tasks 16-18）+ 1 README（Task 19）+ 1 归档（Task 1）+ 全局验证（Task 20）= 20 tasks；spec 中 20 个新文件全部覆盖 |
| 占位扫描 | 无 TBD/TODO/FIXME/XXX（所有 Task 内 code block 完整）|
| 类型一致性 | `FactCheckAgent` 在 Task 17 各步骤定义一致；`myQuizzesPage` 命名在 Task 18 各步骤一致 |
| 步骤完整性 | 每 Task 含 2-3 个 step：写文档 → 自检 → commit（与 spec §7.2 单篇验收对齐）|
| 范围控制 | 仅 `docs/`；不动任何代码文件（Tasks 17、18 含代码示例，但仅作为 walkthrough 文档中的代码块，不实际执行）|

> 注：Task 17 和 Task 18 的 walkthrough 文档含完整代码示例，但实施时**不实际执行这些代码**（即不创建 `app/agents/factcheck.py` 等文件）；这些代码仅作为 walkthrough 文档内容展示。如需实际跑示例，需另起 task。

---

## Execution Handoff

**Plan complete and saved to `docs/superpowers/plans/2026-08-27-xingshi-doc-refactor.md`. Two execution options:**

**1. Subagent-Driven (recommended)** - I dispatch a fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** - Execute tasks in this session using executing-plans, batch execution with checkpoints

**Which approach?**