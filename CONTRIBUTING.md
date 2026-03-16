# Contributing to DDE Agent Skills

We welcome contributions! As a project rooted in **Documentation-Driven Engineering (DDE)**, we follow a specific process for all changes.

## 🤝 The RFC Process
All significant changes to the core DDE protocol or new high-level "Layers" MUST start with a Request for Comments (RFC).

1. **Submit a Proposal**: Create an issue or PR describing the change.
2. **Phase 1: Review**: Discuss the first principles and architectural impact.
3. **Phase 2: Approval**: Wait for maintainer approval (`[APPROVED]`).
4. **Execution**: Implement the changes, starting with documentation updates.

## 🛠 Adding New Skills
New skills should follow the `SKILL.md` format:
- Clear `name` and `description` in frontmatter.
- Defined hierarchical authority (subordinate to `dde-bootstrap`).
- Instruction-based logic that prioritizes safety and verification.

## 📜 Code of Conduct
Be respectful and pragmatic. Focus on engineering excellence and deterministic agent behavior.
