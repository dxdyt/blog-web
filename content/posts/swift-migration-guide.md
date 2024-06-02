---
title: swift-migration-guide
date: 2024-06-02T12:17:32+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1714911463721-193701866e58?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTczMDE3Mjh8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1714911463721-193701866e58?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTczMDE3Mjh8&ixlib=rb-4.0.3
---

# [apple/swift-migration-guide](https://github.com/apple/swift-migration-guide)

# The Swift Concurrency Migration Guide

This repository contains the source for *The Swift Concurrency Migration Guide*,
which is built using [Swift-DocC][docc].

## Contributing

See [the contributing guide][contributing] for instructions on contributing
to the Swift Migration Guide.

## Building

Run `docc preview Guide.docc` in this repository's root directory.

After running DocC,
open the link that `docc` outputs to display a local preview in your browser.

> Note:
>
> If you installed DocC by downloading a toolchain from Swift.org,
> `docc` is located in `usr/bin/`,
> relative to the installation path of the toolchain.
> Make sure your shell's `PATH` environment variable
> includes that directory.
>
> If you installed DocC by downloading Xcode,
> use `xcrun docc` instead.

[contributing]: https://github.com/apple/swift-migration-guide/CONTRIBUTING.md
[docc]: https://github.com/apple/swift-docc
[conduct]: https://www.swift.org/code-of-conduct