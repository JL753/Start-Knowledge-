# 星识 Star-Learn

> **个人智能学习中枢** — 基于多智能体架构的智能教学辅助系统

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-Private-lightgrey)](#)

---

## 项目简介

**星识 (Star-Learn)** 是一个面向学生的 **AI 智能学习中枢**，融合多智能体编排、苏格拉底式教学、个性化学习路径规划、AI 课堂对话、代码练习、心流监测、知识图谱等能力，致力于让每个学习者拥有自己的"私人导师"。

### 核心能力

- 🧠 **多智能体编排**：MasterController 调度 Profiler、Planner、Document/Mindmap/Exercise/Video Generator、ResourcePush、Evaluation、Socratic 等 10+ Agent
- 💬 **AI 课堂对话**：5 种教师 Persona（patient_tutor、socratic_questioner、energetic_lecturer、expert_mentor、caring_counselor），按 `socratic_intensity` 注入反问强度
- 🎯 **学习路径规划**：每日学习路线、SM2 间隔重复、知识节点图谱
- 💻 **代码工坊**：Monaco IDE、实时运行、AI 评审、批量出题、错题本
- 📚 **课程中心**：学科 → 课程 → 章节 → 子章节 四级结构，B 站视频导入
- 🌱 **生态养成**：星宝宠物、植物林场、成就系统
- 🎙 **多媒体**：TTS（MiniMax）、ASR（百度/Whisper）、视频生成（可灵/CogVideo）
- 📊 **心流共振仪**：专注度监测 + 遥测数据可视化
- 🎨 **主题系统**：6 套主题 + 液态玻璃 + 3D 加载动画

---

## 📑 文档中心

完整文档已按主题分层重写，详见 **[docs/README.md](docs/README.md)**。三类入口（开发者 / 运维 / 评委）各有"先读这 3 篇"的速读路径。

主要文档速查：

| 主题 | 文档 |
|------|------|
| 项目入口 | [docs/项目说明.md](docs/项目说明.md) · [docs/架构设计.md](docs/架构设计.md) |
| 后端 / 前端 | [docs/后端服务.md](docs/后端服务.md) · [docs/前端架构.md](docs/前端架构.md) |
| 智能体 / 子系统 | [docs/智能体与流水线.md](docs/智能体与流水线.md) · [docs/子系统详解.md](docs/子系统详解.md) |
| 数据 / 安全 | [docs/数据层与迁移.md](docs/数据层与迁移.md) · [docs/可观测性与安全.md](docs/可观测性与安全.md) |
| 外部依赖 | [docs/外部服务依赖.md](docs/外部服务依赖.md) |
| 部署 / 演示 / 测试 / 脚本 | [docs/部署与运维.md](docs/部署与运维.md) · [docs/演示现场手册.md](docs/演示现场手册.md) · [docs/测试体系.md](docs/测试体系.md) · [docs/脚本索引.md](docs/脚本索引.md) |
| 新人走查 | [docs/walkthrough/01-首次运行.md](docs/walkthrough/01-首次运行.md) · [docs/walkthrough/02-新增智能体.md](docs/walkthrough/02-新增智能体.md) · [docs/walkthrough/03-新增前端页面.md](docs/walkthrough/03-新增前端页面.md) |

> 旧版本文档（重构前）已迁至 [docs/_archive/](docs/_archive/README.md)，仅供历史回溯；如发现出入，**以新文档为准**。

---

## 快速开始

### 5 分钟跑起来

```bash
# 1. 克隆
git clone <repo-url>
cd xingshi

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置环境变量
cp config/.env.example config/.env
# 编辑 config/.env，至少填入 MINIMAX_API_KEY 和 MINIMAX_GROUP_ID
# 也可填入 XUNFEI_API_KEY（讯飞）作为备选 LLM

# 4. 初始化数据库（默认 SQLite，无需额外依赖）
python Navicat/setup_database.py --backend=sqlite
```

### 预置 Demo 内容

首次启动后，应用会自动从 `storage/seed/demo/` 加载演示内容，无需任何手动操作：

- **多个演示课程**（Python / Web 前端 / 数据结构与算法 / AI 导论 / 线性代数），每门含完整富文本讲义 + 思维导图
- **多个演示课堂**（对应每门课程的 PPT），所有用户（含未登录）都能直接打开

所有用户可见 🎁 DEMO 课程，课堂页显示"演示课堂"横幅。

### 修改 / 升级 Demo 内容

1. 编辑 `storage/seed/demo/*.json`
2. 在 `manifest.json` 里 bump `demo_version`（如 `2.0.0` → `2.0.1`）
3. 下次启动自动替换 demo 内容；用户私有数据完全不受影响

```bash
# 手动重置（不依赖启动）
python scripts/seed_demo.py --reset
# 查看当前状态
python scripts/seed_demo.py --check
```

### 启动服务

```bash
# 方式一：推荐启动脚本
python main.py
# 或
python scripts/start_server.py

# 方式二：开发模式（热重载）
uvicorn main:app --reload --port 8000
```

打开浏览器访问：**http://127.0.0.1:8000**

API 文档：**http://127.0.0.1:8000/docs**

> 详细启动指南：[docs/walkthrough/01-首次运行.md](docs/walkthrough/01-首次运行.md)
> 生产部署：[docs/部署与运维.md](docs/部署与运维.md)

---

## 🛠️ 技术栈

| 层级 | 技术 |
|------|------|
| 后端框架 | FastAPI 0.104 + Uvicorn 0.24 |
| ORM | SQLAlchemy 2.0(async) + Alembic 1.13 |
| 数据校验 | Pydantic 2.x + pydantic-settings |
| 数据库 | MySQL 5.7+ / SQLite 3（异步驱动 aiosqlite / asyncmy / aiomysql） |
| Agent 编排 | LangGraph 0.2 + langgraph-checkpoint-mysql |
| 缓存 / 队列 | Redis 7（可选）|
| 向量库 | Qdrant 1.9（可选）|
| LLM | MiniMax（默认）/ 讯飞大模型 |
| TTS | MiniMax TTS(speech-2.8-hd) / OpenAI 兼容 |
| ASR | 百度短语音 / Whisper WASM |
| 视频生成 | 可灵 Kling / CogVideo（本地） |
| 前端 | 原生 HTML/CSS/JS（无构建），Monaco Editor（CDN），Alpine.js + Tailwind CDN |
| 测试 | pytest（后端）+ Vitest / Playwright（前端）|
| 打包 | Inno Setup + 嵌入 CPython → 单 exe 安装包 |

---

## 📁 项目结构

```
xingshi/
├── main.py                    # FastAPI 应用入口（V1 legacy 单体）
├── agents.py                  # 多智能体实现 V1（MasterController + 9 Agent）
├── db.py                      # V1 数据访问（pymysql）
├── state.py                   # Pydantic 数据模型
├── agent_utils.py             # 智能体工具函数
├── llm_stream.py              # LLM 流式调用封装
├── proactive_tutor.py         # 主动辅导模块
├── task_manager.py            # 异步任务管理
├── prompts/                   # 提示词模板整合（含 snippets + templates）
│
├── app/                       # V2 模块化（api/core / schemas / services / models / agents / repositories）
│   ├── api/                   # 23 个 FastAPI 路由模块
│   ├── core/                  # 配置、数据库连接、Feature Flags、健康检查
│   ├── models/                # SQLAlchemy 模型（22 个文件 / 35 表）
│   ├── schemas/               # Pydantic Schema
│   ├── services/              # 服务层（teacher / ppt / tts / asr / agent / security / llm / kb / ...）
│   ├── agents/                # V2 命名实体 Agent（recommend / audit / critic / io_schema）
│   ├── repositories/          # 仓储抽象 + DualWrite 双写
│   └── prompts/               # API 层提示词
│
├── static/                    # 前端静态资源
│   ├── html/                  # 32 个 HTML 页面
│   ├── js/                    # 76 个 JS 文件（含 pages/）
│   ├── css/                   # 60 个 CSS 文件（含 tokens / components / theme）
│   ├── audio/                 # 20 首免版税背景音乐
│   └── demo/                  # 5 个课程封面 SVG
│
├── scripts/                   # 38 个工具脚本（DB 迁移、审计、修复、验证、运维）
├── libs/                      # 工具库（course / video / kling_api / media / pptx）
├── config/                    # 配置中心（.env）
│
├── alembic/                   # 数据库迁移脚本
├── alembic.ini
├── Navicat/                   # 数据库工具
│   └── setup_database.py      # 一键建表（MySQL/SQLite）
│
├── docs/                      # 文档中心（主题分层）
│   ├── README.md              # 文档索引（3 角色速读路径）
│   ├── 项目说明.md / 架构设计.md / 后端服务.md / ...
│   ├── walkthrough/           # 新人走查（01-首次运行 / 02-新增智能体 / 03-新增前端页面）
│   ├── _archive/              # 旧版本文档归档
│   └── sql/                   # SQL 初始化脚本
│
├── storage/                   # 运行时数据（courses / state_storage / seed / task_storage）
├── audio/                     # TTS 输出
├── spool/                     # Agent 行为日志（KB）
│
├── tests/                     # pytest 70+ 文件（agents / api / contracts / cognitive / course / db / exercise / integration / kb / learning_path / orchestrator / repositories / safety / scripts / services / tutor_engine）
├── packaging/                 # Inno Setup + 嵌入 CPython 打包
│
├── requirements.txt           # Python 依赖
├── package.json               # 前端测试依赖
├── docker-compose.dev.yml     # 开发环境 Qdrant + Redis
└── README.md                  # 本文件
```

---

## 💾 数据库

项目支持两种数据库后端：

| 后端 | 适用场景 | 命令 |
|------|---------|------|
| SQLite（默认） | 开发 / 单机 / 演示 | `python Navicat/setup_database.py --backend=sqlite` |
| MySQL 5.7+ | 生产环境 | `python Navicat/setup_database.py --backend=mysql` |
| SQL 文件 | 离线 / K8s / Docker | `mysql < docs/sql/init_mysql.sql` |
| Alembic | ORM 模型变更 | `alembic upgrade head` |

数据库共 **35 张表**，覆盖用户认证、学习记录、知识图谱、AI 对话、课堂会话、闪卡、生态养成、媒体缓存等。

详见 [docs/数据层与迁移.md](docs/数据层与迁移.md) 与 [docs/sql/README.md](docs/sql/README.md)。

---

## 🚀 部署

### 开发环境

```bash
python main.py --reload
# 或
uvicorn main:app --reload --port 8000
```

### 生产环境（推荐）

```bash
# 1. 安装依赖到虚拟环境
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2. 配置环境
cp config/.env.example config/.env && vim config/.env

# 3. 初始化数据库（MySQL）
export MYSQL_USER=starlearn
export MYSQL_PASSWORD=secret
python Navicat/setup_database.py --backend=mysql

# 4. 启动（Systemd）
sudo systemctl enable --now starlearn

# 5. Nginx 反向代理（详见 docs/部署与运维.md §3）
```

完整步骤见 [docs/部署与运维.md](docs/部署与运维.md)。

### Docker

```bash
docker compose -f docker-compose.dev.yml up -d   # 仅启动 Qdrant + Redis
docker build -t starlearn . && docker run -d --name starlearn -p 8000:8000 starlearn
```

### Windows 一键安装包

```bat
packaging\build.bat
:: 或
python packaging\build_portable.py
```

产物为单 exe 安装包（Inno Setup + 嵌入 CPython，约 150 MB），首次启动自动写入 `%APPDATA%\StarLearn\.env` 并打开浏览器。

---

## 🧪 测试

### 后端

```bash
pytest tests/
# 单元测试
pytest tests/ -k "unit"
# 集成测试
pytest tests/ -k "integration"
# 契约测试（dual-backend 一致性）
pytest tests/contracts/
```

### 前端

```bash
npm install
npm run test:unit        # Vitest
npm run test:e2e         # Playwright
npm run test:a11y        # 无障碍测试
npm run test:all         # 全部
```

详见 [docs/测试体系.md](docs/测试体系.md)。

---

## ⚙️ 配置项速查

完整列表见 [docs/部署与运维.md §配置项](docs/部署与运维.md) 与 [docs/外部服务依赖.md](docs/外部服务依赖.md)。

**必填**：

- `MINIMAX_API_KEY` + `MINIMAX_GROUP_ID`（MiniMax LLM/TTS 必需）
- 或 `XUNFEI_API_KEY`（讯飞 LLM 备选）

**生产环境必改**：

- `DATABASE_URL` → MySQL URL
- `APP_DEBUG=False`

**可选服务**（不开则相关功能降级）：

- `KLING_*`：可灵视频生成
- `BAIDU_ASR_*`：百度语音识别
- Qdrant / Redis（通过 Docker 启动）

---

## ❓ 常见问题

- **启动报错 ModuleNotFoundError** → `pip install -r requirements.txt`
- **数据库连接失败** → 检查 `.env` 的 `DATABASE_URL`；或切换 SQLite
- **LLM 401 / 超时** → 检查 API Key 与网络
- **SSE 流断开** → Nginx 必须设置 `proxy_buffering off`
- **静态资源 404** → 检查 Nginx `location` 路径
- **双库不一致** → `python scripts/reconcile_databases.py` 跑对齐

更多：[docs/部署与运维.md §故障排查](docs/部署与运维.md) · [docs/数据层与迁移.md §修复工具](docs/数据层与迁移.md)

---

## 👥 贡献者

- 项目维护：StarLearn Team
- 设计 / 实现：见 [docs/架构设计.md](docs/架构设计.md) 与 [docs/子系统详解.md](docs/子系统详解.md)

## 📜 许可证

本项目为内部项目，未经授权禁止外传。

---

> 最后更新：2026-08-27