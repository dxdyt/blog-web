---
title: nautilus_trader
date: 2025-01-15T12:20:17+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1732574560934-8fc7e8cc3c60?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MzY5MTQ3MTd8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1732574560934-8fc7e8cc3c60?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MzY5MTQ3MTd8&ixlib=rb-4.0.3
---

# [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader)

# <img src="https://github.com/nautechsystems/nautilus_trader/blob/develop/docs/_images/nautilus-trader-logo.png" width="500">

[![codecov](https://codecov.io/gh/nautechsystems/nautilus_trader/branch/master/graph/badge.svg?token=DXO9QQI40H)](https://codecov.io/gh/nautechsystems/nautilus_trader)
[![codspeed](https://img.shields.io/endpoint?url=https://codspeed.io/badge.json)](https://codspeed.io/nautechsystems/nautilus_trader)
![pythons](https://img.shields.io/pypi/pyversions/nautilus_trader)
![pypi-version](https://img.shields.io/pypi/v/nautilus_trader)
![pypi-format](https://img.shields.io/pypi/format/nautilus_trader?color=blue)
[![Downloads](https://pepy.tech/badge/nautilus-trader)](https://pepy.tech/project/nautilus-trader)

| Branch    | Version                                                                                                                                             | Status                                                                                                                                                                                            |
| :-------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `master`  | ![version](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fnautechsystems%2Fnautilus_trader%2Fmaster%2Fversion.json)  | [![build](https://github.com/nautechsystems/nautilus_trader/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/nautechsystems/nautilus_trader/actions/workflows/build.yml)  |
| `nightly` | ![version](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fnautechsystems%2Fnautilus_trader%2Fnightly%2Fversion.json) | [![build](https://github.com/nautechsystems/nautilus_trader/actions/workflows/build.yml/badge.svg?branch=nightly)](https://github.com/nautechsystems/nautilus_trader/actions/workflows/build.yml) |
| `develop` | ![version](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fnautechsystems%2Fnautilus_trader%2Fdevelop%2Fversion.json) | [![build](https://github.com/nautechsystems/nautilus_trader/actions/workflows/build.yml/badge.svg?branch=develop)](https://github.com/nautechsystems/nautilus_trader/actions/workflows/build.yml) |

| Platform           | Rust    | Python |
| :----------------- | :------ | :----- |
| `Linux (x86_64)`   | 1.84.0+ | 3.11+  |
| `macOS (arm64)`    | 1.84.0+ | 3.11+  |
| `Windows (x86_64)` | 1.84.0+ | 3.11+  |

[![](https://dcbadge.limes.pink/api/server/AUWVs3XaCS)](https://discord.gg/AUWVs3XaCS)

- **Docs**: https://nautilustrader.io/docs/
- **Website**: https://nautilustrader.io
- **Support**: [support@nautilustrader.io](mailto:support@nautilustrader.io)

## Introduction

NautilusTrader is an open-source, high-performance, production-grade algorithmic trading platform,
providing quantitative traders with the ability to backtest portfolios of automated trading strategies
on historical data with an event-driven engine, and also deploy those same strategies live, with no code changes.

The platform is *AI-first*, designed to develop and deploy algorithmic trading strategies within a highly performant
and robust Python-native environment. This helps to address the parity challenge of keeping the Python research/backtest
environment consistent with the production live trading environment.

NautilusTrader's design, architecture, and implementation philosophy holds software correctness and safety at the
highest level, with the aim of supporting Python-native, mission-critical, trading system backtesting
and live deployment workloads.

The platform is also universal and asset-class-agnostic - with any REST, WebSocket or FIX API able to be integrated via modular
adapters. Thus, it can handle high-frequency trading operations for any asset classes
including FX, Equities, Futures, Options, CFDs, Crypto and Betting - across multiple venues simultaneously.

## Features

- **Fast**: Core is written in Rust with asynchronous networking using [tokio](https://crates.io/crates/tokio).
- **Reliable**: Type safety and thread safety through Rust. Redis-backed performant state persistence (optional).
- **Portable**: OS independent, runs on Linux, macOS, and Windows. Deploy using Docker.
- **Flexible**: Modular adapters mean any REST, WebSocket, or FIX API can be integrated.
- **Advanced**: Time in force `IOC`, `FOK`, `GTD`, `AT_THE_OPEN`, `AT_THE_CLOSE`, advanced order types and conditional triggers. Execution instructions `post-only`, `reduce-only`, and icebergs. Contingency order lists including `OCO`, `OTO`.
- **Customizable**: Add user-defined custom components, or assemble entire systems from scratch leveraging the cache and message bus.
- **Backtesting**: Run with multiple venues, instruments and strategies simultaneously using historical quote tick, trade tick, bar, order book and custom data with nanosecond resolution.
- **Live**: Use identical strategy implementations between backtesting and live deployments.
- **Multi-venue**: Multiple venue capabilities facilitate market-making and statistical arbitrage strategies.
- **AI Training**: Backtest engine fast enough to be used to train AI trading agents (RL/ES).

![Alt text](https://github.com/nautechsystems/nautilus_trader/blob/develop/docs/_images/nautilus-art.png?raw=true "nautilus")

> _nautilus - from ancient Greek 'sailor' and naus 'ship'._
>
> _The nautilus shell consists of modular chambers with a growth factor which approximates a logarithmic spiral.
> The idea is that this can be translated to the aesthetics of design and architecture._

## Why NautilusTrader?

- **Highly performant event-driven Python**: Native binary core components.
- **Parity between backtesting and live trading**: Identical strategy code.
- **Reduced operational risk**: Enhanced risk management functionality, logical accuracy, and type safety.
- **Highly extendable**: Message bus, custom components and actors, custom data, custom adapters.

Traditionally, trading strategy research and backtesting might be conducted in Python
using vectorized methods, with the strategy then needing to be reimplemented in a more event-driven way
using C++, C#, Java or other statically typed language(s). The reasoning here is that vectorized backtesting code cannot
express the granular time and event dependent complexity of real-time trading, where compiled languages have
proven to be more suitable due to their inherently higher performance, and type safety.

One of the key advantages of NautilusTrader here, is that this reimplementation step is now circumvented - as the critical core components of the platform
have all been written entirely in [Rust](https://www.rust-lang.org/) or [Cython](https://cython.org/).
This means we're using the right tools for the job, where systems programming languages compile performant binaries,
with CPython C extension modules then able to offer a Python-native environment, suitable for professional quantitative traders and trading firms.

## Why Python?

Python was originally created decades ago as a simple scripting language with a clean straight
forward syntax. It has since evolved into a fully fledged general purpose object-oriented
programming language. Based on the TIOBE index, Python is currently the most popular programming language in the world.
Not only that, Python has become the _de facto lingua franca_ of data science, machine learning, and artificial intelligence.

The language out of the box is not without its drawbacks however, especially in the context of
implementing large performance-critical systems. Cython has addressed a lot of these issues, offering all the advantages
of a statically typed language, embedded into Pythons rich ecosystem of software libraries and
developer/user communities.

## What is Rust?

[Rust](https://www.rust-lang.org/) is a multi-paradigm programming language designed for performance and safety, especially safe
concurrency. Rust is blazingly fast and memory-efficient (comparable to C and C++) with no garbage collector.
It can power mission-critical systems, run on embedded devices, and easily integrates with other languages.

Rust’s rich type system and ownership model guarantees memory-safety and thread-safety deterministically —
eliminating many classes of bugs at compile-time.

The project increasingly utilizes Rust for core performance-critical components. Python language binding is handled through
Cython and [PyO3](https://pyo3.rs/latest), with static libraries linked at compile-time before the wheel binaries are packaged, so a user
does not need to have Rust installed to run NautilusTrader.

This project makes the [Soundness Pledge](https://raphlinus.github.io/rust/2020/01/18/soundness-pledge.html):

> “The intent of this project is to be free of soundness bugs.
> The developers will do their best to avoid them, and welcome help in analyzing and fixing them.”

> [!NOTE]
>
> **MSRV:** NautilusTrader relies heavily on improvements in the Rust language and compiler.
> As a result, the Minimum Supported Rust Version (MSRV) is generally equal to the latest stable release of Rust.

## Architecture (data flow)

![Architecture](https://github.com/nautechsystems/nautilus_trader/blob/develop/docs/_images/architecture-overview.png?raw=true "architecture")

## Integrations

NautilusTrader is modularly designed to work with _adapters_, enabling connectivity to trading venues
and data providers by converting their raw APIs into a unified interface.

The following integrations are currently supported:

| Name                                                      | ID                    | Type                    | Status                                                  | Docs                                                                        |
| :-------------------------------------------------------- | :-------------------- | :---------------------- | :------------------------------------------------------ | :-------------------------------------------------------------------------- |
| [Betfair](https://betfair.com)                            | `BETFAIR`             | Sports Betting Exchange | ![status](https://img.shields.io/badge/stable-green)    | [Guide](https://nautilustrader.io/docs/latest/integrations/betfair.html)    |
| [Binance](https://binance.com)                            | `BINANCE`             | Crypto Exchange (CEX)   | ![status](https://img.shields.io/badge/stable-green)    | [Guide](https://nautilustrader.io/docs/latest/integrations/binance.html)    |
| [Binance US](https://binance.us)                          | `BINANCE`             | Crypto Exchange (CEX)   | ![status](https://img.shields.io/badge/stable-green)    | [Guide](https://nautilustrader.io/docs/latest/integrations/binance.html)    |
| [Binance Futures](https://www.binance.com/en/futures)     | `BINANCE`             | Crypto Exchange (CEX)   | ![status](https://img.shields.io/badge/stable-green)    | [Guide](https://nautilustrader.io/docs/latest/integrations/binance.html)    |
| [Bybit](https://www.bybit.com)                            | `BYBIT`               | Crypto Exchange (CEX)   | ![status](https://img.shields.io/badge/stable-green)    | [Guide](https://nautilustrader.io/docs/latest/integrations/bybit.html)      |
| [Databento](https://databento.com)                        | `DATABENTO`           | Data Provider           | ![status](https://img.shields.io/badge/stable-green)    | [Guide](https://nautilustrader.io/docs/latest/integrations/databento.html)  |
| [dYdX](https://dydx.exchange/)                            | `DYDX`                | Crypto Exchange (DEX)   | ![status](https://img.shields.io/badge/stable-green)    | [Guide](https://nautilustrader.io/docs/latest/integrations/dydx.html)       |
| [Interactive Brokers](https://www.interactivebrokers.com) | `INTERACTIVE_BROKERS` | Brokerage (multi-venue) | ![status](https://img.shields.io/badge/stable-green)    | [Guide](https://nautilustrader.io/docs/latest/integrations/ib.html)         |
| [OKX](https://okx.com)                                    | `OKX`                 | Crypto Exchange (CEX)   | ![status](https://img.shields.io/badge/building-orange) | [Guide](https://nautilustrader.io/docs/latest/integrations/okx.html)        |
| [Polymarket](https://polymarket.com)                      | `POLYMARKET`          | Prediction Market (DEX) | ![status](https://img.shields.io/badge/stable-green)    | [Guide](https://nautilustrader.io/docs/latest/integrations/polymarket.html) |
| [Tardis](https://tardis.dev)                              | `TARDIS`              | Data Provider           | ![status](https://img.shields.io/badge/stable-green)    | [Guide](https://nautilustrader.io/docs/latest/integrations/tardis.html)     |

- **ID**: The default client ID for the integrations adapter clients.
- **Type**: The type of integration (often the venue type).

### Status
- `building`: Under construction and likely not in a usable state.
- `beta`: Completed to a minimally working state and in a 'beta' testing phase.
- `stable`: Stabilized feature set and API, the integration has been tested by both developers and users to a reasonable level (some bugs may still remain).

See the [Integrations](https://nautilustrader.io/docs/latest/integrations/index.html) documentation for further details.

### Branches

We aim to maintain a stable, passing build across all branches.

- `master`: Reflects the source code for the latest released version.
- `nightly`: Includes experimental and in-progress features, merged from the `develop` branch daily at **14:00 UTC** and also when required.
- `develop`: The most active branch, frequently updated with new commits, including experimental and in-progress features.

> [!NOTE]
>
> Our [roadmap](/ROADMAP.md) aims to achieve a **stable API for version 2.x** (likely after the Rust port).
> Once this milestone is reached, we plan to implement a formal release process, including deprecation periods for any API changes.
> This approach allows us to maintain a rapid development pace for now.

## Versioning and releases

NautilusTrader is still under active development. Some features may be incomplete, and while
the API is becoming more stable, breaking changes can occur between releases.
We strive to document these changes in the release notes on a **best-effort basis**.

We aim to follow a **weekly release schedule**, though experimental or larger features may cause delays.

## Installation

### From PyPI

We recommend using the latest supported version of Python and setting up [nautilus_trader](https://pypi.org/project/nautilus_trader/) in a virtual environment to isolate dependencies

To install the latest binary wheel (or sdist package) from PyPI using Pythons pip package manager:

    pip install -U nautilus_trader

### From the Nautech Systems package index

The Nautech Systems package index (`packages.nautechsystems.io`) is [PEP-503](https://peps.python.org/pep-0503/) compliant and hosts both stable and development binary wheels for `nautilus_trader`.
This enables users to install either the latest stable release or pre-release versions for testing.

#### Stable wheels

Stable wheels correspond to official releases of `nautilus_trader` on PyPI, and use standard versioning.

To install the latest stable release:

    pip install -U nautilus_trader --index-url=https://packages.nautechsystems.io/simple

#### Development wheels

Development wheels are published from both the `develop` and `nightly` branches for Linux and macOS,
allowing users to test features and fixes ahead of stable releases.

This process also helps preserve compute resources and ensures easy access to the exact binaries tested in CI pipelines,
while adhering to [PEP-440](https://peps.python.org/pep-0440/) versioning standards:

- `develop` wheels use the version format `dev{date}+{build_number}` (e.g., `1.208.0.dev20241212+7001`).
- `nightly` wheels use the version format `a{date}` (alpha) (e.g., `1.208.0a20241212`).

> [!WARNING]
>
> We don't recommend using development wheels in production environments, such as live trading controlling real capital.

#### Installation commands

By default, pip installs the latest stable release. Adding the `--pre` flag ensures that pre-release versions, including development wheels, are considered.

To install the latest available pre-release (including development wheels):

    pip install -U nautilus_trader --pre --index-url=https://packages.nautechsystems.io/simple

To install a specific development wheel (e.g., `1.208.0a20241212` for December 12, 2024):

    pip install nautilus_trader==1.208.0a20241212 --index-url=https://packages.nautechsystems.io/simple

#### Available versions

You can view all available versions of `nautilus_trader` on the [package index](https://packages.nautechsystems.io/simple/nautilus-trader/index.html).

To programmatically fetch and list available versions:

    curl -s https://packages.nautechsystems.io/simple/nautilus-trader/index.html | grep -oP '(?<=<a href=")[^"]+(?=")' | awk -F'#' '{print $1}' | sort

#### Branch updates

- `develop` branch wheels (`.dev`): Are built and published continuously with every merged commit.
- `nightly` branch wheels (`a`): Are built and published daily when `develop` branch is automatically merged at **14:00 UTC** (if there are changes).

#### Retention policies

- `develop` branch wheels (`.dev`): Only the most recent wheel build is retained.
- `nightly` branch wheels (`a`): Only the 3 most recent wheel builds are retained.

### From Source

Installation from source requires the `Python.h` header file, which is included in development releases such as `python-dev`.
You'll also need the latest stable `rustc` and `cargo` to compile the Rust libraries.

For MacBook Pro M1/M2, make sure your Python installed using pyenv is configured with `--enable-shared`:

    PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install <python_version>

See the [PyO3 user guide](https://pyo3.rs/latest/getting-started#virtualenvs) for more details.

It's possible to install from source using pip if you first install the build dependencies
as specified in the `pyproject.toml`. We highly recommend installing using [poetry](https://python-poetry.org/) as below.

1. Install [rustup](https://rustup.rs/) (the Rust toolchain installer):
   - Linux and macOS:
       ```bash
       curl https://sh.rustup.rs -sSf | sh
       ```
   - Windows:
       - Download and install [`rustup-init.exe`](https://win.rustup.rs/x86_64)
       - Install "Desktop development with C++" with [Build Tools for Visual Studio 2019](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16)
   - Verify (any system):
       from a terminal session run: `rustc --version`

2. Enable `cargo` in the current shell:
   - Linux and macOS:
       ```bash
       source $HOME/.cargo/env
       ```
   - Windows:
     - Start a new PowerShell

3. Install [clang](https://clang.llvm.org/) (a C language frontend for LLVM):
   - Linux:
       ```bash
       sudo apt-get install clang
       ```
   - Windows:
       1. Add Clang to your [Build Tools for Visual Studio 2019](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16):
          - Start | Visual Studio Installer | Modify | C++ Clang tools for Windows (12.0.0 - x64…) = checked | Modify
       2. Enable `clang` in the current shell:
          ```powershell
          [System.Environment]::SetEnvironmentVariable('path', "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\Llvm\x64\bin\;" + $env:Path,"User")
          ```
   - Verify (any system):
       from a terminal session run: `clang --version`

4. Install poetry (or follow the installation guide on their site):

       curl -sSL https://install.python-poetry.org | python3 -

5. Clone the source with `git`, and install from the projects root directory:

       git clone --branch develop --depth 1 https://github.com/nautechsystems/nautilus_trader
       cd nautilus_trader
       poetry install --only main --all-extras

> [!NOTE]
>
> The `--branch develop` flag clones only the develop branch, and `--depth 1` fetches just the latest commit for a faster, lightweight clone.

See the [Installation Guide](https://nautilustrader.io/docs/latest/getting_started/installation) for other options and further details.

## Redis

Using Redis with NautilusTrader is **optional** and only required if configured as the backend for a cache database or [message bus](https://nautilustrader.io/docs/latest/concepts/message_bus).
See the Redis section of the [Installation Guide](https://nautilustrader.io/docs/latest/getting_started/installation#redis) for further details.

## Makefile

A `Makefile` is provided to automate most installation and build tasks for development. It provides the following targets:

- `make install`: Installs in `release` build mode with `main`, `dev` and `test` dependencies then installs the package using poetry (default).
- `make install-debug`: Same as `make install` but with `debug` build mode.
- `make install-just-deps`: Installs just the `main`, `dev` and `test` dependencies (does not install package).
- `make build`: Runs the build script in `release` build mode (default).
- `make build-debug`: Runs the build script in `debug` build mode.
- `make build-wheel`: Runs the Poetry build with a wheel format in `release` mode.
- `make build-wheel-debug`: Runs the Poetry build with a wheel format in `debug` mode.
- `make clean`: **CAUTION** removes all non-source artifacts from the repository.
- `make docs`: Builds the documentation HTML using Sphinx.
- `make pre-commit`: Runs the pre-commit checks over all files.
- `make ruff`: Runs ruff over all files using the `pyproject.toml` config (with autofix).
- `make pytest`: Runs all tests with `pytest` (except performance tests).
- `make pytest-coverage`: Same as `make pytest` and additionally runs with test coverage and produces a report.

> [!TIP]
>
> Running `make build-debug` to compile after changes to Rust or Cython code is currently the most efficient workflow when developing.

## Examples

Indicators and strategies can be developed in both Python and Cython. For performance and
latency-sensitive applications, we recommend using Cython. Below are some examples:

- [indicator](/nautilus_trader/examples/indicators/ema_python.py) example written in Python.
- [indicator](/nautilus_trader/indicators/) examples written in Cython.
- [strategy](/nautilus_trader/examples/strategies/) examples written in both Python and Cython.
- [backtest](/examples/backtest/) examples using a `BacktestEngine` directly.

## Docker

Docker containers are built using the base image `python:3.12-slim` with the following variant tags:

- `nautilus_trader:latest` has the latest release version installed.
- `nautilus_trader:nightly` has the head of the `nightly` branch installed.
- `jupyterlab:latest` has the latest release version installed along with `jupyterlab` and an
  example backtest notebook with accompanying data.
- `jupyterlab:nightly` has the head of the `nightly` branch installed along with `jupyterlab` and an
  example backtest notebook with accompanying data.

The container images can be pulled as follows:

    docker pull ghcr.io/nautechsystems/<image_variant_tag> --platform linux/amd64

You can launch the backtest example container by running:

    docker pull ghcr.io/nautechsystems/jupyterlab:nightly --platform linux/amd64
    docker run -p 8888:8888 ghcr.io/nautechsystems/jupyterlab:nightly

Then open your browser at the following address:

    http://127.0.0.1:8888/lab

> [!WARNING]
>
> NautilusTrader currently exceeds the rate limit for Jupyter notebook logging (stdout output).
> As a result, the `log_level` in the examples is set to `ERROR`. Lowering this level to see more
> logging will cause the notebook to hang during cell execution. We are investigating a fix, which
> may involve either raising the configured rate limits for Jupyter or throttling the log flushing
> from Nautilus.
> - https://github.com/jupyterlab/jupyterlab/issues/12845
> - https://github.com/deshaw/jupyterlab-limit-output

## Development

We aim to provide the most pleasant developer experience possible for this hybrid codebase of Python, Cython and Rust.
See the [Developer Guide](https://nautilustrader.io/docs/latest/developer_guide/index.html) for helpful information.

### Testing with Rust

[cargo-nextest](https://nexte.st) is the standard Rust test runner for NautilusTrader. You can install it by running:

    cargo install cargo-nextest

> [!TIP]
>
> Rust tests will only pass when run via `cargo-nextest`.

## Contributing

Thank you for considering contributing to NautilusTrader! We welcome any and all help to improve
the project. If you have an idea for an enhancement or a bug fix, the first step is to open an [issue](https://github.com/nautechsystems/nautilus_trader/issues)
on GitHub to discuss it with the team. This helps to ensure that your contribution will be
well-aligned with the goals of the project and avoids duplication of effort.

Once you're ready to start working on your contribution, make sure to follow the guidelines
outlined in the [CONTRIBUTING.md](https://github.com/nautechsystems/nautilus_trader/blob/develop/CONTRIBUTING.md) file. This includes signing a Contributor License Agreement (CLA)
to ensure that your contributions can be included in the project.

> [!NOTE]
>
> Pull requests should target the `develop` branch (the default branch). This is where new features and improvements are integrated before release.

Thank you again for your interest in NautilusTrader! We look forward to reviewing your contributions and working with you to improve the project.

## Community

Join our community of users and contributors on [Discord](https://discord.gg/AUWVs3XaCS) to chat
and stay up-to-date with the latest announcements and features of NautilusTrader. Whether you're a
developer looking to contribute or just want to learn more about the platform, all are welcome on our server.

## License

The source code for NautilusTrader is available on GitHub under the [GNU Lesser General Public License v3.0](https://www.gnu.org/licenses/lgpl-3.0.en.html).
Contributions to the project are welcome and require the completion of a standard Contributor License Agreement (CLA).

---

NautilusTrader is developed and maintained by Nautech Systems, a technology
company specializing in the development of high-performance trading systems.
Although the project utilizes the Rust programming language and benefits from its ecosystem,
Nautech Systems is not affiliated with the Rust Foundation, and this project is not an official
work of the Rust Foundation.
For more information, visit https://nautilustrader.io.

Copyright (C) 2015-2025 Nautech Systems Pty Ltd. All rights reserved.

![nautechsystems](https://github.com/nautechsystems/nautilus_trader/blob/develop/docs/_images/ns-logo.png?raw=true "nautechsystems")
<img src="https://github.com/nautechsystems/nautilus_trader/blob/develop/docs/_images/ferris.png" width="128">