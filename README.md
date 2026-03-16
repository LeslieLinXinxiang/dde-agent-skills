<div align="center">

# 🛠 DDE Agent Skills
### *Documentation-Driven Engineering: The Deterministic R&D Operating System*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Protocol: DDE v1.4](https://img.shields.io/badge/Protocol-DDE%20v1.4-blueviolet)](docs/protocol/spec.md)
[![Maintenance: Active](https://img.shields.io/badge/Maintenance-Active-green.svg)](https://github.com/YOUR_USERNAME/dde-agent-skills/pulse)

---

**DDE (Documentation-Driven Engineering)** is a shift from probabilistic agent behavior to deterministic governance. 
By enforcing strict hierarchical authority through markdown-based "Laws" (Layers 0-4), DDE turns any repository into a self-governing R&D platform.

[Features](#-features) • [Architecture](#-architecture) • [Deployment](#-deployment-guide) • [FAQ](#-faq) • [中文文档](#-dde-agent-skills-基于文档驱动工程的-rd-操作系统)

</div>

## 🚀 Quick Start (The Laziest Way)

Don't want to copy-paste? Just paste this link into your **Cursor/Windsurf/Claude Code** agent and say:

> "Deploy the DDE skills from this repository to my local agent skills directory."

**URL**: `https://github.com/YOUR_USERNAME/dde-agent-skills`

---

## 🛠 Terminal Installation

### 1. Clone the protocol
```bash
git clone https://github.com/YOUR_USERNAME/dde-agent-skills.git && cd dde-agent-skills
```

### 2. Deploy to your primary Agent environment
```bash
python3 tools/sync_skills.py
```

## ✨ Features

- **🛡️ Deterministic Governance**: No code is written without explicit `[APPROVED]` gates.
- **📚 Layered Authority**: From Project Charter (L0) to Roadmap (L4).
- **🔄 Sync Orchestration**: Keep your skills consistent across Cursor, Windsurf, Trae, and Claude Code.
- **⚡ First-Principles Review**: Built-in sanity checks to prevent LLM hallucinations and scope creep.

## 🏗 Architecture

The DDE system operates on a five-layer documentation authority model:

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

## 📂 Project Structure

```text
.
├── 🛠 skills/           # Modular Agent Skills (Atomic SKILL.md)
│   ├── dde-bootstrap   # Project initializer & L0-L4 enforcer
│   ├── dde-code-guard  # Two-phase modification gatekeeper
│   └── ...             # Subordinate extensions (test, verify, research)
├── 📖 docs/             # DDE Protocol Specifications
└── 🔧 tools/            # Terminal-centric sync & validation tools
```

## 🚀 Deployment Guide (Scenario-based)

| Platform | Command |
| :--- | :--- |
| **Cursor (Global)** | `python3 tools/sync_skills.py --targets ~/.cursor/skills` |
| **Windsurf** | `python3 tools/sync_skills.py --targets ~/.agents/skills` |
| **Trae** | `python3 tools/sync_skills.py --targets ~/.trae/skills` |
| **Claude Code** | `python3 tools/sync_skills.py --targets ~/.agents/skills` |
| **Antigravity** | `python3 tools/sync_skills.py --targets ~/.agents/skills` |

## 🤝 Contributing
We follow the DDE protocol for this repository's development as well. Please submit an RFC for any core protocol changes.

---

<div align="center">

# DDE Agent Skills: 基于文档驱动工程的 R&D 操作系统

[English Readme](#-dde-agent-skills)

</div>

DDE (Documentation-Driven Engineering) 是一种面向 AI Agent 的确定性治理协议。

## 🚀 快速上手 (最懒办法)

不想手动执行？直接把下面的链接发给你的 **Cursor/Windsurf/Claude Code** Agent 并回复：

> “请帮我把这个仓库里的 DDE 技能部署到我的本地 Agent 技能目录中。”

**仓库地址**: `https://github.com/YOUR_USERNAME/dde-agent-skills`

---

## 🛠 纯终端部署

### 1. 克隆仓库
```bash
git clone https://github.com/YOUR_USERNAME/dde-agent-skills.git
cd dde-agent-skills
```

### 2. 一键安装
运行以下指令将核心技能同步到最常用的 Agent 目录：
```bash
python3 tools/sync_skills.py
```

## ✨ 核心特性

- **🛡️ 确定性行为**: 禁止未标记的假设，所有写入必须经过授权。
- **📚 五层架构**: 从项目宪章到执行协议，层层递进。
- **🔄 多环境同步**: 完美支持 Cursor, Windsurf, Trae 等主流 IDE。

## 📜 核心原则
1. **禁止假设**: 未经标记的推断是被禁止的。
2. **硬性关卡**: 未经显式 `[APPROVED]`，禁止进行任何文件写入。
3. **唯一真理来源**: `/docs` 文件夹即法律。

---
*Created by Documentation-Driven Engineering. Built for the next generation of AI Engineers.*
