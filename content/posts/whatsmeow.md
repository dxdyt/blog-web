---
title: whatsmeow
date: 2025-03-31T12:21:21+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1742995917580-becb015f088d?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDMzOTQ4NjJ8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1742995917580-becb015f088d?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDMzOTQ4NjJ8&ixlib=rb-4.0.3
---

# [tulir/whatsmeow](https://github.com/tulir/whatsmeow)

# whatsmeow
[![Go Reference](https://pkg.go.dev/badge/go.mau.fi/whatsmeow.svg)](https://pkg.go.dev/go.mau.fi/whatsmeow)

whatsmeow is a Go library for the WhatsApp web multidevice API.

## Discussion
Matrix room: [#whatsmeow:maunium.net](https://matrix.to/#/#whatsmeow:maunium.net)

For questions about the WhatsApp protocol (like how to send a specific type of
message), you can also use the [WhatsApp protocol Q&A] section on GitHub
discussions.

[WhatsApp protocol Q&A]: https://github.com/tulir/whatsmeow/discussions/categories/whatsapp-protocol-q-a

## Usage
The [godoc](https://pkg.go.dev/go.mau.fi/whatsmeow) includes docs for all methods and event types.
There's also a [simple example](https://pkg.go.dev/go.mau.fi/whatsmeow#example-package) at the top.

## Features
Most core features are already present:

* Sending messages to private chats and groups (both text and media)
* Receiving all messages
* Managing groups and receiving group change events
* Joining via invite messages, using and creating invite links
* Sending and receiving typing notifications
* Sending and receiving delivery and read receipts
* Reading and writing app state (contact list, chat pin/mute status, etc)
* Sending and handling retry receipts if message decryption fails
* Sending status messages (experimental, may not work for large contact lists)

Things that are not yet implemented:

* Sending broadcast list messages (this is not supported on WhatsApp web either)
* Calls
