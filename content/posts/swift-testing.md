---
title: swift-testing
date: 2023-09-24T12:14:50+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1694857936498-4a94ffcafb6c?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTU1Mjg4MzZ8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1694857936498-4a94ffcafb6c?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTU1Mjg4MzZ8&ixlib=rb-4.0.3
---

# [apple/swift-testing](https://github.com/apple/swift-testing)

# `swift-testing`

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2023 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for Swift project authors
-->

`swift-testing` is a modern, open-source testing library for Swift with powerful
and expressive capabilities. It gives developers more confidence with less code.

> [!IMPORTANT]
> This package is under active, ongoing development. Its contents, including all
> interfaces and implementation details, are experimental and are subject to
> change or removal without notice.
>
> We welcome feedback and ideas from the Swift community. Please join us in the
> [Swift forums](https://forums.swift.org/c/related-projects/swift-testing)
> and let us know what you think!

## Feature overview

### Flexible test organization

Define test functions almost anywhere with a single attribute and group related
tests into hierarchies using Swift's type system.

### Customizable metadata

Dynamically enable or disable tests depending on runtime conditions, categorize
tests using tags, and associate bugs directly with the tests that verify their
fixes or reproduce their problems.

### Scalable execution

Automatically parallelize tests in-process, integrate seamlessly with Swift
concurrency, and parameterize test functions across wide ranges of inputs.

## Supported platforms

The table below describes the current level of support that `swift-testing` has
for various platforms:

| **Platform** | **Status** |
|---|---|
| **macOS** | Supported |
| **iOS** | Supported |
| **watchOS** | Supported |
| **tvOS** | Supported |
| **Ubuntu 22.04** | Supported |
| **Windows** | Pending support for macros |

## Getting started

`swift-testing` is under active development. We are working to integrate it with
the rest of the Swift ecosystem, but you can try it out today by following the
steps in our [Getting Started](Sources/Testing/Testing.docc/TemporaryGettingStarted.md)
article.
