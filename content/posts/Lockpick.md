---
title: Lockpick
date: 2023-05-08T12:18:22+08:00
draft: False
featuredImage: https://wallpaperhub.app/api/v1/get/12109/0/1080p
featuredImagePreview: https://wallpaperhub.app/api/v1/get/12109/0/1080p
---

# [shchmue/Lockpick](https://github.com/shchmue/Lockpick)

Lockpick
=
Lockpick is a ground-up C++17 rewrite of homebrew key derivation software, namely [kezplez-nx](https://github.com/tesnos/kezplez-nx). It also dumps titlekeys. This will dump all keys through `*_key_05` on firmwares below `6.2.0` and through `*_key_06` on `6.2.0`.

Due to key generation changes introduced in `7.0.0`, Lockpick is not able to dump keys ending in 07 at all. Furthermore, unfortunately the public method to dump `tsec_root_key` is only available on firmware `6.2.0` so `7.x` consoles can only dump through keys ending in 05.

What this software does differently
=
* Dumps `titlekeys` and SD seed
* Dumps all keys through `6.2.0`
* Uses the superfast `xxHash` instead of `sha256` when searching exefs for keys for a ~5x speed improvement
* Gets all possible keys from running process memory - this means no need to decrypt `Package2` at all, let alone decompress `KIP`s
* Gets bis keys and `header_key` without `tsec`, `sbk`, `master_key_00` or `aes` sources. Shoutout to exelix11 for using this method in [SwitchThemeInjector](https://github.com/exelix11/SwitchThemeInjector)! Homebrew devs should be doing this instead of requiring users to provide key files!

Usage
=
1. Use [Hekate v4.5+](https://github.com/CTCaer/hekate/releases) to dump TSEC and fuses:
    1. Push hekate payload bin using [TegraRCMSmash](https://github.com/rajkosto/TegraRcmSmash)/[TegraRCMGUI](https://github.com/eliboa/TegraRcmGUI)/modchip/injector
    2. Using the `VOL` and `Power` buttons to navigate, select `Console info...`
    3. Select `Print fuse info` (_not_ `kfuse info`)
    4. Press `Power` to save fuse info to SD card
    5. Select `Print TSEC keys`
    6. Press `Power` to save TSEC keys to SD card
2. Launch CFW of choice
3. Open `Homebrew Menu`
4. Run `Lockpick`
5. Use the resulting `/switch/prod.keys` file as needed and rename if required by any software you're using

You may instead use [biskeydump](https://github.com/rajkosto/biskeydump) and dump to SD to get all keys prior to the 6.2.0 generation - all keys up to those ending in 05. Lockpick will dump all keys up to that point regardless which firmware it's run on.

Notes
=
* To get keys ending in 06, you must have firmware `6.2.0` installed
* No one knows `package1_key_06`, it's derived and erased fully within the encrypted TSEC payload. While there's a way to extricate `tsec_root_key` due to the way it's used, this is unfortunately not true of the `package1` key
* If for some reason you dump TSEC keys on `6.2.0` and not fuses (`secure_boot_key`) you will still get everything except any of the `package1` or keyblob keys (without `secure_boot_key`, you can't decrypt keyblobs and that's where `package1` keys live)

Building
=
Release built with [libnx release v2.4.0](https://github.com/switchbrew/libnx).

Uses `freetype` which comes with `switch-portlibs` via `devkitPro pacman`:
```
pacman -S libnx switch-portlibs
```
then run:
```
make
```
to build.

Special Thanks
=
* tèsnos! For making [kezplez-nx](https://github.com/tesnos/kezplez-nx), being an all-around cool and helpful person and open to my contributions, not to mention patient with my *enthusiasm*. kezplez taught me an absolute TON about homebrew.
* SciresM for [hactool](https://github.com/SciresM/hactool), containing to my knowledge the first public key derivation *software*, and for `get_titlekeys.py`
* roblabla for the original keys [gist](https://gist.github.com/roblabla/d8358ab058bbe3b00614740dcba4f208) and for believing in our habilities
* The folks in the [ReSwitched](https://reswitched.team/) Discord server for answering my innumerable questions while researching this (and having such a useful chat backlog!)
* The memory reading code from jakibaki's [sys-netcheat](https://github.com/jakibaki/sys-netcheat) was super useful for getting keys out of running process memory
* The System Save dumping methodology from Adubbz' [Compelled Disclosure](https://github.com/Adubbz/Compelled-Disclosure)
* Shouts out to fellow key derivers: shadowninja108 for [HACGUI](https://github.com/shadowninja108/HACGUI), Thealexbarney for [Libhac](https://github.com/Thealexbarney/LibHac), and [rajkosto](https://github.com/rajkosto/) :eyes:
* [misson2000](https://github.com/misson20000) for help with `std::invoke` to get the function timer working
* [Simon](https://github.com/simontime) for the `eticket_rsa_kek` derivation method and for suggesting invoking `spl` for faster titlekey derivation
* [SciresM](https://github.com/SciresM) for the libnx aes library
* The constantly-improving docs on [Switchbrew wiki](https://switchbrew.org/wiki/) and [libnx](https://switchbrew.github.io/libnx/files.html)
* Literally the friends I made along the way! I came to the scene late and I've still managed to meet some wonderful people :) Thanks for all the help testing, making suggestions, and cheerleading!

Licenses
=
* `es` ipc code is from [Tinfoil](https://github.com/Adubbz/Tinfoil) licensed under [MIT](https://github.com/Adubbz/Tinfoil/blob/master/LICENSE)
* `FatFs R0.13c` is located [here](http://elm-chan.org/fsw/ff/00index_e.html) and is licensed under its own [BSD-style license](source/fatfs/LICENSE.txt)
* Simple `xxHash` implementation is from [stbrumme](https://github.com/stbrumme/xxhash) licensed under [MIT](https://github.com/stbrumme/xxhash/blob/master/LICENSE)
* Padlock icon is from [Icons8](https://icons8.com/) licensed under [Creative Commons Attribution-NoDerivs 3.0 Unported](https://creativecommons.org/licenses/by-nd/3.0/)