---
title: Apollo-CustomApiCredentials
date: 2023-07-03T12:17:16+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1686841812861-d22f3ce23a58?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2ODgzNTc4MjZ8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1686841812861-d22f3ce23a58?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2ODgzNTc4MjZ8&ixlib=rb-4.0.3
---

# [EthanArbuckle/Apollo-CustomApiCredentials](https://github.com/EthanArbuckle/Apollo-CustomApiCredentials)

## Use your own reddit API credentials in Apollo


### Creating an API credential:

sign out of all accounts in Apollo before installing

1. Sign into your reddit account (on desktop) and go here: https://reddit.com/prefs/apps
2. Click the `are you a developer? create an app...` button
3. Fill in the fields
	* name: Use whatever
	* Choose `Installed App`
	* description: bs
	* about url: bs
	* redirect uri: `apollo://reddit-oauth`
4. `create app`

5. After creating the app you'll get a client identifier; it'll be a bunch of random characters. Put it in `Tweak.m`:

       static NSString * const kRedditClientID = @"CLIENT_ID_GOES_HERE";

6. build and install


For now Apollo will still use the original API creds for other services (like imgur), but i'll update this to support replacing those as well
