---
title: kilo
date: 2025-05-22T12:24:11+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1746897785282-cfbdf7497f39?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDc4ODc4MDN8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1746897785282-cfbdf7497f39?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDc4ODc4MDN8&ixlib=rb-4.1.0
---

# [antirez/kilo](https://github.com/antirez/kilo)

Kilo
===

Kilo is a small text editor in less than 1K lines of code (counted with cloc).

A screencast is available here: https://asciinema.org/a/90r2i9bq8po03nazhqtsifksb

Usage: kilo `<filename>`

Keys:

    CTRL-S: Save
    CTRL-Q: Quit
    CTRL-F: Find string in file (ESC to exit search, arrows to navigate)

Kilo does not depend on any library (not even curses). It uses fairly standard
VT100 (and similar terminals) escape sequences. The project is in alpha
stage and was written in just a few hours taking code from my other two
projects, load81 and linenoise.

People are encouraged to use it as a starting point to write other editors
or command line interfaces that are more advanced than the usual REPL
style CLI.

Kilo was written by Salvatore Sanfilippo aka antirez and is released
under the BSD 2 clause license.
