---
title: fsnotify
date: 2023-10-27T12:17:29+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1696326117395-5097014f290a?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTgzODAwOTR8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1696326117395-5097014f290a?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTgzODAwOTR8&ixlib=rb-4.0.3
---

# [fsnotify/fsnotify](https://github.com/fsnotify/fsnotify)

# WARNING

If you are reading this, you use `master` branch of this repository,
which is wrong.

This branch
 - should not be used;
 - is not maintained;
 - is not supported;
 - will be removed soon.

You should switch to using the default branch instead.

## Using git

Here's how to switch your existing local copy of this repository from `master`
to `main` (assuming the remote name is `origin`):

```
git branch -m master main
git fetch origin
git branch -u origin/main main
git remote set-head origin -a
```

In addition to the above, if you want to remove the leftover `origin/master`
remote branch (NOTE this also removes all other remote branches that no longer
exist in `origin`):

```
git remote prune origin
```

## Background

The `master` branch was renamed to `main`, causing an issue with
Yocto/OpenEmbedded's meta-virtualization layer, which explicitly refers
to `master` branch of this repository (see #426).

This temporary branch is created to alleviate the Yocto/OE issue.
