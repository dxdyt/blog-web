---
title: datadog-agent
date: 2025-10-17T12:23:39+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1756232973381-5ed87773a908?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NjA2NzQ4OTd8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1756232973381-5ed87773a908?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NjA2NzQ4OTd8&ixlib=rb-4.1.0
---

# [DataDog/datadog-agent](https://github.com/DataDog/datadog-agent)

# Datadog Agent

![GitHub Release](https://img.shields.io/github/v/release/DataDog/datadog-agent?style=flat&logo=datadog&logoColor=%23632CA6&labelColor=%23FFF&color=%23632CA6)
[![Coverage status](https://codecov.io/github/DataDog/datadog-agent/coverage.svg?branch=main)](https://codecov.io/github/DataDog/datadog-agent?branch=main)
[![GoDoc](https://godoc.org/github.com/DataDog/datadog-agent?status.svg)](https://godoc.org/github.com/DataDog/datadog-agent)

This repository contains the source code of the Datadog Agent version 7 and version 6. Please refer to the [Agent user documentation](https://docs.datadoghq.com/agent/) for information about differences between Agent v5, Agent v6 and Agent v7. Additionally, we provide a list of prepackaged binaries for an easy install process [here](https://app.datadoghq.com/fleet/install-agent/latest?platform=overview).

## Documentation

The [developer docs site](https://datadoghq.dev/datadog-agent/setup/) contains information about how to develop the Datadog Agent itself.

The source of the content is located under [the docs directory](docs) and may contain pages that are not yet published.

## Contributing code

You'll find information and help on how to contribute code to this project under
[the `docs/dev` directory](docs/dev) of the present repo.

## License

The Datadog Agent user space components are licensed under the
[Apache License, Version 2.0](LICENSE). The BPF code is licensed
under the [General Public License, Version 2.0](pkg/ebpf/c/COPYING).
