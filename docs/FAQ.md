# DDE Agent Skills FAQ

### Q: Why not use MCP (Model Context Protocol)?
A: MCP standardizes *how* agents connect to tools. DDE standardizes *how* agents are governed and how they make decisions. They are complementary; you can build a DDE-compliant agent that uses MCP tools.

### Q: Does this work with ChatGPT/Claude web versions?
A: No. DDE is designed for **Agentic AI IDEs** (Cursor, Windsurf, Trae, etc.) or CLI agents that can read local filesystem files.

### Q: How do I create a new "Layer"?
A: Consult `docs/protocol/spec.md`. New layers should be proposed via the RFC process defined in `dde-bootstrap`.

### Q: What is the "R&D OS" philosophy?
A: We believe the codebase, the documentation, and the R&D logs should form a single, machine-legible operating system that guides the AI agent's development loop autonomously.
