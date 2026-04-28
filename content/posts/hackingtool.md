---
title: hackingtool
date: 2026-04-28T14:29:07+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1769006352025-1a429e69398f?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NzczNTc2ODR8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1769006352025-1a429e69398f?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NzczNTc2ODR8&ixlib=rb-4.1.0
---

# [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool)

<div align="center">

<img src="images/logo.svg" alt="HackingTool" width="600">

<p><b>All-in-One Hacking Tool for Security Researchers & Pentesters</b></p>

[![License](https://img.shields.io/github/license/Z4nzu/hackingtool)](LICENSE)&nbsp;
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)&nbsp;
[![Version](https://img.shields.io/badge/v2.0.0-00FF88?style=flat-square)](#)&nbsp;
[![Stars](https://img.shields.io/github/stars/Z4nzu/hackingtool?style=flat-square&color=yellow)](https://github.com/Z4nzu/hackingtool/stargazers)&nbsp;
[![Forks](https://img.shields.io/github/forks/Z4nzu/hackingtool?style=flat-square&color=blue)](https://github.com/Z4nzu/hackingtool/network/members)&nbsp;
[![Issues](https://img.shields.io/github/issues/Z4nzu/hackingtool?style=flat-square&color=red)](https://github.com/Z4nzu/hackingtool/issues)&nbsp;
[![Last Commit](https://img.shields.io/github/last-commit/Z4nzu/hackingtool?style=flat-square&color=00FF88)](https://github.com/Z4nzu/hackingtool/commits/master)

![](https://img.shields.io/badge/20_Categories-7B61FF?style=for-the-badge)
![](https://img.shields.io/badge/185+_Tools-00FF88?style=for-the-badge)
![](https://img.shields.io/badge/19_Tags-FF61DC?style=for-the-badge)
![](https://img.shields.io/badge/Linux_%7C_Kali_%7C_Parrot_%7C_macOS-FFA116?style=for-the-badge&logo=linux&logoColor=white)

<a href="#installation"><img src="https://img.shields.io/badge/Install_Now-00FF88?style=for-the-badge&logo=rocket&logoColor=black" alt="Install Now"></a>&nbsp;
<a href="#quick-commands"><img src="https://img.shields.io/badge/Quick_Commands-7B61FF?style=for-the-badge&logo=terminal&logoColor=white" alt="Quick Commands"></a>&nbsp;
<a href="https://github.com/Z4nzu/hackingtool/issues/new?template=tool_request.md"><img src="https://img.shields.io/badge/Suggest_a_Tool-FF61DC?style=for-the-badge&logo=plus&logoColor=white" alt="Suggest a Tool"></a>

</div>

---


## What's New in v2.0.0

<table>
<tr><td>

| | Feature | Description |
|:---:|---|---|
| **🐍** | **Python 3.10+** | All Python 2 code removed, modern syntax throughout |
| **🖥** | **OS-aware menus** | Linux-only tools hidden automatically on macOS |
| **📦** | **185+ tools** | 35 new modern tools added across 6 categories |
| **🔍** | **Search** | Type `/` to search all tools by name, description, or keyword |
| **🏷** | **Tag filter** | Type `t` to filter by 19 tags — osint, web, c2, cloud, mobile... |
| **💡** | **Recommend** | Type `r` — "I want to scan a network" → shows relevant tools |
| **✅** | **Install status** | ✔/✘ shown next to every tool — know what's ready |
| **⚡** | **Install all** | Option `97` in any category — batch install at once |
| **🔄** | **Smart update** | Each tool has Update — auto-detects git pull / pip upgrade / go install |
| **📂** | **Open folder** | Jump into any tool's directory for manual inspection |
| **🐳** | **Docker** | Builds locally — no unverified external images |
| **🚀** | **One-liner install** | `curl -sSL .../install.sh \| sudo bash` — zero manual steps |
| **🏢** | **3 new categories** | Active Directory, Cloud Security, Mobile Security |

</td></tr>
</table>



---

## Quick Commands

<div align="center">

| Command | Action | Works in |
|:---:|---|:---:|
| `/query` | **Search** — find tools instantly by keyword | Main menu |
| `t` | **Tags** — filter by osint, scanner, c2, cloud, mobile... | Main menu |
| `r` | **Recommend** — "I want to do X" → matching tools | Main menu |
| `?` | **Help** — quick reference card | Everywhere |
| `q` | **Quit** — exit from any depth | Everywhere |
| `97` | **Install All** — batch install all tools in category | Category |
| `99` | **Back** — return to previous menu | Everywhere |

</div>

---


## Tool Categories

<div align="center">

| # | Category | Tools | | # | Category | Tools |
|:---:|---|:---:|---|:---:|---|:---:|
| 1 | 🛡 [Anonymously Hiding](#anonymously-hiding-tools) | 2 | | 11 | 🧰 [Exploit Framework](#exploit-framework) | 4 |
| 2 | 🔍 [Information Gathering](#information-gathering-tools) | 26 | | 12 | 🔁 [Reverse Engineering](#reverse-engineering-tools) | 5 |
| 3 | 📚 [Wordlist Generator](#wordlist-generator) | 7 | | 13 | ⚡ [DDOS Attack](#ddos-attack-tools) | 5 |
| 4 | 📶 [Wireless Attack](#wireless-attack-tools) | 13 | | 14 | 🖥 [RAT](#remote-administrator-tools-rat) | 1 |
| 5 | 🧩 [SQL Injection](#sql-injection-tools) | 7 | | 15 | 💥 [XSS Attack](#xss-attack-tools) | 9 |
| 6 | 🎣 [Phishing Attack](#phishing-attack-tools) | 17 | | 16 | 🖼 [Steganography](#steganography-tools) | 4 |
| 7 | 🌐 [Web Attack](#web-attack-tools) | 20 | | 17 | 🏢 [Active Directory](#active-directory-tools) | 6 |
| 8 | 🔧 [Post Exploitation](#post-exploitation-tools) | 10 | | 18 | ☁ [Cloud Security](#cloud-security-tools) | 4 |
| 9 | 🕵 [Forensics](#forensic-tools) | 8 | | 19 | 📱 [Mobile Security](#mobile-security-tools) | 3 |
| 10 | 📦 [Payload Creation](#payload-creation-tools) | 8 | | 20 | ✨ [Other Tools](#other-tools) | 24 |

</div>



---


## 🛡 Anonymously Hiding Tools

- [Anonymously Surf](https://github.com/Und3rf10w/kali-anonsurf)
- [Multitor](https://github.com/trimstray/multitor)



## 🔍 Information Gathering Tools

- [Network Map (nmap)](https://github.com/nmap/nmap)
- [Dracnmap](https://github.com/Screetsec/Dracnmap)
- Port scanning
- Host to IP
- [Xerosploit](https://github.com/LionSec/xerosploit)
- [RED HAWK](https://github.com/Tuhinshubhra/RED_HAWK)
- [ReconSpider](https://github.com/bhavsec/reconspider)
- IsItDown
- [Infoga](https://github.com/m4ll0k/Infoga)
- [ReconDog](https://github.com/s0md3v/ReconDog)
- [Striker](https://github.com/s0md3v/Striker)
- [SecretFinder](https://github.com/m4ll0k/SecretFinder)
- [Shodanfy](https://github.com/m4ll0k/Shodanfy.py)
- [rang3r](https://github.com/floriankunushevci/rang3r)
- [Breacher](https://github.com/s0md3v/Breacher)
- [theHarvester](https://github.com/laramies/theHarvester) ★
- [Amass](https://github.com/owasp-amass/amass) ★
- [Masscan](https://github.com/robertdavidgraham/masscan) ★
- [RustScan](https://github.com/RustScan/RustScan) ★
- [Holehe](https://github.com/megadose/holehe) ★
- [Maigret](https://github.com/soxoj/maigret) ★
- [httpx](https://github.com/projectdiscovery/httpx) ★
- [SpiderFoot](https://github.com/smicallef/spiderfoot) ★
- [Subfinder](https://github.com/projectdiscovery/subfinder) ★
- [TruffleHog](https://github.com/trufflesecurity/trufflehog) ★
- [Gitleaks](https://github.com/gitleaks/gitleaks) ★



## 📚 Wordlist Generator

- [Cupp](https://github.com/Mebus/cupp)
- [WordlistCreator](https://github.com/Z4nzu/wlcreator)
- [Goblin WordGenerator](https://github.com/UndeadSec/GoblinWordGenerator)
- [Password list (1.4B)](https://github.com/Viralmaniar/SMWYG-Show-Me-What-You-Got)
- [Hashcat](https://github.com/hashcat/hashcat) ★
- [John the Ripper](https://github.com/openwall/john) ★
- [haiti](https://github.com/noraj/haiti) ★



## 📶 Wireless Attack Tools

- [WiFi-Pumpkin](https://github.com/P0cL4bs/wifipumpkin3)
- [pixiewps](https://github.com/wiire/pixiewps)
- [Bluetooth Honeypot (bluepot)](https://github.com/andrewmichaelsmith/bluepot)
- [Fluxion](https://github.com/FluxionNetwork/fluxion)
- [Wifiphisher](https://github.com/wifiphisher/wifiphisher)
- [Wifite](https://github.com/derv82/wifite2)
- [EvilTwin](https://github.com/Z4nzu/fakeap)
- [Fastssh](https://github.com/Z4nzu/fastssh)
- Howmanypeople
- [Airgeddon](https://github.com/v1s1t0r1sh3r3/airgeddon) ★
- [hcxdumptool](https://github.com/ZerBea/hcxdumptool) ★
- [hcxtools](https://github.com/ZerBea/hcxtools) ★
- [Bettercap](https://github.com/bettercap/bettercap) ★



## 🧩 SQL Injection Tools

- [Sqlmap](https://github.com/sqlmapproject/sqlmap)
- [NoSqlMap](https://github.com/codingo/NoSQLMap)
- [DSSS](https://github.com/stamparm/DSSS)
- [Explo](https://github.com/dtag-dev-sec/explo)
- [Blisqy](https://github.com/JohnTroony/Blisqy)
- [Leviathan](https://github.com/leviathan-framework/leviathan)
- [SQLScan](https://github.com/Cvar1984/sqlscan)



## 🎣 Phishing Attack Tools

- [Autophisher](https://github.com/CodingRanjith/autophisher)
- [PyPhisher](https://github.com/KasRoudra/PyPhisher)
- [AdvPhishing](https://github.com/Ignitetch/AdvPhishing)
- [Setoolkit](https://github.com/trustedsec/social-engineer-toolkit)
- [SocialFish](https://github.com/UndeadSec/SocialFish)
- [HiddenEye](https://github.com/Morsmalleo/HiddenEye)
- [Evilginx3](https://github.com/kgretzky/evilginx2)
- [I-See-You](https://github.com/Viralmaniar/I-See-You)
- [SayCheese](https://github.com/hangetzzu/saycheese)
- [QR Code Jacking](https://github.com/cryptedwolf/ohmyqr)
- [BlackEye](https://github.com/thelinuxchoice/blackeye)
- [ShellPhish](https://github.com/An0nUD4Y/shellphish)
- [Thanos](https://github.com/TridevReddy/Thanos)
- [QRLJacking](https://github.com/OWASP/QRLJacking)
- [Maskphish](https://github.com/jaykali/maskphish)
- [BlackPhish](https://github.com/iinc0gnit0/BlackPhish)
- [dnstwist](https://github.com/elceef/dnstwist)



## 🌐 Web Attack Tools

- [Web2Attack](https://github.com/santatic/web2attack)
- Skipfish
- [Sublist3r](https://github.com/aboul3la/Sublist3r)
- [CheckURL](https://github.com/UndeadSec/checkURL)
- [Sub-Domain TakeOver](https://github.com/edoardottt/takeover)
- [Dirb](https://gitlab.com/kalilinux/packages/dirb)
- [Nuclei](https://github.com/projectdiscovery/nuclei) ★
- [ffuf](https://github.com/ffuf/ffuf) ★
- [Feroxbuster](https://github.com/epi052/feroxbuster) ★
- [Nikto](https://github.com/sullo/nikto) ★
- [wafw00f](https://github.com/EnableSecurity/wafw00f) ★
- [Katana](https://github.com/projectdiscovery/katana) ★
- [Gobuster](https://github.com/OJ/gobuster) ★
- [Dirsearch](https://github.com/maurosoria/dirsearch) ★
- [OWASP ZAP](https://github.com/zaproxy/zaproxy) ★
- [testssl.sh](https://github.com/drwetter/testssl.sh) ★
- [Arjun](https://github.com/s0md3v/Arjun) ★
- [Caido](https://github.com/caido/caido) ★
- [mitmproxy](https://github.com/mitmproxy/mitmproxy) ★



## 🔧 Post Exploitation Tools

- [Vegile](https://github.com/Screetsec/Vegile)
- [Chrome Keylogger](https://github.com/UndeadSec/HeraKeylogger)
- [pwncat-cs](https://github.com/calebstewart/pwncat) ★
- [Sliver](https://github.com/BishopFox/sliver) ★
- [Havoc](https://github.com/HavocFramework/Havoc) ★
- [PEASS-ng (LinPEAS/WinPEAS)](https://github.com/peass-ng/PEASS-ng) ★
- [Ligolo-ng](https://github.com/nicocha30/ligolo-ng) ★
- [Chisel](https://github.com/jpillora/chisel) ★
- [Evil-WinRM](https://github.com/Hackplayers/evil-winrm) ★
- [Mythic](https://github.com/its-a-feature/Mythic) ★



## 🕵 Forensic Tools

- Autopsy
- Wireshark
- [Bulk extractor](https://github.com/simsong/bulk_extractor)
- [Guymager](https://guymager.sourceforge.io/)
- [Toolsley](https://www.toolsley.com/)
- [Volatility 3](https://github.com/volatilityfoundation/volatility3) ★
- [Binwalk](https://github.com/ReFirmLabs/binwalk) ★
- [pspy](https://github.com/DominicBreuker/pspy) ★



## 📦 Payload Creation Tools

- [The FatRat](https://github.com/Screetsec/TheFatRat)
- [Brutal](https://github.com/Screetsec/Brutal)
- [Stitch](https://nathanlopez.github.io/Stitch)
- [MSFvenom Payload Creator](https://github.com/g0tmi1k/msfpc)
- [Venom](https://github.com/r00t-3xp10it/venom)
- [Spycam](https://github.com/indexnotfound404/spycam)
- [Mob-Droid](https://github.com/kinghacker0/Mob-Droid)
- [Enigma](https://github.com/UndeadSec/Enigma)



## 🧰 Exploit Framework

- [RouterSploit](https://github.com/threat9/routersploit)
- [WebSploit](https://github.com/The404Hacking/websploit)
- [Commix](https://github.com/commixproject/commix)
- [Web2Attack](https://github.com/santatic/web2attack)



## 🔁 Reverse Engineering Tools

- [Androguard](https://github.com/androguard/androguard)
- [Apk2Gold](https://github.com/lxdvs/apk2gold)
- [JadX](https://github.com/skylot/jadx)
- [Ghidra](https://github.com/NationalSecurityAgency/ghidra) ★
- [Radare2](https://github.com/radareorg/radare2) ★



## ⚡ DDOS Attack Tools

- [DDoS Script](https://github.com/the-deepnet/ddos)
- [SlowLoris](https://github.com/gkbrk/slowloris)
- [Asyncrone](https://github.com/fatihsnsy/aSYNcrone)
- [UFOnet](https://github.com/epsylon/ufonet)
- [GoldenEye](https://github.com/jseidl/GoldenEye)



## 🖥 Remote Administrator Tools (RAT)

- [Pyshell](https://github.com/knassar702/pyshell)



## 💥 XSS Attack Tools

- [DalFox](https://github.com/hahwul/dalfox)
- [XSS Payload Generator](https://github.com/capture0x/XSS-LOADER)
- [Extended XSS Searcher](https://github.com/Damian89/extended-xss-search)
- [XSS-Freak](https://github.com/PR0PH3CY33/XSS-Freak)
- [XSpear](https://github.com/hahwul/XSpear)
- [XSSCon](https://github.com/menkrep1337/XSSCon)
- [XanXSS](https://github.com/Ekultek/XanXSS)
- [XSStrike](https://github.com/UltimateHackers/XSStrike)
- [RVuln](https://github.com/iinc0gnit0/RVuln)



## 🖼 Steganography Tools

- SteganoHide
- [StegoCracker](https://github.com/W1LDN16H7/StegoCracker)
- [Whitespace](https://github.com/beardog108/snow10)



## 🏢 Active Directory Tools

- [BloodHound](https://github.com/BloodHoundAD/BloodHound) ★
- [NetExec (nxc)](https://github.com/Pennyw0rth/NetExec) ★
- [Impacket](https://github.com/fortra/impacket) ★
- [Responder](https://github.com/lgandx/Responder) ★
- [Certipy](https://github.com/ly4k/Certipy) ★
- [Kerbrute](https://github.com/ropnop/kerbrute) ★



## ☁ Cloud Security Tools

- [Prowler](https://github.com/prowler-cloud/prowler) ★
- [ScoutSuite](https://github.com/nccgroup/ScoutSuite) ★
- [Pacu](https://github.com/RhinoSecurityLabs/pacu) ★
- [Trivy](https://github.com/aquasecurity/trivy) ★



## 📱 Mobile Security Tools

- [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) ★
- [Frida](https://github.com/frida/frida) ★
- [Objection](https://github.com/sensepost/objection) ★



## ✨ Other Tools

#### SocialMedia Bruteforce
- [AllinOne SocialMedia Attack](https://github.com/Matrix07ksa/Brute_Force)
- [Facebook Attack](https://github.com/Matrix07ksa/Brute_Force)
- [Application Checker](https://github.com/jakuta-tech/underhanded)

#### Android Hacking Tools
- [Keydroid](https://github.com/F4dl0/keydroid)
- [MySMS](https://github.com/papusingh2sms/mysms)
- [Lockphish](https://github.com/JasonJerry/lockphish)
- [DroidCam / WishFish](https://github.com/kinghacker0/WishFish)
- [EvilApp](https://github.com/crypticterminal/EvilApp)

#### IDN Homograph Attack
- [EvilURL](https://github.com/UndeadSec/EvilURL)

#### Email Verify Tools
- [Knockmail](https://github.com/4w4k3/KnockMail)

#### Hash Cracking Tools
- [Hash Buster](https://github.com/s0md3v/Hash-Buster)

#### Wifi Deauthenticate
- [WifiJammer-NG](https://github.com/MisterBianco/wifijammer-ng)
- [KawaiiDeauther](https://github.com/aryanrtm/KawaiiDeauther)

#### SocialMedia Finder
- [Find SocialMedia By Facial Recognition](https://github.com/Greenwolf/social_mapper)
- [Find SocialMedia By UserName](https://github.com/xHak9x/finduser)
- [Sherlock](https://github.com/sherlock-project/sherlock)
- [SocialScan](https://github.com/iojw/socialscan)

#### Payload Injector
- [Debinject](https://github.com/UndeadSec/Debinject)
- [Pixload](https://github.com/chinarulezzz/pixload)

#### Web Crawling
- [Gospider](https://github.com/jaeles-project/gospider)

#### Mix Tools
- Terminal Multiplexer (tilix)
- [Crivo](https://github.com/GMDSantana/crivo)


---

## Contributing — Add a New Tool

<table>
<tr>
<td width="50%">

### Open an Issue

> **Title:** `[Tool Request] ToolName — Category`

Use the [Tool Request](.github/ISSUE_TEMPLATE/tool_request.md) template.

Required: tool name, GitHub URL, category, OS, install command, reason.

</td>
<td width="50%">

### Open a Pull Request

> **Title:** `[New Tool] ToolName — Category`

Use the [PR template](.github/PULL_REQUEST_TEMPLATE.md) checklist.

Required: class in `tools/*.py`, TITLE, DESCRIPTION, INSTALL/RUN commands, SUPPORTED_OS, test locally.

</td>
</tr>
</table>

> Issues or PRs that don't follow the title format will be closed without review.

---

## Installation

<table>
<tr>
<td>

### One-liner (recommended)

```bash
curl -sSL https://raw.githubusercontent.com/Z4nzu/hackingtool/master/install.sh | sudo bash
```

Handles everything — prerequisites, clone, venv, launcher.

</td>
<td>

### Manual

```bash
git clone https://github.com/Z4nzu/hackingtool.git
cd hackingtool
sudo python3 install.py
```

Then run: `hackingtool`

</td>
</tr>
</table>


### Docker

```bash
# Build
docker build -t hackingtool .

# Run (direct)
docker run -it --rm hackingtool

# Run (Compose — recommended)
docker compose up -d
docker exec -it hackingtool bash

# Dev mode (live source mount)
docker compose --profile dev up
docker exec -it hackingtool-dev bash

# Stop
docker compose down        # stop container
docker compose down -v     # also remove data volume
```



### Requirements

| Dependency | Version | Needed for |
|---|---|---|
| Python | 3.10+ | Core |
| Go | 1.21+ | nuclei, ffuf, amass, httpx, katana, dalfox, gobuster, subfinder |
| Ruby | any | haiti, evil-winrm |
| Docker | any | Mythic, MobSF (optional) |

```bash
pip install -r requirements.txt
```

---

## Star History

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Z4nzu/hackingtool&type=Date&theme=dark" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Z4nzu/hackingtool&type=Date" />
  <img alt="HackingTool Star History Chart" src="https://api.star-history.com/svg?repos=Z4nzu/hackingtool&type=Date" />
</picture>

---

## Support

If this project helps you, consider buying me a coffee:

<a href="https://buymeacoffee.com/hardikzinzu" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="50"></a>

## Social

[![Twitter](https://img.shields.io/badge/Twitter-Follow-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/_Zinzu07)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Z4nzu/)

> **For authorized security testing only.**
> Thanks to all original authors of the tools included in hackingtool.

Your favourite tool is not listed? [Suggest it here](https://github.com/Z4nzu/hackingtool/issues/new?template=tool_request.md)
