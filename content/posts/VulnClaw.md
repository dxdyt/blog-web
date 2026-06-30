---
title: VulnClaw
date: 2026-06-30T15:54:07+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1780856036092-1ef0934f3f55?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3ODI4MDU5NjZ8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1780856036092-1ef0934f3f55?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3ODI4MDU5NjZ8&ixlib=rb-4.1.0
---

# [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw)

<div align="center">

# VulnClaw 🦞

> *AI 驱动的渗透测试 CLI 工具 — 说人话，打漏洞。*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![OpenAI Compatible](https://img.shields.io/badge/API-OpenAI_Compatible-green)](https://platform.openai.com/)
[![MCP](https://img.shields.io/badge/Toolchain-MCP-orange)](https://modelcontextprotocol.io/)
[![PyPI](https://img.shields.io/badge/PyPI-v0.3.2-blueviolet)](https://pypi.org/project/vulnclaw/)
[![Security](https://img.shields.io/badge/Scope-Authorized_Only-red)](#-安全声明)
<br>

🌐 **English version**: [`README_EN.md`](README_EN.md)

**本项目是可独立运行的 AI 渗透测试 Agent。**

<br>

基于 LLM Agent + MCP 工具链 + 渗透 Skill 编排，
配合 OpenAI / MiniMax / DeepSeek 等兼容模型，
自然语言输入 → 自动完成「信息收集 → 漏洞发现 → 漏洞利用 → 报告生成」全流程。

[快速开始](#快速开始) · [架构设计](#️-架构) · [Skill 体系](#-内置-skill)

</div>

---

## 它能做什么

输入自然语言，AI 自动执行渗透测试全流程：

```
用户输入：帮我对 http://target.example.com 进行渗透测试

VulnClaw 自动执行：
  Round 1:  信息收集 → 指纹识别、端口扫描、目录枚举
  Round 2:  漏洞发现 → 检测注入点、已知 CVE、配置缺陷
  Round 3:  漏洞利用 → PoC 验证、权限获取
  Round 4:  报告生成 → 结构化报告 + Python PoC 脚本
```

<img width="1148" height="642" alt="image" src="https://github.com/user-attachments/assets/576e1cf6-25da-4969-864b-40e77d020dbf" />


适用于已授权的渗透测试、CTF 竞赛、安全教学、红队演练等场景。

---

## 特性

- **目标驱动求解引擎（默认）** — 抛弃固定轮数工作流，以「目标达成 / 探索前沿耗尽 / 安全预算」为终止条件，自动收敛
- **黑板图状态空间搜索** — 把渗透建模为从 origin 向 goal 的搜索：Fact（已确认事实）+ Intent（探索方向），结构上杜绝"原地打转"
- **证据级反幻觉闸门** — 声称的 flag/结论必须在真实工具输出里逐字符出现才被采信，杜绝凭空编造 flag 的假胜利
- **自然语言驱动** — 用人话描述渗透意图，自动识别阶段和工具
- **13 个 LLM Provider** — OpenAI / MiniMax / DeepSeek / 智谱 / Moonshot / 千问 / SiliconFlow / 豆包 / 百川 / 阶跃星辰 / 商汤 / 零一万物，一键切换
- **MCP 工具链** — 4 个 MCP 服务：`fetch` / `memory` 本地实现开箱即用，`chrome-devtools` / `burp` 对接外部 MCP 服务实现浏览器自动化和 HTTP 抓包重放
- **AI Agent 核心** — OpenAI 兼容协议 + Tool Calling + 自主渗透循环
- **结构化推理 + 自适应反思** — 已知事实/约束/攻击链结构化沉淀；失败自动归类并按 L0-L4 渐进升级 payload 绕过策略
- **漏洞检测插件体系** — 低耦合插件运行时 + 内置只读 Web 插件，结果自动汇入报告链路（`vulnclaw plugins`）
- **21 个渗透 Skill** — 7 核心 + 14 专项 Skill（含 CTF Web/Crypto/Misc、osint-recon、secknowledge-skill），含 180 个参考文档
- **编解码/加解密工具** — 29 种操作（Base64/Hex/URL/AES/JWT/Morse 等），LLM 可精确调用，不再靠猜测
- **Python 代码执行** — 内置 `python_execute` 工具，适合 payload 构造和响应解析；当前仍属高风险实验能力，不应视为强隔离沙箱
- **持续性渗透测试** — 周期循环（默认 100 轮/周期 × 10 周期 = 1000 轮），每周期自动生成报告，直到手动终止
- **推理过程显示控制** — `think on/off` 一键切换 LLM 思考过程的显示/隐藏，默认关闭，干净输出只看结论
- **沙盒模式提示词** — 解锁 AI 安全测试能力，CTF / 授权渗透场景专用
- **自动报告 & PoC** — 生成结构化 Markdown 报告和可运行的 Python PoC 脚本
- **Web UI 模式** — `vulnclaw web` 启动本地 Web 界面，浏览器操作渗透测试全流程，默认 `127.0.0.1:7788`
- **安全知识库** — 已内置知识库模块与基础种子数据，CLI 可维护；检索增强正在逐步接入主流程

---

## 架构升级：从「固定轮数工作流」到「目标驱动求解」

旧版自主渗透是**固定轮数循环**（跑满 N 轮才停），在弱模型上容易陷入"反复请求同一页面、嘴上说要测注入却不发包"的死循环。新版把渗透重构为**状态空间搜索**，这是本次重构的核心。

### 黑板图 + OODA 求解循环（默认引擎 `solve`）

把渗透看作从 **origin**（目标）向 **goal**（拿到 flag / shell / 确认高危漏洞）的有向搜索，用两个原语驱动：

| 原语 | 含义 |
|------|------|
| **Fact** | 已被真实工具输出证实的客观事实（探索的落脚点） |
| **Intent** | 声明的探索方向（尚未执行的一步），从 Fact 出发，结论后产出新 Fact |

循环结构（`vulnclaw/agent/solver.py`）：

```
REASON（读全图）→ 目标达成? / 提出新探索方向 / 不提出
        │
EXPLORE（领一个 Intent）→ 用工具实际执行 → 把确认的结论写回为一个 Fact
        │
终止：目标达成 / 探索前沿耗尽（Reason 不再提方向）/ 触达安全预算
```

**为什么结构上杜绝打转**：一旦"首页是登录框"成为一个 Fact，Reason 就不会再提"去看首页"，而是提"测 SQL 注入"；每个 Intent 领取一次、结论一次即标记 `concluded`/`abandoned`，**不可能重复**。终止由目标驱动，不再是数死轮数。

### 证据级反幻觉闸门

弱模型常凭空编造 flag。新引擎在 `solve()` 里录制**所有真实工具输出**（HTTP 响应体、`python_execute` 输出）作为唯一可信证据：

- **结论闸门**：Explore 结论里声称的 flag，若未在真实工具输出里逐字符出现 → 判定幻觉、丢弃、标记 `[未验证]`。
- **完成闸门**：Reason 宣布"目标达成"时，若目标要 flag 但真实输出里从无 flag → 拒绝完成、继续探索。
- **即时收敛**：一旦拿到经证据验证的 flag，立即完成，不再空跑验证轮。

> 这套机制对弱模型尤其友好：旧的固定轮数循环容易在重复请求里空转，而「目标驱动 + 证据反幻觉」会逼着 Agent 用真实工具输出一步步逼近目标，并拒绝任何无证据支撑的「完成」。

### 结构化推理 + 自适应反思

- **推理状态层**（`reasoning_state.py`）：已知事实（带置信度）、推理障碍（WAF/过滤等）、候选攻击链，结构化沉淀并注入提示词。
- **反思引擎**（`reflexion.py`）：失败自动归类（环境限制/路径错误/参数错误/信息不足），按 **L0-L4 渐进升级** payload 绕过策略（原始 → URL 编码 → 双写注释 → Unicode/hex → 多层混淆/换攻击面），persistent 模式跨周期保留失败记忆。

### 漏洞检测插件体系

低耦合插件运行时（`vulnclaw/plugins/`）+ 内置只读 Web 插件（安全响应头 / JWT / JS 端点分析），插件结果可去重合并进 `SessionState.findings` 进入报告链路。

> 切回旧的固定轮数引擎：`vulnclaw config set session.engine rounds`

---

## 快速开始

### 安装

```bash
# 从 PyPI 安装（推荐）
pip install vulnclaw

# 从源码安装
git clone https://github.com/Unclecheng-li/VulnClaw.git
cd VulnClaw
pip install -e .
```

### Docker 运行（可选）

镜像已内置 Web UI 以及默认 MCP 服务所需的运行时（`npx` / `uvx`），所有状态（配置、会话、目标、报告）持久化到 `/data` 数据卷。

```bash
cp .env.example .env          # 填入 VULNCLAW_LLM_API_KEY 等
docker compose up --build      # 构建镜像并启动 Web UI
# 打开 http://127.0.0.1:7788
```

也可用纯 docker 运行某条 CLI 命令：

```bash
docker run --rm -it \
  -e VULNCLAW_LLM_API_KEY=sk-your-key-here \
  -v vulnclaw-data:/data \
  vulnclaw:latest scan <target>
```

> ⚠️ 容器内的 `localhost` 指向容器自身。扫描宿主机服务请使用 `host.docker.internal`，扫描其它容器请共享网络并用容器名访问。详见 [DOCKER.md](DOCKER.md)。

### 四步启动

```bash
# 1. 选择提供商（自动填充 Base URL 和模型名）
vulnclaw config provider minimax   (或 openai/deepseek/zhipu/moonshot/qwen/siliconflow)

# 1.2（可选）自定义 Base URL 或模型名
vulnclaw config set llm.base_url https://your-own-api.example.com/v1 
vulnclaw config set llm.model your-model-name

# 2. 设置 API Key
vulnclaw config set llm.api_key sk-your-key-here
#    — 或改用 ChatGPT 订阅登录（无需 API Key）：
#      vulnclaw login   （浏览器登录；详见 docs/keyless-auth.md，注意 ToS 风险）

# 3. 默认：打开原 CLI / REPL
vulnclaw

# 4. 可选：打开 TUI 工作台
vulnclaw tui
```

### 环境检查

```bash
vulnclaw doctor
```

输出示例：

```
🦞 VulnClaw 环境检查

  Python: 3.14.4
  Node.js: v24.14.1
  npx: 已安装
  nmap: 已安装

LLM 配置:
  Provider: openai
  Auth Mode: static
  Credentials: configured
  Base URL: https://api.openai.com/v1
  Model: gpt-4o

MCP 服务:
  fetch: 已启用 [P0]
  memory: 已启用 [P0]
  ...

✅ 环境就绪，运行 vulnclaw 开始
```

---

## CLI 命令速查

`vulnclaw --help` 查看所有命令：

```bash
$ vulnclaw --help

🦞 VulnClaw — AI-powered penetration testing CLI

 Usage: vulnclaw [OPTIONS] COMMAND [ARGS]...

 Options:
   --version  Show version and exit.
   --help     Show this message and exit.

 Commands:
   run           🚀 一键全流程渗透测试
   persistent    🔄 持续性渗透测试（100轮/周期）
   recon         🔍 仅信息收集阶段
   scan          🔎 执行漏洞扫描阶段
   exploit       💥 执行漏洞利用阶段
   report        📝 从会话记录生成报告
   repl          💬 启动经典 REPL 交互界面
   config        ⚙️  管理配置（set/get/list/provider）
   init          🔧 初始化配置
   doctor        🏥  检查运行环境
   tui           🖥️  打开终端图形化工作台
   web           🌐 启动本地 Web UI
```

### 命令详解

| 命令 | 说明 | 示例 |
|------|------|------|
| `vulnclaw` | 默认打开原 CLI / REPL 交互界面 | `vulnclaw` |
| `vulnclaw tui` | 显式打开终端图形化工作台 | `vulnclaw tui` / `vulnclaw tui --target target.com` |
| `vulnclaw repl` | 启动经典 REPL 交互界面 | `vulnclaw repl` |
| `vulnclaw solve <target>` | 目标驱动求解（无固定轮数，拿到目标即停） | `vulnclaw solve target.com --goal "拿到flag"` |
| `vulnclaw run <target>` | 一键全流程渗透（默认走 solve 引擎） | `vulnclaw run 192.168.1.1` |
| `vulnclaw persistent <target>` | 持续性渗透（100轮/周期） | `vulnclaw persistent 192.168.1.1` |
| `vulnclaw recon <target>` | 仅信息收集（不利用漏洞） | `vulnclaw recon target.com` |
| `vulnclaw scan <target>` | 漏洞扫描阶段 | `vulnclaw scan target.com --ports 80,443` |
| `vulnclaw exploit <target>` | 漏洞利用阶段 | `vulnclaw exploit target.com --cve CVE-2024-1234` |
| `vulnclaw report <session>` | 从会话 JSON 生成报告 | `vulnclaw report session_xxx.json` |
| `vulnclaw config set <key> <value>` | 设置配置项 | `vulnclaw config set llm.api_key sk-xxx` |
| `vulnclaw config get <key>` | 查看配置项 | `vulnclaw config get llm.model` |
| `vulnclaw config list` | 列出所有配置 | `vulnclaw config list` |
| `vulnclaw config provider <name>` | 切换 LLM 提供商 | `vulnclaw config provider minimax` |
| `vulnclaw init` | 初始化配置文件 | `vulnclaw init` |
| `vulnclaw doctor` | 检查运行环境 | `vulnclaw doctor` |
| `vulnclaw plugins list` | 列出漏洞检测插件 | `vulnclaw plugins list --stage discovery` |
| `vulnclaw plugins info <id>` | 查看插件元信息 | `vulnclaw plugins info builtin.web.headers` |
| `vulnclaw plugins run <id>` | 运行插件（仅分析传入数据） | `vulnclaw plugins run builtin.web.headers --input headers.json --session s.json` |
| `vulnclaw web` | 启动本地 Web UI | `vulnclaw web` / `vulnclaw web --port 8080` |

### TUI 工作台

`vulnclaw tui` 是可选的终端图形化工作台入口。它会在终端中展示授权目标、检查模式、运行概览、安全边界、命令预览、历史状态、报告和内联环境诊断，让用户先确认范围再启动任务。

```bash
vulnclaw tui
vulnclaw tui --target https://target.example --mode quick --only-port 443
vulnclaw tui --dry-run --target https://target.example --mode deep --only-path /admin
```

默认 `vulnclaw` 仍然进入原 CLI / REPL 交互；只有显式输入 `vulnclaw tui` 才会进入 TUI。
运行概览会读取已选目标的历史快照、风险数量、持久化约束和约束拦截次数，帮助用户在继续测试前确认上下文没有衰减。
在 TUI 的“设置测试范围”中可以直接编辑允许动作和禁止动作，例如只允许 `recon,scan`，或禁止 `exploit,post_exploitation`。

### 配置管理

```bash
# 查看所有提供商并切换
vulnclaw config provider --list    # 查看所有可用提供商
vulnclaw config provider minimax   # 切换到 MiniMax

# 手动设置（custom 模式）
vulnclaw config set llm.base_url https://your-api.com/v1
vulnclaw config set llm.model your-model-name
vulnclaw config set llm.api_key sk-your-key
```

---

## 使用方式

### 方式一：原 CLI / REPL 交互模式（默认）

```bash
$ vulnclaw
```

无参数启动会进入原本的 🦞 交互界面，用自然语言对话：

```
🦞 vulnclaw> 对 192.168.1.100 进行渗透测试，这是我授权的靶场

[*] 进入自主渗透模式，按 Ctrl+C 可随时中断
── Round 1 ──
  [+] 目标: 192.168.1.100
  [+] 开放端口: 22, 80, 443, 8080
```

### 方式二：TUI 工作台（显式启用）

```bash
$ vulnclaw tui
```

TUI 会先展示目标、检查模式、运行概览和安全边界，让你确认授权范围后再启动任务：

```text
VulnClaw TUI 工作台

授权目标        https://example.com
检查模式        快速摸底 / recon
运行概览        历史快照、风险数量、持久化约束、约束拦截
安全边界        仅测试端口 443，禁止 exploit/persistent/post_exploitation

1 设置授权目标
2 选择检查模式
3 设置测试范围
4 开始授权安全检查
8 模型/API 配置
```

常用启动方式：

```bash
vulnclaw tui
vulnclaw tui --target https://target.example --mode quick --only-port 443
vulnclaw tui --dry-run --target https://target.example --mode deep --only-path /admin
```

菜单 3 “设置测试范围”可编辑主机、端口、路径、排除项、允许动作和禁止动作；这些边界会进入启动前确认和实际任务命令。
菜单 7 “环境诊断入口”会在 TUI 内显示 Python、Node/npx/uvx/nmap、LLM 配置和 MCP 服务/工具摘要；需要完整详情时再运行 `vulnclaw doctor`。
菜单 8 “模型/API 配置”可直接切换 Provider、Base URL、Model 和 API Key，保存后工作台会立刻使用新配置。

### 方式三：经典 REPL 子命令

```bash
$ vulnclaw repl
```

进入经典 🦞 交互界面，用自然语言对话：

```
🦞 vulnclaw> 对 192.168.1.100 进行渗透测试，这是我授权的靶场

[*] 进入自主渗透模式，按 Ctrl+C 可随时中断
── Round 1 ──
  [+] 目标: 192.168.1.100
  [+] 开放端口: 22, 80, 443, 8080
  [+] Web 指纹: Apache/2.4.62
── Round 2 ──
  [+] 发现 /manager/html (Tomcat Manager)
  [+] 命中 CVE-202X-XXXX: Apache Tomcat 认证绕过
── Round 3 ──
  [+] 漏洞验证成功

🦞 192.168.1.100 | 报告> 生成渗透报告
[+] 报告已保存: ./reports/192.168.1.100_20260418.md
[+] PoC 脚本已保存: ./pocs/CVE-202X-XXXX.py
```

#### 经典 REPL 内置命令

| 命令                  | 说明                                       |
| --------------------- | ------------------------------------------ |
| `target <host>`       | 设置渗透测试目标                           |
| `status`              | 查看当前状态（目标、阶段、工具、推理显示） |
| `tools`               | 列出当前可用 MCP 工具                      |
| `think`               | 切换推理过程显示/隐藏                      |
| `think on` / `off`    | 精确控制推理过程显示                       |
| `persistent`          | 启动持续性渗透测试（100轮/周期，自动报告） |
| `persistent <host>`   | 对指定目标启动持续性渗透                   |
| `clear`               | 清空当前会话                               |
| `help`                | 显示帮助信息                               |
| `exit` / `quit` / `q` | 退出 VulnClaw                              |

#### 自主渗透模式

VulnClaw 检测到以下关键词 + 目标时，自动进入多轮自主渗透循环：

| 触发方式 | 示例 |
| -------- | ---- |
| 渗透指令 | `对 http://target.com 进行渗透测试` |
| CTF / 找 flag | `帮我对 http://ctf.site 找出flag` |
| 爆破 / 绕过 | `对 http://target.com 弱口令爆破` |
| **显式触发** | `目标：http://target.com，进入自主渗透模式` |

> 💡 在 REPL 中输入 `Ctrl+C` 可随时中断自主循环。切换目标时自动重置会话上下文。

### 方式二：单命令模式

```bash
# 一键全流程渗透测试
vulnclaw run 192.168.1.100

# 持续性渗透测试（每周期100轮，最多10周期，自动生成报告）
vulnclaw persistent 192.168.1.100

# 自定义周期参数
vulnclaw persistent 192.168.1.100 --rounds 200 --cycles 5

# 仅信息收集
vulnclaw recon 192.168.1.100

# 漏洞扫描（可指定端口）
vulnclaw scan 192.168.1.100 --ports 80,443,8080

# 漏洞利用（可指定 CVE）
vulnclaw exploit 192.168.1.100 --cve CVE-2024-1234 --cmd id

# 生成报告
vulnclaw report session.json
```

### 方式三：持续性渗透模式

适用于需要长时间深度渗透的场景。VulnClaw 以**周期循环**方式运行：

```
┌──────────────────────────────────────────────┐
│  Cycle 1 (100轮) → 自动报告 → 继续          │
│  Cycle 2 (100轮) → 自动报告 → 继续          │
│  Cycle 3 (100轮) → 自动报告 → 继续          │
│  ...                                         │
│  直到 Ctrl+C 或达到最大周期数（默认10）      │
└──────────────────────────────────────────────┘
```

**特点**：
- **跨周期状态保持** — 每个周期保留之前的所有发现、漏洞和步骤记录
- **周期报告** — 每个周期结束自动生成独立的 Markdown 报告（含新增漏洞和累计汇总）
- **灵活中断** — Ctrl+C 随时中断，中断时仍生成本周期报告
- **增量发现** — 报告区分"本周期新增"和"累计总计"，清晰追踪进展
- **可配置** — 每周期轮数、最大周期数、是否自动报告均可配置

```bash
# CLI 方式
vulnclaw persistent 192.168.1.100              # 默认 100轮/周期 × 10周期
vulnclaw persistent 192.168.1.100 -r 200 -c 5  # 200轮/周期 × 5周期
vulnclaw persistent 192.168.1.100 --no-report   # 不自动生成报告

# TUI 方式
vulnclaw tui --target 192.168.1.100 --mode continuous

# REPL 方式
🦞 vulnclaw> target 192.168.1.100
🦞 vulnclaw> persistent
# 或直接
🦞 vulnclaw> persistent 192.168.1.100
```

### 方式四：Web UI 模式

通过浏览器操作渗透测试全流程，适合偏好图形界面的用户。

```bash
# 安装 Web 依赖
pip install vulnclaw[web]

# 启动 Web UI（默认 127.0.0.1:7788）
vulnclaw web

# 自定义端口
vulnclaw web --port 8080

# 仅检查启动信息（不实际启动服务）
vulnclaw web --dry-run
```

启动后浏览器访问 `http://127.0.0.1:7788` 即可使用。

> ⚠️ 默认仅绑定本地回环地址。如需远程访问须显式指定 `--host 0.0.0.0 --allow-remote`，请确保网络环境安全。

---

## LLM 提供商配置

VulnClaw 支持所有 OpenAI 兼容协议的 API，内置 8 个提供商预设：

```bash
vulnclaw config provider --list    # 查看所有提供商
vulnclaw config provider minimax   # 一键切换
```

| 提供商      | 命令                   | 默认模型              |
| ----------- | ---------------------- | --------------------- |
| OpenAI      | `provider openai`      | gpt-4o                |
| MiniMax     | `provider minimax`     | MiniMax-M3            |
| DeepSeek    | `provider deepseek`    | deepseek-v4-pro       |
| 智谱 GLM    | `provider zhipu`       | glm-4.7               |
| Kimi        | `provider moonshot`    | kimi-k2.6             |
| 通义千问    | `provider qwen`        | qwen3-max             |
| SiliconFlow | `provider siliconflow` | DeepSeek-V4-Flash     |
| 豆包        | `provider doubao`      | Doubao-Seed-2.0-Pro   |
| 百川        | `provider baichuan`    | Baichuan4-Turbo       |
| 阶跃星辰    | `provider stepfun`     | step-3.5-flash        |
| 商汤        | `provider sensetime`   | SenseNova-6.7-Flash-Lite |
| 零一万物    | `provider yi`          | yi-lightning          |
| 自定义      | `provider custom`      | 手动填写              |

---

## 架构

```
┌─────────────────────────────────────────────┐
│                VulnClaw CLI                  │
│  ┌─────────┐  ┌─────────┐  ┌────────────┐  │
│  │  自然语言 │  │  任务编排 │  │ 报告 & PoC │  │
│  │  交互层  │  │  引擎    │  │   生成器   │  │
│  └────┬────┘  └────┬────┘  └─────┬──────┘  │
│       └─────────────┼─────────────┘        │
│               ┌─────▼──────┐                │
│               │ LLM Agent  │                │
│               │ (越狱+Skill)│               │
│               └─────┬──────┘                │
│               ┌─────▼──────┐                │
│               │ MCP 编排层  │                │
│               │ (4 服务)   │                │
│               └─────┬──────┘                │
│               ┌─────▼──────┐                │
│               │ 安全知识库  │                │
│               └────────────┘                │
└─────────────────────────────────────────────┘
```

### 核心模块

| 模块           | 文件                                             | 说明                                          |
| -------------- | ------------------------------------------------ | --------------------------------------------- |
| **CLI/TUI 入口** | `cli/main.py` + `cli/tui.py`                   | Typer 命令 + 默认原 CLI/REPL + 显式 TUI       |
| **Agent 核心** | `agent/core.py`                                  | AgentCore 协调入口（核心重构后主要保留少量协调职责） |
| **求解引擎（默认）** | `agent/solver.py` + `agent/blackboard.py`  | 目标驱动 OODA 循环 + Fact/Intent 黑板图 + 证据级反幻觉闸门 |
| **推理 / 反思**   | `agent/reasoning_state.py` + `reflexion.py`   | 结构化事实/约束/攻击链 + 失败归类与 L0-L4 升级 |
| **插件体系**   | `plugins/`（registry/runtime/web）                | 低耦合漏洞检测插件运行时 + 内置只读 Web 插件   |
| **动态提示词** | `agent/prompts.py`                               | 基础身份 + 核心契约 + Skill + MCP 工具列表    |
| **Prompt 组装** | `agent/system_prompt.py` + `prompt_context.py`  | system prompt / round context / attack summary 组装 |
| **输入分析**   | `agent/input_analysis.py`                        | 目标识别、阶段识别、用户漏洞提示提取          |
| **反死循环 / CTF** | `agent/anti_loop.py` + `ctf_mode.py`        | 完成信号、攻击路径、失败目标、flag 状态机      |
| **会话状态**   | `agent/context.py`                               | 阶段追踪 + 漏洞发现 + 步骤记录                |
| **Skill / KB 上下文** | `agent/skill_context.py` + `kb_context.py` | Skill 选择与知识库 prompt 注入                |
| **目标状态继承** | `target_state/store.py`                        | 同目标成果沉淀、恢复、快照、回滚、target 报告 |
| **MCP 编排**   | `mcp/registry.py` + `lifecycle.py` + `router.py` | 服务注册 + 生命周期 + 自然语言→工具路由       |
| **Skill 调度** | `skills/loader.py` + `dispatcher.py`             | 目录格式 Skill + CTF/SRC/AI/Web 等意图动态调度 |
| **编解码工具** | `skills/crypto_tools.py`                         | 29 种编解码/加解密操作，注册为内置 Agent 工具  |
| **配置管理**   | `config/schema.py` + `settings.py`               | Pydantic 模型 + YAML 持久化 + 8 Provider 预设 |
| **报告生成**   | `report/generator.py` + `poc_builder.py`         | Markdown 报告 + Python PoC 模板               |
| **安全知识库** | `kb/store.py` + `retriever.py`                   | JSON 存储 + CVE/技术/工具检索                 |

---

## MCP 工具链

| MCP 服务 | 工具数 | 模式 | 用途 | 状态 |
|---|---|---|---|---|
| fetch | 1 | 本地 (httpx) | HTTP 请求、API 测试 | 开箱即用 |
| memory | 2 | 本地 (JSON) | 上下文记忆、状态持久化 | 开箱即用 |
| chrome-devtools | 31+ | stdio MCP | 浏览器自动化、截图、JS 执行 | 需部署 |
| burp | 多个 | stdio MCP | HTTP 抓包、重放、漏洞扫描 | 需部署 |

> 另有 5 个内置 Agent 工具（`python_execute` + `nmap_scan` + `crypto_decode` + `brute_force_login` + `load_skill_reference`），无需 MCP 即可调用。

### Chrome DevTools MCP 部署

[仓库: ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) — 31+ 工具，覆盖点击/表单/截图/JS执行/网络监控/性能分析

**前置条件**: Node.js LTS (v20+) + Chrome 浏览器

```bash
# Step 1: 启动 Chrome 远程调试
# Windows
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir=C:\tmp\chrome-debug
# Linux/Mac
google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug

# Step 2: 启用 VulnClaw 配置（自动通过 npx 拉取，无需手动安装）
vulnclaw config set mcp.servers.chrome-devtools.enabled true
```

VulnClaw 配置已内置 `npx -y chrome-devtools-mcp@latest`，启用后自动连接。如需指定 Chrome 调试地址，编辑 `~/.vulnclaw/config.yaml`：

```yaml
mcp:
  servers:
    chrome-devtools:
      enabled: true
      transport:
        type: stdio
        command: npx
        args: ["-y", "chrome-devtools-mcp@latest", "--browser-url=http://127.0.0.1:9222"]
```

### Burp Suite MCP 部署

[仓库: PortSwigger/mcp-server](https://github.com/PortSwigger/mcp-server) — 官方 MCP 扩展，支持 SSE + Stdio 协议

**前置条件**: Java 11+ + Burp Suite Professional

```bash
# Step 1: 克隆并构建
git clone https://github.com/PortSwigger/mcp-server.git burp-mcp
cd burp-mcp
./gradlew embedProxyJar    # Windows: gradlew.bat embedProxyJar
# 产物: build/libs/burp-mcp-all.jar

# Step 2: 加载到 Burp Suite
# Burp → Extensions → Add → Type: Java → 选择 burp-mcp-all.jar

# Step 3: 在 Burp 的 MCP 标签页勾选 "Enabled"（默认监听 127.0.0.1:9876）

# Step 4: 启用 VulnClaw 配置
vulnclaw config set mcp.servers.burp.enabled true
```

建议将 JAR 复制到固定位置并更新配置：

```yaml
mcp:
  servers:
    burp:
      enabled: true
      transport:
        type: stdio
        command: java
        args: ["-jar", "~/.vulnclaw/tools/burp-mcp-all.jar", "--sse-url", "http://127.0.0.1:9876"]
```

> 详细部署说明参见 [docs/mcp-deployment.md](docs/mcp-deployment.md)

---

## 内置 Skill

### 核心 Skill (7)

| Skill             | 说明               |
| ----------------- | ------------------ |
| pentest-flow      | 渗透测试全流程编排 |
| recon             | 信息收集流程       |
| vuln-discovery    | 漏洞发现流程       |
| exploitation      | 漏洞利用流程       |
| post-exploitation | 后渗透流程         |
| reporting         | 报告生成流程       |
| waf-bypass        | WAF 绕过技巧库     |

### 专项 Skill (14)

| Skill                     | 参考文档数 | 说明                                         |
| ------------------------- | ---------- | -------------------------------------------- |
| web-pentest               | 4          | Web 应用渗透                                 |
| android-pentest           | 9          | 安卓应用渗透                                 |
| client-reverse            | 20         | 客户端逆向分析                               |
| web-security-advanced     | 34         | Web 安全进阶（注入、绕过、利用链）           |
| ai-mcp-security           | 7          | AI/MCP 安全测试                              |
| intranet-pentest-advanced | 15         | 内网渗透进阶                                 |
| pentest-tools             | 18         | 渗透工具速查                                 |
| rapid-checklist           | 3          | 快速检查清单                                 |
| crypto-toolkit            | 3          | 编解码/加解密（29 种操作，注册为内置工具）   |
| **ctf-web**               | 9          | CTF Web 攻击知识库（PHP绕过/RCE/SSTI/反序列化） |
| **ctf-crypto**            | 6          | CTF 密码学攻击知识库（RSA/AES/ECC/PRNG/格攻击） |
| **ctf-misc**              | 6          | CTF 杂项知识库（PyJail/BashJail/编码链/VM逆向） |
| **osint-recon**           | 7          | OSINT 开源情报收集（四维模型：服务器/网站/域名/人员） |
| **secknowledge-skill**    | 39         | Web+AI 安全测试知识库，面向 CTF/SRC/众测场景（WooYun/先知/GAARM/OWASP 方法论） |

Skill 会根据用户输入自动调度，无需手动选择。专项 Skill 含 `references/` 目录下的详细方法论文档，LLM 可通过 `load_skill_reference` 工具按需加载。

`secknowledge-skill` 集成自 [`Pa55w0rd/secknowledge-skill`](https://github.com/Pa55w0rd/secknowledge-skill)，上游 `references/` 的 38 个文档已完整纳入，并额外增加 `vulnclaw-ctf-src-routing.md` 作为 VulnClaw 的 CTF/SRC 场景导航。它会在 `SRC`、`漏洞挖掘`、`众测`、`GAARM`、`OWASP LLM/ASI/WSTG`、`Web+AI` 等强信号输入下触发，用于按需加载 SQLi、XSS、RCE、SSRF、AI/MCP、Agent、风险矩阵和测试方法论等资料。

### 内置编解码/加解密工具 (crypto_decode)

`crypto_decode` 注册为 Agent 内置工具，LLM 在任何上下文中均可调用，不再靠猜测解码结果：

| 类别     | 操作                                                                                     |
| -------- | ---------------------------------------------------------------------------------------- |
| 编解码   | base64, base32, base58, hex, url, html, unicode, rot13, caesar, morse（各有 encode/decode） |
| 哈希     | md5, sha1, sha256, sha512                                                                |
| 加解密   | aes_encrypt, aes_decrypt（CBC 模式，PKCS7 填充）                                          |
| JWT      | jwt_decode, jwt_encode                                                                   |
| 自动识别 | auto_decode — 尝试所有常见编码，返回匹配结果                                              |

---

## 配置管理

### 命令行配置

```bash
vulnclaw config list                          # 查看所有配置
vulnclaw config get llm.model                 # 查看单项
vulnclaw config set llm.api_key sk-xx         # 设置 API Key
vulnclaw config set session.max_rounds 30     # 设置自主渗透最大轮数（默认 15）
vulnclaw config set session.stale_rounds_threshold 8  # 设置死循环检测阈值（默认 5）
vulnclaw config set session.show_thinking false # 隐藏推理过程（也可在 REPL 中用 think off）
```

### 可配置项

| 配置项                   | 默认值 | 说明                                     |
| ------------------------ | ------ | ---------------------------------------- |
| `llm.provider`           | openai | LLM 提供商（8 个内置 + custom）          |
| `llm.api_key`            | 空     | API Key（auth_mode=static）              |
| `llm.auth_mode`          | static | `static`（api_key）或 `oauth`（`vulnclaw login`） |
| `llm.chatgpt_auto_proxy` | false  | 自动启动内置 ChatGPT 后端桥接代理         |
| `llm.base_url`           | 按 provider | API 基础 URL，可自定义              |
| `llm.model`              | 按 provider | 模型名称，可自定义                   |
| `llm.temperature`        | 0.1    | 采样温度                                 |
| `llm.max_tokens`         | 4096   | 单次最大输出 token                       |
| `session.engine`         | solve  | 自主引擎：`solve`（目标驱动，默认）/ `rounds`（旧固定轮数） |
| `session.solve_max_steps` | 40    | solve 探索步数安全上限（兜底，非固定工作流长度） |
| `session.solve_max_intents` | 3   | 每次 Reason 最多提出的新探索方向数        |
| `session.solve_max_tool_rounds` | 6 | 每个 Intent 探索的最大工具调用轮数        |
| `session.max_rounds`     | 15     | 旧 `rounds` 引擎的最大轮数（建议 10-50）  |
| `session.output_dir`     | ./vulnclaw-output | 报告输出目录                    |
| `session.report_format`  | markdown | 报告格式（markdown / html）            |
| `session.poc_language`   | python | PoC 生成语言（python / bash）            |
| `session.show_thinking`  | false  | 显示 LLM 推理过程（think 标签内容，默认关闭） |
| `session.persistent_rounds_per_cycle` | 100 | 持续性渗透每周期轮数 |
| `session.persistent_max_cycles` | 10 | 持续性渗透最大周期数（0=无限） |
| `session.persistent_auto_report` | true | 持续性渗透每周期自动生成报告 |
| `session.stale_rounds_threshold` | 5 | 死循环检测阈值 — 连续无新发现轮数达到此值时触发强制策略切换 |

### 环境变量

| 变量                          | 说明                   |
| ----------------------------- | ---------------------- |
| `VULNCLAW_LLM_PROVIDER`       | LLM 提供商名称         |
| `VULNCLAW_LLM_API_KEY`        | API Key                |
| `VULNCLAW_LLM_AUTH_MODE`      | static / oauth         |
| `VULNCLAW_LLM_CHATGPT_AUTO_PROXY` | 内置 ChatGPT 代理  |
| `VULNCLAW_LLM_BASE_URL`       | API 基础 URL           |
| `VULNCLAW_LLM_MODEL`          | 模型名称               |
| `VULNCLAW_SESSION_MAX_ROUNDS`| 自主渗透最大轮数       |
| `VULNCLAW_SESSION_STALE_ROUNDS_THRESHOLD` | 死循环检测阈值 |
| `VULNCLAW_SESSION_REASONING_STATE_ENABLED` | 结构化推理状态开关 |
| `VULNCLAW_SESSION_REFLEXION_ENABLED` | 自适应反思引擎开关 |
| `VULNCLAW_SESSION_REFLEXION_MAX_SAME_VULN_FAILS` | 同类漏洞连败触发反思阈值 |
| `VULNCLAW_SESSION_ESCALATION_MAX_LEVEL` | Payload 升级上限（0-4） |
| `VULNCLAW_SESSION_PLUGIN_RUNTIME_ENABLED` | 插件运行时开关 |
| `VULNCLAW_SESSION_PLUGIN_MAX_REQUESTS_PER_TARGET` | 单目标插件请求预算 |

优先级：**环境变量 > 配置文件 > 内置默认值**

配置文件位于 `~/.vulnclaw/config.yaml`。

---

## 更新日志

### v0.4.1

**并行探索 + 记忆引擎 + 信息收集工具链 + MCP streamable-http**

- **多 intent 并行探索** — solve 引擎支持同时探索多个方向（默认 max_parallel=3），单个方向异常不影响其他，每个 intent 有独立的证据缓冲区和工具调用记录。
- **agent 记忆引擎** — blackboard 新增工具调用日志（跨 intent 可见），reason 阶段显式列出已放弃方向并禁止重复提出，explore 上下文带"已执行工具"摘要；checkpoint 机制在图状态没变时跳过 reason 避免空转；已放弃方向做 Jaccard 去重兜底。
- **conclude 判定优化** — 放宽了"有进展"的标准（发现新接口、确认未授权都算推进），不再轻易丢弃有价值的发现；最后一步注入 conclude override 指令防止空转；证据兜底防止 conclude 误判丢弃实际有数据返回的探索。
- **完成判定否定闸门** — 模型在 complete 字段里写"未达到完成标准"等否定结论时不会再被误判为已完成；显式要求 complete=true 布尔值 + evidence fact 引用。
- **JS 信息收集（js_recon）** — 抓取页面及全部 JS 文件，提取 API 路径 / 关联域名 / 硬编码密钥；动态发现 PascalCase 实体名并与 base path + CRUD 动词排列组合推断隐藏接口；收集到的接口自动做 GET+POST 未授权探测。
- **未授权探测（unauth_test）** — 批量无凭据请求，按状态码/响应体/内容类型判定；支持有/无 token 差分对比确认未授权；自动跳过 delete/save/sms 等破坏性接口。
- **目录枚举（dir_enum）** — 并发字典爆破，带 404 基线与全局伪装 200 识别（随机路径返回 200 自动停止），状态码与响应长度过滤。
- **空间测绘（space_search）** — FOFA / Hunter / Quake / Shodan / ZoomEye / 0.zone 六引擎统一查询，engine=all 时并发查询所有已配置 key 的引擎。
- **子域名枚举（subdomain_enum）** — 空间测绘被动聚合 + 内置字典 DNS 爆破，自动去重。
- **MCP streamable-http 支持** — 支持 Chrome DevTools MCP 等 HTTP 传输的 MCP 服务器；惰性连接（启动时不占 session slot）；首次调用时自动建连 + 工具发现；连接失败降级为 service_unavailable 不影响 solve 循环。
- **Chrome MCP 工具名修正** — 占位工具改为真实 Chrome MCP 工具名（chrome_navigate / chrome_read_page / chrome_pentest_* 等）。
- 工具返回 undefined 标记为失败而非静默成功；fact_seq / intent_seq session 恢复后正确续接；新增 ReconConfig 配置区块与 solve_max_parallel 配置项。

### v0.4.0

**核心：自主引擎从「固定轮数工作流」重构为「目标驱动求解」**

- **新增目标驱动求解引擎（默认）** — 基于 Fact/Intent 黑板图的 OODA 循环，以「目标达成 / 探索前沿耗尽 / 安全预算」为终止条件，结构上杜绝"原地打转"；新增 `vulnclaw solve` 命令，`run`/REPL 自主模式默认改走该引擎（`session.engine=rounds` 可回退旧逻辑）。
- **新增证据级反幻觉闸门** — 录制所有真实工具输出作为唯一可信证据；声称的 flag/完成必须在真实输出里逐字符出现才被采信，否则判定幻觉并继续探索；拿到验证过的 flag 即时收敛。
- **新增结构化推理 + 自适应反思** — 已知事实（带置信度）/约束/攻击链结构化沉淀并注入提示词；失败自动归类并按 L0–L4 渐进升级 payload 绕过策略，persistent 模式跨周期保留失败记忆。
- **新增漏洞检测插件体系** — 低耦合插件运行时 + 内置只读 Web 插件（安全响应头 / JWT / JS 端点），结果可去重合并进 findings 与报告链路；新增 `vulnclaw plugins list/info/run` 命令。
- **修复 #45 工具被误约束** — 动作约束不再把 HTTP 方法（OPTIONS/POST）或使用 `requests` 误判为「利用」；只有实际攻击载荷（SQLi/RCE/路径穿越等）才算 exploit；`load_skill_reference`/`crypto_decode` 等纯本地工具豁免范围约束。
- 新增 `session.engine` / `solve_*` / `reflexion_*` / `plugin_*` 等配置项，均支持环境变量注入。

---

## 安全声明

VulnClaw 仅用于**已授权的安全测试**。使用本工具前，请确保：

1. 你已获得目标系统的**明确授权**
2. 测试范围已与目标所有者**书面确认**
3. 你遵守当地**法律法规**

未经授权对系统进行渗透测试是违法行为。本工具作者不对滥用行为承担责任。

---

## 许可证

[MIT License](LICENSE)

---

## 加入社区

与更多安全爱好者一起交流、分享与成长

| 社区交流群 | 开发者群聊 |
|:--:|:--:|
| 欢迎加入讨论分享，获取最新产品动态与使用技巧 | 加入我们，参与开源贡献与技术深度探讨 |
| ![VulnClaw 社区交流群](assets/社区交流群.jpg) | ![VulnClaw 开发者群聊](assets/VulnClaw开发者群聊.png) |
| **QQ 群号：954402631** | **QQ 群号：1065858551** |

---

<div align="center">

> 🦞 **VulnClaw** — 让每一次渗透都有章可循。

</div>
