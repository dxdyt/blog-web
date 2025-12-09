---
title: slidev
date: 2025-12-09T12:28:32+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1762912302731-508b4580735f?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NjUyNTQ0Nzh8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1762912302731-508b4580735f?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NjUyNTQ0Nzh8&ixlib=rb-4.1.0
---

# [slidevjs/slidev](https://github.com/slidevjs/slidev)

<br>
<p align="center">
<a href="https://sli.dev" target="_blank">
<img src="https://sli.dev/logo-title.png" alt="Slidev" height="250" width="250"/>
</a>
</p>

<p align="center">
Presentation <b>slide</b>s for <b>dev</b>elopers 🧑‍💻👩‍💻👨‍💻
</p>

<p align="center">
<a href="https://www.npmjs.com/package/@slidev/cli" target="__blank"><img src="https://img.shields.io/npm/v/@slidev/cli?color=2B90B6&label=" alt="NPM version"></a>
<a href="https://www.npmjs.com/package/@slidev/cli" target="__blank"><img alt="NPM Downloads" src="https://img.shields.io/npm/dm/@slidev/cli?color=349dbe&label="></a>
<a href="https://sli.dev/" target="__blank"><img src="https://img.shields.io/static/v1?label=&message=docs%20%26%20demos&color=45b8cd" alt="Docs & Demos"></a>
<a href="https://sli.dev/resources/theme-gallery" target="__blank"><img src="https://img.shields.io/static/v1?label=&message=themes&color=4ec5d4" alt="Themes"></a>
<br>
<a href="https://github.com/slidevjs/slidev/stargazers" target="__blank"><img alt="GitHub stars" src="https://img.shields.io/github/stars/slidevjs/slidev?style=social"></a>
</p>

<p align="center">
  <a href="https://twitter.com/antfu7/status/1389604687502995457">Video Preview</a> | <a href="https://sli.dev">Documentation</a>
</p>

<div align="center">
<table>
<tbody>
<td align="center">
<img width="2000" height="0" alt="" aria-hidden><br>
<sub>Made possible by my <a href="https://github.com/sponsors/antfu">Sponsor Program 💖</a></sub><br>
<img width="2000" height="0" alt="" aria-hidden>
</td>
</tbody>
</table>
</div>

## Features

- 📝 [**Markdown-based**](https://sli.dev/guide/syntax) - focus on content and use your favorite editor
- 🧑‍💻 [**Developer Friendly**](https://sli.dev/guide/syntax#code-blocks) - built-in code highlighting, live coding, etc.
- 🎨 [**Themable**](https://sli.dev/resources/theme-gallery) - theme can be shared and used with npm packages
- 🌈 [**Stylish**](https://sli.dev/guide/syntax#embedded-styles) - on-demand utilities via [UnoCSS](https://github.com/unocss/unocss).
- 🤹 [**Interactive**](https://sli.dev/custom/directory-structure#components) - embedding Vue components seamlessly
- 🎙 [**Presenter Mode**](https://sli.dev/guide/ui#presenter-mode) - use another window, or even your phone to control your slides
- 🎨 [**Drawing**](https://sli.dev/features/drawing) - draw and annotate on your slides
- 🧮 [**LaTeX**](https://sli.dev/features/latex) - built-in LaTeX math equations support
- 📰 [**Diagrams**](https://sli.dev/guide/syntax#diagrams) - creates diagrams using textual descriptions with [Mermaid](https://mermaid.js.org/)
- 🌟 [**Icons**](https://sli.dev/features/icons) - access to icons from any icon set directly
- 💻 [**Editor**](https://sli.dev/guide/index#editor) - integrated editor, or the [VSCode extension](https://sli.dev/features/vscode-extension)
- 🎥 [**Recording**](https://sli.dev/features/recording) - built-in recording and camera view
- 📤 [**Portable**](https://sli.dev/guide/exporting) - export into PDF, PNGs, or PPTX
- ⚡️ [**Fast**](https://vitejs.dev) - instant reloading powered by [Vite](https://vitejs.dev)
- 🛠 [**Hackable**](https://sli.dev/custom/) - using Vite plugins, Vue components, or any npm packages

## Getting Started

### Try it Online ⚡️

[sli.dev/new](https://sli.dev/new)

[![](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://sli.dev/new)

### Init Project Locally

Install [Node.js >=18](https://nodejs.org/) and run the following command:

```bash
npm init slidev
```

Documentation:
**[English](https://sli.dev)** | [中文文档](https://cn.sli.dev) | [Français](https://fr.sli.dev) | [Español](https://es.sli.dev) | [Русский](https://ru.sli.dev) | [Português-BR](https://br.sli.dev)

Discord: [chat.sli.dev](https://chat.sli.dev)

For a full example, you can check the [demo](https://github.com/slidevjs/slidev/blob/main/demo) folder, which is also the source file for [my previous talk](https://antfu.me/posts/composable-vue-vueday-2021).

## Tech Stack

- [Vite](https://vitejs.dev) - An extremely fast frontend tooling
- [Vue 3](https://v3.vuejs.org/) powered [Markdown](https://daringfireball.net/projects/markdown/syntax) - Focus on the content while having the power of HTML and Vue components whenever needed
- [UnoCSS](https://github.com/unocss/unocss) - On-demand utility-first CSS engine, style your slides at ease
- [Shiki](https://github.com/shikijs/shiki), [Monaco Editor](https://github.com/Microsoft/monaco-editor) - First-class code snippets support with live coding capability
- [RecordRTC](https://recordrtc.org) - Built-in recording and camera view
- [VueUse](https://vueuse.org) family - [`@vueuse/core`](https://github.com/vueuse/vueuse), [`@vueuse/motion`](https://github.com/vueuse/motion), etc.
- [Iconify](https://iconify.design/) - Icon sets collection.
- [Drauu](https://github.com/antfu/drauu) - Drawing and annotations support
- [KaTeX](https://katex.org/) - LaTeX math rendering.
- [Mermaid](https://mermaid-js.github.io/mermaid) - Textual Diagrams.

## Sponsors

This project is made possible by all the sponsors supporting my work:

<p align="center">
  <a href="https://github.com/sponsors/antfu">
    <img src='https://cdn.jsdelivr.net/gh/antfu/static/sponsors.svg' alt="Logos from Sponsors" />
  </a>
</p>

## License

MIT License © 2021 [Anthony Fu](https://github.com/antfu)
