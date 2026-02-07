---
title: anet
date: 2026-02-07T13:05:11+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1769489050642-3d768e3e959a?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NzA0NDA2NjR8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1769489050642-3d768e3e959a?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NzA0NDA2NjR8&ixlib=rb-4.1.0
---

# [ZeroTworu/anet](https://github.com/ZeroTworu/anet)

# ANet: Сеть Друзей

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Language](https://img.shields.io/badge/rust-1.84%2B-orange)
![Protocol](https://img.shields.io/badge/protocol-ASTP_v1.0-blue)

**ANet** — это инструмент для организации приватного, защищенного информационного пространства между близкими людьми. Мы строим цифровые мосты там, где обычные пути недоступны.

Это не сервис. Это технология для связи тех, кто доверяет друг другу.

## Особенности

В основе проекта лежит собственный транспортный протокол **ASTP (ANet Secure Transport Protocol)**, разработанный с фокусом на:

*   **Приватность:** Полное сквозное шифрование (ChaCha20Poly1305 / X25519).
*   **Устойчивость:** Стабильная работа в сетях с высокими потерями пакетов и нестабильным соединением.
*   **Мимикрия:** Транспортный уровень неотличим от случайного шума (High-entropy UDP stream).
*   **Кроссплатформенность:** Клиенты для Linux, Windows и Android.

## Структура проекта

Проект написан на Rust и разделен на модули:

*   `anet-server` — Узел координации.
*   `anet-client-cli` — Консольный клиент для Linux/Headless систем.
*   `anet-client-gui` — Графический клиент (Windows/Linux) с минималистичным интерфейсом.
*   `anet-mobile` — Библиотека и JNI-биндинги для Android.
*   `anet-common` — Реализация протокола ASTP и криптографии.
*   `anet-keygen` — Утилита для генерации ключей доступа.

## Сборка

Требуется установленный Rust (cargo).

```bash
# Сборка всех компонентов
cargo build --release
```

Support the Chaos / Поддержать Хаос

Разработка ведется в условиях повышенной радиации (Черниковка), под пристальным взглядом Ханюши и с использованием альтернативных источников энергии (C2H5OH).

Если ANet помог тебе пробить стену цензуры — налей автору.

    На водку разрабу (чтобы код компилился): 2202 2084 3646 6800

    На булочки для Ханю (чтобы не кусалась): 2202 2084 3646 6800

    На J7 (для выхода из штопора): 2202 2084 3646 6800