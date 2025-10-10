---
title: winboat
date: 2025-10-10T12:21:45+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1742410938424-109762e50b55?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NjAwNzAwNjh8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1742410938424-109762e50b55?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NjAwNzAwNjh8&ixlib=rb-4.1.0
---

# [TibixDev/winboat](https://github.com/TibixDev/winboat)

<div align="left">
  <table>
    <tr>
      <td>
        <img src="gh-assets/winboat_logo.svg" alt="WinBoat Logo" width="150">
      </td>
      <td>
        <h1 style="color: #7C86FF; margin: 0; font-size: 32px;">WinBoat</h1>
        <p style="color: oklch(90% 0 0); font-size: 14px; margin: 5px 0;">Windows for Penguins.<br>
        Run Windows apps on 🐧 Linux with ✨ seamless integration</p>
      </td>
    </tr>
  </table>
</div>

## Screenshots
<div align="center">
  <img src="gh-assets/features/feat_dash.png" alt="WinBoat Dashboard" width="45%">
  <img src="gh-assets/features/feat_apps.png" alt="WinBoat Apps" width="45%">
  <img src="gh-assets/features/feat_native.png" alt="Native Windows" width="45%">
</div>

## ⚠️ Work in Progress ⚠️
WinBoat is currently in beta, so expect to occasionally run into hiccups and bugs. You should be comfortable with some level of troubleshooting if you decide to try it, however we encourage you to give it a shot anyway.

## Features
- **🎨 Elegant Interface**: Sleek and intuitive interface that seamlessly integrates Windows into your Linux desktop environment, making it feel like a native experience
- **📦 Automated Installs**: Simple installation process through our interface - pick your preferences & specs and let us handle the rest
- **🚀 Run Any App**: If it runs on Windows, it can run on WinBoat. Enjoy the full range of Windows applications as native OS-level windows in your Linux environment
- **🖥️ Full Windows Desktop**: Access the complete Windows desktop experience when you need it, or run individual apps seamlessly integrated into your Linux workflow
- **📁 Filesystem Integration**: Your home directory is mounted in Windows, allowing easy file sharing between the two systems without any hassle
- **✨ And many more**: Smartcard passthrough, resource monitoring, and more features being added regularly

## How Does It Work?
WinBoat is an Electron app which allows you to run Windows apps on Linux using a containerized approach. Windows runs as a VM inside a Docker container, we communicate with it using the [WinBoat Guest Server](https://github.com/TibixDev/winboat/tree/main/guest_server) to retrieve data we need from Windows. For compositing applications as native OS-level windows, we use FreeRDP together with Windows's RemoteApp protocol.

## Prerequisites
Before running WinBoat, ensure your system meets the following requirements:

- **RAM**: At least 4 GB of RAM
- **CPU**: At least 2 CPU threads  
- **Storage**: At least 32 GB free space in `/var`
- **Virtualization**: KVM enabled in BIOS/UEFI
  - [How to enable virtualization](https://duckduckgo.com/?t=h_&q=how+to+enable+virtualization+in+%3Cmotherboard+brand%3E+bios&ia=web)
- **Docker**: Required for containerization
  - [Installation Guide](https://docs.docker.com/engine/install/)
  - **⚠️ NOTE:** Docker Desktop is **not** supported, you will run into issues if you use it
- **Docker Compose v2**: Required for compatibility with docker-compose.yml files
  - [Installation Guide](https://docs.docker.com/compose/install/#plugin-linux-only)
- **Docker User Group**: Add your user to the `docker` group
  - [Setup Instructions](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)
- **FreeRDP**: Required for remote desktop connection (Please make sure you have **Version 3.x.x** with sound support included)
  - [Installation Guide](https://github.com/FreeRDP/FreeRDP/wiki/PreBuilds)
- [OPTIONAL] **Kernel Modules**: The `iptables` / `nftables` and `iptable_nat` kernel modules can be loaded for network autodiscovery and better shared filesystem performance, but this is not obligatory in newer versions of WinBoat
  - [Module loading instructions](https://rentry.org/rmfq2e5e)

## Downloading
You can download the latest Linux builds under the [Releases](https://github.com/TibixDev/winboat/releases) tab. We currently offer four variants:
- **AppImage:** A popular & portable app format which should run fine on most distributions
- **Unpacked:** The raw unpacked files, simply run the executable (`linux-unpacked/winboat`)
- **.deb:** The intended format for Debian based distributions
- **.rpm:** The intended format for Fedora based distributions

## Known Issues About Container Runtimes
- Podman is **unsupported** for now
- Docker Desktop is **unsupported** for now
- Distros that emulate Docker through a Podman socket are **unsupported**
- Any rootless containerization solution is currently **unsupported**

## Building WinBoat
- For building you need to have NodeJS and Go installed on your system
- Clone the repo (`git clone https://github.com/TibixDev/WinBoat`)
- Install the dependencies (`npm i`)
- Build the app and the guest server using `npm run build:linux-gs`
- You can now find the built app under `dist` with an AppImage and an Unpacked variant

## Running WinBoat in development mode
- Make sure you meet the [prerequisites](#prerequisites)
- Additionally, for development you need to have NodeJS and Go installed on your system
- Clone the repo (`git clone https://github.com/TibixDev/WinBoat`)
- Install the dependencies (`npm i`)
- Build the guest server (`npm run build-guest-server`)
- Run the app (`npm run dev`)

## Contributing
Contributions are welcome! Whether it's bug fixes, feature improvements, or documentation updates, we appreciate your help making WinBoat better.

**Please note**: We maintain a focus on technical contributions only. Pull requests containing political/sexual content, or other sensitive/controversial topics will not be accepted. Let's keep things focused on making great software! 🚀

Feel free to:
- Report bugs and issues
- Submit feature requests  
- Contribute code improvements
- Help with documentation
- Share feedback and suggestions

Check out our issues page to get started, or feel free to open a new issue if you've found something that needs attention.

## License
WinBoat is licensed under the [MIT](https://github.com/TibixDev/winboat/blob/main/LICENSE) license

## Inspiration / Alternatives
These past few years some cool projects have surfaced with similar concepts, some of which we've also taken inspirations from.\
They're awesome and you should check them out:
- [WinApps](https://github.com/winapps-org/winapps)
- [Cassowary](https://github.com/casualsnek/cassowary)
- [dockur/windows](https://github.com/dockur/windows) (🌟 Also used in WinBoat)

## Socials & Contact
- [![Website](https://img.shields.io/badge/Website-winboat.app-blue?style=flat&logo=googlechrome&logoColor=white)](https://www.winboat.app/)
- [![Twitter](https://img.shields.io/badge/Twitter-@winboat__app-1DA1F2?style=flat&logo=x&logoColor=white)](https://x.com/winboat_app)
- [![Mastodon](https://img.shields.io/badge/Mastodon-@winboat-6364FF?style=flat&logo=mastodon&logoColor=white)](https://fosstodon.org/@winboat)
- [![Bluesky](https://img.shields.io/badge/Bluesky-winboat.app-00A8E8?style=flat&logo=bluesky&logoColor=white)](http://bsky.app/profile/winboat.app)
- [![Discord](https://img.shields.io/badge/Discord-Join_Community-5865F2?style=flat&logo=discord&logoColor=white)](http://discord.gg/MEwmpWm4tN)
- [![Email](https://img.shields.io/badge/Email-staff@winboat.app-D14836?style=flat&logo=gmail&logoColor=white)](mailto:staff@winboat.app)
- [![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/TibixDev/winboat)

## Star History
<a href="https://www.star-history.com/#tibixdev/winboat&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=tibixdev/winboat&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=tibixdev/winboat&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=tibixdev/winboat&type=Date" />
 </picture>
</a>
