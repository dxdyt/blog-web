---
title: nexus-zkvm
date: 2024-12-13T12:21:17+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1732530361158-09f4154b6b3b?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MzQwNjM2NjJ8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1732530361158-09f4154b6b3b?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MzQwNjM2NjJ8&ixlib=rb-4.0.3
---

# [nexus-xyz/nexus-zkvm](https://github.com/nexus-xyz/nexus-zkvm)

# The Nexus zkVM

<div align="left">
    <a href="https://t.me/nexus_zkvm">
        <img src="https://img.shields.io/endpoint?color=neon&logo=telegram&label=chat&url=https%3A%2F%2Fmogyo.ro%2Fquart-apis%2Ftgmembercount%3Fchat_id%3Dnexus_zkvm"/></a>
    <a href="https://github.com/nexus-xyz/nexus-zkvm/graphs/contributors">
        <img src="https://img.shields.io/github/contributors/nexus-xyz/nexus-zkvm.svg"></a>
    <a href="https://twitter.com/NexusLabsHQ">
        <img src="https://img.shields.io/badge/Twitter-black?logo=x&logoColor=white"/></a>
    <a href="https://nexus.xyz">
        <img src="https://img.shields.io/static/v1?label=Stage&message=Alpha&color=2BB4AB"/></a>
    <a href="https://github.com/nexus-xyz/nexus-zkvm/blob/main/LICENSE-MIT">
        <img src="https://img.shields.io/badge/license-MIT-blue"/></a>
    <a href="https://github.com/nexus-xyz/nexus-zkvm/blob/main/LICENSE-APACHE">
        <img src="https://img.shields.io/badge/license-APACHE-blue"/></a>
</div>

<p align="center">
  <p align="center">
   <img width="100%" src="assets/nexus_docs-header.png" alt="Logo">
  </p>
</p>

The Nexus zkVM is a modular, extensible, open-source, and highly-parallelized zkVM, designed to run at *a trillion CPU cycles proved per second* given enough machine power.

## Folding schemes

If you're interested in our implementation of folding schemes, check the [`nexus-nova`](./nova/) crate.

## Quick Start

### 1. Install the Nexus zkVM

First, install Rust: https://www.rust-lang.org/tools/install.

Also, make sure you have a working version of [cmake](https://cmake.org/).

Note: cmake is a required dependency.

Next, install the RISC-V target:

```shell
rustup target add riscv32i-unknown-none-elf
```

Then, install the Nexus zkVM:

```shell
cargo install --git https://github.com/nexus-xyz/nexus-zkvm cargo-nexus --tag 'v0.2.4'
```

Verify the installation:

```shell
cargo nexus --help
```

This should print the available CLI commands.

### 2. Create a new Nexus project

```shell
cargo nexus new nexus-project
```

And change directory to the new project:

```shell
cd nexus-project
```

This will create a new Rust project directory with the following structure:

```shell
./nexus-project
├── Cargo.lock
├── Cargo.toml
└── src
    └── main.rs
```

As an example, you can change the content of `./src/main.rs` to:

```rust
#![cfg_attr(target_arch = "riscv32", no_std, no_main)]
 
use nexus_rt::write_log;
 
#[nexus_rt::main]
fn main() {
    write_log("Hello, World!\n");
}
```

### 3. Run your program

```bash
cargo nexus run
```

You should see the program print:
```bash
"Hello, World!"
```

This command should run successfully. To print the full step-by-step execution trace on the NVM, run:

```bash
cargo nexus run -v
```

### 4. Prove your program

Generate a proof for your Rust program using the Nexus zkVM.

```shell
cargo nexus prove
```

This command will save the proof to `./nexus-proof`.

### 5. Verify your proof

Finally, load and verify the proof:

```shell
cargo nexus verify
```

You should see the program print "Verifying Proof..." and finally "Finished" when complete.

## Learn More

Run `cargo nexus --help` to see all the available commands.

Also check out the documentation at [docs.nexus.xyz](https://docs.nexus.xyz), or join our [Telegram](https://t.me/nexus_zkvm) chat to discuss!

Nexus is committed to open-source. All of our code is dual licensed under MIT and Apache licenses. We encourage and appreciate contributions.
