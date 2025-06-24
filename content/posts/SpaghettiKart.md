---
title: SpaghettiKart
date: 2025-06-24T12:29:13+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1748701821466-0b9f8bf839ac?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTA3MzkzMDV8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1748701821466-0b9f8bf839ac?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTA3MzkzMDV8&ixlib=rb-4.1.0
---

# [HarbourMasters/SpaghettiKart](https://github.com/HarbourMasters/SpaghettiKart)

![Spaghetti Kart](docs/spaghettigithublight.png#gh-light-mode-only)
![Spaghetti Kart](docs/spaghettigithubnight.png#gh-dark-mode-only)

## Help Wanted!
This project is looking for a C or C++ coder interested in making a couple scrollable menus that can have lots of items in it. As a method to display custom content does not exist. A tick/render system for custom menus already exists. So just someone willing to build out the menu.

## Discord

Official Discord: https://discord.com/invite/shipofharkinian

If you're having any trouble after reading through this `README`, feel free ask for help in the SpaghettiKart Support text channels. Please keep in mind that we do not condone piracy.

# Quick Start

SpaghettiKart does not include any copyrighted assets.  You are required to provide a supported copy of the game.

### 1. Verify your ROM dump
The US ROM is the only supported version. You can verify you have dumped a supported copy of the game by using the SHA-1 File Checksum Online at https://www.romhacking.net/hash/. The hash for a US ROM is SHA-1: 579C48E211AE952530FFC8738709F078D5DD215E.

### 2. Verify your ROM is in .z64 format
Your ROM needs to be in .z64 format. If it's in .n64 format, use the following to convert it to a .z64: https://hack64.net/tools/swapper.php

### 2. Download SpaghettiKart from [Releases](https://github.com/HarbourMasters/SpaghettiKart/releases)

### 3. Generating the O2R from the ROM
#### Windows
* Extract every file from the zip into a folder of your choosing.
* Run "Spaghettify.exe" and select your US ROM.

#### Linux
* Extract every file from the zip into a folder of your choosing.
* Run "spaghetti.appimage" and select your US ROM. You may have to chmod +x the appimage via terminal.

#### Nintendo Switch
* Run one of the PC releases to generate an `mk64.o2r` file. After launching the game on PC, you will be able to find these files in the same directory as `Spaghettify.exe` or `spaghetti.appimage`.
* Copy the files to your sd card

### 4. Play!
* Launch `Spaghettify.exe`
Congratulations, you are now sailing with SpaghettiKart! Have fun!

# Configuration

### Default keyboard configuration
| N64 | A | B | Z | Start | Analog stick | C buttons | D-Pad |
| - | - | - | - | - | - | - | - |
| Keyboard | Shift | Ctrl | Z | Enter | Arrow keys | TGFH (↑ ↓ ← →) | Num 8 2 4 6 |

### Other shortcuts
| Keys | Action |
| - | - |
| F11 | Fullscreen |
| Tab | Toggle Alternate assets |
| Ctrl+R | Reset |
| Esc | Settings |

### Graphics Backends
Currently, there are three rendering APIs supported: DirectX11 (Windows), OpenGL (all platforms), and Metal (macOS). You can change which API to use in the `Settings` menu of the menubar, which requires a restart.  If you're having an issue with crashing, you can change the API in the `spaghettify.cfg.json` file by finding the line `"Backend":{`... and changing the `id` value to `3` and set the `Name` to `OpenGL`. `DirectX 11` with id `2` is the default on Windows. `Metal` with id `4` is the default on macOS.

# Custom Assets
Custom assets are packed in `.o2r` or stored `.zip` files. To use custom assets, place them in the `mods` folder.

If you're interested in creating and/or packing your own custom asset `.o2r` files, check out the following tools:
* [**retro - O2R generator**](https://github.com/HarbourMasters64/retro)
* [**fast64 - Blender plugin**](https://github.com/HarbourMasters/fast64)

**Note that .otr archives are not supported in SpaghettiKart!**

# Development
### Building

If you want to manually compile SpaghettiKart, please consult the [building instructions](https://github.com/HarbourMasters/SpaghettiKart/blob/main/docs/BUILDING.md).

### Playtesting
If you want to playtest a continuous integration build, you can find them at the links below. Keep in mind that these are for playtesting only, and you will likely encounter bugs and possibly crashes. 

* [Windows](https://nightly.link/HarbourMasters/SpaghettiKart/workflows/main/main/spaghettify-windows.zip)
* [Linux](https://nightly.link/HarbourMasters/SpaghettiKart/workflows/main/main/SpaghettiKart-linux.zip)
* [Switch](https://nightly.link/HarbourMasters/SpaghettiKart/workflows/main/main/Spaghettify-switch.zip)

Maintainers: [MegaMech](https://www.github.com/MegaMech), [Coco](https://www.github.com/coco875), [Kirito](https://github.com/KiritoDv)

<a href="https://github.com/Kenix3/libultraship/">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./docs/poweredbylus.darkmode.png">
    <img alt="Powered by libultraship" src="./docs/poweredbylus.lightmode.png">
  </picture>
</a>
