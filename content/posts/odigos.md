---
title: odigos
date: 2023-11-01T12:17:58+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1697301453753-19514aeb0199?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTg4MTIxMDl8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1697301453753-19514aeb0199?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTg4MTIxMDl8&ixlib=rb-4.0.3
---

# [keyval-dev/odigos](https://github.com/keyval-dev/odigos)

<p align="center">
    <a href="https://github.com/keyval-dev/odigos/actions/workflows/main.yml" target="_blank">
        <img src="https://github.com/keyval-dev/odigos/actions/workflows/main.yml/badge.svg" alt="GitHub Actions Workflow Status" style="margin-right: 10px; border: 1px solid #007acc; border-radius: 4px; padding: 5px;">
    </a>
    <a href="https://goreportcard.com/report/github.com/keyval-dev/odigos/cli" target="_blank">
        <img src="https://goreportcard.com/badge/github.com/keyval-dev/odigos/cli" alt="Go Report Card" style="margin-right: 10px; border: 1px solid #4CAF50; border-radius: 4px; padding: 5px;">
    </a>
    <a href="https://godoc.org/github.com/keyval-dev/odigos/cli" target="_blank">
        <img src="https://godoc.org/github.com/keyval-dev/odigos/cli?status.svg" alt="GoDoc" style="border: 1px solid #f39c12; border-radius: 4px; padding: 5px;">
    </a>
</p>


<p align="center">
<img src="assets/logo.png" width="350" /></br>
Generate distributed traces for any application without code changes.
</p>

<h2 align="center">
    <a href="https://www.youtube.com/watch?v=nynyV7FC4VI">Demo Video</a> • <a href="https://docs.odigos.io">Documentation</a> • <a href="https://join.slack.com/t/odigos/shared_invite/zt-1d7egaz29-Rwv2T8kyzc3mWP8qKobz~A">Join Slack Community</a>
</h2>

Odigos uses OpenTelemetry and eBPF to automatically build agnostic observability pipelines for all application in a k8s cluster with no code changes.

### ✨ Language Agnostic Auto-instrumentation

Odigos supports any application written in Java, Python, .NET, Node.js, and **Go**.  
Historically, compiled languages like Go have been difficult to instrument without code changes. Odigos solves this problem by uniquely leveraging [eBPF](https://ebpf.io).

![Works on any application](assets/choose_apps.png)


### 🤝 Keep your existing observability tools
Odigos currently supports all the popular managed and open source destinations.  
By producing data in the [OpenTelemetry](https://opentelemetry.io) format, Odigos can be used with any observability tool that supports OTLP.

For a complete list of supported destinations, see [here](#supported-destinations).

![Works with any observability tool](assets/choose_dest.png)

### 🎛️ Collectors Management 
Odigos automatically scales OpenTelemetry collectors based on observability data volume.  
Manage and configure collectors via a convenient web UI.

![Collectors Management](assets/overview_page.png)

## Installation

Installing Odigos takes less than 5 minutes and requires no code changes.
Download our [CLI](https://docs.odigos.io/installation) and run the following command:


```bash
odigos install
```

For more details, see our [quickstart guide](https://docs.odigos.io/intro).

## Supported Destinations

**For step by step instructions detailed for every destination, see these [docs](https://docs.odigos.io/backends).**

### Managed

|                         | Traces | Metrics | Logs |
|-------------------------| ------ | ------- |------|
| New Relic               | ✅      | ✅      | ✅    |
| Datadog                 | ✅      | ✅      | ✅    |
| Grafana Cloud           | ✅      | ✅      | ✅    |
| Honeycomb               | ✅      | ✅      | ✅    |
| Chronosphere            | ✅      | ✅      |       |
| Logz.io                 | ✅      | ✅      | ✅    |
| qryn.cloud              | ✅      | ✅      | ✅    |
| OpsVerse                | ✅      | ✅      | ✅    |
| Dynatrace               | ✅      | ✅      | ✅    |
| Google Cloud Monitoring | ✅      |         | ✅    |
| Google Cloud Storage    | ✅      |         | ✅    |
| Azure Blob Storage      | ✅      |         | ✅    |
| AWS S3                  | ✅      |         | ✅    |
| Splunk                  | ✅      |         |      |
| Lightstep               | ✅      |         |      |
| Sentry                  | ✅      |         |      |
| Axiom                   | ✅      |         | ✅   |

### Open Source

|               | Traces | Metrics | Logs |
| ------------- | ------ | ------- | ---- |
| Prometheus    |        | ✅      |      |
| Tempo         | ✅     |         |      |
| Loki          |        |         | ✅   |
| Jaeger        | ✅     |         |      |
| SigNoz        | ✅     | ✅      | ✅   |
| qryn          | ✅     | ✅      | ✅   |
| Elasticsearch | ✅     |         | ✅   |

Can't find the destination you need? Help us by following our quick [add new destination](https://docs.odigos.io/adding-new-dest) guide and submitting a PR.

## Contributing

Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for information about how to get involved. We welcome issues, questions, and pull requests. You are welcome to join our active [Slack Community](https://join.slack.com/t/odigos/shared_invite/zt-1d7egaz29-Rwv2T8kyzc3mWP8qKobz~A).

## All Thanks To Our Contributors

<a href="https://github.com/keyval-dev/odigos/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=keyval-dev/odigos" />
</a>

## License

This project is licensed under the terms of the Apache 2.0 open source license. Please refer to [LICENSE](LICENSE) for the full terms.
