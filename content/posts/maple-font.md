---
title: maple-font
date: 2025-03-21T12:21:17+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1735317461815-1a0ba64e9a56?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDI1MzA4MTh8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1735317461815-1a0ba64e9a56?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDI1MzA4MTh8&ixlib=rb-4.0.3
---

# [subframe7536/maple-font](https://github.com/subframe7536/maple-font)

![Cover](./resources/header.png)

<p align="center">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/subframe7536/maple-font">
  <img alt="GitHub Downloads (all assets, all releases)" src="https://img.shields.io/github/downloads/subframe7536/maple-font/total">
  <img alt="GitHub Release" src="https://img.shields.io/github/v/release/subframe7536/maple-font">
  <img alt="X (formerly Twitter) Follow" src="https://img.shields.io/twitter/follow/subframe7536">
</p>

<p align="center">
  <a href="#download">Download</a> |
  <a href="https://font.subf.dev">Website</a> |
  English |
  <a href="./README_CN.md">中文</a>
</p>

# Maple Mono

Maple Mono is an open source monospace font focused on smoothing your coding flow.

I create it to enhance my working experience, and hope that it can be useful to others.

V7 is a completely remade version, providing variable font format and source files of font project, redesigning more than half of the glyphs and offering smarter ligatures. You can checkout V6 [here](https://github.com/subframe7536/maple-font/tree/main)

## Features

- ✨ Variable - Infinity font weights with fine-grained italic glyphs.
- ☁️ Smooth - Round corner, brand-new glyph of `@ $ % & Q ->` and cursive `f i j k l x y` in italic style.
- 💪 Useful - Large amount of smart ligatures, see in [`features/`](./source/features/README.md)
- 🎨 Icon - First-Class [Nerd-Font](https://github.com/ryanoasis/nerd-fonts) support, make your terminal more vivid.
- 🔨 Customize - Enable or disable font features as you want, just make your own font.

### Simpified Chinese, Traditional Chinese and Japanese

CN version based on [Resource Han Rounded](https://github.com/CyanoHao/Resource-Han-Rounded) provides complete character set support for Chinese development environments, including Simplified Chinese, Traditional Chinese, and Japanese. Meanwhile, the characteristic of perfect 2:1 alignment between Chinese and English allows this font to achieve a neat, uniform, beautiful, and comfortable appearance in scenarios such as multilingual display and Markdown tables. However, the spacing of Chinese characters is larger compared to other popular Chinese fonts. See details in [release notes](https://github.com/subframe7536/maple-font/releases/tag/cn-base) and [this issue](https://github.com/subframe7536/maple-font/issues/211).

![2-1.png](./resources/2-1.png)

## ScreenShots

![showcase.png](./resources/showcase.png)

- Pictured by [CodeImg](https://github.com/subframe7536/vscode-codeimg)
- Theme: [Maple](https://github.com/subframe7536/vscode-theme-maple)
- Config: font size 16px, line height 1.8, default letter spacing

## Download

You can download all the font archives from [Releases](https://github.com/subframe7536/maple-font/releases).

### Scoop (Windows)

```sh
# Add bucket
scoop bucket add nerd-fonts
# Maple Mono (ttf format)
scoop install Maple-Mono
# Maple Mono (hinted ttf format)
scoop install Maple-Mono-autohint
# Maple Mono (otf format)
scoop install Maple-Mono-otf
# Maple Mono NF
scoop install Maple-Mono-NF
# Maple Mono NF CN
scoop install Maple-Mono-NF-CN
```

### Homebrew (MacOS, Linux)

```sh
# Maple Mono
brew install --cask font-maple-mono
# Maple Mono NF
brew install --cask font-maple-mono-nf
# Maple Mono CN
brew install --cask font-maple-mono-cn
# Maple Mono NF CN
brew install --cask font-maple-mono-nf-cn

# Maple Mono Normal
brew install --cask font-maple-mono-normal
# Maple Mono Normal NF
brew install --cask font-maple-mono-normal-nf
# Maple Mono Normal CN
brew install --cask font-maple-mono-normal-cn
# Maple Mono Normal NF CN
brew install --cask font-maple-mono-normal-nf-cn
```

### AUR (Arch Linux)

```shell
# Maple Mono
paru -S ttf-maple-beta
# Maple Mono NF
paru -S ttf-maple-beta-nf
# Maple Mono NF CN
paru -S ttf-maple-beta-nf-cn
```

## CDN

### Maple Mono

- [fontsource](https://fontsource.org/fonts/maple-mono)
- [ZeoSeven Fonts](https://fonts.zeoseven.com/items/443/)

### Maple Mono CN

- [The Chinese Web Fonts Plan (中文网字计划)](https://chinese-font.netlify.app/zh-cn/fonts/maple-mono-cn/MapleMono-CN-Regular)
- [ZeoSeven Fonts](https://fonts.zeoseven.com/items/442/)

## Usage & Feature Configurations

See in [document](./source/features/README.md) or try it in [Playground](https://font.subf.dev/en/playground)

> [!note]
> The web tool for custom build is under development.

## Naming FAQ

### Features

- **Ligature**: Default version with ligatures (`Maple Mono`)
- **No-Ligature**: Default version without ligatures (`Maple Mono NL`)
- **Normal-Ligature**: [`--normal` preset](#preset) with ligatures (`Maple Mono Normal`)
- **Normal-No-Ligature**: [`--normal` preset](#preset) without ligatures (`Maple Mono Normal NL`)

### Format and Glyph Set

- **Variable**: Minimal version, smoothly change font weight by variable
- **TTF**: Minimal version, ttf format [Recommend!]
- **OTF**: Minimal version, otf format
- **WOFF2**: Minimal version, woff2 format, for small size on web pages
- **NF**: Nerd-Font patched version, add icons for terminal (With `-NF` suffix)
- **CN**: Chinese version, embed with Chinese and Japanese glyphs (With `-CN` suffix)
- **NF-CN**: Full version, embed with icons, Chinese and Japanese glyphs (With `-NF-CN` suffix)

### Font Hint

- **Hinted font** is used for low resolution screen to have better render effect. From my experience, if your screen resolution is lower or equal than 1080P, it is recommended to use "hinted font". Using "unhinted font" will lead to misalignment or uneven thickness on your text.
  - In this case, you can choose `MapleMono-TTF-AutoHint` / `MapleMono-NF` / `MapleMono-NF-CN`, etc.
- **Unhinted font** is used for high resolution screen (e.g. for MacBook). Using "hinted font" will blur your text or make it looks weird.
  - In this case, you can choose `MapleMono-OTF` / `MapleMono-TTF` / `MapleMono-NF-unhinted` / `MapleMono-NF-CN-unhinted`, etc.
- Why there exists `-AutoHint` and `-unhinted` suffix?
  - for backward compatibility, I keep the original naming scheme. `-AutoHint` is only used for `TTF` format.


## Custom Build

The [`config.json`](./config.json) file is used to configure the build process. Checkout the [schema](./source/schema.json) or [document](./source/features/README.md) for more details.

There also have some [command line options](#build-script-usage) for customizing the build process. Cli options have higher priority than options in `config.json`.

### Use Github Actions

You can use [Github Actions](https://github.com/subframe7536/maple-font/actions/workflows/custom.yml) to build the font.

1. Fork the repo
2. (Optional) Change the content in `config.json`
3. Go to Actions tab
4. Click on `Custom Build` menu item on the left
5. Click on `Run workflow` button with options setup
6. Wait for the build to finish
7. Download the font archives from Releases

### Use Docker

```shell
git clone https://github.com/subframe7536/maple-font --depth 1 -b variable
docker build -t maple-font .
docker run -v "$(pwd)/fonts:/app/fonts" -e BUILD_ARGS="--normal" maple-font
```

### Local Build

Clone the repo and run on your local machine. Make sure you have `python3` and `pip` installed

```shell
git clone https://github.com/subframe7536/maple-font --depth 1 -b variable
pip install -r requirements.txt
python build.py
```

- For `Ubuntu` or `Debian`, maybe `python-is-python3` is needed as well

If you have trouble installing the dependencies, just create a new GitHub Codespace and run the commands there

#### Custom Nerd-Font

For custom `font-patcher` args, `font-forge` (and maybe `python3-fontforge` as well) is required.

Maybe you should also change `"nerd_font.extra_args"` in [config.json](./config.json)

Default args: `-l --careful --outputdir dir`
- if `"nerd_font.mono"` is `true`, then add `--mono`

#### Preset

Run `build.py` with `--normal` flag, make the font looks not such "Opinioned" , just like `JetBrains Mono` (with slashed zero).

#### Font Feature Freeze

There are three kind of options for feature freeze ([Why](https://github.com/subframe7536/maple-font/issues/233#issuecomment-2410170270)):

1. `enable`: Forcely enable the features without setting up `cvXX` / `ssXX` / `zero` in font features config, just as default glyphs / ligatures
2. `disable`: Remove the features in `cvXX` / `ssXX` / `zero`, which will no longer effect, even if you enable it manually
3. `ignore`: Do nothing

#### Load Custom Feature File

Run `build.py` with `--apply-fea-file` flag, the feature file from [`source/features/{regular,italic}.fea`](./source/features) will be applied into variable font. You can modify it to change all features, e.g. remove some ligatures in `calt`.

### Chinese version

CN version is disabled by default. Run `python build.py` with `--cn` flag, the CN base fonts (about 130 MB) will download from GitHub.

If you want to build CN base fonts from variable (about 35 MB), setup `"cn.use_static_base_font": false` in [config.json](./config.json) and **BE PATIENT**, instantiation will take about 20-30 minutes.

#### Narrow spacing in CN glyphs

If you think that CN glyphs spacing is **tooooo large**, there is a **EXPERIMENTAL** build option `cn.narrow` or flag `--cn-narrow` to narrow spacing in CN glyphs. You can see effect and track issues in [#249](https://github.com/subframe7536/maple-font/issues/249)

#### GitHub Mirror

The build script will auto download required assets from GitHub. If you have trouble downloading, please setup `github_mirror` in [config.json](./config.json) or `$GITHUB` to your environment variable. (Target URL will be `https://<github_mirror>/<user>/<repo>/releases/download/<tag>/<file>`), or just download the target `.zip` file and put it in the same directory as `build.py`.

### Build Script Usage

```
usage: build.py [-h] [-v] [-d] [--debug] [-n] [--feat FEAT] [--apply-fea-file]
                [--hinted | --no-hinted] [--liga | --no-liga] [--cn-narrow]
                [--nerd-font | --no-nerd-font] [--cn | --no-cn] [--cn-both]
                [--ttf-only] [--cache] [--cn-rebuild] [--archive]

✨ Builder and optimizer for Maple Mono

options:
  -h, --help        show this help message and exit
  -v, --version     show program's version number and exit
  -d, --dry         Output config and exit
  --debug           Add `Debug` suffix to family name, skip optimization

Feature Options:
  -n, --normal      Use normal preset, just like `JetBrains Mono` with slashed zero
  --feat FEAT       Freeze font features, splited by `,` (e.g. `--feat
                    zero,cv01,ss07,ss08`). No effect on variable format
  --apply-fea-file  Load feature file from `source/features/{regular,italic}.fea` to
                    variable font
  --hinted          Use hinted font as base font in NF / CN / NF-CN (default)
  --no-hinted       Use unhinted font as base font in NF / CN / NF-CN
  --liga            Preserve all the ligatures (default)
  --no-liga         Remove all the ligatures
  --cn-narrow       Make CN characters narrow (experimental)

Build Options:
  --nerd-font       Build Nerd-Font version (default)
  --no-nerd-font    Do not build Nerd-Font version
  --cn              Build Chinese version
  --no-cn           Do not build Chinese version (default)
  --cn-both         Build both `Maple Mono CN` and `Maple Mono NF CN`. Nerd-Font
                    version must be enabled
  --ttf-only        Only build TTF format
  --cache           Reuse font cache of TTF, OTF and Woff2 formats
  --cn-rebuild      Reinstantiate CN base font
  --archive         Build font archives with config and license. If has `--cache`
                    flag, only archive Nerd-Font and CN formats
```

## Credit

- [JetBrains Mono](https://github.com/JetBrains/JetBrainsMono)
- [Roboto Mono](https://github.com/googlefonts/RobotoMono)
- [Fira Code](https://github.com/tonsky/FiraCode)
- [Victor Mono](https://github.com/rubjo/victor-mono)
- [Commit Mono](https://github.com/eigilnikolajsen/commit-mono)
- [Code Sample](https://github.com/TheRenegadeCoder/sample-programs-website)
- [Nerd Font](https://github.com/ryanoasis/nerd-fonts)
- [Font Freeze](https://github.com/MuTsunTsai/fontfreeze/)
- [Font Viewer](https://tophix.com/font-tools/font-viewer)
- [Monolisa](https://www.monolisa.dev/)
- [Recursive](https://www.recursive.design/)

## Sponser

If this font is helpful to you, please feel free to buy me a coffee

<a href="https://www.buymeacoffee.com/subframe753"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=subframe753&button_colour=5F7FFF&font_colour=ffffff&font_family=Lato&outline_colour=000000&coffee_colour=FFDD00" /></a>

or sponser me through [Afdian](https://afdian.com/a/subframe7536)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=subframe7536/maple-font&type=Date)](https://www.star-history.com/#subframe7536/maple-font&Date)

## License

SIL Open Font License 1.1
