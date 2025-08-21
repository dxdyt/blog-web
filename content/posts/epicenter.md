---
title: epicenter
date: 2025-08-21T12:23:12+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1753121354334-18bf331648e4?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTU3NTAwOTl8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1753121354334-18bf331648e4?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTU3NTAwOTl8&ixlib=rb-4.1.0
---

# [epicenter-so/epicenter](https://github.com/epicenter-so/epicenter)

<p align="center">
  <a href="https://epicenter.so">
    <img width="200" src="https://github.com/user-attachments/assets/9e210c52-2740-43b6-af3f-e6eaf4b5c397" alt="Epicenter">
  </a>
  <h1 align="center">Epicenter</h1>
  <p align="center">Local-first, open-source apps</p>
  <p align="center">Own your data. Use any model you want. Free and open source ❤️</p>
</p>

> **📢 Repository Update:** The [Whispering](https://github.com/braden-w/whispering/) repository is now part of **Epicenter**! You can find it [here](https://github.com/epicenter-so/epicenter/tree/main/apps/whispering). Everything else remains the same—same tools, same philosophy, same team.

<p align="center">
  <!-- GitHub Stars Badge -->
  <a href="https://github.com/epicenter-so/epicenter" target="_blank">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/epicenter-so/epicenter?style=flat-square" />
  </a>
  <!-- Latest Version Badge -->
  <img src="https://img.shields.io/github/v/release/epicenter-so/epicenter?style=flat-square&label=Latest%20Version&color=brightgreen" />
  <!-- License Badge -->
  <a href="LICENSE" target="_blank">
    <img alt="MIT License" src="https://img.shields.io/github/license/epicenter-so/epicenter.svg?style=flat-square" />
  </a>
  <!-- Discord Badge -->
  <a href="https://go.epicenter.so/discord" target="_blank">
    <img alt="Discord" src="https://img.shields.io/badge/Discord-Join%20us-5865F2?style=flat-square&logo=discord&logoColor=white" />
  </a>
  <!-- Platform Support Badges -->
  <a href="https://github.com/epicenter-so/epicenter/releases" target="_blank">
    <img alt="macOS" src="https://img.shields.io/badge/-macOS-black?style=flat-square&logo=apple&logoColor=white" />
  </a>
  <a href="https://github.com/epicenter-so/epicenter/releases" target="_blank">
    <img alt="Windows" src="https://img.shields.io/badge/-Windows-blue?style=flat-square&logo=windows&logoColor=white" />
  </a>
  <a href="https://github.com/epicenter-so/epicenter/releases" target="_blank">
    <img alt="Linux" src="https://img.shields.io/badge/-Linux-yellow?style=flat-square&logo=linux&logoColor=white" />
  </a>
</p>

<p align="center">
  <a href="#current-tools">Tools</a> •
  <a href="#where-were-headed">Vision</a> •
  <a href="#join-us">Contributing</a> •
  <a href="https://go.epicenter.so/discord">Discord</a> •
</p>

---

## What is Epicenter?

Epicenter is an ecosystem of open-source, local-first apps. Our eventual goal is to store all of your data—notes, transcripts, chat histories—in a single folder of plain text and SQLite. Every tool we build shares this memory. It's open, tweakable, and yours. Grep it, open it in Obsidian, host it wherever you like. The choice is yours.



## Current Tools

<table>
  <tr>
    <td align="center" width="50%">
      <h3>🎙️ <a href="https://github.com/epicenter-so/epicenter/tree/main/apps/whispering">Whispering</a></h3>
      <p>Press shortcut → speak → get text. Desktop transcription that cuts out the middleman. Bring your own API key.</p>
      <p><strong>→ <a href="https://github.com/epicenter-so/epicenter/tree/main/apps/whispering">Explore Whispering</a></strong></p>
    </td>
    <td align="center" width="50%">
      <h3>🤖 <a href="https://github.com/epicenter-so/epicenter/tree/main/apps/sh">epicenter.sh</a></h3>
      <p>A local-first assistant you can chat with. It lives in your folder, becoming the access point to everything you've ever written, thought, or built.</p>
      <p><strong>→ <a href="https://github.com/epicenter-so/epicenter/tree/main/apps/sh">Explore epicenter.sh</a></strong></p>
    </td>
  </tr>
</table>

## Where We're Headed

Our vision is to build a personal workspace where you own your data, choose your models, and replace siloed apps with open, interoperable alternatives. All while preserving authenticity and being free and open source.


## Quick Start

Epicenter will have more apps in the future, but for now, the best way to get started is to run Whispering locally:

```bash
# Prerequisites: Install Bun from https://bun.sh (run bun upgrade if there's issues)
git clone https://github.com/epicenter-so/epicenter.git
cd epicenter
bun install  # Will prompt to upgrade if your Bun version is too old
cd apps/whispering
bun dev
```

## Join Us

## Discord Community

If you think like a generalist, build like a hacker, and value tools that respect your mind—you'll fit right in.

**→ [Join our Discord](https://go.epicenter.so/discord)**

### We're looking for contributors

If you're passionate about open source, local-first software, or are just a cracked Svelte/TypeScript developer—we'd love to build with you.

**→ [Read our Contributing Guide](CONTRIBUTING.md) to get started**

Contributors coordinate and share ideas in our Discord community.

## Tech Stack

<p align="center">
  <img alt="Svelte 5" src="https://img.shields.io/badge/-Svelte%205-orange?style=flat-square&logo=svelte&logoColor=white" />
  <img alt="Tauri" src="https://img.shields.io/badge/-Tauri-blue?style=flat-square&logo=tauri&logoColor=white" />
  <img alt="TypeScript" src="https://img.shields.io/badge/-TypeScript-blue?style=flat-square&logo=typescript&logoColor=white" />
  <img alt="Rust" src="https://img.shields.io/badge/-Rust-orange?style=flat-square&logo=rust&logoColor=white" />
  <img alt="TanStack Query" src="https://img.shields.io/badge/-TanStack%20Query-red?style=flat-square&logo=react-query&logoColor=white" />
  <img alt="Tailwind CSS" src="https://img.shields.io/badge/-Tailwind%20CSS-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white" />
</p>

## License

[MIT](LICENSE). Build on it. Fork it. Make it yours. Please contribute if you can.

---

<p align="center">
  <strong>Contact:</strong> <a href="mailto:github@bradenwong.com">github@bradenwong.com</a> | <a href="https://go.epicenter.so/discord">Discord</a> | <a href="https://twitter.com/braden_wong_">@braden_wong_</a>
</p>

<p align="center">
  <sub>Built with ❤️ for data ownership, local-first, and open-souce</sub>
</p>
