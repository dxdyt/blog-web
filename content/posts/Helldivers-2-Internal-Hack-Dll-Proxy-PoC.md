---
title: Helldivers-2-Internal-Hack-Dll-Proxy-PoC
date: 2024-03-09T12:14:28+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1707334459557-e3034e158035?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDk5NTc2MzV8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1707334459557-e3034e158035?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDk5NTc2MzV8&ixlib=rb-4.0.3
---

# [emoisback/Helldivers-2-Internal-Hack-Dll-Proxy-PoC](https://github.com/emoisback/Helldivers-2-Internal-Hack-Dll-Proxy-PoC)

# Helldivers-2-Internal-Hack-Dll-Proxy-PoC

#### This is a PoC that I created to learn about dll proxy using C++ on 64bit application / game.

### Thanks to cfemen and gir489 for all information and CE Tables.

## Feature List
<details>
  <summary>Click to show</summary>
  
  | Cheat | Description |
  |----------|----------|
  | Infinite Health | Makes you invulnerable to most forms of damage |
  | Infinite Grenades | Grenades are always at max capacity |
  | Infinite Grenades (legit) | Grenades decrease, but never drops to zero. Allows you to collect grenade boxes |
  | Infinite Ammunition | Ammunition is always at max capacity |
  | Infinite Ammunition (legit) | Ammunition decreases, but never drops to zero. Allows you to collect supply packs |
  | Infinite Syringes | Syringes are always at max capacity |
  | Infinite Syringes (legit) | Syringes decrease, but never drops to zero. Allows you to collect supply packs |
  | Infinite Stamina | Disables stamina meter. Run forever |
  | Infinite Stratagems | Stratagems are always at maximum capacity. No stratagem cooldown |
  | MoveSpeed x6 | Move 6x faster than usual |
  | Infinite Mission Time | Mission timer does not decrease |
  | No Reload | Magazine capacity does not decrease |
  | Max Resources | Picking up a sample will pick up x500 of each type. There is a max capacity on board your own ship |
  | Add 5 samples | Picking up a sample adds 5 samples to your inventory |
  | No Recoil | Prevents your weapon from having a recoil effect |
  | Infinite Backpack | Backpack 'resource' is never depleted (eg. full ammo, rover no overheat) |
  | Infinite Special Weapon | Special weapon has unlimited ammunition |
  | No Laser Cannon Overheat | Laser cannon can be fired forever without swapping cartridge |
  | Instant Railgun | Arc Thrower and Railgun do not need to be charged for max damage |
  | Show All Map Icons | Simulates radar tower, all POI and objectives shown on the map |
  | No Stationary Turret Overheat | Heavy Machine Gun emplacement does not require cooling down |
  | No Backpack Shield Cooldown | When backpack energy shield is broken, it instantly gets replaced |
  | No Jetpack Cooldown | Jetpack does not require recharging, jump constantly |
  | All Stratagems in Loadout | Enables in-development stratagems, as well as locked stratagems |
  | All Equipment in Armory | Enables in-development, or locked, primary, secondary weapons, and grenades |
  | All Armor in Armory | Enables in-development, or locked armor |
</details>

## How to use
### - Download DLL
Get the latest by clicking the most recent action [here](https://github.com/emoisback/Helldivers-2-Internal-Hack-Dll-Proxy-PoC/actions) and downloading "version" from the artifacts section
### - Extract DLL inside helldivers 2 game folder ( same folder as helldivers2.exe ), and rename it to version.dll
### - Run Game
### - Choose Feature ( Navigate using arrow key to up/down, space for select / unselect )
### - Enter To Applied Feature
### - Happy Cheating

### Doesnt need old exe, you can use latest exe.

## Building 
You don't need to build this in Visual Studio, the most recent versions are posted here: \
https://github.com/emoisback/Helldivers-2-Internal-Hack-Dll-Proxy-PoC/actions \
Because github automatically builds the master branch, you can:
- Fork the repository. 
- Go to the Actions tab and make sure workflow is enabled.
- Make any changes to a file, and github will rebuild the .dll in the Actions tab of that fork.

For example: [https://github.com/DeathWrench/Helldivers-2-Internal-Hack-Dll-Proxy-PoC/actions](https://github.com/emoisback/Helldivers-2-Internal-Hack-Dll-Proxy-PoC/actions) \
As you can see, commits from forks get built by github as long as they're in the master branch.
#### Still if you want to build it yourself in Visual Studio:
![image](https://github.com/DeathWrench/Helldivers-2-Internal-Hack-Dll-Proxy-PoC/assets/45341450/cd8bb59e-72fb-492e-be0d-1a952295e27c)\
![image](https://github.com/DeathWrench/Helldivers-2-Internal-Hack-Dll-Proxy-PoC/assets/45341450/d7ef335a-ff96-48d0-bce6-e6bf2445f264)\
File will be here: \
``Helldivers-2-Internal-Hack-Dll-Proxy-PoC\x64\Release\``**version.dll**
