---
title: imessage
date: 2023-12-25T12:16:45+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1703179120646-37642ea08138?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDM0Nzc3NDh8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1703179120646-37642ea08138?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDM0Nzc3NDh8&ixlib=rb-4.0.3
---

# [beeper/imessage](https://github.com/beeper/imessage)

# beeper-imessage
A Matrix-iMessage puppeting bridge.

## Documentation
The bridge works like any other mautrix-go bridge, so the instructions at
<https://docs.mau.fi/bridges/go/setup.html> can be applied directly.
You can find precompiled binaries from the GitLab CI at
<https://mau.dev/mautrix/imessagego>.

Additionally, the bridge requires a registration provider running on a [Mac] or
[jailbroken iPhone], as well as a [relay server] to help the bridge and
registration provider connect to each other.

[Mac]: https://github.com/beeper/mac-registration-provider
[jailbroken iPhone]: https://github.com/beeper/phone-registration-provider
[relay server]: https://github.com/beeper/registration-relay

When connecting the bridge to your Beeper account with bbctl, you don't need to
self-host the relay, you only need to run the provider.

## Discussion
Matrix room: [#imessage:maunium.net](https://matrix.to/#/#imessage:maunium.net)
