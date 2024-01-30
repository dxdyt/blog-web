---
title: PalWorld-NetCrack
date: 2024-01-30T12:16:54+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1684162440652-107bf47ab89b?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDY1ODgwNTZ8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1684162440652-107bf47ab89b?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDY1ODgwNTZ8&ixlib=rb-4.0.3
---

# [swordbluesword/PalWorld-NetCrack](https://github.com/swordbluesword/PalWorld-NetCrack)

# PalWorld-NetCrack
This is the PalWorld network cracking framework
modifying player data in the Player tab
Network cracking in the Exploit tab
# Note: The master branch does not include visual,but In imperfect branch, we'll add something that isn't on the master branch.

# Player Features
- Modify Player Speed
- Modify Player Attack Power
- Modify Player Defense Power
- Infinite Stamina
- Infinite Ammo

# Exploits
- SafeTeleport(You can choose the implementation for TP)  
- HomeTP  
- AnywhereTP(It requires you to manually give a position)  
- ToggleFly  
- DeleteSelf(Warning: After testing, it will delete your data on the server)  
- GodHealth  
- Give EXP (Credit: WoodgamerHD)  
- Give Pal (Credit: Kaotic13)  
- Spawn Pal

# AOBS
> GObjects: `48 8B 05 ? ? ? ? 48 8B 0C C8 4C 8D 04 D1 EB 03`  
> FNames: `48 8D 05 ? ? ? ? EB 13 48 8D 0D ? ? ? ? E8 ? ? ? ? C6 05 ? ? ? ? ? 0F 10`  
> GWorld: `48 8B 1D ?? ?? ?? ?? 48 85 DB 74 33 41 B0`  

## External Library Credits
[Dear ImGui](https://github.com/ocornut/imgui)  
[MinHook](https://github.com/TsudaKageyu/minhook)  
[Dumper7](https://github.com/Encryqed/Dumper-7)  
[DX11-Internal-Base](https://github.com/NightFyre/DX11-ImGui-Internal-Hook)  
