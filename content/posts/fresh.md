---
title: fresh
date: 2025-12-07T12:32:26+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1764693756851-10ef8825a787?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NjUwODE5MTJ8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1764693756851-10ef8825a787?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NjUwODE5MTJ8&ixlib=rb-4.1.0
---

# [sinelaw/fresh](https://github.com/sinelaw/fresh)

# Fresh

[Visit the official Fresh website](https://sinelaw.github.io/fresh/)

**[📦 Installation Instructions](#installation)**

A terminal-based text editor.

## Discovery & Ease of Use

Fresh is designed for discovery. It features native UIs, a full Menu system, and a powerful Command Palette. With full mouse support, transitioning from graphical editors is seamless.

## Modern Extensibility

Extend Fresh easily using modern tools. Plugins are written in TypeScript and run securely in a sandboxed Deno environment, providing access to a modern JavaScript ecosystem without compromising stability.

## Zero-Latency Performance

Fresh is engineered for speed. It delivers a near zero-latency experience, with text appearing instantly. The editor is designed to be light and fast, reliably opening and editing huge files up to multi-gigabyte sizes without slowdown.

## Comprehensive Feature Set

- **File Management**: open/save/new/close, file explorer, tabs, auto-revert, git file finder
- **Editing**: undo/redo, multi-cursor, block selection, smart indent, comments, clipboard
- **Search & Replace**: incremental search, find in selection, query replace, git grep
- **Navigation**: go to line/bracket, word movement, position history, bookmarks, error navigation
- **Views & Layout**: split panes, line numbers, line wrap, backgrounds, markdown preview
- **Language Server (LSP)**: go to definition, references, hover, code actions, rename, diagnostics, autocompletion
- **Productivity**: command palette, menu bar, keyboard macros, git log, diagnostics panel
- **Plugins & Extensibility**: TypeScript plugins, color highlighter, TODO highlighter, merge conflicts, path complete, keymaps

![Fresh Screenshot](docs/screenshot1.png)
![Fresh Screenshot](docs/screenshot2.png)
![Fresh Screenshot](docs/screenshot3.png)

## Installation

| Platform | Method |
|----------|--------|
| macOS | [Homebrew](#macos-homebrew) |
| Arch Linux | [AUR](#arch-linux-aur) |
| Debian/Ubuntu | [.deb](#debianubuntu-deb) |
| Fedora/RHEL | [.rpm](#fedorarhelopensuse-rpm) |
| All platforms | [Pre-built binaries](#pre-built-binaries) |
| npm | [npm / npx](#npm) |
| Rust users | [crates.io](#from-cratesio) |
| Developers | [From source](#from-source) |

### macOS (Homebrew)

```bash
brew tap sinelaw/fresh
brew install fresh-editor
```

### Arch Linux ([AUR](https://aur.archlinux.org/packages/fresh-editor))

```bash
yay -S fresh-editor
```

### Debian/Ubuntu (.deb)

Download the `.deb` file from the [releases page](https://github.com/sinelaw/fresh/releases) and install:

```bash
sudo dpkg -i fresh-editor_*.deb
```

### Fedora/RHEL/openSUSE (.rpm)

Download the `.rpm` file from the [releases page](https://github.com/sinelaw/fresh/releases) and install:

```bash
sudo rpm -i fresh-editor-*.rpm
```

### Pre-built binaries

Download the latest release for your platform from the [releases page](https://github.com/sinelaw/fresh/releases).

### npm

```bash
npm install -g @fresh-editor/fresh-editor
```

Or try it without installing:

```bash
npx @fresh-editor/fresh-editor
```

### From crates.io

```bash
cargo install fresh-editor
```

### From source

```bash
git clone https://github.com/sinelaw/fresh.git
cd fresh
cargo build --release
./target/release/fresh [file]
```

## Documentation

- [User Guide](docs/USER_GUIDE.md)
- [Plugin Development](docs/PLUGIN_DEVELOPMENT.md)
- [Architecture](docs/ARCHITECTURE.md)

## License

Copyright (c) Noam Lewis

This project is licensed under the GNU General Public License v2.0 (GPL-2.0).
