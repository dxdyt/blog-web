---
title: buttercup
date: 2025-08-12T12:27:19+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1753808446192-dcb2083936e2?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTQ5NzI4MTV8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1753808446192-dcb2083936e2?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTQ5NzI4MTV8&ixlib=rb-4.1.0
---

# [trailofbits/buttercup](https://github.com/trailofbits/buttercup)

# Buttercup Cyber Reasoning System (CRS)

[![Tests](https://github.com/trailofbits/buttercup/actions/workflows/tests.yml/badge.svg)](https://github.com/trailofbits/buttercup/actions/workflows/tests.yml)
[![Tests (Nightly)](https://github.com/trailofbits/buttercup/actions/workflows/tests.yml/badge.svg?event=schedule)](https://github.com/trailofbits/buttercup/actions/workflows/tests.yml)
[![Integration](https://github.com/trailofbits/buttercup/actions/workflows/integration.yml/badge.svg)](https://github.com/trailofbits/buttercup/actions/workflows/integration.yml)

**Buttercup** is a Cyber Reasoning System (CRS) developed by **Trail of Bits** for the **DARPA AIxCC (AI Cyber Challenge)**. Buttercup finds and patches software vulnerabilities in open-source code repositories like [example-libpng](https://github.com/tob-challenges/example-libpng). It starts by running an AI/ML-assisted fuzzing campaign (built on oss-fuzz) for the program. When vulnerabilities are found, Buttercup analyzes them and uses a multi-agent AI-driven patcher to repair the vulnerability. **Buttercup** system consists of several components:

- **Orchestrator**: Coordinates the overall task process and manages the workflow
- **Seed Generator**: Creates inputs for vulnerability discovery
- **Fuzzer**: Discovers vulnerabilities through intelligent fuzzing techniques
- **Program Model**: Analyzes code structure and semantics for better understanding
- **Patcher**: Generates and applies security patches to fix vulnerabilities

## System Requirements

### Minimum Requirements

- **CPU:** 8 cores
- **Memory:** 16 GB RAM
- **Storage:** 100 GB available disk space
- **Network:** Stable internet connection for downloading dependencies

**Note:** Buttercup uses third-party AI providers (LLMs from companies like OpenAI, Anthropic and Google), which cost money. Please ensure that you manage per-deployment costs by using the built-in LLM budget setting.

**Note:** Buttercup works best with access to models from OpenAI **and** Anthropic, but can be run with at least one API key from one third-party provider (support for Gemini coming soon).

### Supported Systems

- **Linux x86_64** (fully supported)
- **ARM64** (partial support for upstream Google OSS-Fuzz projects)

### Required System Packages

Before setup, ensure you have these packages installed:

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y make curl git

# RHEL/CentOS/Fedora
sudo yum install -y make curl git
# or
sudo dnf install -y make curl git

# MacOS
brew install make curl git
```

### Supported Targets

Buttercup works with:

- **C source code repositories** that are OSS-Fuzz compatible
- **Java source code repositories** that are OSS-Fuzz compatible
- Projects that build successfully and have existing fuzzing harnesses

## Quick Start

1. Clone the repository with submodules:

```bash
git clone --recurse-submodules https://github.com/trailofbits/buttercup.git
cd buttercup
```

2. Run automated setup (Recommended)

```bash
make setup-local
```

This script will install all dependencies, configure the environment, and guide you through the setup process.

**Note:** If you prefer manual setup, see the [Manual Setup Guide](MANUAL_SETUP.md).

3. Start Buttercup locally

```bash
make deploy-local
```

4. Verify local deployment:

```bash
make status
```

When a deployment is successful, you should see all pods in "Running" or "Completed" status.

5. Send Buttercup a simple task

**Note:** When tasked, Buttercup will start consuming third-party AI resources.

This command will make Buttercup pull down an example repo [example-libpng](https://github.com/tob-challenges/example-libpng) with a known vulnerability. Buttercup will start fuzzing it to find and patch vulnerabilities.

```bash
make send-libpng-task
```

6. Access Buttercup's web-based GUI

Run:

```bash
make web-ui
```

Then navigate to `http://localhost:31323` in your web browser.

In the GUI you can monitor active tasks and see when Buttercup finds bugs and generates patches for them.

7. Stop Buttercup

**Note:** This is an important step to ensure Buttercup shuts down and stops consuming third-party AI resources.

```bash
make undeploy
```

## Accessing Logs

Buttercup includes local SigNoz deployment by default for comprehensive system observability. You can access logs, traces, and metrics through the SigNoz UI:

```bash
make signoz-ui
```

Then navigate to `http://localhost:33301` in your web browser to view:
- Distributed traces
- Application metrics 
- Error monitoring
- Performance insights

If you configured LangFuse during setup, you can also monitor LLM usage and costs there.

For additional log access methods, see the [Quick Reference Guide](QUICK_REFERENCE.md).

## Additional Resources

- [Quick Reference Guide](QUICK_REFERENCE.md) - Common commands and troubleshooting
- [Manual Setup Guide](MANUAL_SETUP.md) - Detailed manual installation steps
- [AKS Deployment Guide](AKS_DEPLOYMENT.md) - Production deployment on Azure
- [Contributing Guidelines](CONTRIBUTING.md) - Development workflow and standards
- [Deployment Documentation](deployment/README.md) - Advanced deployment configuration
- [Writing Custom Challenges](CUSTOM_CHALLENGES.md) - Custom project configuration and setup
