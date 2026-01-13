---
title: claude-flow
date: 2026-01-13T12:40:20+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1766229298250-88f02fa015ee?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NjgyNzkxNjB8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1766229298250-88f02fa015ee?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NjgyNzkxNjB8&ixlib=rb-4.1.0
---

# [ruvnet/claude-flow](https://github.com/ruvnet/claude-flow)

# 🌊 Claude-Flow v2.7.0: Enterprise AI Orchestration Platform

<div align="center">

[![🌟 Star on GitHub](https://img.shields.io/github/stars/ruvnet/claude-flow?style=for-the-badge&logo=github&color=gold)](https://github.com/ruvnet/claude-flow)
[![📈 Downloads](https://img.shields.io/npm/dt/claude-flow?style=for-the-badge&logo=npm&color=blue&label=Downloads)](https://www.npmjs.com/package/claude-flow)
[![📦 Latest Release](https://img.shields.io/npm/v/claude-flow/alpha?style=for-the-badge&logo=npm&color=green&label=v2.7.0-alpha.10)](https://www.npmjs.com/package/claude-flow)
[![⚡ Claude Code](https://img.shields.io/badge/Claude%20Code-SDK%20Integrated-green?style=for-the-badge&logo=anthropic)](https://github.com/ruvnet/claude-flow)
[![🏛️ Agentics Foundation](https://img.shields.io/badge/Agentics-Foundation-crimson?style=for-the-badge&logo=openai)](https://discord.com/invite/dfxmpwkG2D)
[![🛡️ MIT License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=opensourceinitiative)](https://opensource.org/licenses/MIT)

</div>

## 🌟 **Overview**

**Claude-Flow v2.7** is an enterprise-grade AI orchestration platform that combines **hive-mind swarm intelligence**, **persistent memory**, and **100+ advanced MCP tools** to revolutionize AI-powered development workflows.

### 🎯 **Key Features**

- **🎨 25 Claude Skills**: Natural language-activated skills for development, GitHub, memory, and automation
- **🚀 AgentDB v1.3.9 Integration**: 96x-164x faster vector search with semantic understanding (PR #830)
- **🧠 Hybrid Memory System**: AgentDB + ReasoningBank with automatic fallback
- **🔍 Semantic Vector Search**: HNSW indexing (O(log n)) + 9 RL algorithms
- **🐝 Hive-Mind Intelligence**: Queen-led AI coordination with specialized worker agents
- **🔧 100 MCP Tools**: Comprehensive toolkit for swarm orchestration and automation
- **🔄 Dynamic Agent Architecture (DAA)**: Self-organizing agents with fault tolerance
- **💾 Persistent Memory**: 150x faster search, 4-32x memory reduction (quantization)
- **🪝 Advanced Hooks System**: Automated workflows with pre/post operation hooks
- **📊 GitHub Integration**: 6 specialized modes for repository management
- **🌐 Flow Nexus Cloud**: E2B sandboxes, AI swarms, challenges, and marketplace

> 🔥 **Revolutionary AI Coordination**: Build faster, smarter, and more efficiently with AI-powered development orchestration
>
> 🆕 **NEW: AgentDB Integration**: 96x-164x performance boost with semantic vector search, reflexion memory, and skill library auto-consolidation


---

## ⚡ **Quick Start**

### 📋 **Prerequisites**

- **Node.js 18+** (LTS recommended)
- **npm 9+** or equivalent package manager
- **Windows users**: See [Windows Installation Guide](./docs/windows-installation.md) for special instructions

⚠️ **IMPORTANT**: Claude Code must be installed first:

```bash
# 1. Install Claude Code globally
npm install -g @anthropic-ai/claude-code

# 2. (Optional) Skip permissions check for faster setup
claude --dangerously-skip-permissions
```

### 🚀 **Install Latest Alpha**

```bash
# NPX (recommended - always latest)
npx claude-flow@alpha init --force
npx claude-flow@alpha --help

# Or install globally
npm install -g claude-flow@alpha
claude-flow --version
# v2.7.0-alpha.10
```

---

## 🎨 **Skills System**

Claude-Flow includes **25 specialized skills** that activate automatically via natural language - no commands to memorize:

```bash
# Just describe what you want - skills activate automatically
"Let's pair program on this feature"        → pair-programming skill
"Review this PR for security issues"       → github-code-review skill
"Use vector search to find similar code"   → agentdb-vector-search skill
"Create a swarm to build this API"         → swarm-orchestration skill
```

**Skill Categories:**
- **Development & Methodology** (3) - SPARC, pair programming, skill builder
- **Intelligence & Memory** (6) - AgentDB integration with 150x-12,500x performance
- **Swarm Coordination** (3) - Multi-agent orchestration and hive-mind
- **GitHub Integration** (5) - PR review, workflows, releases, multi-repo
- **Automation & Quality** (4) - Hooks, verification, performance analysis
- **Flow Nexus Platform** (3) - Cloud sandboxes and neural training

📚 **[Complete Skills Tutorial](./docs/skills-tutorial.md)** - Full guide with usage examples

---

## 🆕 **What's New in v2.7.0-alpha.10**

### ✅ **Semantic Search Fixed**
Critical bug fix for semantic search returning 0 results:
- ✅ Fixed stale compiled code (dist-cjs/ now uses Node.js backend)
- ✅ Fixed result mapping for `retrieveMemories()` flat structure
- ✅ Fixed parameter mismatch (namespace vs domain)
- ✅ 2-3ms query latency with hash embeddings
- ✅ Works without API keys (deterministic 1024-dim embeddings)

### 🧠 **ReasoningBank Integration (agentic-flow@1.5.13)**
- **Node.js Backend**: Replaced WASM with SQLite + better-sqlite3
- **Persistent Storage**: All memories saved to `.swarm/memory.db`
- **Semantic Search**: MMR ranking with 4-factor scoring
- **Database Tables**: patterns, embeddings, trajectories, links
- **Performance**: 2ms queries, 400KB per pattern with embeddings

```bash
# Semantic search now fully functional
npx claude-flow@alpha memory store test "API configuration" --namespace semantic --reasoningbank
npx claude-flow@alpha memory query "configuration" --namespace semantic --reasoningbank
# ✅ Found 3 results (semantic search) in 2ms
```

📚 **Release Notes**: [v2.7.0-alpha.10](./docs/RELEASE-NOTES-v2.7.0-alpha.10.md)

## 🧠 **Memory System Commands**

### **🚀 NEW: AgentDB v1.3.9 Integration (96x-164x Performance Boost)**

**Revolutionary Performance Improvements:**
- **Vector Search**: 96x faster (9.6ms → <0.1ms)
- **Batch Operations**: 125x faster
- **Large Queries**: 164x faster
- **Memory Usage**: 4-32x reduction via quantization

```bash
# Semantic vector search (understands meaning, not just keywords)
npx claude-flow@alpha memory vector-search "user authentication flow" \
  --k 10 --threshold 0.7 --namespace backend

# Store with vector embedding for semantic search
npx claude-flow@alpha memory store-vector api_design "REST endpoints" \
  --namespace backend --metadata '{"version":"v2"}'

# Get AgentDB integration status and capabilities
npx claude-flow@alpha memory agentdb-info

# Installation (hybrid mode - 100% backward compatible)
npm install agentdb@1.3.9
```

**New Features:**
- ✅ **Semantic vector search** (HNSW indexing, O(log n))
- ✅ **9 RL algorithms** (Q-Learning, PPO, MCTS, Decision Transformer)
- ✅ **Reflexion memory** (learn from past experiences)
- ✅ **Skill library** (auto-consolidate successful patterns)
- ✅ **Causal reasoning** (understand cause-effect relationships)
- ✅ **Quantization** (binary 32x, scalar 4x, product 8-16x reduction)
- ✅ **100% backward compatible** (hybrid mode with graceful fallback)

**Documentation**: `docs/agentdb/PRODUCTION_READINESS.md` | **PR**: #830

---

### **ReasoningBank (Legacy SQLite Memory - Still Supported)**

```bash
# Store memories with pattern matching
npx claude-flow@alpha memory store api_key "REST API configuration" \
  --namespace backend --reasoningbank

# Query with pattern search (2-3ms latency)
npx claude-flow@alpha memory query "API config" \
  --namespace backend --reasoningbank
# ✅ Found 3 results (pattern matching)

# List all memories
npx claude-flow@alpha memory list --namespace backend --reasoningbank

# Check status and statistics
npx claude-flow@alpha memory status --reasoningbank
# ✅ Total memories: 30
#    Embeddings: 30
#    Storage: .swarm/memory.db
```

**Features:**
- ✅ **No API Keys Required**: Hash-based embeddings (1024 dimensions)
- ✅ **Persistent Storage**: SQLite database survives restarts
- ✅ **Pattern Matching**: LIKE-based search with similarity scoring
- ✅ **Namespace Isolation**: Organize memories by domain
- ✅ **Fast Queries**: 2-3ms average latency
- ✅ **Process Cleanup**: Automatic database closing

**Optional Enhanced Embeddings:**
```bash
# For better semantic accuracy with text-embedding-3-small (1536 dimensions)
# Set OPENAI environment variable (see ReasoningBank documentation)
```

---

## 🐝 **Swarm Orchestration**

### **Quick Swarm Commands**

```bash
# Quick task execution (recommended)
npx claude-flow@alpha swarm "build REST API with authentication" --claude

# Multi-agent coordination
npx claude-flow@alpha swarm init --topology mesh --max-agents 5
npx claude-flow@alpha swarm spawn researcher "analyze API patterns"
npx claude-flow@alpha swarm spawn coder "implement endpoints"
npx claude-flow@alpha swarm status
```

### **Hive-Mind for Complex Projects**

```bash
# Initialize hive-mind system
npx claude-flow@alpha hive-mind wizard
npx claude-flow@alpha hive-mind spawn "build enterprise system" --claude

# Session management
npx claude-flow@alpha hive-mind status
npx claude-flow@alpha hive-mind resume session-xxxxx
```

**When to Use:**
| Feature | `swarm` | `hive-mind` |
|---------|---------|-------------|
| **Best For** | Quick tasks | Complex projects |
| **Setup** | Instant | Interactive wizard |
| **Memory** | Task-scoped | Project-wide SQLite |
| **Sessions** | Temporary | Persistent + resume |

---

## 🔧 **MCP Tools Integration**

### **Setup MCP Servers**

```bash
# Add Claude Flow MCP server (required)
claude mcp add claude-flow npx claude-flow@alpha mcp start

# Optional: Enhanced coordination
claude mcp add ruv-swarm npx ruv-swarm mcp start

# Optional: Cloud features (requires registration)
claude mcp add flow-nexus npx flow-nexus@latest mcp start
```

### **Available MCP Tools (100 Total)**

**Core Tools:**
- `swarm_init`, `agent_spawn`, `task_orchestrate`
- `memory_usage`, `memory_search`
- `neural_status`, `neural_train`, `neural_patterns`

**Memory Tools:**
- `mcp__claude-flow__memory_usage` - Store/retrieve persistent memory
- `mcp__claude-flow__memory_search` - Pattern-based search

**GitHub Tools:**
- `github_repo_analyze`, `github_pr_manage`, `github_issue_track`

**Performance Tools:**
- `benchmark_run`, `performance_report`, `bottleneck_analyze`

📚 **Full Reference**: [MCP Tools Documentation](./docs/MCP-TOOLS.md)

---

## 🪝 **Advanced Hooks System**

### **Automated Workflow Enhancement**

Claude-Flow automatically configures hooks for enhanced operations:

```bash
# Auto-configures hooks during init
npx claude-flow@alpha init --force
```

### **Available Hooks**

**Pre-Operation:**
- `pre-task`: Auto-assigns agents by complexity
- `pre-edit`: Validates files and prepares resources
- `pre-command`: Security validation

**Post-Operation:**
- `post-edit`: Auto-formats code
- `post-task`: Trains neural patterns
- `post-command`: Updates memory

**Session Management:**
- `session-start`: Restores previous context
- `session-end`: Generates summaries
- `session-restore`: Loads memory

---

## 🎯 **Common Workflows**

### **Pattern 1: Single Feature Development**
```bash
# Initialize once per feature
npx claude-flow@alpha init --force
npx claude-flow@alpha hive-mind spawn "Implement authentication" --claude

# Continue same feature (reuse hive)
npx claude-flow@alpha memory query "auth" --recent
npx claude-flow@alpha swarm "Add password reset" --continue-session
```

### **Pattern 2: Multi-Feature Project**
```bash
# Project initialization
npx claude-flow@alpha init --force --project-name "my-app"

# Feature 1: Authentication
npx claude-flow@alpha hive-mind spawn "auth-system" --namespace auth --claude

# Feature 2: User management
npx claude-flow@alpha hive-mind spawn "user-mgmt" --namespace users --claude
```

### **Pattern 3: Research & Analysis**
```bash
# Start research session
npx claude-flow@alpha hive-mind spawn "Research microservices" \
  --agents researcher,analyst --claude

# Check learned knowledge
npx claude-flow@alpha memory stats
npx claude-flow@alpha memory query "microservices patterns" --reasoningbank
```

---

## 📊 **Performance & Stats**

- **84.8% SWE-Bench solve rate** - Industry-leading problem-solving
- **32.3% token reduction** - Efficient context management
- **2.8-4.4x speed improvement** - Parallel coordination
- **96x-164x faster search** - 🆕 AgentDB vector search (9.6ms → <0.1ms)
- **4-32x memory reduction** - 🆕 AgentDB quantization
- **2-3ms query latency** - ReasoningBank pattern search (legacy)
- **64 specialized agents** - Complete development ecosystem
- **100 MCP tools** - Comprehensive automation toolkit
- **180 AgentDB tests** - >90% coverage, production-ready

---

## 📚 **Documentation**

### **📖 Core Documentation**
- **[Documentation Hub](./docs/)** - Complete documentation index with organized structure
- **[Skills Tutorial](./docs/guides/skills-tutorial.md)** - Complete guide to 25 Claude Flow skills with natural language invocation
- **[Installation Guide](./docs/INSTALLATION.md)** - Setup instructions
- **[Memory System Guide](./docs/MEMORY-SYSTEM.md)** - ReasoningBank + AgentDB hybrid
- **[MCP Tools Reference](./docs/MCP-TOOLS.md)** - Complete tool catalog
- **[Agent System](./docs/AGENT-SYSTEM.md)** - All 64 agents

### **🚀 Release Notes & Changelogs**
- **[v2.7.1](./docs/releases/v2.7.1/)** - Current stable release with critical fixes
- **[v2.7.0-alpha.10](./docs/releases/v2.7.0-alpha.10/)** - Semantic search fix
- **[v2.7.0-alpha.9](./docs/releases/v2.7.0-alpha.9/)** - Process cleanup
- **[Changelog](./CHANGELOG.md)** - Full version history

### **🧠 AgentDB Integration (96x-164x Performance Boost)**
- **[AgentDB Documentation](./docs/agentdb/)** - 🆕 Complete AgentDB v1.3.9 integration docs
  - [Production Readiness Guide](./docs/agentdb/PRODUCTION_READINESS.md) - Deployment guide
  - [Implementation Complete](./docs/agentdb/SWARM_IMPLEMENTATION_COMPLETE.md) - 3-agent swarm details (180 tests)
  - [Backward Compatibility](./docs/agentdb/BACKWARD_COMPATIBILITY_GUARANTEE.md) - 100% compatibility guarantee
  - [Integration Plan](./docs/agentdb/AGENTDB_INTEGRATION_PLAN.md) - Planning and design
  - [Optimization Report](./docs/agentdb/OPTIMIZATION_REPORT.md) - Performance analysis

### **⚡ Performance & Quality**
- **[Performance Documentation](./docs/performance/)** - Optimization guides and benchmarks
  - [JSON Improvements](./docs/performance/PERFORMANCE-JSON-IMPROVEMENTS.md) - JSON optimization results
  - [Metrics Guide](./docs/performance/PERFORMANCE-METRICS-GUIDE.md) - Performance tracking
- **[Bug Fixes](./docs/fixes/)** - Bug fix documentation and patches
- **[Validation Reports](./docs/validation/)** - Test reports and verification results

### **🛠️ Advanced Topics**
- **[Neural Module](./docs/NEURAL-MODULE.md)** - SAFLA self-learning
- **[Goal Module](./docs/GOAL-MODULE.md)** - GOAP intelligent planning
- **[Hive-Mind Intelligence](./docs/HIVE-MIND.md)** - Queen-led coordination
- **[GitHub Integration](./docs/GITHUB-INTEGRATION.md)** - Repository automation

### **⚙️ Configuration & Setup**
- **[CLAUDE.md Templates](./docs/CLAUDE-MD-TEMPLATES.md)** - Project configs
- **[SPARC Methodology](./docs/SPARC.md)** - TDD patterns
- **[Windows Installation](./docs/windows-installation.md)** - Windows setup

---

## 🤝 **Community & Support**

- **GitHub Issues**: [Report bugs or request features](https://github.com/ruvnet/claude-flow/issues)
- **Discord**: [Join the Agentics Foundation community](https://discord.com/invite/dfxmpwkG2D)
- **Documentation**: [Complete guides and tutorials](https://github.com/ruvnet/claude-flow/wiki)
- **Examples**: [Real-world usage patterns](https://github.com/ruvnet/claude-flow/tree/main/examples)

---

## 🚀 **Roadmap & Targets**

### **Immediate (Q4 2025)**
- ✅ Semantic search fix (v2.7.0-alpha.10)
- ✅ ReasoningBank Node.js backend
- ✅ AgentDB v1.3.9 integration (PR #830) - 96x-164x performance boost
- 🔄 AgentDB production deployment (Q4 2025)
- 🔄 Enhanced embedding models
- 🔄 Multi-user collaboration features

### **Q1 2026**
- Advanced neural pattern recognition
- Cloud swarm coordination
- Real-time agent communication
- Enterprise SSO integration

### **Growth Targets**
- 5K+ GitHub stars, 50K npm downloads/month
- $25K MRR, 15 enterprise customers
- 90%+ error prevention
- 30+ minutes saved per developer per week

---

## Star History

<a href="https://www.star-history.com/#ruvnet/claude-flow&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ruvnet/claude-flow&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ruvnet/claude-flow&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ruvnet/claude-flow&type=Date" />
 </picture>
</a>

---

## 📄 **License**

MIT License - see [LICENSE](./LICENSE) for details

---

**Built with ❤️ by [rUv](https://github.com/ruvnet) | Powered by Revolutionary AI**

*v2.7.0-alpha.10 - Semantic Search Fixed + ReasoningBank Node.js Backend*

</div>
