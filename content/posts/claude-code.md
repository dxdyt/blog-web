---
title: claude-code
date: 2025-05-26T12:25:36+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1744236404781-530428ffbad5?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDgyMzM0NzN8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1744236404781-530428ffbad5?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDgyMzM0NzN8&ixlib=rb-4.1.0
---

# [anthropics/claude-code](https://github.com/anthropics/claude-code)

# Claude Code

![](https://img.shields.io/badge/Node.js-18%2B-brightgreen?style=flat-square) [![npm]](https://www.npmjs.com/package/@anthropic-ai/claude-code)

[npm]: https://img.shields.io/npm/v/@anthropic-ai/claude-code.svg?style=flat-square

Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

Some of its key capabilities include:

- Edit files and fix bugs across your codebase
- Answer questions about your code's architecture and logic
- Execute and fix tests, lint, and other commands
- Search through git history, resolve merge conflicts, and create commits and PRs

**Learn more in the [official documentation](https://docs.anthropic.com/en/docs/claude-code/overview)**.

## Get started

1. If you are new to Node.js and Node Package Manager (`npm`), then it is recommended that you configure an NPM prefix for your user.
   Instructions on how to do this can be found [here](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#recommended-solution-create-a-user-writable-npm-prefix).

   _Important_ We recommend installing this package as a non-privileged user, not as an administrative user like `root`.
   Installing as a non-privileged user helps maintain your system's security and stability.

2. Install Claude Code:

   ```sh
   npm install -g @anthropic-ai/claude-code
   ```

3. Navigate to your project directory and run `claude`.

4. Complete the one-time OAuth process with your Claude Max or Anthropic Console account.

### Reporting Bugs

We welcome feedback during this beta period. Use the `/bug` command to report issues directly within Claude Code, or file a [GitHub issue](https://github.com/anthropics/claude-code/issues).

### Data collection, usage, and retention

When you use Claude Code, we collect feedback, which includes usage data (such as code acceptance or rejections), associated conversation data, and user feedback submitted via the `/bug` command.

#### How we use your data

We may use feedback to improve our products and services, but we will not train generative models using your feedback from Claude Code. Given their potentially sensitive nature, we store user feedback transcripts for only 30 days.

If you choose to send us feedback about Claude Code, such as transcripts of your usage, Anthropic may use that feedback to debug related issues and improve Claude Code's functionality (e.g., to reduce the risk of similar bugs occurring in the future).

### Privacy safeguards

We have implemented several safeguards to protect your data, including limited retention periods for sensitive information, restricted access to user session data, and clear policies against using feedback for model training.

For full details, please review our [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and [Privacy Policy](https://www.anthropic.com/legal/privacy).
