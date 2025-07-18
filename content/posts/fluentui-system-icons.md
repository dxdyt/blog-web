---
title: fluentui-system-icons
date: 2025-06-20T12:26:38+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1748500351969-91142546a971?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTAzOTM1NjJ8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1748500351969-91142546a971?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTAzOTM1NjJ8&ixlib=rb-4.1.0
---

# [microsoft/fluentui-system-icons](https://github.com/microsoft/fluentui-system-icons)

# Fluent UI System Icons

![CI](https://github.com/microsoft/fluentui-system-icons/workflows/CI/badge.svg)

Fluent UI System Icons are a collection of familiar, friendly and modern icons from Microsoft.

![fluent system icons](art/readme-banner.png)

## Icon List

[View the full list of regular icons](icons_regular.md)

[View the full list of filled icons](icons_filled.md)

## Installation

### Android

The library is published via Maven Central, please ensure that the `mavenCentral()` repository has been added to the root `build.gradle` file:

```groovy
repositories {
    ...
    mavenCentral()
}
```

Include the following dependency in your project's `build.gradle`

```groovy
implementation 'com.microsoft.design:fluent-system-icons:1.1.179@aar'
```

For library docs, see [android/README.md](android/README.md).

### iOS and macOS

#### CocoaPods

```ruby
use_frameworks!

pod "FluentIcons", "1.1.179"
```

#### Carthage

```bash
git "git@github.com:microsoft/fluentui-system-icons.git" "1.1.179"
```

For library docs, see [ios/README.md](ios/README.md).

### Flutter

In the `pubspec.yaml` of your flutter project, add the following dependency:

```yaml
dependencies:
  ...
  fluentui_system_icons: ^1.1.179
```

For library docs, see [flutter/README.md](flutter/README.md)

### Plain svg

Inline svg directly. See [packages/svg-icons/README.md](packages/svg-icons/README.md).

## Contributing

### Importer

The importer generates the Android and iOS libraries from the icons in the `assets` directory.

Jump into the directory

```
cd importer
```

Install npm dependencies

```
npm install
npm run clean
```

List all the available commands

```
npm run
```

### Build Pipeline

Our [build pipeline](https://github.com/microsoft/fluentui-system-icons/actions) runs `deploy:android` and `deploy:ios` to create the libraries. The build definitions are located in `.github/workflows/`.

## Demo apps

You can build and run the demo apps following the steps below.

### Android

1. Follow the **Importer** section above and run the command `npm run deploy:android`
2. Open the [android](android) directory in Android Studio
3. Select the `sample-showcase` in the build configuration dropdown
4. Click run

### Flutter

Prerequisite: Make sure you have flutter configured in Android Studio

1. Open the [flutter](flutter) directory in Android Studio
2. Select the 'example' in the directory and open it in Android Studio
3. Click run

## Contact

Please feel free to [open a GitHub issue](https://github.com/microsoft/fluentui-system-icons/issues/new) and assign to the following points of contact with questions or requests.

- Jason Custer([@jasoncuster](https://github.com/jasoncuster)) / Spencer Nelson([@spencer-nelson](https://github.com/spencer-nelson)) / Joe Woodward([@thewoodpecker](https://github.com/thewoodpecker)) - Design
- Nick Romano([@rickromano](https://github.com/nickromano)) - iOS
- Will Hou([@willhou](https://github.com/willhou)) - Android
- Akashdeep Singh([@aakash1313](https://github.com/aakash1313)) - Flutter

## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct) or contact opencode@microsoft.com with any additional questions or comments.
