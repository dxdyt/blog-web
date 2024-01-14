---
title: yuzu-android
date: 2024-01-14T12:17:43+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1704636487929-6a09f864d53f?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDUyMDU3Mzl8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1704636487929-6a09f864d53f?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDUyMDU3Mzl8&ixlib=rb-4.0.3
---

# [yuzu-emu/yuzu-android](https://github.com/yuzu-emu/yuzu-android)

| Pull Request | Commit | Title | Author | Merged? |
|----|----|----|----|----|
| [12579](https://github.com/yuzu-emu/yuzu-android//pull/12579) | [`66ae60a9e`](https://github.com/yuzu-emu/yuzu-android//pull/12579/files) | Core: Implement Device Mapping & GPU SMMU | [FernandoS27](https://github.com/FernandoS27/) | Yes |
| [12610](https://github.com/yuzu-emu/yuzu-android//pull/12610) | [`200b371d1`](https://github.com/yuzu-emu/yuzu-android//pull/12610/files) | server_manager: respond to session close correctly | [liamwhite](https://github.com/liamwhite/) | Yes |
| [12611](https://github.com/yuzu-emu/yuzu-android//pull/12611) | [`2f0b57ca1`](https://github.com/yuzu-emu/yuzu-android//pull/12611/files) | kernel: fix resource management issues | [liamwhite](https://github.com/liamwhite/) | Yes |
| [12612](https://github.com/yuzu-emu/yuzu-android//pull/12612) | [`76880b84f`](https://github.com/yuzu-emu/yuzu-android//pull/12612/files) | fsp-srv: use program registry for SetCurrentProcess | [liamwhite](https://github.com/liamwhite/) | Yes |
| [12652](https://github.com/yuzu-emu/yuzu-android//pull/12652) | [`2a0d707ce`](https://github.com/yuzu-emu/yuzu-android//pull/12652/files) | shader_recompiler: emulate 8-bit and 16-bit storage writes with cas loop | [liamwhite](https://github.com/liamwhite/) | Yes |
| [12659](https://github.com/yuzu-emu/yuzu-android//pull/12659) | [`d94097478`](https://github.com/yuzu-emu/yuzu-android//pull/12659/files) | audio: fetch process object from handle table | [liamwhite](https://github.com/liamwhite/) | Yes |


End of merge log. You can find the original README.md below the break.

-----

<!--
SPDX-FileCopyrightText: 2018 yuzu Emulator Project
SPDX-License-Identifier: GPL-2.0-or-later
-->

<h1 align="center">
  <br>
  <a href="https://yuzu-emu.org/"><img src="https://raw.githubusercontent.com/yuzu-emu/yuzu-assets/master/icons/icon.png" alt="yuzu" width="200"></a>
  <br>
  <b>yuzu</b>
  <br>
</h1>

<h4 align="center"><b>yuzu</b> is the world's most popular, open-source, Nintendo Switch emulator — started by the creators of <a href="https://citra-emu.org" target="_blank">Citra</a>.
<br>
It is written in C++ with portability in mind, and we actively maintain builds for Windows, Linux and Android.
</h4>

<p align="center">
    <a href="https://dev.azure.com/yuzu-emu/yuzu/">
        <img src="https://dev.azure.com/yuzu-emu/yuzu/_apis/build/status/yuzu%20mainline?branchName=master"
            alt="Azure Mainline CI Build Status">
    </a>
    <a href="https://discord.com/invite/u77vRWY">
        <img src="https://img.shields.io/discord/398318088170242053?color=5865F2&label=yuzu&logo=discord&logoColor=white"
            alt="Discord">
    </a>
</p>

<p align="center">
  <a href="#compatibility">Compatibility</a> |
  <a href="#development">Development</a> |
  <a href="#building">Building</a> |
  <a href="#download">Download</a> |
  <a href="#support">Support</a> |
  <a href="#license">License</a>
</p>

## Compatibility

The emulator is capable of running most commercial games at full speed, provided you meet the [necessary hardware requirements](https://yuzu-emu.org/help/quickstart/#hardware-requirements).

For a full list of games yuzu supports, please visit our [Compatibility page](https://yuzu-emu.org/game/).

Check out our [website](https://yuzu-emu.org/) for the latest news on exciting features, monthly progress reports, and more!

## Development

Most of the development happens on GitHub. It's also where [our central repository](https://github.com/yuzu-emu/yuzu) is hosted. For development discussion, please join us on [Discord](https://discord.com/invite/u77vRWY).

If you want to contribute, please take a look at the [Contributor's Guide](https://github.com/yuzu-emu/yuzu/wiki/Contributing) and [Developer Information](https://github.com/yuzu-emu/yuzu/wiki/Developer-Information).
You can also contact any of the developers on Discord in order to know about the current state of the emulator.

If you want to contribute to the user interface translation project, please check out the [yuzu project on transifex](https://www.transifex.com/yuzu-emulator/yuzu). We centralize translation work there, and periodically upstream translations.

## Building

* __Windows__: [Windows Build](https://github.com/yuzu-emu/yuzu/wiki/Building-For-Windows)
* __Linux__: [Linux Build](https://github.com/yuzu-emu/yuzu/wiki/Building-For-Linux)

## Download

You can download the latest releases automatically via the installer on our [downloads](https://yuzu-emu.org/downloads/) page.


## Support

If you enjoy the project and want to support us financially, check out our Patreon!

<a href="https://www.patreon.com/yuzuteam">
    <img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

Any donations received will go towards things like:
* Switch consoles to explore and reverse-engineer the hardware
* Switch games for testing, reverse-engineering, and implementing new features
* Web hosting and infrastructure setup
* Software licenses (e.g. Visual Studio, IDA Pro, etc.)
* Additional hardware (e.g. GPUs as-needed to improve rendering support, other peripherals to add support for, etc.)

If you wish to support us a different way, please join our [Discord](https://discord.gg/u77vRWY) and talk to bunnei. You may also contact: donations@yuzu-emu.org.

## License

yuzu is licensed under the GPLv3 (or any later version). Refer to the [LICENSE.txt](https://github.com/yuzu-emu/yuzu/blob/master/LICENSE.txt) file.
