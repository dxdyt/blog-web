---
title: ore-cli-gpu
date: 2024-04-18T12:15:33+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1711948742565-5943c7583603?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTM0MTM3MTB8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1711948742565-5943c7583603?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTM0MTM3MTB8&ixlib=rb-4.0.3
---

# [BenjaSOL/ore-cli-gpu](https://github.com/BenjaSOL/ore-cli-gpu)

# Ore CLI with Nvidia GPU Support

A command line interface for the Ore program to utilize Nvidia GPU's. 


Built by [@BenjaSOL](https://x.com/benjasol_) & [@KaedonsCrypto](https://x.com/KaedonsCrypto)

## Building

To build the Ore CLI, you will need to have the Rust programming language installed. You can install Rust by following the instructions on the [Rust website](https://www.rust-lang.org/tools/install).

You must have CUDA installed 

```sh
export CUDA_VISIBLE_DEVICES=<GPU_INDEX>
```

Windows users

```sh
nvcc windows.cu -o windows
```

Linux users

```sh
nvcc linux.cu -o linux
```

Take the path to the executsble that was just created and replace the PATH_TO_EXE with the path to the .exe in the mine.rs.

Once you have Rust installed, you can build the Ore CLI by running the following command:

```sh
cargo build --release
```


```sh
./target/release/ore.exe --rpc "" --priority-fee 1 --keypair 'path to keypair' --priority-fee 1 mine --threads 4
```

You will now run your hashing on the GPU instead of the CPU!

Donations in ORE or SOL: EVK3M6Cth3uPZcATCtnZ16mqArSNXt5oC6kcmakwXudb

## Credits

[ORE Miner](https://github.com/tonyke-bot/ore-miner)

[ORE CLI](https://github.com/HardhatChad/ore-cli)