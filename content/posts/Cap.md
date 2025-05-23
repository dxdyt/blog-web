---
title: Cap
date: 2025-05-07T12:22:44+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1745594151309-6c7d9172c7c3?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDY1OTE2NjN8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1745594151309-6c7d9172c7c3?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDY1OTE2NjN8&ixlib=rb-4.1.0
---

# [CapSoftware/Cap](https://github.com/CapSoftware/Cap)

<p align="center">
  <p align="center">
   <img width="150" height="150" src="https://github.com/CapSoftware/Cap/blob/main/apps/desktop/src-tauri/icons/Square310x310Logo.png" alt="Logo">
  </p>
	<h1 align="center"><b>Cap</b></h1>
	<p align="center">
		The open source Loom alternative.
    <br />
    <a href="https://cap.so"><strong>Cap.so »</strong></a>
    <br />
    <br />
    <b>Downloads for </b>
		<a href="https://cap.so/download">macOS & Windows</a>
    <br />
  </p>
</p>
<br/>

[![Open Bounties](https://img.shields.io/endpoint?url=https%3A%2F%2Fconsole.algora.io%2Fapi%2Fshields%2FCapSoftware%2Fbounties%3Fstatus%3Dopen)](https://console.algora.io/org/CapSoftware/bounties?status=open)

Cap is the open source alternative to Loom. It's a video messaging tool that allows you to record, edit and share videos in seconds.

<img src="https://raw.githubusercontent.com/CapSoftware/Cap/refs/heads/main/apps/web/public/landing-cover.png"/>

# Cap Self Hosting *(Updated May 2025)*

Self-hosting deployment options for Cap are currently being worked on. This includes a [Dockerfile](https://github.com/CapSoftware/Cap/blob/main/Dockerfile) and also [one-click deployment via Railway](https://railway.com/template/PwpGcf). Documentation on how to deploy will be released as soon as we make the Dockerfile and Railway deployment template stable. You will be able to take your self hosted URL and paste directly into the desktop app for direct, instant use.

Join the <a href="https://discord.gg/y8gdQ3WRN3">Cap Discord</a> if you want to help contribute to this particular project.

# Monorepo App Architecture

We use a combination of Rust, React (Next.js), TypeScript, Tauri, Drizzle (ORM), MySQL, TailwindCSS throughout this Turborepo powered monorepo.

### Apps:

- `desktop`: A [Tauri](https://tauri.app) (Rust) app, using [SolidStart](https://start.solidjs.com) on the frontend.
- `web`: A [Next.js](https://nextjs.org) web app.

### Packages:

- `ui`: A [React](https://reactjs.org) Shared component library.
- `utils`: A [React](https://reactjs.org) Shared utility library.
- `tsconfig`: Shared `tsconfig` configurations used throughout the monorepo.
- `database`: A [React](https://reactjs.org) and [Drizzle ORM](https://orm.drizzle.team/) Shared database library.
- `config`: `eslint` configurations (includes `eslint-config-next`, `eslint-config-prettier` other configs used throughout the monorepo).

# Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for more information. This guide is a work in progress, and is updated regularly as the app matures.
