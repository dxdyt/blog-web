---
title: KernelSU
date: 2023-07-11T12:18:51+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1686731216673-5ee46b7d7d91?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2ODkwNDkwMTh8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1686731216673-5ee46b7d7d91?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2ODkwNDkwMTh8&ixlib=rb-4.0.3
---

# [tiann/KernelSU](https://github.com/tiann/KernelSU)

**English** | [Español](README_ES.md) | [简体中文](README_CN.md) | [繁體中文](README_TW.md) | [日本語](README_JP.md) | [Polski](README_PL.md) | [Portuguese-Brazil](README_PT-BR.md) | [Türkçe](README_TR.md)

# KernelSU

A Kernel based root solution for Android devices.

## Features

1. Kernel-based `su` and root access management.
2. Module system based on overlayfs.

## Compatibility State

KernelSU officially supports Android GKI 2.0 devices(with kernel 5.10+), old kernels(4.14+) is also compatible, but you need to build kernel yourself.

WSA and containter-based Android should also work with KernelSU integrated.

And the current supported ABIs are : `arm64-v8a` and `x86_64`

## Usage

[Installation](https://kernelsu.org/guide/installation.html)

## Build

[How to build?](https://kernelsu.org/guide/how-to-build.html)

### Discussion

- Telegram: [@KernelSU](https://t.me/KernelSU)

## License

- Files under `kernel` directory are [GPL-2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
- All other parts except `kernel` directory are [GPL-3](https://www.gnu.org/licenses/gpl-3.0.html)

## Credits

- [kernel-assisted-superuser](https://git.zx2c4.com/kernel-assisted-superuser/about/): the KernelSU idea.
- [genuine](https://github.com/brevent/genuine/): apk v2 signature validation.
- [Diamorphine](https://github.com/m0nad/Diamorphine): some rootkit skills.
- [Magisk](https://github.com/topjohnwu/Magisk): the sepolicy implementation.
