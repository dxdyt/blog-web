---
title: nvim-treesitter
date: 2025-05-27T12:26:21+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1747629382443-4176ca83b5de?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDgzMTk4Nzh8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1747629382443-4176ca83b5de?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDgzMTk4Nzh8&ixlib=rb-4.1.0
---

# [nvim-treesitter/nvim-treesitter](https://github.com/nvim-treesitter/nvim-treesitter)

<div align="center">
  <h1>nvim-treesitter</h1>
  <p>
    <a href="https://matrix.to/#/#nvim-treesitter:matrix.org">
      <img alt="Matrix Chat" src="https://img.shields.io/matrix/nvim-treesitter:matrix.org" />
    </a>
    <a href="https://github.com/nvim-treesitter/nvim-treesitter/actions?query=workflow%3A%22Linting+and+style+checking%22+branch%3Amaster">
      <img alt="Linting and Style" src="https://github.com/nvim-treesitter/nvim-treesitter/workflows/Linting%20and%20style%20checking/badge.svg" />
    </a>
    <a href="https://github.com/nvim-treesitter/nvim-treesitter/actions?query=workflow%3A%22Check+loading+of+syntax+files%22+branch%3Amaster">
      <img alt="Syntax files" src="https://github.com/nvim-treesitter/nvim-treesitter/workflows/Check%20loading%20of%20syntax%20files/badge.svg" />
    </a>
  </p>
</div>

<div align="center">
  <p>
    <img src="assets/logo.png" align="center" alt="Logo" />
  </p>
  <p>
    <a href="https://github.com/tree-sitter/tree-sitter">Treesitter</a>
    configurations and abstraction layer for
    <a href="https://github.com/neovim/neovim/">Neovim</a>.
  </p>
  <p>
    <i>
      Logo by <a href="https://github.com/steelsojka">@steelsojka</a>
    </i>
  </p>
</div>

>[!CAUTION]
> The `master` branch is frozen and provided for backward compatibility only. All future updates happen on the [`main` branch](https://github.com/nvim-treesitter/nvim-treesitter/blob/main/README.md), which will become the default branch in the future.

The goal of `nvim-treesitter` is both to provide a simple and easy way to use the interface for [tree-sitter](https://github.com/tree-sitter/tree-sitter) in Neovim and to provide some basic functionality such as highlighting based on it:

![example-cpp](https://user-images.githubusercontent.com/2361214/202753610-e923bf4e-e88f-494b-bb1e-d22a7688446f.png)

Traditional highlighting (left) vs Treesitter-based highlighting (right).
More examples can be found in [our gallery](https://github.com/nvim-treesitter/nvim-treesitter/wiki/Gallery).

**Warning: Treesitter and nvim-treesitter highlighting are an experimental feature of Neovim.
Please consider the experience with this plug-in as experimental until Tree-Sitter support in Neovim is stable!
We recommend using the nightly builds of Neovim if possible.
You can find the current roadmap [here](https://github.com/nvim-treesitter/nvim-treesitter/issues/4767).
The roadmap and all features of this plugin are open to change, and any suggestion will be highly appreciated!**

Nvim-treesitter is based on three interlocking features: [**language parsers**](#language-parsers), [**queries**](#adding-queries), and [**modules**](#available-modules), where _modules_ provide features – e.g., highlighting – based on _queries_ for syntax objects extracted from a given buffer by _language parsers_.
Users will generally only need to interact with parsers and modules as explained in the next section.
For more detailed information on setting these up, see ["Advanced setup"](#advanced-setup).

---

### Table of contents

- [Quickstart](#quickstart)
- [Supported languages](#supported-languages)
- [Available modules](#available-modules)
- [Advanced setup](#advanced-setup)
- [Extra features](#extra-features)
- [Troubleshooting](#troubleshooting)

---

# Quickstart

## Requirements

- **Neovim 0.10** or later (supported up to Neovim 0.12);
- `tar` and `curl` in your path (or alternatively `git`);
- a C compiler in your path and libstdc++ installed ([Windows users please read this!](https://github.com/nvim-treesitter/nvim-treesitter/wiki/Windows-support)).

## Installation

You can install `nvim-treesitter` with your favorite package manager (or using the native `package` feature of vim, see `:h packages`).

**NOTE: This plugin is only guaranteed to work with specific versions of language parsers** (as specified in the `lockfile.json`). **When upgrading the plugin, you must make sure that all installed parsers are updated to the latest version** via `:TSUpdate`.
It is strongly recommended to automate this; e.g., if you are using `lazy.nvim`, put this in your `init.lua` file:

```lua
require("lazy").setup({
  {"nvim-treesitter/nvim-treesitter", branch = 'master', lazy = false, build = ":TSUpdate"}
})
```

>[!CAUTION]
> * This plugin does not support lazy-loading.
> * Make sure to specify the `master` branch, as the default branch will switch to `main` in the future.

For other plugin managers such as `packer.nvim`, see this [Installation page from the wiki](https://github.com/nvim-treesitter/nvim-treesitter/wiki/Installation) (Note that this page is community maintained).

## Language parsers

Treesitter uses a different _parser_ for every language, which needs to be generated via `tree-sitter-cli` from a `grammar.js` file, then compiled to a `.so` library that needs to be placed in neovim's `runtimepath` (typically under `parser/{language}.so`).
To simplify this, `nvim-treesitter` provides commands to automate this process.
If the language is already [supported by `nvim-treesitter`](#supported-languages), you can install it with

```vim
:TSInstall <language_to_install>
```

This command supports tab expansion.
You can also get a list of all available languages and their installation status with `:TSInstallInfo`.
Parsers not on this list can be added manually by following the steps described under ["Adding parsers"](#adding-parsers) below.

To make sure a parser is at the latest compatible version (as specified in `nvim-treesitter`'s `lockfile.json`), use `:TSUpdate {language}`. To update all parsers unconditionally, use `:TSUpdate all` or just `:TSUpdate`.

## Modules

Each module provides a distinct tree-sitter-based feature such as [highlighting](#highlight), [indentation](#indentation), or [folding](#folding); see [`:h nvim-treesitter-modules`](doc/nvim-treesitter.txt) or ["Available modules"](#available-modules) below for a list of modules and their options.

Following examples assume that you are configuring neovim with lua. If you are using vimscript, see `:h lua-heredoc`.
All modules are disabled by default and need to be activated explicitly in your `init.lua`, e.g., via

```lua
require'nvim-treesitter.configs'.setup {
  -- A list of parser names, or "all" (the listed parsers MUST always be installed)
  ensure_installed = { "c", "lua", "vim", "vimdoc", "query", "markdown", "markdown_inline" },

  -- Install parsers synchronously (only applied to `ensure_installed`)
  sync_install = false,

  -- Automatically install missing parsers when entering buffer
  -- Recommendation: set to false if you don't have `tree-sitter` CLI installed locally
  auto_install = true,

  -- List of parsers to ignore installing (or "all")
  ignore_install = { "javascript" },

  ---- If you need to change the installation directory of the parsers (see -> Advanced Setup)
  -- parser_install_dir = "/some/path/to/store/parsers", -- Remember to run vim.opt.runtimepath:append("/some/path/to/store/parsers")!

  highlight = {
    enable = true,

    -- NOTE: these are the names of the parsers and not the filetype. (for example if you want to
    -- disable highlighting for the `tex` filetype, you need to include `latex` in this list as this is
    -- the name of the parser)
    -- list of language that will be disabled
    disable = { "c", "rust" },
    -- Or use a function for more flexibility, e.g. to disable slow treesitter highlight for large files
    disable = function(lang, buf)
        local max_filesize = 100 * 1024 -- 100 KB
        local ok, stats = pcall(vim.loop.fs_stat, vim.api.nvim_buf_get_name(buf))
        if ok and stats and stats.size > max_filesize then
            return true
        end
    end,

    -- Setting this to true will run `:h syntax` and tree-sitter at the same time.
    -- Set this to `true` if you depend on 'syntax' being enabled (like for indentation).
    -- Using this option may slow down your editor, and you may see some duplicate highlights.
    -- Instead of true it can also be a list of languages
    additional_vim_regex_highlighting = false,
  },
}
```

Each module can also be enabled or disabled interactively through the following commands:

```vim
:TSBufEnable {module} " enable module on current buffer
:TSBufDisable {module} " disable module on current buffer
:TSEnable {module} [{ft}] " enable module on every buffer. If filetype is specified, enable only for this filetype.
:TSDisable {module} [{ft}] " disable module on every buffer. If filetype is specified, disable only for this filetype.
:TSModuleInfo [{module}] " list information about modules state for each filetype
```

Check [`:h nvim-treesitter-commands`](doc/nvim-treesitter.txt) for a list of all available commands.
It may be necessary to reload the buffer (e.g., via `:e`) after enabling a module interactively.

# Supported languages

For `nvim-treesitter` to support a specific feature for a specific language requires both a parser for that language and an appropriate language-specific query file for that feature.

The following is a list of languages for which a parser can be installed through `:TSInstall`; a checked box means that `nvim-treesitter` also contains queries at least for the `highlight` module.

Experimental parsers are parsers that have a maintainer but are not stable enough for
daily use yet.

We are looking for maintainers to add more parsers and to write query files for their languages. Check our [tracking issue](https://github.com/nvim-treesitter/nvim-treesitter/issues/2282) for open language requests.

<!--This section of the README is automatically updated by a CI job-->
<!--parserinfo-->
- [x] [ada](https://github.com/briot/tree-sitter-ada) (maintained by @briot)
- [x] [agda](https://github.com/tree-sitter/tree-sitter-agda) (maintained by @Decodetalkers)
- [x] [angular](https://github.com/dlvandenberg/tree-sitter-angular) (experimental, maintained by @dlvandenberg)
- [x] [apex](https://github.com/aheber/tree-sitter-sfapex) (maintained by @aheber, @xixiaofinland)
- [x] [arduino](https://github.com/ObserverOfTime/tree-sitter-arduino) (maintained by @ObserverOfTime)
- [x] [asm](https://github.com/RubixDev/tree-sitter-asm) (maintained by @RubixDev)
- [x] [astro](https://github.com/virchau13/tree-sitter-astro) (maintained by @virchau13)
- [x] [authzed](https://github.com/mleonidas/tree-sitter-authzed) (maintained by @mattpolzin)
- [ ] [awk](https://github.com/Beaglefoot/tree-sitter-awk)
- [x] [bash](https://github.com/tree-sitter/tree-sitter-bash) (maintained by @TravonteD)
- [x] [bass](https://github.com/vito/tree-sitter-bass) (maintained by @amaanq)
- [x] [beancount](https://github.com/polarmutex/tree-sitter-beancount) (maintained by @polarmutex)
- [x] [bibtex](https://github.com/latex-lsp/tree-sitter-bibtex) (maintained by @theHamsta, @clason)
- [x] [bicep](https://github.com/amaanq/tree-sitter-bicep) (maintained by @amaanq)
- [x] [bitbake](https://github.com/amaanq/tree-sitter-bitbake) (maintained by @amaanq)
- [x] [blade](https://github.com/EmranMR/tree-sitter-blade) (maintained by @calebdw)
- [x] [blueprint](https://gitlab.com/gabmus/tree-sitter-blueprint.git) (experimental, maintained by @gabmus)
- [x] [bp](https://github.com/ambroisie/tree-sitter-bp) (maintained by @ambroisie)
- [x] [brightscript](https://github.com/ajdelcimmuto/tree-sitter-brightscript) (maintained by @ajdelcimmuto)
- [x] [c](https://github.com/tree-sitter/tree-sitter-c) (maintained by @amaanq)
- [x] [c_sharp](https://github.com/tree-sitter/tree-sitter-c-sharp) (maintained by @amaanq)
- [x] [caddy](https://github.com/opa-oz/tree-sitter-caddy) (maintained by @opa-oz)
- [x] [cairo](https://github.com/amaanq/tree-sitter-cairo) (maintained by @amaanq)
- [x] [capnp](https://github.com/amaanq/tree-sitter-capnp) (maintained by @amaanq)
- [x] [chatito](https://github.com/ObserverOfTime/tree-sitter-chatito) (maintained by @ObserverOfTime)
- [x] [circom](https://github.com/Decurity/tree-sitter-circom) (maintained by @alexandr-martirosyan)
- [x] [clojure](https://github.com/sogaiu/tree-sitter-clojure) (maintained by @NoahTheDuke)
- [x] [cmake](https://github.com/uyha/tree-sitter-cmake) (maintained by @uyha)
- [x] [comment](https://github.com/stsewd/tree-sitter-comment) (maintained by @stsewd)
- [x] [commonlisp](https://github.com/theHamsta/tree-sitter-commonlisp) (maintained by @theHamsta)
- [x] [cooklang](https://github.com/addcninblue/tree-sitter-cooklang) (maintained by @addcninblue)
- [x] [corn](https://github.com/jakestanger/tree-sitter-corn) (maintained by @jakestanger)
- [x] [cpon](https://github.com/amaanq/tree-sitter-cpon) (maintained by @amaanq)
- [x] [cpp](https://github.com/tree-sitter/tree-sitter-cpp) (maintained by @theHamsta)
- [x] [css](https://github.com/tree-sitter/tree-sitter-css) (maintained by @TravonteD)
- [x] [csv](https://github.com/amaanq/tree-sitter-csv) (maintained by @amaanq)
- [x] [cuda](https://github.com/theHamsta/tree-sitter-cuda) (maintained by @theHamsta)
- [x] [cue](https://github.com/eonpatapon/tree-sitter-cue) (maintained by @amaanq)
- [x] [cylc](https://github.com/elliotfontaine/tree-sitter-cylc) (maintained by @elliotfontaine)
- [x] [d](https://github.com/gdamore/tree-sitter-d) (maintained by @amaanq)
- [x] [dart](https://github.com/UserNobody14/tree-sitter-dart) (maintained by @akinsho)
- [x] [desktop](https://github.com/ValdezFOmar/tree-sitter-desktop) (maintained by @ValdezFOmar)
- [x] [devicetree](https://github.com/joelspadin/tree-sitter-devicetree) (maintained by @jedrzejboczar)
- [x] [dhall](https://github.com/jbellerb/tree-sitter-dhall) (maintained by @amaanq)
- [x] [diff](https://github.com/the-mikedavis/tree-sitter-diff) (maintained by @gbprod)
- [x] [disassembly](https://github.com/ColinKennedy/tree-sitter-disassembly) (maintained by @ColinKennedy)
- [x] [djot](https://github.com/treeman/tree-sitter-djot) (maintained by @NoahTheDuke)
- [x] [dockerfile](https://github.com/camdencheek/tree-sitter-dockerfile) (maintained by @camdencheek)
- [x] [dot](https://github.com/rydesun/tree-sitter-dot) (maintained by @rydesun)
- [x] [doxygen](https://github.com/amaanq/tree-sitter-doxygen) (maintained by @amaanq)
- [x] [dtd](https://github.com/tree-sitter-grammars/tree-sitter-xml) (maintained by @ObserverOfTime)
- [x] [earthfile](https://github.com/glehmann/tree-sitter-earthfile) (maintained by @glehmann)
- [x] [ebnf](https://github.com/RubixDev/ebnf) (experimental, maintained by @RubixDev)
- [x] [editorconfig](https://github.com/ValdezFOmar/tree-sitter-editorconfig) (maintained by @ValdezFOmar)
- [x] [eds](https://github.com/uyha/tree-sitter-eds) (maintained by @uyha)
- [x] [eex](https://github.com/connorlay/tree-sitter-eex) (maintained by @connorlay)
- [x] [elixir](https://github.com/elixir-lang/tree-sitter-elixir) (maintained by @connorlay)
- [x] [elm](https://github.com/elm-tooling/tree-sitter-elm) (maintained by @zweimach)
- [x] [elsa](https://github.com/glapa-grossklag/tree-sitter-elsa) (maintained by @glapa-grossklag, @amaanq)
- [x] [elvish](https://github.com/elves/tree-sitter-elvish) (maintained by @elves)
- [ ] [embedded_template](https://github.com/tree-sitter/tree-sitter-embedded-template)
- [x] [enforce](https://github.com/simonvic/tree-sitter-enforce) (maintained by @simonvic)
- [x] [erlang](https://github.com/WhatsApp/tree-sitter-erlang) (maintained by @filmor)
- [x] [facility](https://github.com/FacilityApi/tree-sitter-facility) (maintained by @bryankenote)
- [x] [faust](https://github.com/khiner/tree-sitter-faust) (maintained by @khiner)
- [x] [fennel](https://github.com/alexmozaidze/tree-sitter-fennel) (maintained by @alexmozaidze)
- [x] [fidl](https://github.com/google/tree-sitter-fidl) (maintained by @chaopeng)
- [x] [firrtl](https://github.com/amaanq/tree-sitter-firrtl) (maintained by @amaanq)
- [x] [fish](https://github.com/ram02z/tree-sitter-fish) (maintained by @ram02z)
- [x] [foam](https://github.com/FoamScience/tree-sitter-foam) (experimental, maintained by @FoamScience)
- [x] [forth](https://github.com/AlexanderBrevig/tree-sitter-forth) (maintained by @amaanq)
- [x] [fortran](https://github.com/stadelmanma/tree-sitter-fortran) (maintained by @amaanq)
- [x] [fsh](https://github.com/mgramigna/tree-sitter-fsh) (maintained by @mgramigna)
- [x] [fsharp](https://github.com/ionide/tree-sitter-fsharp) (maintained by @nsidorenco)
- [x] [func](https://github.com/amaanq/tree-sitter-func) (maintained by @amaanq)
- [x] [fusion](https://gitlab.com/jirgn/tree-sitter-fusion.git) (maintained by @jirgn)
- [x] [GAP system](https://github.com/gap-system/tree-sitter-gap) (maintained by @reiniscirpons)
- [x] [GAP system test files](https://github.com/gap-system/tree-sitter-gaptst) (maintained by @reiniscirpons)
- [x] [Godot (gdscript)](https://github.com/PrestonKnopp/tree-sitter-gdscript) (maintained by @PrestonKnopp)
- [x] [gdshader](https://github.com/GodOfAvacyn/tree-sitter-gdshader) (maintained by @godofavacyn)
- [x] [git_config](https://github.com/the-mikedavis/tree-sitter-git-config) (maintained by @amaanq)
- [x] [git_rebase](https://github.com/the-mikedavis/tree-sitter-git-rebase) (maintained by @gbprod)
- [x] [gitattributes](https://github.com/ObserverOfTime/tree-sitter-gitattributes) (maintained by @ObserverOfTime)
- [x] [gitcommit](https://github.com/gbprod/tree-sitter-gitcommit) (maintained by @gbprod)
- [x] [gitignore](https://github.com/shunsambongi/tree-sitter-gitignore) (maintained by @theHamsta)
- [x] [gleam](https://github.com/gleam-lang/tree-sitter-gleam) (maintained by @amaanq)
- [x] [Glimmer and Ember](https://github.com/ember-tooling/tree-sitter-glimmer) (maintained by @NullVoxPopuli)
- [x] [glimmer_javascript](https://github.com/NullVoxPopuli/tree-sitter-glimmer-javascript) (maintained by @NullVoxPopuli)
- [x] [glimmer_typescript](https://github.com/NullVoxPopuli/tree-sitter-glimmer-typescript) (maintained by @NullVoxPopuli)
- [x] [glsl](https://github.com/theHamsta/tree-sitter-glsl) (maintained by @theHamsta)
- [x] [GN (Generate Ninja)](https://github.com/amaanq/tree-sitter-gn) (maintained by @amaanq)
- [x] [gnuplot](https://github.com/dpezto/tree-sitter-gnuplot) (maintained by @dpezto)
- [x] [go](https://github.com/tree-sitter/tree-sitter-go) (maintained by @theHamsta, @WinWisely268)
- [x] [goctl](https://github.com/chaozwn/tree-sitter-goctl) (maintained by @chaozwn)
- [x] [Godot Resources (gdresource)](https://github.com/PrestonKnopp/tree-sitter-godot-resource) (maintained by @pierpo)
- [x] [gomod](https://github.com/camdencheek/tree-sitter-go-mod) (maintained by @camdencheek)
- [x] [gosum](https://github.com/amaanq/tree-sitter-go-sum) (maintained by @amaanq)
- [x] [gotmpl](https://github.com/ngalaiko/tree-sitter-go-template) (maintained by @qvalentin)
- [x] [gowork](https://github.com/omertuc/tree-sitter-go-work) (maintained by @omertuc)
- [x] [gpg](https://github.com/ObserverOfTime/tree-sitter-gpg-config) (maintained by @ObserverOfTime)
- [x] [graphql](https://github.com/bkegley/tree-sitter-graphql) (maintained by @bkegley)
- [x] [gren](https://github.com/MaeBrooks/tree-sitter-gren) (maintained by @MaeBrooks)
- [x] [groovy](https://github.com/murtaza64/tree-sitter-groovy) (maintained by @murtaza64)
- [x] [gstlaunch](https://github.com/theHamsta/tree-sitter-gstlaunch) (maintained by @theHamsta)
- [ ] [hack](https://github.com/slackhq/tree-sitter-hack)
- [x] [hare](https://github.com/amaanq/tree-sitter-hare) (maintained by @amaanq)
- [x] [haskell](https://github.com/tree-sitter/tree-sitter-haskell) (maintained by @mrcjkb)
- [x] [haskell_persistent](https://github.com/MercuryTechnologies/tree-sitter-haskell-persistent) (maintained by @lykahb)
- [x] [hcl](https://github.com/MichaHoffmann/tree-sitter-hcl) (maintained by @MichaHoffmann)
- [x] [heex](https://github.com/connorlay/tree-sitter-heex) (maintained by @connorlay)
- [x] [helm](https://github.com/ngalaiko/tree-sitter-go-template) (maintained by @qvalentin)
- [x] [hjson](https://github.com/winston0410/tree-sitter-hjson) (maintained by @winston0410)
- [x] [hlsl](https://github.com/theHamsta/tree-sitter-hlsl) (maintained by @theHamsta)
- [x] [hlsplaylist](https://github.com/Freed-Wu/tree-sitter-hlsplaylist) (maintained by @Freed-Wu)
- [x] [hocon](https://github.com/antosha417/tree-sitter-hocon) (maintained by @antosha417)
- [x] [hoon](https://github.com/urbit-pilled/tree-sitter-hoon) (experimental, maintained by @urbit-pilled)
- [x] [html](https://github.com/tree-sitter/tree-sitter-html) (maintained by @TravonteD)
- [x] [htmldjango](https://github.com/interdependence/tree-sitter-htmldjango) (experimental, maintained by @ObserverOfTime)
- [x] [http](https://github.com/rest-nvim/tree-sitter-http) (maintained by @amaanq, @NTBBloodbath)
- [x] [hurl](https://github.com/pfeiferj/tree-sitter-hurl) (maintained by @pfeiferj)
- [x] [hyprlang](https://github.com/luckasRanarison/tree-sitter-hyprlang) (maintained by @luckasRanarison)
- [x] [idl](https://github.com/cathaysia/tree-sitter-idl) (maintained by @cathaysia)
- [x] [idris](https://github.com/kayhide/tree-sitter-idris) (maintained by @srghma)
- [x] [ini](https://github.com/justinmk/tree-sitter-ini) (experimental, maintained by @theHamsta)
- [x] [inko](https://github.com/inko-lang/tree-sitter-inko) (maintained by @yorickpeterse)
- [x] [ipkg](https://github.com/srghma/tree-sitter-ipkg) (maintained by @srghma)
- [x] [ispc](https://github.com/fab4100/tree-sitter-ispc) (maintained by @fab4100)
- [x] [janet_simple](https://github.com/sogaiu/tree-sitter-janet-simple) (maintained by @sogaiu)
- [x] [java](https://github.com/tree-sitter/tree-sitter-java) (maintained by @p00f)
- [x] [javadoc](https://github.com/rmuir/tree-sitter-javadoc) (maintained by @rmuir)
- [x] [javascript](https://github.com/tree-sitter/tree-sitter-javascript) (maintained by @steelsojka)
- [x] [jinja](https://github.com/cathaysia/tree-sitter-jinja) (maintained by @cathaysia)
- [x] [jinja_inline](https://github.com/cathaysia/tree-sitter-jinja) (maintained by @cathaysia)
- [x] [jq](https://github.com/flurie/tree-sitter-jq) (maintained by @ObserverOfTime)
- [x] [jsdoc](https://github.com/tree-sitter/tree-sitter-jsdoc) (maintained by @steelsojka)
- [x] [json](https://github.com/tree-sitter/tree-sitter-json) (maintained by @steelsojka)
- [x] [json5](https://github.com/Joakker/tree-sitter-json5) (maintained by @Joakker)
- [x] [JSON with comments](https://gitlab.com/WhyNotHugo/tree-sitter-jsonc.git) (maintained by @WhyNotHugo)
- [x] [jsonnet](https://github.com/sourcegraph/tree-sitter-jsonnet) (maintained by @nawordar)
- [x] [julia](https://github.com/tree-sitter/tree-sitter-julia) (maintained by @fredrikekre)
- [x] [just](https://github.com/IndianBoy42/tree-sitter-just) (maintained by @Hubro)
- [x] [kcl](https://github.com/kcl-lang/tree-sitter-kcl) (maintained by @bertbaron)
- [x] [kconfig](https://github.com/amaanq/tree-sitter-kconfig) (maintained by @amaanq)
- [x] [kdl](https://github.com/amaanq/tree-sitter-kdl) (maintained by @amaanq)
- [x] [kotlin](https://github.com/fwcd/tree-sitter-kotlin) (maintained by @SalBakraa)
- [x] [koto](https://github.com/koto-lang/tree-sitter-koto) (maintained by @irh)
- [x] [kusto](https://github.com/Willem-J-an/tree-sitter-kusto) (maintained by @Willem-J-an)
- [x] [lalrpop](https://github.com/traxys/tree-sitter-lalrpop) (maintained by @traxys)
- [x] [latex](https://github.com/latex-lsp/tree-sitter-latex) (maintained by @theHamsta, @clason)
- [x] [ledger](https://github.com/cbarrete/tree-sitter-ledger) (maintained by @cbarrete)
- [x] [leo](https://github.com/r001/tree-sitter-leo) (maintained by @r001)
- [x] [linkerscript](https://github.com/amaanq/tree-sitter-linkerscript) (maintained by @amaanq)
- [x] [liquid](https://github.com/hankthetank27/tree-sitter-liquid) (maintained by @hankthetank27)
- [x] [liquidsoap](https://github.com/savonet/tree-sitter-liquidsoap) (maintained by @toots)
- [x] [llvm](https://github.com/benwilliamgraham/tree-sitter-llvm) (maintained by @benwilliamgraham)
- [x] [lua](https://github.com/MunifTanjim/tree-sitter-lua) (maintained by @muniftanjim)
- [x] [luadoc](https://github.com/amaanq/tree-sitter-luadoc) (maintained by @amaanq)
- [x] [lua patterns](https://github.com/amaanq/tree-sitter-luap) (maintained by @amaanq)
- [x] [luau](https://github.com/amaanq/tree-sitter-luau) (maintained by @amaanq)
- [x] [m68k](https://github.com/grahambates/tree-sitter-m68k) (maintained by @grahambates)
- [x] [make](https://github.com/alemuller/tree-sitter-make) (maintained by @lewis6991)
- [x] [markdown (basic highlighting)](https://github.com/MDeiml/tree-sitter-markdown) (experimental, maintained by @MDeiml)
- [x] [markdown_inline (needed for full highlighting)](https://github.com/MDeiml/tree-sitter-markdown) (experimental, maintained by @MDeiml)
- [x] [matlab](https://github.com/acristoffers/tree-sitter-matlab) (maintained by @acristoffers)
- [x] [menhir](https://github.com/Kerl13/tree-sitter-menhir) (maintained by @Kerl13)
- [ ] [mermaid](https://github.com/monaqa/tree-sitter-mermaid) (experimental)
- [x] [meson](https://github.com/Decodetalkers/tree-sitter-meson) (maintained by @Decodetalkers)
- [x] [mlir](https://github.com/artagnon/tree-sitter-mlir) (experimental, maintained by @artagnon)
- [x] [muttrc](https://github.com/neomutt/tree-sitter-muttrc) (maintained by @Freed-Wu)
- [x] [nasm](https://github.com/naclsn/tree-sitter-nasm) (maintained by @ObserverOfTime)
- [x] [nginx](https://github.com/opa-oz/tree-sitter-nginx) (maintained by @opa-oz)
- [ ] [nickel](https://github.com/nickel-lang/tree-sitter-nickel)
- [x] [nim](https://github.com/alaviss/tree-sitter-nim) (maintained by @aMOPel)
- [x] [nim_format_string](https://github.com/aMOPel/tree-sitter-nim-format-string) (maintained by @aMOPel)
- [x] [ninja](https://github.com/alemuller/tree-sitter-ninja) (maintained by @alemuller)
- [x] [nix](https://github.com/cstrahan/tree-sitter-nix) (maintained by @leo60228)
- [x] [norg](https://github.com/nvim-neorg/tree-sitter-norg) (maintained by @JoeyGrajciar, @vhyrro)
- [x] [nqc](https://github.com/amaanq/tree-sitter-nqc) (maintained by @amaanq)
- [x] [nu](https://github.com/nushell/tree-sitter-nu) (maintained by @abhisheksingh0x558)
- [x] [objc](https://github.com/amaanq/tree-sitter-objc) (maintained by @amaanq)
- [x] [objdump](https://github.com/ColinKennedy/tree-sitter-objdump) (maintained by @ColinKennedy)
- [x] [ocaml](https://github.com/tree-sitter/tree-sitter-ocaml) (maintained by @undu)
- [x] [ocaml_interface](https://github.com/tree-sitter/tree-sitter-ocaml) (maintained by @undu)
- [x] [ocamllex](https://github.com/atom-ocaml/tree-sitter-ocamllex) (maintained by @undu)
- [x] [odin](https://github.com/amaanq/tree-sitter-odin) (maintained by @amaanq)
- [x] [pascal](https://github.com/Isopod/tree-sitter-pascal) (maintained by @Isopod)
- [x] [passwd](https://github.com/ath3/tree-sitter-passwd) (maintained by @amaanq)
- [x] [pem](https://github.com/ObserverOfTime/tree-sitter-pem) (maintained by @ObserverOfTime)
- [x] [perl](https://github.com/tree-sitter-perl/tree-sitter-perl) (maintained by @RabbiVeesh, @LeoNerd)
- [x] [php](https://github.com/tree-sitter/tree-sitter-php) (maintained by @tk-shirasaka, @calebdw)
- [x] [php_only](https://github.com/tree-sitter/tree-sitter-php) (maintained by @tk-shirasaka, @calebdw)
- [x] [phpdoc](https://github.com/claytonrcarter/tree-sitter-phpdoc) (experimental, maintained by @mikehaertl)
- [x] [pioasm](https://github.com/leo60228/tree-sitter-pioasm) (maintained by @leo60228)
- [x] [po](https://github.com/erasin/tree-sitter-po) (maintained by @amaanq)
- [x] [pod](https://github.com/tree-sitter-perl/tree-sitter-pod) (maintained by @RabbiVeesh, @LeoNerd)
- [x] [Path of Exile item filter](https://github.com/ObserverOfTime/tree-sitter-poe-filter) (experimental, maintained by @ObserverOfTime)
- [x] [pony](https://github.com/amaanq/tree-sitter-pony) (maintained by @amaanq, @mfelsche)
- [x] [powershell](https://github.com/airbus-cert/tree-sitter-powershell) (maintained by @L2jLiga)
- [x] [printf](https://github.com/ObserverOfTime/tree-sitter-printf) (maintained by @ObserverOfTime)
- [x] [prisma](https://github.com/victorhqc/tree-sitter-prisma) (maintained by @elianiva)
- [x] [problog](https://github.com/foxyseta/tree-sitter-prolog) (maintained by @foxyseta)
- [x] [prolog](https://github.com/foxyseta/tree-sitter-prolog) (maintained by @foxyseta)
- [x] [promql](https://github.com/MichaHoffmann/tree-sitter-promql) (maintained by @MichaHoffmann)
- [x] [properties](https://github.com/tree-sitter-grammars/tree-sitter-properties) (maintained by @ObserverOfTime)
- [x] [proto](https://github.com/treywood/tree-sitter-proto) (maintained by @treywood)
- [x] [prql](https://github.com/PRQL/tree-sitter-prql) (maintained by @matthias-Q)
- [x] [psv](https://github.com/amaanq/tree-sitter-csv) (maintained by @amaanq)
- [x] [pug](https://github.com/zealot128/tree-sitter-pug) (experimental, maintained by @zealot128)
- [x] [puppet](https://github.com/amaanq/tree-sitter-puppet) (maintained by @amaanq)
- [x] [purescript](https://github.com/postsolar/tree-sitter-purescript) (maintained by @postsolar)
- [x] [PyPA manifest](https://github.com/ObserverOfTime/tree-sitter-pymanifest) (maintained by @ObserverOfTime)
- [x] [python](https://github.com/tree-sitter/tree-sitter-python) (maintained by @stsewd, @theHamsta)
- [x] [ql](https://github.com/tree-sitter/tree-sitter-ql) (maintained by @pwntester)
- [x] [qmldir](https://github.com/Decodetalkers/tree-sitter-qmldir) (maintained by @amaanq)
- [x] [qmljs](https://github.com/yuja/tree-sitter-qmljs) (maintained by @Decodetalkers)
- [x] [Tree-Sitter query language](https://github.com/nvim-treesitter/tree-sitter-query) (maintained by @steelsojka)
- [x] [r](https://github.com/r-lib/tree-sitter-r) (maintained by @ribru17)
- [ ] [racket](https://github.com/6cdh/tree-sitter-racket)
- [x] [ralph](https://github.com/alephium/tree-sitter-ralph) (maintained by @tdroxler)
- [x] [rasi](https://github.com/Fymyte/tree-sitter-rasi) (maintained by @Fymyte)
- [x] [razor](https://github.com/tris203/tree-sitter-razor) (maintained by @tris203)
- [x] [rbs](https://github.com/joker1007/tree-sitter-rbs) (maintained by @joker1007)
- [x] [re2c](https://github.com/amaanq/tree-sitter-re2c) (maintained by @amaanq)
- [x] [readline](https://github.com/ribru17/tree-sitter-readline) (maintained by @ribru17)
- [x] [regex](https://github.com/tree-sitter/tree-sitter-regex) (maintained by @theHamsta)
- [x] [rego](https://github.com/FallenAngel97/tree-sitter-rego) (maintained by @FallenAngel97)
- [x] [pip requirements](https://github.com/ObserverOfTime/tree-sitter-requirements) (maintained by @ObserverOfTime)
- [x] [rescript](https://github.com/rescript-lang/tree-sitter-rescript) (maintained by @ribru17)
- [x] [rnoweb](https://github.com/bamonroe/tree-sitter-rnoweb) (maintained by @bamonroe)
- [x] [robot](https://github.com/Hubro/tree-sitter-robot) (maintained by @Hubro)
- [x] [robots](https://github.com/opa-oz/tree-sitter-robots-txt) (maintained by @opa-oz)
- [x] [roc](https://github.com/faldor20/tree-sitter-roc) (maintained by @nat-418)
- [x] [ron](https://github.com/amaanq/tree-sitter-ron) (maintained by @amaanq)
- [x] [rst](https://github.com/stsewd/tree-sitter-rst) (maintained by @stsewd)
- [x] [ruby](https://github.com/tree-sitter/tree-sitter-ruby) (maintained by @TravonteD)
- [x] [runescript](https://github.com/2004Scape/tree-sitter-runescript) (maintained by @2004Scape)
- [x] [rust](https://github.com/tree-sitter/tree-sitter-rust) (maintained by @amaanq)
- [x] [scala](https://github.com/tree-sitter/tree-sitter-scala) (maintained by @stevanmilic)
- [x] [scfg](https://github.com/rockorager/tree-sitter-scfg) (maintained by @WhyNotHugo)
- [ ] [scheme](https://github.com/6cdh/tree-sitter-scheme)
- [x] [scss](https://github.com/serenadeai/tree-sitter-scss) (maintained by @elianiva)
- [x] [sflog](https://github.com/aheber/tree-sitter-sfapex) (maintained by @aheber, @xixiaofinland)
- [x] [slang](https://github.com/theHamsta/tree-sitter-slang) (experimental, maintained by @theHamsta)
- [x] [slim](https://github.com/theoo/tree-sitter-slim) (maintained by @theoo)
- [x] [slint](https://github.com/slint-ui/tree-sitter-slint) (maintained by @hunger)
- [x] [smali](https://github.com/tree-sitter-grammars/tree-sitter-smali) (maintained by @amaanq)
- [x] [smithy](https://github.com/indoorvivants/tree-sitter-smithy) (maintained by @amaanq, @keynmol)
- [ ] [snakemake](https://github.com/osthomas/tree-sitter-snakemake) (experimental)
- [x] [solidity](https://github.com/JoranHonig/tree-sitter-solidity) (maintained by @amaanq)
- [x] [soql](https://github.com/aheber/tree-sitter-sfapex) (maintained by @aheber, @xixiaofinland)
- [x] [sosl](https://github.com/aheber/tree-sitter-sfapex) (maintained by @aheber, @xixiaofinland)
- [x] [sourcepawn](https://github.com/nilshelmig/tree-sitter-sourcepawn) (maintained by @Sarrus1)
- [x] [sparql](https://github.com/GordianDziwis/tree-sitter-sparql) (maintained by @GordianDziwis)
- [x] [sql](https://github.com/derekstride/tree-sitter-sql) (maintained by @derekstride)
- [x] [squirrel](https://github.com/amaanq/tree-sitter-squirrel) (maintained by @amaanq)
- [x] [ssh_config](https://github.com/ObserverOfTime/tree-sitter-ssh-config) (maintained by @ObserverOfTime)
- [x] [starlark](https://github.com/amaanq/tree-sitter-starlark) (maintained by @amaanq)
- [x] [strace](https://github.com/sigmaSd/tree-sitter-strace) (maintained by @amaanq)
- [x] [styled](https://github.com/mskelton/tree-sitter-styled) (maintained by @mskelton)
- [x] [supercollider](https://github.com/madskjeldgaard/tree-sitter-supercollider) (maintained by @madskjeldgaard)
- [x] [superhtml](https://github.com/kristoff-it/superhtml) (maintained by @rockorager)
- [x] [surface](https://github.com/connorlay/tree-sitter-surface) (maintained by @connorlay)
- [x] [svelte](https://github.com/tree-sitter-grammars/tree-sitter-svelte) (maintained by @amaanq)
- [x] [sway](https://github.com/FuelLabs/tree-sitter-sway.git) (maintained by @ribru17)
- [x] [swift](https://github.com/alex-pinkus/tree-sitter-swift) (maintained by @alex-pinkus)
- [x] [sxhkdrc](https://github.com/RaafatTurki/tree-sitter-sxhkdrc) (maintained by @RaafatTurki)
- [x] [systemtap](https://github.com/ok-ryoko/tree-sitter-systemtap) (maintained by @ok-ryoko)
- [x] [t32](https://gitlab.com/xasc/tree-sitter-t32.git) (maintained by @xasc)
- [x] [tablegen](https://github.com/amaanq/tree-sitter-tablegen) (maintained by @amaanq)
- [x] [tact](https://github.com/tact-lang/tree-sitter-tact) (maintained by @novusnota)
- [x] [tcl](https://github.com/tree-sitter-grammars/tree-sitter-tcl) (maintained by @lewis6991)
- [x] [teal](https://github.com/euclidianAce/tree-sitter-teal) (maintained by @euclidianAce)
- [x] [templ](https://github.com/vrischmann/tree-sitter-templ) (maintained by @vrischmann)
- [x] [tera](https://github.com/uncenter/tree-sitter-tera) (maintained by @uncenter)
- [x] [terraform](https://github.com/MichaHoffmann/tree-sitter-hcl) (maintained by @MichaHoffmann)
- [x] [textproto](https://github.com/PorterAtGoogle/tree-sitter-textproto) (maintained by @Porter)
- [x] [thrift](https://github.com/duskmoon314/tree-sitter-thrift) (maintained by @amaanq, @duskmoon314)
- [x] [tiger](https://github.com/ambroisie/tree-sitter-tiger) (maintained by @ambroisie)
- [x] [tlaplus](https://github.com/tlaplus-community/tree-sitter-tlaplus) (maintained by @ahelwer, @susliko)
- [x] [tmux](https://github.com/Freed-Wu/tree-sitter-tmux) (maintained by @Freed-Wu)
- [x] [todotxt](https://github.com/arnarg/tree-sitter-todotxt) (experimental, maintained by @arnarg)
- [x] [toml](https://github.com/tree-sitter-grammars/tree-sitter-toml) (maintained by @tk-shirasaka)
- [x] [tsv](https://github.com/amaanq/tree-sitter-csv) (maintained by @amaanq)
- [x] [tsx](https://github.com/tree-sitter/tree-sitter-typescript) (maintained by @steelsojka)
- [x] [turtle](https://github.com/GordianDziwis/tree-sitter-turtle) (maintained by @GordianDziwis)
- [x] [twig](https://github.com/gbprod/tree-sitter-twig) (maintained by @gbprod)
- [x] [typescript](https://github.com/tree-sitter/tree-sitter-typescript) (maintained by @steelsojka)
- [x] [typespec](https://github.com/happenslol/tree-sitter-typespec) (maintained by @happenslol)
- [x] [typoscript](https://github.com/Teddytrombone/tree-sitter-typoscript) (maintained by @Teddytrombone)
- [x] [typst](https://github.com/uben0/tree-sitter-typst) (maintained by @uben0, @RaafatTurki)
- [x] [udev](https://github.com/ObserverOfTime/tree-sitter-udev) (maintained by @ObserverOfTime)
- [x] [ungrammar](https://github.com/Philipp-M/tree-sitter-ungrammar) (maintained by @Philipp-M, @amaanq)
- [x] [unison](https://github.com/kylegoetz/tree-sitter-unison) (maintained by @tapegram)
- [x] [usd](https://github.com/ColinKennedy/tree-sitter-usd) (maintained by @ColinKennedy)
- [x] [uxn tal](https://github.com/amaanq/tree-sitter-uxntal) (maintained by @amaanq)
- [x] [v](https://github.com/vlang/v-analyzer) (maintained by @kkharji, @amaanq)
- [x] [vala](https://github.com/vala-lang/tree-sitter-vala) (maintained by @Prince781)
- [x] [vento](https://github.com/ventojs/tree-sitter-vento) (maintained by @wrapperup, @oscarotero)
- [x] [verilog](https://github.com/gmlarumbe/tree-sitter-systemverilog) (maintained by @zhangwwpeng)
- [x] [vhdl](https://github.com/jpt13653903/tree-sitter-vhdl) (maintained by @jpt13653903)
- [x] [vhs](https://github.com/charmbracelet/tree-sitter-vhs) (maintained by @caarlos0)
- [x] [vim](https://github.com/neovim/tree-sitter-vim) (maintained by @clason)
- [x] [vimdoc](https://github.com/neovim/tree-sitter-vimdoc) (maintained by @clason)
- [x] [vrl](https://github.com/belltoy/tree-sitter-vrl) (maintained by @belltoy)
- [x] [vue](https://github.com/tree-sitter-grammars/tree-sitter-vue) (maintained by @WhyNotHugo, @lucario387)
- [x] [wgsl](https://github.com/szebniok/tree-sitter-wgsl) (maintained by @szebniok)
- [x] [wgsl_bevy](https://github.com/theHamsta/tree-sitter-wgsl-bevy) (maintained by @theHamsta)
- [x] [wing](https://github.com/winglang/tree-sitter-wing) (maintained by @gshpychka, @MarkMcCulloh)
- [x] [wit](https://github.com/liamwh/tree-sitter-wit) (maintained by @liamwh)
- [x] [xcompose](https://github.com/ObserverOfTime/tree-sitter-xcompose) (maintained by @ObserverOfTime)
- [x] [xml](https://github.com/tree-sitter-grammars/tree-sitter-xml) (maintained by @ObserverOfTime)
- [x] [xresources](https://github.com/ValdezFOmar/tree-sitter-xresources) (maintained by @ValdezFOmar)
- [x] [yaml](https://github.com/tree-sitter-grammars/tree-sitter-yaml) (maintained by @amaanq)
- [x] [yang](https://github.com/Hubro/tree-sitter-yang) (maintained by @Hubro)
- [x] [yuck](https://github.com/Philipp-M/tree-sitter-yuck) (maintained by @Philipp-M, @amaanq)
- [x] [zathurarc](https://github.com/Freed-Wu/tree-sitter-zathurarc) (maintained by @Freed-Wu)
- [x] [zig](https://github.com/tree-sitter-grammars/tree-sitter-zig) (maintained by @amaanq)
- [x] [ziggy](https://github.com/kristoff-it/ziggy) (maintained by @rockorager)
- [x] [ziggy_schema](https://github.com/kristoff-it/ziggy) (maintained by @rockorager)
<!--parserinfo-->

For related information on the supported languages, including related plugins, see [this wiki page](https://github.com/nvim-treesitter/nvim-treesitter/wiki/Supported-Languages-Information).

# Available modules

Modules provide the top-level features of `nvim-treesitter`.
The following is a list of modules included in `nvim-treesitter` and their configuration via `init.lua` (where multiple modules can be combined in a single call to `setup`).
Note that not all modules work for all languages (depending on the queries available for them).
Additional modules can be provided as [external plugins](https://github.com/nvim-treesitter/nvim-treesitter/wiki/Extra-modules-and-plugins).

#### Highlight

Consistent syntax highlighting.

```lua
require'nvim-treesitter.configs'.setup {
  highlight = {
    enable = true,
    -- Setting this to true will run `:h syntax` and tree-sitter at the same time.
    -- Set this to `true` if you depend on 'syntax' being enabled (like for indentation).
    -- Using this option may slow down your editor, and you may see some duplicate highlights.
    -- Instead of true it can also be a list of languages
    additional_vim_regex_highlighting = false,
  },
}
```

To customize the syntax highlighting of a capture, simply define or link a highlight group of the same name:

```lua
-- Highlight the @foo.bar capture group with the "Identifier" highlight group
vim.api.nvim_set_hl(0, "@foo.bar", { link = "Identifier" })
```

For a language-specific highlight, append the name of the language:

```lua
-- Highlight @foo.bar as "Identifier" only in Lua files
vim.api.nvim_set_hl(0, "@foo.bar.lua", { link = "Identifier" })
```

See `:h treesitter-highlight-groups` for details.

#### Incremental selection

Incremental selection based on the named nodes from the grammar.

```lua
require'nvim-treesitter.configs'.setup {
  incremental_selection = {
    enable = true,
    keymaps = {
      init_selection = "gnn", -- set to `false` to disable one of the mappings
      node_incremental = "grn",
      scope_incremental = "grc",
      node_decremental = "grm",
    },
  },
}
```

#### Indentation

Indentation based on treesitter for the `=` operator.
**NOTE: This is an experimental feature**.

```lua
require'nvim-treesitter.configs'.setup {
  indent = {
    enable = true
  }
}
```

#### Folding

Tree-sitter based folding (implemented in Neovim itself, see `:h vim.treesitter.foldexpr()`). To enable it for the current window, set

```lua
vim.wo.foldmethod = 'expr'
vim.wo.foldexpr = 'v:lua.vim.treesitter.foldexpr()'
```

This will respect your `foldminlines` and `foldnestmax` settings.

# Advanced setup

## Changing the parser install directory

If you want to install the parsers to a custom directory you can specify this
directory with `parser_install_dir` option in that is passed to `setup`.
`nvim-treesitter` will then install the parser files into this directory.

This directory must be writeable and must be explicitly prepended to the
`runtimepath`. For example:

```lua
  -- It MUST be at the beginning of runtimepath. Otherwise the parsers from Neovim itself
  -- is loaded that may not be compatible with the queries from the 'nvim-treesitter' plugin.
  vim.opt.runtimepath:prepend("/some/path/to/store/parsers")

  require'nvim-treesitter.configs'.setup {
    parser_install_dir = "/some/path/to/store/parsers",

    ...

  }
```

If this option is not included in the setup options, or is explicitly set to
`nil` then the default install directories will be used. If this value is set
the default directories will be ignored.

Bear in mind that any parser installed into a parser folder on the runtime path
will still be considered installed. (For example if
"~/.local/share/nvim/site/parser/c.so" exists then the "c" parser will be
considered installed, even though it is not in `parser_install_dir`)

The default paths are:

1. first the package folder. Where `nvim-treesitter` is installed.
2. second the site directory. This is the "site" subdirectory of `stdpath("data")`.

## Adding parsers

If you have a parser that is not on the list of supported languages (either as a repository on Github or in a local directory), you can add it manually for use by `nvim-treesitter` as follows:

1. Clone the repository or [create a new project](https://tree-sitter.github.io/tree-sitter/creating-parsers#project-setup) in, say, `~/projects/tree-sitter-zimbu`. Make sure that the `tree-sitter-cli` executable is installed and in your path; see <https://tree-sitter.github.io/tree-sitter/creating-parsers#installation> for installation instructions.
2. Run `tree-sitter generate` in this directory (followed by `tree-sitter test` for good measure).
3. Add the following snippet to your `init.lua`:

```lua
local parser_config = require "nvim-treesitter.parsers".get_parser_configs()
parser_config.zimbu = {
  install_info = {
    url = "~/projects/tree-sitter-zimbu", -- local path or git repo
    files = {"src/parser.c"}, -- note that some parsers also require src/scanner.c or src/scanner.cc
    -- optional entries:
    branch = "main", -- default branch in case of git repo if different from master
    generate_requires_npm = false, -- if stand-alone parser without npm dependencies
    requires_generate_from_grammar = false, -- if folder contains pre-generated src/parser.c
  },
  filetype = "zu", -- if filetype does not match the parser name
}
```

If you wish to set a specific parser for a filetype, you should use `vim.treesitter.language.register()`:

```lua
vim.treesitter.language.register('python', 'someft')  -- the someft filetype will use the python parser and queries.
```

Note this requires Nvim v0.9.

4. Start `nvim` and `:TSInstall zimbu`.

You can also skip step 2 and use `:TSInstallFromGrammar zimbu` to install directly from a `grammar.js` in the top-level directory specified by `url`.
Once the parser is installed, you can update it (from the latest revision of the `main` branch if `url` is a Github repository) with `:TSUpdate zimbu`.

Note that neither `:TSInstall` nor `:TSInstallFromGrammar` copy query files from the grammar repository.
If you want your installed grammar to be useful, you must manually [add query files](#adding-queries) to your local nvim-treesitter installation.
Note also that module functionality is only triggered if your language's filetype is correctly identified.
If Neovim does not detect your language's filetype by default, you can use [Neovim's `vim.filetype.add()`](<https://neovim.io/doc/user/lua.html#vim.filetype.add()>) to add a custom detection rule.

If you use a git repository for your parser and want to use a specific version, you can set the `revision` key
in the `install_info` table for you parser config.

## Adding queries

Queries are what `nvim-treesitter` uses to extract information from the syntax tree;
they are located in the `queries/{language}/*` runtime directories (see `:h rtp`),
like the `queries` folder of this plugin, e.g. `queries/{language}/{locals,highlights,textobjects}.scm`.
Other modules may require additional queries such as `folding.scm`. You can find a
list of all supported capture names in [CONTRIBUTING.md](https://github.com/nvim-treesitter/nvim-treesitter/blob/master/CONTRIBUTING.md#parser-configurations).

The first query file on `runtimepath` will be used (see `:h treesitter-query`).
If you want to make a query on the user config extend other queries instead of
replacing them, see `:h treesitter-query-modeline-extends`.

If you want to completely override a query, you can use `:h vim.treesitter.query.set()`.
For example, to override the `injections` queries from `c` with your own:

```lua
vim.treesitter.query.set("c", "injections", "(comment) @comment")
```

Note: when using `query.set()`, all queries in the runtime directories will be ignored.

## Adding modules

If you wish you write your own module, you need to support

- tree-sitter language detection support;
- attaching and detaching to buffers;
- all nvim-treesitter commands.

At the top level, you can use the `define_modules` function to define one or more modules or module groups:

```lua
require'nvim-treesitter'.define_modules {
  my_cool_plugin = {
    attach = function(bufnr, lang)
      -- Do cool stuff here
    end,
    detach = function(bufnr)
      -- Undo cool stuff here
    end,
    is_supported = function(lang)
      -- Check if the language is supported
    end
  }
}
```

with the following properties:

- `module_path` specifies a require path (string) that exports a module with an `attach` and `detach` function. This is not required if the functions are on this definition.
- `enable` determines if the module is enabled by default. This is usually overridden by the user.
- `disable` takes a list of languages that this module is disabled for. This is usually overridden by the user.
- `is_supported` takes a function that takes a language and determines if this module supports that language.
- `attach` takes a function that attaches to a buffer. This is required if `module_path` is not provided.
- `detach` takes a function that detaches from a buffer. This is required if `module_path` is not provided.

# Extra features

### Statusline indicator

```vim
echo nvim_treesitter#statusline(90)  " 90 can be any length
module->expression_statement->call->identifier
```

### Utilities

You can get some utility functions with

```lua
local ts_utils = require 'nvim-treesitter.ts_utils'
```

Check [`:h nvim-treesitter-utils`](doc/nvim-treesitter.txt) for more information.

# Troubleshooting

Before doing anything, make sure you have the latest version of this plugin and run `:checkhealth nvim-treesitter`.
It can also help to update the parsers via `:TSUpdate`.

#### Feature `X` does not work for `{language}`...

First, check the `health#nvim_treesitter#check` and the `health#treesitter#check` sections of `:checkhealth` for any warning.
If there is one, it's highly likely that this is the cause of the problem.

Next check the `## Parser/Features` subsection of the `health#nvim_treesitter#check` section of `:checkhealth` to ensure the desired module is enabled for your language.
If not, you might be missing query files; see [Adding queries](#adding-queries).

Finally, ensure Neovim is correctly identifying your language's filetype using the `:echo &filetype` command while one of your language's files is open in Neovim.
If not, add a short Vimscript file to nvim-treesitter's `ftdetect` runtime directory following [Neovim's documentation](https://neovim.io/doc/user/filetype.html#new-filetype) on filetype detection.
You can also quickly & temporarily set the filetype for a single buffer with the `:set filetype=langname` command to test whether it fixes the problem.

If everything is okay, then it might be an actual error.
In that case, feel free to [open an issue here](https://github.com/nvim-treesitter/nvim-treesitter/issues/new/choose).

#### I get `module 'vim.treesitter.query' not found`

Make sure you have the latest version of Neovim.

#### I get `Error detected while processing .../plugin/nvim-treesitter.vim` every time I open Neovim

This is probably due to a change in a parser's grammar or its queries.
Try updating the parser that you suspect has changed (`:TSUpdate {language}`) or all of them (`:TSUpdate`).
If the error persists after updating all parsers,
please [open an issue](https://github.com/nvim-treesitter/nvim-treesitter/issues/new/choose).

#### I get `query error: invalid node type at position`

This could be due a query file outside this plugin using outdated nodes,
or due to an outdated parser.

- Make sure you have the parsers up to date with `:TSUpdate`
- Make sure you don't have more than one `parser` runtime directory.
  You can execute this command `:echo nvim_get_runtime_file('parser', v:true)` to find all runtime directories.
  If you get more than one path, remove the ones that are outside this plugin (`nvim-treesitter` directory),
  so the correct version of the parser is used.

#### I experience weird highlighting issues similar to [#78](https://github.com/nvim-treesitter/nvim-treesitter/issues/78)

This is a well known issue, which arises when the tree and the buffer have gotten out of sync.
As this is an upstream issue, we don't have any definite fix.
To get around this, you can force reparsing the buffer with

```vim
:write | edit | TSBufEnable highlight
```

This will save, restore and enable highlighting for the current buffer.

#### I experience bugs when using `nvim-treesitter`'s `foldexpr` similar to [#194](https://github.com/nvim-treesitter/nvim-treesitter/issues/194)

This might happen, and is known to happen, with `vim-clap`.
To avoid these kind of errors, please use `setlocal` instead of `set` for the respective filetypes.

#### I run into errors like `module 'nvim-treesitter.configs' not found` at startup

This is because of `rtp` management in `nvim`, adding `packadd
nvim-treesitter` should fix the issue.

#### I want to use Git instead of curl for downloading the parsers

In your Lua config:

```lua
require("nvim-treesitter.install").prefer_git = true
```

#### I want to use a HTTP proxy for downloading the parsers

You can either configure curl to use additional CLI arguments in your Lua config:

```lua
require("nvim-treesitter.install").command_extra_args = {
    curl = { "--proxy", "<proxy url>" },
}
```

or you can configure git via `.gitconfig` and use git instead of curl

```lua
require("nvim-treesitter.install").prefer_git = true
```

#### I want to use a mirror instead of "https://github.com/"

In your Lua config:

```lua
for _, config in pairs(require("nvim-treesitter.parsers").get_parser_configs()) do
  config.install_info.url = config.install_info.url:gsub("https://github.com/", "something else")
end

require'nvim-treesitter.configs'.setup {
    --
    --
}
```

#### Using an existing parser for another filetype

For example, to use the `bash` tree-sitter to highlight file with
`filetype=apkbuild`, use:

```lua
vim.treesitter.language.register("bash", "apkbuild")
```

The `bash` tree-sitter must be installed following the usual procedure [as
described above](#language-parsers).
