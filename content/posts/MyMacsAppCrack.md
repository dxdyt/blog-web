---
title: MyMacsAppCrack
date: 2023-06-11T12:15:55+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1684777621503-dac77147f93b?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2ODY0NTY4NjV8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1684777621503-dac77147f93b?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2ODY0NTY4NjV8&ixlib=rb-4.0.3
---

# [QiuChenlyOpenSource/MyMacsAppCrack](https://github.com/QiuChenlyOpenSource/MyMacsAppCrack)


# <p align="center">macOS Apps Inject Plugin</p>

<p align="center">K'ed By QiuChenly(秋城落叶)</p>
<p align="center">为我的Mac独奏MVP凯歌</p>
<p align="center">Powered By 青海摇</p>
<p align="center">更新日期 2023.06.11</p>
<p align="center"><a href="https://github.com/QiuChenly/MyMacsAppCrack/blob/main/CN.md">中文</a> | <a href="https://github.com/QiuChenly/MyMacsAppCrack/blob/main/EN.md">English</a></p>

# <p align="center">版权申明/免责声明</p>

<details><summary>Proclaim & Announcement</summary>

本项目仅交流学习软件安全技术使用，不会发布任何形式的成品App，不收任何人钱，各位谨防受骗。

本项目主要目的是为了证明macOS上软件安全漏洞，在此致谢开发这些软件的厂商，如果您认为这侵犯了您的合法权益，我将会删除与您相关的任何代码。

不要将本项目研究成果进行**传播**破坏软件公司的利益，所有法律责任由传播者独自承担，作者从未为任何破解软件传播组织提供过任何形式的技术支持，不支持不赞同不理解传播盗版软件这种违法行为。

因使用者传播者传播破解软件导致的任何法律责任与包括但不仅限于引起系统故障 财产损失等问题作者概不负责。

如果您觉得作者侵犯了您的合法权益，请致信********@qq.com此邮箱地址，我将删除与您利益相关的代码和文件。
</details>

## <p align="center">查询作者的成分</p>
<details>
<summary>点击查看作者的精神状态</summary>

女👊主义者，爱狗人士，高技术力舔狗。

b站抽象小鬼，烂梗之王，话题终结者。

贴吧黄牌老东西，v8元老，孙笑川吧老东西。

柯洁铁粉，七海娜娜米结晶人，冬雪莲男友粉，Otto棍孝子。

顶级雏草姬，举办塔菲喵，举办塔菲谢谢喵。

火星包包孝子，引流之主EQQA炮车没🐎。

青海社会摇2023代传人，但是不穿豆豆鞋紧身衣。

西安摇强劲对手，苏南张诗尧，青海摇集大成者。

U R B B R,G R O U GAY!
</details>

## <p align="center">点击上方的中文/英文查看具体使用方法,或者翻到本页面下面查看我编写的使用说明</p>

&nbsp;&nbsp;每次github文件更新后要及时下载更新, 我希望看到的是大家愉快的使用我的智慧成果而不是有小可爱拿旧版本文件问我为什么激活不了新版本，那我倒是要问问你，为什么不下载新的补丁文件？

&nbsp;&nbsp;然后还有Dinner加群专门问我为什么不能激活新版本的App，你拿着清朝的剑斩本朝的官我都懒得喷你了。

&nbsp;&nbsp;都用破解软件了连SIP都不会关的dinner滚一边，有不要脸还来问我SIP怎么关的我上来就骂。你可以不知道怎么关但是连百度都不会用那确实低能，这种人我建议你别用macOS了，你不适合用电脑。

# 代码开源
本项目所使用的注入Dylib文件源代码已经基于GPLV3协议开源，欢迎关注&提交Pull Requests。
地址: https://github.com/QiuChenlyOpenSource/macOS-InjectPluginCode

# 重构InjectLib版本已支持M系/Intel处理器
新项目地址: https://github.com/QiuChenlyOpenSource/InjectLib
本项目已经不再更新，请关注新项目。

# <center>注入补丁支持的App列表一览 </center>

数字上标可点击查看注入方法 下载链接点击会跳转到官方下载链接.

<details>
<summary>必看！点我查看关于不要Codesign App和关闭SIP的说明</summary>
<pre>

注入完成后千万不要删除补丁文件，软件运行时还是需要依赖这个补丁文件的！

本补丁支持的所有app只需要注入进去即可，不要自作聪明去Codesign破坏原始app的完整签名，这样会丢失App的权限和功能缺失。

最简单的例子：CleanMyMac X多少人自作聪明注入完我的补丁然后去codesign整个App？最后无限弹出权限请求，还有状态栏组件不解锁？然后还认为是我的问题，我只能说，脑子不需要可以捐了。本篇使用说明通篇tmd就没叫你们codesign过！

注入完补丁打不开App提示崩溃的自己先看看关没关macOS SIP再来提issues。大部分App必须关闭SIP才能在注入后正常运行，很多人不关SIP还想用破解软件我只能说你在脱裤子放屁。老子利用的就是nmd关掉SIP后动态注入了App内存修改的激活代码，不然你tm以为老子怎么做到的？不关SIP老子怎么注入进App内存？怎么修改代码？动动脑子行吗各位。

不要听风就是雨，要有自己的主观思考意识。
</pre>
</details>

| App名称                                             | 支持的版本             | 下载链接                                                                                                          |破解原因|
|-----------------------------------------------------|---------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Omi 录屏专家[^omi_recording_pro]                    | v1.2.4(2023020802)  | MacAppStore                                                                                                      |随便破破|
| Omi NTFS 磁盘专家 Pro[^omi_ntfs]                    | v1.2.3 (2023020701) | [官方下载链接](https://cdn.zh.okaapps.com/resource/download/NTFS-Pro-Installer.pkg)                       |随便破破|
| Fig Player[^fig_player]                             | v1.3.0(2023051702)  | MacAppStore                                                                                                      |随便破破|
| Bandizip365[^bandizip365]                           | v7.22               | [MacAppStore](https://apps.apple.com/cn/app/bandizip-365-%E5%8E%8B%E7%BC%A9%E5%92%8C%E8%A7%A3%E5%8E%8B%E7%BC%A9/id1596426184?mt=12)                                                                                                      |随便破破|
| Macs Fan Control[^macs_fan_control]                 | v1.5.15             | [官方下载链接](https://crystalidea.com/downloads/macsfancontrol.zip)                                      |随便破破|
| Record it Pro[^record_it_pro]                       | v1.7.6              | MacAppStore                                                                                                        |随便破破|
| PlistEdit Pro[^plistedit_pro]                       | v1.10b1             | Here                                                                                                            |随便破破|
| Sublime Text Dev[^sublimetext]                      | v4149               | [官方下载链接](https://download.sublimetext.com/sublime_text_build_4149_mac.zip)                          |随便破破|
| CleanMyMac X[^cmm]                               | v4.13.4           | [官方下载链接](https://dl.devmate.com/com.macpaw.CleanMyMac4/CleanMyMacX.dmg)                             |随便破破|
| App Cleaner & Uninstaller[^app_cleaner_uninstaller] | v8.1.4                | [官方下载链接](https://download.nektony.com/download/app-cleaner-uninstaller/app-cleaner-uninstaller.dmg) |随便破破|
| PopClip[^popclip]                                   | v2022.12            | [官方下载链接](https://pilotmoon.com/downloads/PopClip-2022.12.zip)                                       |随便破破|
| MWeb Pro[^mwebpro]                                  | v4.4.4 - 直接通杀后续版本             | [官方下载链接](https://mweb-1256924220.cos.accelerate.myqcloud.com/MWebPro441.dmg)                        |随便破破|
| Ulysses[^ulysses]                                   | v29.4               | MacAppStore                                                                                                      |随便破破|
| iShot[^ishot]                                       | v2.3.4              | MacAppStore                                                                                                      |国产App之光，谨此致敬🫡|
| AutoSwitchInput[^autoswitch]                        | v2.2.1              | MacAppStore                                                                                                      |随便破破|
| SuperRightKey[^irightmouse]                         | v2.2.3              | MacAppStore                                                                                                      |随便破破|
| 解优2[^bestzip2]                         | v1.6.1              | [MacAppStore](https://apps.apple.com/cn/app/%E8%A7%A3%E4%BC%98-2-%E4%B8%93%E4%B8%9A%E7%9A%84-7z-rar-zip-%E8%A7%A3%E5%8E%8B%E7%BC%A9%E5%B7%A5%E5%85%B7/id1525983573?mt=12)                                                                                                      |UI 很好看|
| OmniPlayer[^omniPlayer]                         | v2.1.0 (2023032801)              | [MacAppStore](https://apps.apple.com/cn/app/omni-player-%E9%AB%98%E6%B8%85%E5%BD%B1%E9%9F%B3%E6%92%AD%E6%94%BE%E5%99%A8/id1470926410?mt=12)                                                                                                      |UI 很好看|
| Filmage Screen[^FilmageScreen]                         | v1.4.7              | [官方下载链接](https://pdfreaderpro.oss-cn-shanghai.aliyuncs.com/downloads/FilmageScreen.dmg)                                                                                                      |那天正好比较无聊而已|
| Xmind[^xmind]                                       | v23.05.2661 Win/Mac 通杀版         | [官方下载链接](https://xmind.cn/download/)                                       |随便破破|
|Navicat Premium[^Navicat] |v16.1.10 - 直接通杀后续版本|[MacAppStore](https://apps.apple.com/cn/app/navicat-premium-16/id1594061654?mt=12)|Navicat重度用户表示不破不立|
|Infuse Pro[^Infuse] |v7.5.4|[MacAppStore](https://apps.apple.com/cn/app/infuse-%E6%99%BA%E8%83%BD%E8%A7%86%E9%A2%91%E6%92%AD%E6%94%BE%E5%99%A8/id1136220934)|App做的很好 但下一秒正版授权就是我的了|
|Parallels Desktop[^pd18] |v18.3.0-53606|[官方下载链接](https://download.parallels.com/desktop/v18/18.3.0-53606/ParallelsDesktop-18.3.0-53606.dmg)|Mac平台最强大的虚拟机 没有之一|
|Surge Enterprise[^surge] |v5.1.1 (2264)|[官方下载链接](https://dl.nssurge.com/mac/v5/Surge-5.1.1-2264-6f04d8ac1bbf1c91178a09124e45e37e.zip)|App做的很好 但下一秒正版企业授权就是我的了 一定要指定的版本!|
|Microsoft Office 365 Excel/PowerPoint/Word[^excel365] |v16.73|[MacAppStore](https://apps.apple.com/cn/app/microsoft-excel/id462058435?mt=12)|全球最牛逼的产品|
|Adobe 全系破解 | N/A |官方Creative Cloud中下载|设计领域最牛逼的产品，补丁支持的解锁版本在下面有说明|
|Affinity 全家桶破解 | 2.1.0 | Mac AppStore 下载 | 设计领域比较牛逼的产品，补丁支持的解锁版本在下面有说明 |
| Effie | 2.7.1 | [官方下载链接](https://download.effie.co/effie/effie-2.7.1.dmg) | Markdown良心国产软件 希望大家支持正版 |

## 指南
<details>
<summary>对非专业IT人士</summary>

我一点都没学过软件，你说的操作步骤我根本看不懂啊！

好，那我就在此认认真真的跟你讲一遍怎么用.
1. 下载zip压缩包:
    ![](media/16819809573287.jpg)
2. 解压得到:
    ![](media/16819809983900.jpg)
3. 找到某个目标app,查看注入位置:
    ![](media/16819811321427.jpg)
    跳转到对应说明
    ![](media/16819810903366.jpg)
4. 这里iShot举例，第一步根据上面Copy后面的文件路径复制一份原文件备用，macOS会自动加"_副本"这三个字在后面，这里的PTHotkey文件被复制到PTHotkey_副本。
5. 第二步打开终端输入:
    ![](media/16819812468264.jpg)
    输入sudo+空格+拖入insert_dylib文件+空格+拖入dylib文件+空格。注意是全路径！！不是文件名！！ 
    最后看起来如下所示：
    ![](media/16819815456397.jpg)
    错误示范:
    ![](media/16819815924314.jpg)
6. 鼠标按图示的顺序把第一步复制好的文件拖到终端里,如下:
    ![](media/16819818525680.jpg)

    “_副本”结尾的文件放在前面，然后后面加上空格再跟上原文件。

    按下回车重新打开App即可。所有操作的文件全都是完整路径，下方注入说明写的不详细请参考这里。

    一定要用鼠标拖入到终端上，而不要偷懒自作聪明复制文件路径粘贴到终端上去！
    
    楼主看到这种自作聪明的小可爱都笑嘻了。

    **有些app文件名有空格**你单纯复制路径是不会自动转义的！
    千万要记住是 **直!接!用!** 鼠标拖动文件到终端上！他会自动加上空格！
</details>

<details>
<summary>对IT专业人士</summary>
搞技术的终端都会用吧？

```
sudo insert_dylib文件完整路径 libInlineInjectPlugin.dylib文件完整路径 /Appxxx/xxx/xxx副本 /Appxxx/xxx/xxx
```
回车并重新打开app即可。
</details>


<details>
<summary>补充说明</summary>
写这么多跟技术有关的一句没有，全在解决跟技术无关的操作问题。你要是实在用不了就别用了，自己dinner不要觉得别人跟你一样dinner。

还有，版本更新快不快取决于我能不能第一时间发现新版本并patch，如果我没有更新你就别升级，升级完了我都没发布升级补丁，有什么用？
</details>

### 注入补丁是否安全?

至少比你下的TNT破解版安全。
部分破解过程可以看过来:
1. [How To Crack Macs Fan Control?](./howtocrack.md)

2. [52破解论坛](https://www.52pojie.cn/forum.php?mod=forumdisplay&fid=5&filter=typeid&typeid=377)

### 怎么破解?

点击App名称上面的数字上标1,2...17----然后看下方的提示.

如何体验正版?表格中的app右侧上方有数字上标，点击可查看对应的体验办法。

# QQ吹牛群 
群号已经删除 别找了 避免被说成引流

【烟Distance】
靠近我一点，别理我那么远～oh～
可是雪～豹～已失联～

# Affinity 全系破解
注入文件: 都是liblibxml.dylib
/Applications/Affinity\ Publisher\ 2.app/Contents/Frameworks/liblibxml.dylib
/Applications/Affinity\ Designer\ 2.app/Contents/Frameworks/liblibxml.dylib
/Applications/Affinity\ Photo\ 2.app/Contents/Frameworks/liblibxml.dylib

注入示例:
sudo insert_dylib /你的目录！！不要直接复制执行本shell！/libInlineInjectPlugin.dylib /Applications/Affinity\ Photo\ 2.app/Contents/Frameworks/liblibzlib_副本.dylib /Applications/Affinity\ Photo\ 2.app/Contents/Frameworks/liblibzlib.dylib

支持版本:
Mac AppStore 2.1.0

# Adobe 全系破解

省流:

除了有特殊说明的 App，其他App都是找到App文件里面的AdobeAGM.framework/Versions/A/AdobeAGM 这个文件注入进去。

特殊说明 - 不能注入到AdobeAGM中的App:
1. Adobe XD
2. 无

```
Adobexxxxx.app/Contents/Frameworks/AdobeAGM.framework/Versions/A/AdobeAGM

意思就是让你去App目录下找到这个文件所在的位置，一般都在Frameworks里面.
```

下方没有列出来的版本表示暂不支持。

另外，补丁只支持Intel Mac，M1/M2电脑据群友反馈说打开Rosseta可以运行，你们自己测试吧。

参考注入代码: 

看不懂的换个脑子就好了
```shell
sudo insert_dylib的全路径 libInlineInjectPlugin.dylib的全路径 Adobexxxxx.app/Contents/Frameworks/AdobeAGM.framework/Versions/A/AdobeAGM副本 Adobexxxxx.app/Contents/Frameworks/AdobeAGM.framework/Versions/A/AdobeAGM
```

<details>
<summary>Adobe全家桶中具体支持解锁的App版本和注入说明</summary>

## Adobe XD 版本 56.1.12.1

注入文件: /Applications/Adobe\ XD/Adobe\ XD.app/Contents/Frameworks/nanopb.framework/Versions/A/nanopb
```
sudo insert_dylib /Users/qiuchenly/你的文件夹路径！！！不要直接复制本Shell！！！/libInlineInjectPlugin.dylib /Applications/Adobe\ XD/Adobe\ XD.app/Contents/Frameworks/nanopb.framework/Versions/A/nanopb_副本 /Applications/Adobe\ XD/Adobe\ XD.app/Contents/Frameworks/nanopb.framework/Versions/A/nanopb
```

## Adobe Audition 2023 23.3

注入文件: /Applications/Adobe\ Audition\ 2023/Adobe\ Audition\ 2023.app/Contents/Frameworks/AdobeAGM.framework/Versions/A/AdobeAGM
```
sudo insert_dylib /Users/qiuchenly/你的文件夹路径！！！不要直接复制本Shell！！！/libInlineInjectPlugin.dylib /Applications/Adobe\ Audition\ 2023/Adobe\ Audition\ 2023.app/Contents/Frameworks/AdobeAGM.framework/Versions/A/AdobeAGM_副本 /Applications/Adobe\ Audition\ 2023/Adobe\ Audition\ 2023.app/Contents/Frameworks/AdobeAGM.framework/Versions/A/AdobeAGM
```

## Adobe Illustrator 27.5.0

注入文件: AdobeAGM.framework/Versions/A/AdobeAGM
文件和注入方式跟Adobe Audition 2023一样，略。

## Adobe Dreamweaver 2021 21.3.0.15593

同上。

## Adobe AfterEffects 23.4

```shell
sudo /你的文件完整路径/insert_dylib /你的文件完整路径/libInlineInjectPlugin.dylib /Applications/Adobe\ After\ Effects\ 2023/Adobe\ After\ Effects\ 2023.app/Contents/Frameworks/AdobeAGM.framework/Versions/A/AdobeAGM_副本 /Applications/Adobe\ After\ Effects\ 2023/Adobe\ After\ Effects\ 2023.app/Contents/Frameworks/AdobeAGM.framework/Versions/A/AdobeAGM
```
同上。

## Adobe PremierePro 23.4

```shell
sudo /你的文件完整路径/insert_dylib /你的文件完整路径/libInlineInjectPlugin.dylib /Applications/Adobe\ Premiere\ Pro\ 2023/Adobe\ Premiere\ Pro\ 2023.app/Contents/Frameworks/AdobeAGM.framework/Versions/A/AdobeAGM_副本 /Applications/Adobe\ Premiere\ Pro\ 2023/Adobe\ Premiere\ Pro\ 2023.app/Contents/Frameworks/AdobeAGM.framework/Versions/A/AdobeAGM
```
同上。

## Adobe Animate 2023 23.0.1
同上。

## Adobe Media Encoder 2023 23.4

```shell
sudo /你的文件完整路径/insert_dylib /你的文件完整路径/libInlineInjectPlugin.dylib /Applications/Adobe\ Media\ Encoder\ 2023/Adobe\ Media\ Encoder\ 2023.app/Contents/Frameworks/AdobeAGM.framework/Versions/A/AdobeAGM_副本 /Applications/Adobe\ Media\ Encoder\ 2023/Adobe\ Media\ Encoder\ 2023.app/Contents/Frameworks/AdobeAGM.framework/Versions/A/AdobeAGM
```
同上。

## Adobe Lightroom Classic 12.3
Lrc有时候会抽风，似乎只有网络请求正常情况下才会走我的hook逻辑，看各位脸了。
同上。

## Adobe PhotoShop 24.5
同上。

## Adobe PhotoShop 24.6 Beta
同上。

## Adobe InCopy 18.3.0.50
同上。

## Adobe InDesign 18.3.0.50
同上。

## Adobe Acrobat 23.001.20143
同上。
注意这个App有一个Adobe Acrobat Distiller 应用程序，Distiller这个App里面同样的文件注入进去即可使用。
这个 App 比较特殊，最近两个版本没有破解完整，大家不要用。等什么时候看不到这句话了就说明能用了。



</details>

# 注入小贴士

[^pd18]: Parallels Desktop 18
    1. 执行 sh install_parallels.sh 并输入管理员权限。
    2. ok。

[^surge]: Surge完整企业授权
    一定要打开测试版本更新到我指定的最新版本！
    1. 复制/Applications/Surge.app/Contents/Frameworks/MMMarkdown.framework/Versions/A/MMMarkdown为/Applications/Surge.app/Contents/Frameworks/MMMarkdown.framework/Versions/A/MMMarkdown_副本 备用。
    2. sudo 你的文件夹路径！！！不要直接复制本Shell！！！/insert_dylib 你的文件夹路径！！！不要直接复制本Shell！！！/libInlineInjectPlugin.dylib /Applications/Surge.app/Contents/Frameworks/MMMarkdown.framework/Versions/A/MMMarkdown_副本 /Applications/Surge.app/Contents/Frameworks/MMMarkdown.framework/Versions/A/MMMarkdown
    3. Ok。

[^excel365]: Office Excel 365/Office PowerPoint 365/Office Word 365
    1. Copy /Applications/Microsoft Excel.app/Contents/Frameworks/FluentUI.framework/Versions/A/FluentUI to /Applications/Microsoft Excel.app/Contents/Frameworks/FluentUI.framework/Versions/A/FluentUI的副本
    2. sudo insert_dylib /Users/qiuchenly/你的文件夹路径！！！不要直接复制本Shell！！！/libInlineInjectPlugin.dylib /Applications/Microsoft\ Excel.app/Contents/Frameworks/FluentUI.framework/Versions/A/FluentUI的副本 /Applications/Microsoft\ Excel.app/Contents/Frameworks/FluentUI.framework/Versions/A/FluentUI
    3. ok.

[^Infuse]: Infuse Pro
    1. Copy /Applications/Infuse.app/Contents/Frameworks/GZIP.framework/Versions/A/GZIP to /Applications/Infuse.app/Contents/Frameworks/GZIP.framework/Versions/A/GZIP的副本.
    2. sudo insert_dylib /你的文件夹路径！！！不要直接复制本Shell！！！/libInlineInjectPlugin.dylib /Applications/Infuse.app/Contents/Frameworks/GZIP.framework/Versions/A/GZIP的副本 /Applications/Infuse.app/Contents/Frameworks/GZIP.framework/Versions/A/GZIP
    3. ok.

[^Navicat]: Navicat Premium
    1. Copy /Applications/Navicat Premium.app/Contents/Frameworks/NAVTabBarView.framework/Versions/A/NAVTabBarView to /Applications/Navicat Premium.app/Contents/Frameworks/NAVTabBarView.framework/Versions/A/NAVTabBarView的副本.
    2. sudo insert_dylib /你的文件夹路径！！！不要直接复制本Shell！！！/libInlineInjectPlugin.dylib /Applications/Navicat\ Premium.app/Contents/Frameworks/NAVTabBarView.framework/Versions/A/NAVTabBarView的副本 /Applications/Navicat\ Premium.app/Contents/Frameworks/NAVTabBarView.framework/Versions/A/NAVTabBarView
    3. ok.

[^FilmageScreen]: FilmageScreen
    1. Copy /Applications/Filmage Screen.app/Contents/Frameworks/KMDrawViewSDK_Mac.framework/Versions/A/KMDrawViewSDK_Mac to /Applications/Filmage Screen.app/Contents/Frameworks/KMDrawViewSDK_Mac.framework/Versions/A/KMDrawViewSDK_Mac的副本
    2. sudo insert_dylib /你的文件夹路径！！！不要直接复制本Shell！！！/libInlineInjectPlugin.dylib /Applications/Filmage\ Screen.app/Contents/Frameworks/KMDrawViewSDK_Mac.framework/Versions/A/KMDrawViewSDK_Mac的副本 /Applications/Filmage\ Screen.app/Contents/Frameworks/KMDrawViewSDK_Mac.framework/Versions/A/KMDrawViewSDK_Mac
    3. ok.

[^omniPlayer]: OmniPlayer

    1. Copy /Applications/OmniPlayerStore.app/Contents/Frameworks/XADMaster.framework/Versions/A/XADMaster to /Applications/OmniPlayerStore.app/Contents/Frameworks/XADMaster.framework/Versions/A/XADMaster的副本
    2. sudo insert_dylib /Users/qiuchenly/...YOUR...FILE...PATH...!!!.../libInlineInjectPlugin.dylib /Applications/OmniPlayerStore.app/Contents/Frameworks/XADMaster.framework/Versions/A/XADMaster的副本 /Applications/OmniPlayerStore.app/Contents/Frameworks/XADMaster.framework/Versions/A/XADMaster
    3. ok.

[^bestzip2]: 解优2

    这是一个我接触MacBook就开始眼馋的App。因为当时刚出来一代的时候AppStore霸榜第一的实力足以让我垂涎欲滴。
    1. Copy the file /Applications/BestZip 2.app/Contents/Frameworks/JSONModel.framework/Versions/A/JSONModel to /Applications/BestZip 2.app/Contents/Frameworks/JSONModel.framework/Versions/A/JSONModel的副本
    2. ```sudo insert_dylib /Users/qiuchenly/...YOUR...PATH...!!!!.../libInlineInjectPlugin.dylib /Applications/BestZip\ 2.app/Contents/Frameworks/JSONModel.framework/Versions/A/JSONModel的副本 /Applications/BestZip\ 2.app/Contents/Frameworks/JSONModel.framework/Versions/A/JSONModel```
    3. Ok.Open it and read activation's from Preference.

[^ulysses]: Ulysses

    1. Copy /Applications/UlyssesMac.app/Contents/Frameworks/KissXML.framework/Versions/A/KissXML to /Applications/UlyssesMac.app/Contents/Frameworks/KissXML.framework/Versions/A/KissXML\_副本
    2. ```bash
       sudo insert_dylib libInlineInjectPlugin.dylib <your_xxx_副本_file> <your_xxx_file>
       ```

[^xmind]: Xmind

    1. modify some javascript.
    2. about crack the app for windows/Macos  more infomation pls read it: :https://www.52pojie.cn/thread-1786811-1-1.html
    3. The asar file so big, i can't upload it.

[^app_cleaner_uninstaller]: App Cleaner & Uninstaller

    1. Copy /Applications/App Cleaner 8.app/Contents/Frameworks/NektonyFallManager.framework/Versions/A/NektonyFallManager to /Applications/App Cleaner 8.app/Contents/Frameworks/NektonyFallManager.framework/Versions/A/NektonyFallManager\_副本
    2. ```bash
       sudo insert_dylib libInlineInjectPlugin.dylib <your_xxx_副本_file> <your_xxx_file>
       ```

[^mwebpro]: MWeb Pro

    1. Copy /Applications/MWeb Pro.app/Contents/Frameworks/Sparkle.framework/Versions/B/Sparkle to /Applications/MWeb Pro.app/Contents/Frameworks/Sparkle.framework/Versions/B/Sparkle\_副本
    2. ```bash
       sudo insert_dylib libInlineInjectPlugin.dylib <your_xxx_副本_file> <your_xxx_file>
       ```

[^popclip]: PopClip

    1. Copy /Applications/PopClip.app/Contents/Frameworks/ShortcutRecorder.framework/Versions/A/ShortcutRecorder to /Applications/PopClip.app/Contents/Frameworks/ShortcutRecorder.framework/Versions/A/ShortcutRecorder\_副本
    2. ```bash
       sudo insert_dylib libInlineInjectPlugin.dylib <your_xxx_副本_file> <your_xxx_file>
       ```

[^ishot]: iShot Pro

    1. Copy /Applications/iShot.app/Contents/Frameworks/PTHotKey.framework/Versions/A/PTHotKey to /Applications/iShot.app/Contents/Frameworks/PTHotKey.framework/Versions/A/PTHotKey\_副本
    2. ```bash
       sudo insert_dylib libInlineInjectPlugin.dylib <your_xxx_副本_file> <your_xxx_file>
       ```

[^autoswitch]: AutoSwitchInput

    1. Copy /Applications/AutoSwitchInput.app/Contents/Frameworks/PTHotKey.framework/Versions/A/PTHotKey to /Applications/AutoSwitchInput.app/Contents/Frameworks/PTHotKey.framework/Versions/A/PTHotKey\_副本
    2. ```bash
       sudo insert_dylib libInlineInjectPlugin.dylib <your_xxx_副本_file> <your_xxx_file>
       ```

[^irightmouse]: iRightMouse

    1. Copy /Applications/iRightMouse.app/Contents/MacOS/iRightMouse to /Applications/iRightMouse.app/Contents/MacOS/iRightMouse\_副本
    2. ```bash
       sudo insert_dylib libInlineInjectPlugin.dylib <your_xxx_副本_file> <your_xxx_file>
       ```

[^omi_recording_pro]: Omi 录屏专家

    1. Clear Permission: tccutil reset ScreenCapture com.mac.utility.screen.recorder
    2. Download App from Mac App Store.
    3. copy /Applications/OmniRecorder.app/Contents/MacOS/OmniRecorder to /Applications/OmniRecorder.app/Contents/MacOS/OmniRecorder\_副本.
    4. Execute the code:
       ```bash
       sudo insert_dylib libInlineInjectPlugin.dylib <your_xxx_副本_file> <your_xxx_file>
       ```
       <your*xxx*副本*file> is /Applications/OmniRecorder.app/Contents/MacOS/OmniRecorder*副本
       <your_xxx_file> is /Applications/OmniRecorder.app/Contents/MacOS/OmniRecorder

[^record_it_pro]: Record it

    1. extract app from "Record it.zip"
    2. copy to application folder.
    3. codesign yourself.
       sudo codesign -f -s - --timestamp=none /Applications/Record it.app

    4. if you won't get Recording Screen Permission, Terminate execute:
       tccutil reset ScreenCapture

[^bandizip365]: Bandizip365 Crack

    1. Download App from Mac App Store.
    2. Copy the file /Applications/Bandizip365.app/Contents/MacOS/Bandizip365 to /Applications/Bandizip365.app/Contents/MacOS/Bandizip365\_副本.
    3. Execute the code:
       ```bash
       sudo insert_dylib libInlineInjectPlugin.dylib <your_xxx_副本_file> <your_xxx_file>
       ```
       <your*xxx*副本*file> is /Applications/Bandizip365.app/Contents/MacOS/Bandizip365*副本
       <your_xxx_file> is /Applications/Bandizip365.app/Contents/MacOS/Bandizip365

[^plistedit_pro]: PlistEdit Pro

    1. In Terminal execute the code for your self sign:
       `bash
sudo codesign -f -s - --timestamp=none /Applications/PlistEdit Pro.app
`
       YOU CAN USE IT:"PlistEdit Pro v1.10b1.zip" extract copy to "Applications" and "codesign -f -s - --timestamp=none /Applications/PlistEdit Pro.app", you get it!

[^macs_fan_control]: Macs Fan Control

    1. copy "/Applications/Macs Fan Control.app/Contents/Frameworks/QtMacExtras.framework/Versions/5/QtMacExtras" file to "/Applications/Macs Fan Control.app/Contents/Frameworks/QtMacExtras.framework/Versions/5/QtMacExtras\_副本".
    2. in Terminal execute the code for your self sign:
       ```bash
       sudo insert_dylib libInlineInjectPlugin.dylib /Applications/Macs Fan Control.app/Contents/Frameworks/QtMacExtras.framework/Versions/5/QtMacExtras_副本 /Applications/Macs Fan Control.app/Contents/Frameworks/QtMacExtras.framework/Versions/5/QtMacExtras
       ```
    3. Crack Over!

[^sublimetext]: Sublime Text Dev v4148 Crack

    Target File: /Applications/Sublime Text.app/Contents/MacOS/sublime_text

    Crack Point: `verify_signature(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> const&, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> const&, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> const&)
__Z16verify_signatureRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_S7_ proc near`

    1. Copy And Backup the file.
    2. Open 'sublime_text' file use 'Hex Friends',find:
        0249FFC6 EBE15B41 5C415E41 5F5DC355 4889E5
    3. Replace The Hashcode with: 
        0249FFC6 EBE15B41 5C415E41 5F5DC36A 0158C3

        ![](./Sublime%20Text%204147.png)
        
    4. Open Sublime Text v4147, input the fake Licence get activation:

        ```
        ----- BEGIN LICENSE -----
        秋城落叶@52pojie.com
        Unlimited User License
        EA7E-8888
        88888888888888888888888888888888
        88888888888888888888888888888888
        88888888888888888888888888888888
        88888888888888888888888888888888
        88888888888888888888888888888888
        88888888888888888888888888888888
        88888888888888888888888888888888
        88888888888888888888888888888888
        ------ END LICENSE ------
        ```
    5. [Maybe Not Need]in Terminal execute the code for your self sign
       ```bash
       sudo codesign -f -s - --timestamp=none /Applications/Sublime\ Text.app
       ```

[^cmm]: Clean My Mac Crack

    1. First copy the Announcements to Announcements\_副本
    2. Download app from website, normal install, open and upgrade to latest test version.
    3. just run command in Terminal:
       ```bash
       sudo insert_dylib libInlineInjectPlugin.dylib <your_xxx_副本_file> <your_xxx_file>
       ```
       <your*xxx*副本*file> is /Applications/CleanMyMac\ X.app/Contents/Frameworks/Announcements.framework/Versions/A/Announcements*副本
       <your_xxx_file> is /Applications/CleanMyMac\ X.app/Contents/Frameworks/Announcements.framework/Versions/A/Announcements

[^omi_ntfs]: Omi NTFS 磁盘专家

    1. First copy the /Applications/OmniRecorder.app/Contents/MacOS/OmniRecorder to /Applications/OmniRecorder.app/Contents/MacOS/OmniRecorder\_副本
    2. Download app from website, normal install, open and upgrade to latest test version.
    3. just run command in Terminal:
       ```bash
       sudo insert_dylib libInlineInjectPlugin.dylib <your_xxx_副本_file> <your_xxx_file>
       ```

[^fig_player]: Fig Player

    1. First copy the /Applications/PotPlayerX.app/Contents/Frameworks/XADMaster.framework/Versions/A/XADMaster to /Applications/PotPlayerX.app/Contents/Frameworks/XADMaster.framework/Versions/A/XADMaster\_副本
    2. Download app from website, normal install, open and upgrade to latest test version.
    3. just run command in Terminal:
       ```bash
       sudo insert_dylib libInlineInjectPlugin.dylib <your_xxx_副本_file> <your_xxx_file>
       ```
