---
title: gitu
date: 2024-03-13T12:15:27+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1709786704802-d1641c3ad048?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTAzMDMyODl8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1709786704802-d1641c3ad048?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTAzMDMyODl8&ixlib=rb-4.0.3
---

# [altsem/gitu](https://github.com/altsem/gitu)

## It's Gitu! - A Git porcelain *outside* of Emacs
[![CI](https://github.com/altsem/gitu/actions/workflows/ci.yml/badge.svg)](https://github.com/altsem/gitu/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/altsem/gitu/graph/badge.svg?token=5YWPU7GWFW)](https://codecov.io/gh/altsem/gitu)

A terminal user interface for Git. Inspired by Magit, and launched straight from the terminal.

<img src="vhs/rec.gif"/>

### Features
Gitu aims to implement many of the core features of Magit over time. 
It should be familiar to any previous Magit users.

A rough list of so-far supported features:
- File/Hunk-level stage/unstage
- Show (view commits / open EDITOR at line)
- Show branches
- Branch:
  - checkout
- Commit:
  - commit, amend, fixup
- Fetch:
  - all
- Log:
  - current
- Pull / Push:
  - remote
- Rebase:
  - abort, continue, autosquash, interactive

### Keybinds
A help-menu can be shown by pressing the `h` key.

<img src="vhs/help.png"/>

### Install
#### Using Cargo
Run the command (recommended):
`cargo install gitu --locked`

...or to install from git, run:
`cargo install --git https://github.com/altsem/gitu.git --locked`

#### Using Release binaries

gitu is available on Github Releases and should be installed from there.

The latest release is available
[here](https://github.com/altsem/gitu/releases).

Download the archive that is appropriate for your platform and extract the
binary into your `$PATH`. A common valid path location is `/usr/local/bin`.

### Configuration
The environment variables `GIT_EDITOR`, `VISUAL` or `EDITOR` (checked in this order) dictate which editor Gitu will open.

Configuration is also loaded from `~/.config/gitu/config.toml`,
you could copy the [default configuration](src/default_config.toml).
