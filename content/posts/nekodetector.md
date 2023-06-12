---
title: nekodetector
date: 2023-06-12T12:17:11+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1683734568726-905fe1ea73de?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2ODY1NDMzMDR8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1683734568726-905fe1ea73de?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2ODY1NDMzMDR8&ixlib=rb-4.0.3
---

# [MCRcortex/nekodetector](https://github.com/MCRcortex/nekodetector)

# Neko Detector 

> A tool to help detect if you are infected by the fractureiser malware.

The fractureiser malware once you run it, infects any jar it is able to find. This tool will help you detect if you are infected by the malware by scanning every jar file in your computer and checking if it shows sign of infection. *For more information about the malware, please refer to the [information document](https://github.com/fractureiser-investigation/fractureiser/blob/main/README.md).*

## Usage

```
java -jar scanner.jar <# of threads> <path to scan> <optional: 'true' for failed jar file opening errors>
```

## Example

```bash
# Scan your entire Windows system with 4 threads
java -jar scanner.jar 4 C:\

# Scan your entire Linux system with 4 threads
java -jar scanner.jar 4 /
```
