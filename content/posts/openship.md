---
title: openship
date: 2026-07-21T14:28:48+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1784146929766-3d69334d602d?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3ODQ2MTUyMDV8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1784146929766-3d69334d602d?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3ODQ2MTUyMDV8&ixlib=rb-4.1.0
---

# [oblien/openship](https://github.com/oblien/openship)

<h1 align="center">Openship</h1>

<p align="center">
  Open-source, self-hostable deployment platform with built-in CI/CD.<br>
  Push code, ship containers, manage infrastructure — from a desktop app, web dashboard, or CLI.
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/openship"><img src="https://img.shields.io/npm/v/openship?color=0b7285&label=npm" alt="npm version" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue" alt="License" /></a>
  <a href="https://openship.io"><img src="https://img.shields.io/badge/website-openship.io-0b7285" alt="Website" /></a>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> ·
  <a href="#features">Features</a> ·
  <a href="#three-interfaces">Interfaces</a> ·
  <a href="https://openship.io/docs">Docs</a> ·
  <a href="CONTRIBUTING.md">Contributing</a>
</p>

<p align="center">
  <a href="README.md"><img src="https://img.shields.io/badge/lang-English-0b7285" alt="English" /></a>
  <a href="docs/i18n/README.ar.md"><img src="https://img.shields.io/badge/lang-العربية-555" alt="العربية" /></a>
  <a href="docs/i18n/README.zh.md"><img src="https://img.shields.io/badge/lang-简体中文-555" alt="简体中文" /></a>
  <a href="docs/i18n/README.es.md"><img src="https://img.shields.io/badge/lang-Español-555" alt="Español" /></a>
  <a href="docs/i18n/README.fr.md"><img src="https://img.shields.io/badge/lang-Français-555" alt="Français" /></a>
  <a href="docs/i18n/README.ja.md"><img src="https://img.shields.io/badge/lang-日本語-555" alt="日本語" /></a>
  <a href="docs/i18n/README.pt.md"><img src="https://img.shields.io/badge/lang-Português-555" alt="Português" /></a>
  <a href="docs/i18n/README.de.md"><img src="https://img.shields.io/badge/lang-Deutsch-555" alt="Deutsch" /></a>
</p>

<p align="center">
  <img src="docs/screenshots/screen.png" alt="Openship dashboard" width="800" />
</p>

---

## Quick Start

```bash
npm i -g openship     # or: curl -fsSL https://get.openship.io | sh
openship up           # installs Openship as a background service (starts on boot, auto-restarts)
```

`openship open` opens the dashboard; `openship stop` stops the service. Want a one-off attached run instead? `openship up --foreground`. To deploy a project:

```bash
cd your-project
openship init         # link this directory to a project
openship deploy
```

Prefer Docker? Clone the repo and use the compose stack:

```bash
git clone https://github.com/oblien/openship.git && cd openship
cp .env.example .env
docker compose up -d
```

Or grab the desktop app (`openship install`, or download from [openship.io](https://openship.io)).

---

## What It Does

Point it at a repo. Openship detects your stack, builds it, configures everything, and ships it — zero config files, zero pipelines, zero YAML.

Databases, domains, SSL, CDN, mail, backups — all managed from one place.

Works with **Openship Cloud** (managed) or **any Linux server** you own. Solo devs shipping side projects and teams running production use the same tool.

---

## Features

| | |
|---|---|
| **Built-in CI/CD** | Push-to-deploy, preview environments, staging/prod flows, rollbacks |
| **Any stack** | Node, Python, Go, Rust, PHP, Ruby, Java, .NET, Docker, monorepos |
| **Full backend** | Postgres, MySQL, MongoDB, Redis, workers, WebSockets, storage |
| **Domains & SSL** | Automatic Let's Encrypt, wildcards, unlimited domains, auto-renewal |
| **CDN** | Edge caching, HTTP/3, Brotli compression, instant purge |
| **Mail server** | Built-in SMTP with DKIM/SPF/DMARC — no Mailgun or SES needed |
| **Backups** | Scheduled, databases + volumes, one-click restore, export anytime |
| **Real-time monitoring** | Live build logs, container metrics, and resource usage streamed to your screen |
| **Scaling** | Auto-scaling on cloud, multi-node ready on self-hosted |
| **Portability** | Standard Docker containers — move between providers freely |
| **Docker Compose** | Deploy existing compose files as-is |

---

## Deploy Anywhere

- **Openship Cloud** — managed, auto-scaling, zero setup
- **Any VPS** — Hetzner, DigitalOcean, Linode, OVH, and the rest
- **Dedicated servers** — bare metal, colo, homelab
- **Multi-server** — spread workloads across machines

Same interface regardless of where you deploy.

---

## Three Interfaces

- **Desktop app** — full GUI, real-time logs, one-click everything.
- **Web dashboard** — the same UI in the browser, built for teams.
- **CLI** — scriptable and CI-friendly.

A **REST API** and **MCP** (AI agent protocol) round it out for automation and tooling integration. Full command and API reference at [openship.io/docs](https://openship.io/docs).

> [!NOTE]
> The docs are still a work in progress — we're actively filling them out. If something's missing or unclear, [contributions](CONTRIBUTING.md) are hugely welcome and help us get there faster.

---

## Status

Production-ready core, actively developed.

**Coming next:** multi-node clusters, load-balancing UI, private networking, advanced monitoring, and visual CI/CD pipelines.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Releasing

Cut a release with the version script — it syncs every package's version,
commits the bump, tags `vX.Y.Z`, and pushes:

```bash
bun scripts/release.ts 0.2.0        # explicit version
# or a bump keyword: patch | minor | major | rc   (minor from 0.1.x → 0.2.0)
```

Pushing the tag triggers [`.github/workflows/release.yml`](.github/workflows/release.yml), which:

- builds the **macOS / Windows / Linux installers** and the server tarballs (with SHA-256 sidecars),
- **publishes the `openship` CLI to npm** — via npm [OIDC trusted publishing](https://docs.npmjs.com/trusted-publishers) (no token), and
- creates the **GitHub Release** with the built assets (notes come from the tag).

To flag a release as **critical** (or add recommended/info advisories) in the
in-app updater, add an entry to [`release-advisories.json`](release-advisories.json)
**before** tagging — clients pull it pinned to the release tag. High-level notes
live in [`CHANGELOG.md`](CHANGELOG.md).

---

## Security

Found a vulnerability? We welcome your report — please disclose it **privately**,
never in a public issue, PR, or discussion.

- **Report it here (preferred):** [Report a vulnerability](https://github.com/oblien/openship/security/advisories/new) — a private GitHub advisory, visible only to you and the maintainers.
- Scope, what to include, and our response/disclosure process: [SECURITY.md](SECURITY.md).

Good-faith security research is **authorized** under our
[safe-harbor policy](SECURITY.md#safe-harbor), and we're happy to credit valid
first reports.

---

## License

Openship is **open-source** software, licensed under the [Apache License 2.0](LICENSE).

You may use, run, modify, self-host, and distribute it — including in commercial
and closed-source products — under the terms of the Apache 2.0 license. See
[LICENSE](LICENSE) for the full text.
