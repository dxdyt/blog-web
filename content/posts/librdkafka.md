---
title: librdkafka
date: 2025-02-01T12:19:38+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1736135290115-ec129b0f31fc?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MzgzODM1MDV8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1736135290115-ec129b0f31fc?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MzgzODM1MDV8&ixlib=rb-4.0.3
---

# [confluentinc/librdkafka](https://github.com/confluentinc/librdkafka)

librdkafka - the Apache Kafka C/C++ client library
==================================================

Copyright (c) 2012-2022, [Magnus Edenhill](http://www.edenhill.se/).
              2023 [Confluent Inc.](https://www.confluent.io/).

[https://github.com/confluentinc/librdkafka](https://github.com/confluentinc/librdkafka)

**librdkafka** is a C library implementation of the
[Apache Kafka](https://kafka.apache.org/) protocol, providing Producer, Consumer
and Admin clients. It was designed with message delivery reliability
and high performance in mind, current figures exceed 1 million msgs/second for
the producer and 3 million msgs/second for the consumer.

**librdkafka** is licensed under the 2-clause BSD license.

KAFKA is a registered trademark of The Apache Software Foundation and
has been licensed for use by librdkafka. librdkafka has no
affiliation with and is not endorsed by The Apache Software Foundation.


# Features #
  * Full Exactly-Once-Semantics (EOS) support
  * High-level producer, including Idempotent and Transactional producers
  * High-level balanced KafkaConsumer (requires broker >= 0.9)
  * Simple (legacy) consumer
  * Admin client
  * Compression: snappy, gzip, lz4, zstd
  * [SSL](https://github.com/confluentinc/librdkafka/wiki/Using-SSL-with-librdkafka) support
  * [SASL](https://github.com/confluentinc/librdkafka/wiki/Using-SASL-with-librdkafka) (GSSAPI/Kerberos/SSPI, PLAIN, SCRAM, OAUTHBEARER) support
  * Full list of [supported KIPs](INTRODUCTION.md#supported-kips)
  * Broker version support: >=0.8 (see [Broker version compatibility](INTRODUCTION.md#broker-version-compatibility))
  * Guaranteed API stability for C & C++ APIs (ABI safety guaranteed for C)
  * [Statistics](STATISTICS.md) metrics
  * Debian package: librdkafka1 and librdkafka-dev in Debian and Ubuntu
  * RPM package: librdkafka and librdkafka-devel
  * Gentoo package: dev-libs/librdkafka
  * Portable: runs on Linux, MacOS X, Windows, Solaris, FreeBSD, AIX, ...

# Documentation

 * Public API in [C header](src/rdkafka.h) and [C++ header](src-cpp/rdkafkacpp.h).
 * Introduction and manual in [INTRODUCTION.md](https://github.com/confluentinc/librdkafka/blob/master/INTRODUCTION.md).
 * Configuration properties in
[CONFIGURATION.md](https://github.com/confluentinc/librdkafka/blob/master/CONFIGURATION.md).
 * Statistics metrics in [STATISTICS.md](https://github.com/confluentinc/librdkafka/blob/master/STATISTICS.md).
 * [Frequently asked questions](https://github.com/confluentinc/librdkafka/wiki).
 * Step-by-step tutorial [Getting Started with Apache Kafka and C/C++](https://developer.confluent.io/get-started/c/).

**NOTE**: The `master` branch is actively developed, use latest [release](https://github.com/confluentinc/librdkafka/releases) for production use.


# Installation

## Installing prebuilt packages

On Mac OSX, install librdkafka with homebrew:

```bash
$ brew install librdkafka
```

On Debian and Ubuntu, install librdkafka from the Confluent APT repositories,
see instructions [here](https://docs.confluent.io/current/installation/installing_cp/deb-ubuntu.html#get-the-software) and then install librdkafka:

 ```bash
 $ apt install librdkafka-dev
 ```

On RedHat, CentOS, Fedora, install librdkafka from the Confluent YUM repositories,
instructions [here](https://docs.confluent.io/current/installation/installing_cp/rhel-centos.html#get-the-software) and then install librdkafka:

```bash
$ yum install librdkafka-devel
```

On Windows, reference [librdkafka.redist](https://www.nuget.org/packages/librdkafka.redist/) NuGet package in your Visual Studio project.


For other platforms, follow the source building instructions below.


## Installing librdkafka using vcpkg

You can download and install librdkafka using the [vcpkg](https://github.com/Microsoft/vcpkg) dependency manager:

```bash
# Install vcpkg if not already installed
$ git clone https://github.com/Microsoft/vcpkg.git
$ cd vcpkg
$ ./bootstrap-vcpkg.sh
$ ./vcpkg integrate install

# Install librdkafka
$ vcpkg install librdkafka
```

The librdkafka package in vcpkg is kept up to date by Microsoft team members and community contributors.
If the version is out of date, please [create an issue or pull request](https://github.com/Microsoft/vcpkg) on the vcpkg repository.


## Build from source

### Requirements
	The GNU toolchain
	GNU make
   	pthreads
	zlib-dev (optional, for gzip compression support)
	libssl-dev (optional, for SSL and SASL SCRAM support)
	libsasl2-dev (optional, for SASL GSSAPI support)
	libzstd-dev (optional, for ZStd compression support)
	libcurl-dev (optional, for SASL OAUTHBEARER OIDC support)

**NOTE**: Static linking of ZStd (requires zstd >= 1.2.1) in the producer
          enables encoding the original size in the compression frame header,
          which will speed up the consumer.
          Use `STATIC_LIB_libzstd=/path/to/libzstd.a ./configure --enable-static`
          to enable static ZStd linking.
          MacOSX example:
          `STATIC_LIB_libzstd=$(brew ls -v zstd | grep libzstd.a$) ./configure --enable-static`


### Building

      ./configure
      # Or, to automatically install dependencies using the system's package manager:
      # ./configure --install-deps
      # Or, build dependencies from source:
      # ./configure --install-deps --source-deps-only

      make
      sudo make install


**NOTE**: See [README.win32](README.win32) for instructions how to build
          on Windows with Microsoft Visual Studio.

**NOTE**: See [CMake instructions](packaging/cmake/README.md) for experimental
          CMake build (unsupported).


## Usage in code

See [getting Started with Apache Kafka and C/C++](https://developer.confluent.io/get-started/c/) for a basic tutorial.

1. Refer to the [examples directory](examples/) for code using:

    * Producers: basic producers, idempotent producers, transactional producers.
    * Consumers: basic consumers, reading batches of messages.
    * Performance and latency testing tools.

2. Refer to the [examples GitHub repo](https://github.com/confluentinc/examples/tree/master/clients/cloud/c) for code connecting to a cloud streaming data service based on Apache Kafka

3. Link your program with `-lrdkafka` (C) or `-lrdkafka++` (C++).


## Commercial support

Commercial support is available from [Confluent Inc](https://www.confluent.io/)


## Community support

**Only the [latest official release](https://github.com/confluentinc/librdkafka/releases) is supported for community members.**

File bug reports and feature requests using [GitHub Issues](https://github.com/confluentinc/librdkafka/issues).

Questions and discussions are welcome on the [Discussions](https://github.com/confluentinc/librdkafka/discussions) forum, and on the [Confluent Community slack](https://launchpass.com/confluentcommunity) #clients channel.


# Language bindings #

  * C#/.NET: [confluent-kafka-dotnet](https://github.com/confluentinc/confluent-kafka-dotnet) (based on [rdkafka-dotnet](https://github.com/ah-/rdkafka-dotnet))
  * C++: [cppkafka](https://github.com/mfontanini/cppkafka)
  * C++: [modern-cpp-kafka](https://github.com/Morgan-Stanley/modern-cpp-kafka)
  * Common Lisp: [cl-rdkafka](https://github.com/SahilKang/cl-rdkafka)
  * D (C-like): [librdkafka](https://github.com/DlangApache/librdkafka/)
  * D (C++-like): [librdkafkad](https://github.com/tamediadigital/librdkafka-d)
  * Erlang: [erlkaf](https://github.com/silviucpp/erlkaf)
  * Go: [confluent-kafka-go](https://github.com/confluentinc/confluent-kafka-go)
  * Haskell (kafka, conduit, avro, schema registry): [hw-kafka](https://github.com/haskell-works/hw-kafka)
  * Kotlin Native: [Kafka-Kotlin-Native](https://github.com/icemachined/kafka-kotlin-native)
  * Lua: [luardkafka](https://github.com/mistsv/luardkafka)
  * Node.js: [node-rdkafka](https://github.com/Blizzard/node-rdkafka)
  * OCaml: [ocaml-kafka](https://github.com/didier-wenzek/ocaml-kafka)
  * Perl: [Net::Kafka](https://github.com/bookingcom/perl-Net-Kafka)
  * PHP: [php-rdkafka](https://github.com/arnaud-lb/php-rdkafka)
  * PHP: [php-simple-kafka-client](https://github.com/php-kafka/php-simple-kafka-client)
  * Python: [confluent-kafka-python](https://github.com/confluentinc/confluent-kafka-python)
  * Python: [PyKafka](https://github.com/Parsely/pykafka)
  * Ruby: [Hermann](https://github.com/reiseburo/hermann)
  * Ruby: [rdkafka-ruby](https://github.com/appsignal/rdkafka-ruby)
  * Rust: [rust-rdkafka](https://github.com/fede1024/rust-rdkafka)
  * Tcl: [KafkaTcl](https://github.com/flightaware/kafkatcl)
  * Shell: [kafkacat](https://github.com/edenhill/kafkacat) - Apache Kafka command line tool
  * Swift: [Perfect-Kafka](https://github.com/PerfectlySoft/Perfect-Kafka)


See [Powered by librdkafka](https://github.com/confluentinc/librdkafka/wiki/Powered-by-librdkafka) for an incomplete list of librdkafka users.
