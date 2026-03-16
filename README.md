<div align="center">

# 🛠 DDE Agent Skills
### *Documentation-Driven Engineering: The Deterministic R&D Operating System*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Protocol: DDE v1.4](https://img.shields.io/badge/Protocol-DDE%20v1.4-blueviolet)](docs/protocol/spec.md)
[![Maintenance: Active](https://img.shields.io/badge/Maintenance-Active-green.svg)](https://github.com/LeslieLinXinxiang/dde-agent-skills/pulse)

---

**DDE (Documentation-Driven Engineering)** is a shift from probabilistic agent behavior to deterministic governance. 
By enforcing strict hierarchical authority through markdown-based "Laws" (Layers 0-4), DDE turns any repository into a self-governing R&D platform.

[Features](#-features) • [Deployment](#-quick-start-the-laziest-way) • [Skills Dictionary](#-skills-dictionary) • [FAQ](#-faq) • [中文文档](#-dde-agent-skills-基于文档驱动工程的-rd-操作系统)

</div>

## 🚀 Quick Start (The Laziest Way)

Don't want to copy-paste? Just paste this link into your **Cursor/Windsurf/Claude Code** agent and say:

> "Deploy the DDE skills from this repository to my local agent skills directory."

**URL**: `https://github.com/LeslieLinXinxiang/dde-agent-skills`

---

## 🛠 Terminal Installation

### 1. Clone the protocol
```bash
git clone https://github.com/LeslieLinXinxiang/dde-agent-skills.git && cd dde-agent-skills
```

### 2. Deploy (Core Core)
```bash
python3 tools/sync_skills.py
```

## ✨ Features

- **🛡️ Deterministic Governance**: No code is written without explicit `[APPROVED]` gates.
- **📚 Layered Authority**: From Project Charter (L0) to Roadmap (L4).
- **🔄 Sync Orchestration**: Keep your skills consistent across Cursor, Windsurf, Trae, and Claude Code.
- **⚡ First-Principles Review**: Built-in sanity checks to prevent LLM hallucinations.

## 🏗 Architecture

```text
┌─────────────────────────────────────────────────────────┐
│              Layer 0: Project Charter (Law)             │
│   (Objective · Scope · Constraints · Non-Goals)         │
└──────────────┬──────────────────────────────────────────┘
               │
┌──────────────▼──────────────┐      ┌────────────────────┐
│   Layer 1: Architecture     │◄────┤  Layer 3: Protocol  │
│   (Modules · Dependencies)  │      │  (RFC · Gates)     │
└──────────────┬──────────────┘      └────────────────────┘
               │
┌──────────────▼──────────────┐      ┌────────────────────┐
│    Layer 2: Data & Spec     │      │  Layer 4: Roadmap  │
│    (Producers · Consumers)  │      │  (Timeline · Log)  │
└─────────────────────────────┘      └────────────────────┘
```

## 📂 Skills Dictionary

| Skill Name | Purpose |
| :--- | :--- |
| **`dde-bootstrap`** | The initializer. Enforces Layer 0-4 consistency and project grounding. |
| **`dde-code-guard`** | The gatekeeper. Implements the [PROPOSAL] -> [APPROVED] lifecycle. |
| **`dde-ext-verification-loop`** | Continuous verification of complex logic chains. |
| **`dde-ext-brainstorm`** | High-level architectural ideation without code side-effects. |
| **`dde-ext-search-first`** | Enforces "search first, code later" to prevent library re-invention. |
| **`dde-task-closer`** | Autonomous cleanup and verification of completed features. |
| **`drawio-graph-builder`** | Turns markdown specs into visual Draw.io diagrams. |

## 🚀 Deployment Guide (Scenario-based)

| Platform | Command |
| :--- | :--- |
| **Cursor (Global)** | `python3 tools/sync_skills.py --targets ~/.cursor/skills` |
| **Windsurf** | `python3 tools/sync_skills.py --targets ~/.agents/skills` |
| **Trae** | `python3 tools/sync_skills.py --targets ~/.trae/skills` |
| **Claude Code** | `python3 tools/sync_skills.py --targets ~/.agents/skills` |

## 🤝 Contributing
We follow the DDE protocol for this repository's development as well. Please submit an RFC for any core protocol changes.

---

<div align="center">

# DDE Agent Skills: 基于文档驱动工程的 R&D 操作系统

[English Readme](#-dde-agent-skills)

</div>

DDE (Documentation-Driven Engineering) 是一种面向 AI Agent 的确定性治理协议。通过将传统的概率性 Agent 逻辑转化为基于文档（Layer 0-4）的确定性治理，DDE 将任何仓库转变为一个自我管理的研发平台。

## 🚀 快速上手 (最懒办法)

不想手动执行？直接把下面的链接发给你的 **Cursor/Windsurf/Claude Code** Agent 并回复：

> “请帮我把这个仓库里的 DDE 技能部署到我的本地 Agent 技能目录中。”

**仓库地址**: `https://github.com/LeslieLinXinxiang/dde-agent-skills`

---

## 🛠 纯终端部署

### 1. 克隆仓库
```bash
git clone https://github.com/LeslieLinXinxiang/dde-agent-skills.git
cd dde-agent-skills
```

### 2. 一键安装
运行以下指令将核心技能同步到最常用的 Agent 目录：
```bash
python3 tools/sync_skills.py
```

## ✨ 核心特性

- **🛡️ 确定性行为**: 禁止未标记的假设，所有写入必须经过授权。
- **📚 五层架构**: 从项目宪章（Layer 0）到执行协议，层层递进。
- **🔄 多环境同步**: 完美支持 Cursor, Windsurf, Trae, Claude Code 等主流 IDE。
- **⚡ 第一性原理审查**: 内置审查机制，防止 LLM 幻觉和需求偏移。

## 📖 技能字典

| 技能名称 | 用途 |
| :--- | :--- |
| **`dde-bootstrap`** | 初始化器。强制执行 Layer 0-4 文档的一致性与项目对齐。 |
| **`dde-code-guard`** | 守门员。实施 [PROPOSAL] -> [APPROVED] 代码修改生命周期。 |
| **`dde-ext-verification-loop`** | 对复杂逻辑链进行持续验证。 |
| **`dde-ext-brainstorm`** | 高层架构构思，无代码副作用。 |
| **`dde-ext-search-first`** | 强制执行“先搜索，后写码”，防止重复造轮子。 |
| **`dde-task-closer`** | 自动清理并验证已完成的功能点。 |
| **`drawio-graph-builder`** | 将 Markdown 规范转换为可视化的 Draw.io 图表。 |

## 📜 核心原则
1. **禁止假设**: 未经标记的推断是被禁止的。
2. **硬性关卡**: 未经显式 `[APPROVED]`，禁止进行任何文件写入。
3. **唯一真理来源**: `/docs` 文件夹即法律。

---
*Created by Documentation-Driven Engineering. Built for the next generation of AI Engineers.*
