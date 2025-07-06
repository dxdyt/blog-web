---
title: toutatis
date: 2025-07-06T12:32:33+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1750250522370-2c874a8814b2?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTE3NzYzMDR8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1750250522370-2c874a8814b2?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTE3NzYzMDR8&ixlib=rb-4.1.0
---

# [megadose/toutatis](https://github.com/megadose/toutatis)

# Toutatis
👋 Hi there! For any professional inquiries or collaborations, please reach out to me at:
megadose@protonmail.com

📧 Preferably, use your professional email for correspondence. Let's keep it short and sweet, and all in English!

Toutatis is a tool that allows you to extract information from instagrams accounts such as e-mails, phone numbers and more </br>
For BTC Donations : 1FHDM49QfZX6pJmhjLE5tB2K6CaTLMZpXZ
## 💡 Prerequisite
[Python 3](https://www.python.org/downloads/release/python-370/)

## 🛠️ Installation
### With PyPI

```pip install toutatis```

### With Github

```bash
git clone https://github.com/megadose/toutatis.git
cd toutatis/
python3 setup.py install
```

## 📚 Usage:

### Find information from a username

```
toutatis -u username -s instagramsessionid
```

### Find information from an Instagram ID

```
toutatis -i instagramID -s instagramsessionid
```

## 📈 Example

```
Informations about     : xxxusernamexxx
Full Name              : xxxusernamesxx | userID : 123456789
Verified               : False | Is buisness Account : False
Is private Account     : False
Follower               : xxx | Following : xxx
Number of posts        : x
Number of tag in posts : x
External url           : http://example.com
IGTV posts             : x
Biography              : example biography
Public Email           : public@example.com
Public Phone           : +00 0 00 00 00 00
Obfuscated email       : me********s@examplemail.com
Obfuscated phone       : +00 0xx xxx xx 00
------------------------
Profile Picture        : https://scontent-X-X.cdninstagram.com/
```

## 📚 To retrieve the sessionID
![](https://files.catbox.moe/1rfi6j.png)

## Thank you to :

- [EyupErgin](https://github.com/eyupergin)
- [yazeed44](https://github.com/yazeed44)
