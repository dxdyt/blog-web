---
title: go-wallet-sdk
date: 2023-07-20T12:17:24+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1686904423955-b928225c6488?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2ODk4MjY1MDR8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1686904423955-b928225c6488?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2ODk4MjY1MDR8&ixlib=rb-4.0.3
---

# [okx/go-wallet-sdk](https://github.com/okx/go-wallet-sdk)

# go-wallet-sdk

This is a Go language wallet solution that supports offline transactions. We currently support various mainstream public blockchains, and will gradually release the source codes for each blockchain.

## Supported chains

- BTC: Supports transaction creation and signing. Also Supports BRC20-related functions, including inscription creation, BRC20 buying and selling.
- Ethereum: Supports transaction creation and signing.
- Filecoin: Supports transaction creation and signing.
- Polkadot: Supports transaction creation and signing.
- Starknet: Supports transaction creation and signing.

## Main modules

- coins: Implements transaction creation and signature in each coin type.
- crypto: Handles general security and signature algorithms.
- util: Provides various utility class methods.

## Example

For specific usage examples of each coin type, please refer to the corresponding test files. Remember to replace the placeholder private key with your own private key, which is generally in hex format.

## Feedback

You can provide feedback directly in GitHub Issues, and we will respond promptly.
