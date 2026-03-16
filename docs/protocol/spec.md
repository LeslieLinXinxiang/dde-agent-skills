# DDE Protocol Specification (v1.4)

Documentation-Driven Engineering (DDE) is a governance framework that ensures AI agents operate within deterministic boundaries defined by human-approved documentation.

## The Five-Layer Model

### Layer 0 — Project Charter (`docs/project_charter.md`)
Defines the mission, goals, non-goals, and boundary conditions of the project. This is the ultimate authority for project scope.

### Layer 1 — Architecture (`docs/architecture.md`)
Describes the system overview, module list, responsibilities, and dependency rules.

### Layer 2 — Dataflow & Module Specs (`docs/dataflow.md`, `docs/module_specs/*.md`)
Specifies how data moves through the system and the internal/external contracts for each module.

### Layer 3 — Execution Protocol (`docs/execution_protocol.md`)
Defines the Request for Change (RFC) procedure, approval requirements, and consistency re-validation rules.

### Layer 4 — Roadmap (`docs/roadmap.md`)
A highly granular task tracker and rolling log that maintains the timeline and backlog.

---

## Core Governance Rules

1. **No Assumptions**: All inference must be explicitly labeled `ASSUMPTION`.
2. **RFC State Machine**: Modifications to requirements require an RFC, a Document Diff Proposal, and an `[APPROVED]` signal.
3. **Hard Gates**: Subordinate skills cannot bypass `dde-code-guard` write gates.
4. **Deterministic Stop**: On any protocol violation, the agent must output `PROTOCOL_VIOLATION` and stop execution.
