---
title: learn-claude-code
date: 2026-02-26T13:20:22+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1771272338329-1ab5145559a5?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NzIwODMxMzR8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1771272338329-1ab5145559a5?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NzIwODMxMzR8&ixlib=rb-4.1.0
---

# [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)

# Learn Claude Code -- A nano Claude Code-like agent, built from 0 to 1

[English](./README.md) | [中文](./README-zh.md) | [日本語](./README-ja.md)

```
                    THE AGENT PATTERN
                    =================

    User --> messages[] --> LLM --> response
                                      |
                            stop_reason == "tool_use"?
                           /                          \
                         yes                           no
                          |                             |
                    execute tools                    return text
                    append results
                    loop back -----------------> messages[]


    That's the minimal loop. Every AI coding agent needs this loop.
    Production agents add policy, permissions, and lifecycle layers.
```

**12 progressive sessions, from a simple loop to isolated autonomous execution.**
**Each session adds one mechanism. Each mechanism has one motto.**

> **s01** &nbsp; *"Bash is all you need"* &mdash; one tool + one loop = an agent
>
> **s02** &nbsp; *"The loop didn't change"* &mdash; adding tools means adding handlers, not rewriting the loop
>
> **s03** &nbsp; *"Plan before you act"* &mdash; visible plans improve task completion
>
> **s04** &nbsp; *"Process isolation = context isolation"* &mdash; fresh messages[] per subagent
>
> **s05** &nbsp; *"Load on demand, not upfront"* &mdash; inject knowledge via tool_result, not system prompt
>
> **s06** &nbsp; *"Strategic forgetting"* &mdash; forget old context to enable infinite sessions
>
> **s07** &nbsp; *"State survives /compact"* &mdash; file-based state outlives context compression
>
> **s08** &nbsp; *"Fire and forget"* &mdash; non-blocking threads + notification queue
>
> **s09** &nbsp; *"Append to send, drain to read"* &mdash; async mailboxes for persistent teammates
>
> **s10** &nbsp; *"Same request_id, two protocols"* &mdash; one FSM pattern powers shutdown + plan approval
>
> **s11** &nbsp; *"Poll, claim, work, repeat"* &mdash; no coordinator needed, agents self-organize
>
> **s12** &nbsp; *"Isolate by directory, coordinate by task ID"* &mdash; task board + optional worktree lanes

---

## The Core Pattern

```python
def agent_loop(messages):
    while True:
        response = client.messages.create(
            model=MODEL, system=SYSTEM,
            messages=messages, tools=TOOLS,
        )
        messages.append({"role": "assistant",
                         "content": response.content})

        if response.stop_reason != "tool_use":
            return

        results = []
        for block in response.content:
            if block.type == "tool_use":
                output = TOOL_HANDLERS[block.name](**block.input)
                results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": output,
                })
        messages.append({"role": "user", "content": results})
```

Every session layers one mechanism on top of this loop -- without changing the loop itself.

## Scope (Important)

This repository is a 0->1 learning project for building a nano Claude Code-like agent.
It intentionally simplifies or omits several production mechanisms:

- Full event/hook buses (for example PreToolUse, SessionStart/End, ConfigChange).  
  s12 includes only a minimal append-only lifecycle event stream for teaching.
- Rule-based permission governance and trust workflows
- Session lifecycle controls (resume/fork) and advanced worktree lifecycle controls
- Full MCP runtime details (transport/OAuth/resource subscribe/polling)

Treat the team JSONL mailbox protocol in this repo as a teaching implementation, not a claim about any specific production internals.

## Quick Start

```sh
git clone https://github.com/shareAI-lab/learn-claude-code
cd learn-claude-code
pip install -r requirements.txt
cp .env.example .env   # Edit .env with your ANTHROPIC_API_KEY

python agents/s01_agent_loop.py       # Start here
python agents/s11_autonomous_agents.py  # Full autonomous team
python agents/s12_worktree_task_isolation.py  # Task-aware worktree isolation
```

### Web Platform

Interactive visualizations, step-through diagrams, source viewer, and documentation.

```sh
cd web && npm install && npm run dev   # http://localhost:3000
```

## Learning Path

```
Phase 1: THE LOOP                    Phase 2: PLANNING & KNOWLEDGE
==================                   ==============================
s01  The Agent Loop          [1]     s03  TodoWrite               [5]
     while + stop_reason                  TodoManager + nag reminder
     |                                    |
     +-> s02  Tools              [4]     s04  Subagents            [5]
              dispatch map: name->handler     fresh messages[] per child
                                              |
                                         s05  Skills               [5]
                                              SKILL.md via tool_result
                                              |
                                         s06  Compact              [5]
                                              3-layer compression

Phase 3: PERSISTENCE                 Phase 4: TEAMS
==================                   =====================
s07  Tasks                   [8]     s09  Agent Teams             [9]
     file-based CRUD + deps graph         teammates + JSONL mailboxes
     |                                    |
s08  Background Tasks        [6]     s10  Team Protocols          [12]
     daemon threads + notify queue        shutdown + plan approval FSM
                                          |
                                     s11  Autonomous Agents       [14]
                                          idle cycle + auto-claim
                                     |
                                     s12  Worktree Isolation      [16]
                                          task coordination + optional isolated execution lanes

                                     [N] = number of tools
```

## Architecture

```
learn-claude-code/
|
|-- agents/                        # Python reference implementations (s01-s12 + full)
|-- docs/{en,zh,ja}/               # Mental-model-first documentation (3 languages)
|-- web/                           # Interactive learning platform (Next.js)
|-- skills/                        # Skill files for s05
+-- .github/workflows/ci.yml      # CI: typecheck + build
```

## Documentation

Mental-model-first: problem, solution, ASCII diagram, minimal code.
Available in [English](./docs/en/) | [中文](./docs/zh/) | [日本語](./docs/ja/).

| Session | Topic | Motto |
|---------|-------|-------|
| [s01](./docs/en/s01-the-agent-loop.md) | The Agent Loop | *Bash is all you need* |
| [s02](./docs/en/s02-tool-use.md) | Tools | *The loop didn't change* |
| [s03](./docs/en/s03-todo-write.md) | TodoWrite | *Plan before you act* |
| [s04](./docs/en/s04-subagent.md) | Subagents | *Process isolation = context isolation* |
| [s05](./docs/en/s05-skill-loading.md) | Skills | *Load on demand, not upfront* |
| [s06](./docs/en/s06-context-compact.md) | Compact | *Strategic forgetting* |
| [s07](./docs/en/s07-task-system.md) | Tasks | *State survives /compact* |
| [s08](./docs/en/s08-background-tasks.md) | Background Tasks | *Fire and forget* |
| [s09](./docs/en/s09-agent-teams.md) | Agent Teams | *Append to send, drain to read* |
| [s10](./docs/en/s10-team-protocols.md) | Team Protocols | *Same request_id, two protocols* |
| [s11](./docs/en/s11-autonomous-agents.md) | Autonomous Agents | *Poll, claim, work, repeat* |
| [s12](./docs/en/s12-worktree-task-isolation.md) | Worktree + Task Isolation | *Isolate by directory, coordinate by task ID* |

## License

MIT

---

**The model is the agent. Our job is to give it tools and stay out of the way.**
