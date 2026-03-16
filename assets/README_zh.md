# DDE Agent Skills: 基于文档驱动工程的 R&D 操作系统

DDE (Documentation-Driven Engineering) 是一种面向 AI Agent 的确定性治理协议。与依赖概率性 Prompt 匹配的传统 Agent 不同，DDE 通过严格的、人类审核的文档（Layer 0-4）强制执行层级化权限管理。

## 🚀 愿景
让每一个代码仓库都成为一个能够自我文档化、自我管理的研发平台。在这里，Agent 不仅仅是一个工具，而是一个符合协议规范的系统维护者。

## 🛠 核心组件
- **`dde-bootstrap`**: 指挥官。初始化项目并强制执行 Layer 0-4 的一致性检查。
- **`dde-code-guard`**: 守门员。为所有代码修改强制执行两个阶段的生命周期：[提案 PROPOSAL] -> [审批 APPROVED] -> [执行 EXECUTION]。
- **扩展技能**: 针对测试、验证和调研的模块化技能。

## 📂 仓库结构
```text
.
├── skills/           # 模块化 Agent 技能 (符合 SKILL.md 格式)
├── docs/             # DDE 协议规范
├── tools/            # 同步与校验工具
└── assets/           # 静态资源与多语言文档
```

## 🛠 安装与使用
将这些技能链接到你的本地 Agent 环境（Cursor/Windsurf/Trae）：
```bash
python3 tools/sync_skills.py
```

## 📜 核心原则
1. **禁止假设**: 未经标记的推断是被禁止的。
2. **硬性关卡**: 未经显式 `[APPROVED]`，禁止进行任何文件写入。
3. **唯一真理来源**: `/docs` 文件夹即法律。

## 🤝 参与贡献
本仓库自身的开发也遵循 DDE 协议。对核心协议的任何修改请先提交 RFC 提案。

---
*Created by Documentation-Driven Engineering.*
