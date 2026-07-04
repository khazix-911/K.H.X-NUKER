
<!--

-->

# 💀 K.H.X NUKER v1.0

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/khazix-911/K.H.X-NUKER?style=for-the-badge&color=ff0000)](https://github.com/khazix-911/K.H.X-NUKER/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/khazix-911/K.H.X-NUKER?style=for-the-badge&color=ff6600)](https://github.com/khazix-911/K.H.X-NUKER/network)
[![GitHub issues](https://img.shields.io/github/issues/khazix-911/K.H.X-NUKER?style=for-the-badge&color=ffcc00)](https://github.com/khazix-911/K.H.X-NUKER/issues)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Discord.py](https://img.shields.io/badge/Discord.py-2.3.0%2B-5865F2?style=for-the-badge&logo=discord)](https://github.com/Rapptz/discord.py)
[![License](https://img.shields.io/badge/License-All%20Rights%20Reserved-red?style=for-the-badge)](https://github.com/khazix-911/K.H.X-NUKER)

</div>

---

## 🚀 Overview

**K.H.X-NUKER v1.0** is a lightning-fast Discord automation tool built with Python and powered by parallel execution. Unlike traditional nukers, it leverages asyncio.gather for ultra-low latency and massive concurrency, making it ideal for high-speed server raiding, bulk member management (ban/kick), channel flooding, and webhook spam. Designed for educational testing and server stress evaluation, it features a smart rate limiter that automatically handles Discord's API restrictions, ensuring maximum uptime and minimal failures.

**⚠️ IMPORTANT: This tool is for EDUCATIONAL PURPOSES only. Unauthorized use on servers you don't own is strictly prohibited.**

---

## ✨ Key Features

| Feature | Description |
|:---|:---|
| ⚡ **Hyper Speed** | Advanced parallelism with `asyncio.gather` for instant execution |
| 🔄 **Smart Retry** | Automatic rate limit handling with retry logic |
| 🎯 **11 Powerful Commands** | Complete server destruction and management tools |
| 🎨 **Beautiful UI** | Colored console interface with real-time statistics |
| 🔒 **Protected Members** | Whitelist system to protect specific users |
| 🌐 **Cross-Platform** | Works on Windows, Linux, and macOS |
| 📊 **Live Statistics** | Track every action in real-time |
| 💾 **Webhook Integration** | Advanced webhook spam capabilities |

---

## 📋 Full Command List

### 🔥 Destruction Commands

| # | Command | Description |
|:---|:---|:---|
| **1** | **NUKE** | Full parallel execution - deletes channels, bans members, creates new channels & spams |
| **5** | **Kick All** | Kick every member in the server instantly |
| **6** | **Ban All** | Ban every member in the server instantly |

### ⚙️ Creation Commands

| # | Command | Description |
|:---|:---|:---|
| **2** | **Create Channels** | Mass create text or voice channels with custom names |
| **7** | **Create Roles** | Mass create roles with random colors |

### 🌀 Spam Commands

| # | Command | Description |
|:---|:---|:---|
| **3** | **Spam Channels** | Spam messages in all channels |
| **4** | **Webhook Spam** | Lightning-fast spam via webhooks |
| **10** | **DM All** | Send a DM to every member |

### 🎯 Advanced Commands

| # | Command | Description |
|:---|:---|:---|
| **8** | **Get Admin** | Grant admin role to yourself or all members |
| **9** | **Change Server** | Change server name, icon, and description |
| **11** | **Auto Raid** | Automated raid from config settings |

### 📊 Utility Commands

| # | Command | Description |
|:---|:---|:---|
| **00** | **Exit** | Exit the program |
| **0** | **Change Server** | Switch to another server |

---

## 🚀 Installation

### 📦 Requirements

| Requirement | Version |
|:---|:---|
| **Python** | 3.8 or higher |
| **pip** | Latest version |

### ⚡ Quick Install

```bash
# Clone the repository
git clone https://github.com/khazix-911/K.H.X-NUKER.git
cd K.H.X-NUKER

# Install dependencies
pip install -r requirements.txt

# Run the tool
python main.py
```

### 📦 Manual Installation

```bash
pip install discord.py aiohttp pystyle
```

---

## ⚙️ Configuration

### 📝 config.py Structure

```python
# ============================================================
# K.H.X NUKER v1.0 - Settings File
# Copyright (c) 2026 Khazix-911
# ============================================================

# 🔑 Server Icon
NUKE_ICON_URL = ""  # Put your icon file name here

# 🎨 Embedded Message Settings
EMBED_CONFIG = {
    "title": "",           # Big bold text at the top
    "description": "",     # Main message text
    "color": 0xFF0000,     # Embed color (red by default)
    "fields": [],          # Additional fields
    "image": "",           # Image URL
    "footer": "",          # Footer text
    "message": "",         # Extra text before embed
}

# 📝 Server Changes
SERVER_CONFIG = {
    "new_name": "",        # New server name
    "new_icon": "",        # New server icon URL
    "new_description": "", # New server description
}

# 🔗 Webhook Settings
WEBHOOK_CONFIG = {"default_name": ""}

# 💥 Auto Raid Settings
AUTO_RAID_CONFIG = {
    "num_channels": 20,    # Number of channels to create
    "channel_type": "text", # "text" or "voice"
    "channel_name": "",    # Channel name
    "num_messages": 5,     # Messages per channel
    "message_content": "", # Message content
}

# 🛡️ Protected Members (Won't be banned/kicked)
NO_BAN_KICK_ID = []       # List of user IDs

# 👑 Admin Members (Will get admin role)
ADMIN_IDS = []            # List of user IDs

# 🤖 Bot Status
BOT_PRESENCE = {"type": "playing", "text": ""}

# ⚡ Performance Settings
RATE_LIMIT_DELAY = 0      # 0 = fastest
MAX_CONCURRENT_TASKS = 100

# 📁 Channel Names (For multiple channel names)
CHANNELS_CONFIG = {"names": []}

# 🎭 Role Names (For multiple roles)
ROLES_CONFIG = {"names": []}
```

---

## 🎮 Usage Guide

### ▶️ Running the Tool

```bash
python main.py
```

### 📋 Step-by-Step Process

| Step | Action |
|:---|:---|
| 1️⃣ | Enter your bot token when prompted |
| 2️⃣ | Select a server by number or ID |
| 3️⃣ | View the bot's permissions in the server |
| 4️⃣ | Choose a command from the main menu |
| 5️⃣ | Follow any additional prompts |
| 6️⃣ | Watch the action in real-time |

### 🎮 Console Navigation

| Key | Function |
|:---|:---|
| **1-11** | Select a command |
| **00** | Exit the program |
| **0** | Change server |
| **Enter** | Continue after viewing results |

---

## 📁 File Structure

```
K.H.X-NUKER/
│
├── 📄 main.py              # Main program file
├── 📄 config.py            # Configuration file
├── 📄 requirements.txt     # Python dependencies
├── 📄 README.md            # This documentation
├── 📄 LICENSE              # License agreement
│
└── 📁 data/                # Created automatically
    ├── 📁 logs/            # Log files
    │   └── 📄 YYYY-MM-DD.log
    │
    └── 📁 backups/         # Backup files
        └── 📄 backup_*.json
```

---

## 🛡️ Permissions System

### 🔒 Tiered Access Control

| Level | Access | Description |
|:---|:---|:---|
| 👑 **Whitelisted** | Full Access | Can use all 11 commands |
| ❌ **Others** | No Access | Cannot use the bot |

### 🔐 Permission Checks

```python
# Protected members won't be banned or kicked
if member.id in NO_BAN_KICK_ID:
    printer.member_skipped_whitelist(member.id, member.name)
    continue
```

---

## 📊 Statistics & Logging

### 📈 Real-time Statistics

| Stat | Description |
|:---|:---|
| `channels_deleted` | Total channels deleted |
| `channels_created` | Total channels created |
| `members_banned` | Total members banned |
| `members_kicked` | Total members kicked |
| `messages_sent` | Total spam messages sent |
| `webhooks_created` | Total webhooks created |
| `webhook_messages` | Messages sent via webhooks |
| `roles_created` | Total roles created |
| `dms_sent` | Total DMs sent |
| `admin_granted` | Total admin grants |

### 📝 Logging System

| Type | Location | Format |
|:---|:---|:---|
| 🖥️ **Console** | Real-time display | Colored output |
| 📁 **File** | `data/logs/YYYY-MM-DD.log` | Plain text |

---

## 🔧 Advanced Features

### 🧠 Parallel Execution

```python
async def parallel_execute(tasks, max_concurrent=100):
    """Execute tasks in parallel with rate limiting"""
    semaphore = asyncio.Semaphore(max_concurrent)
    async def bounded_task(task):
        async with semaphore:
            return await task()
    return await asyncio.gather(*[bounded_task(t) for t in tasks])
```

### 🔄 Smart Retry Logic

```python
async def ban_with_retry(member):
    while True:
        try:
            await member.ban(reason="K.H.X NUKER by Khazix-911")
            return True
        except discord.HTTPException as e:
            if e.status == 429:
                retry_after = e.retry_after or 1.0
                await asyncio.sleep(retry_after)
```

---

## 🎯 Examples

### 🎯 Ban All Members

```
[?] Choose: 6
[+] Banning all members...
[+] Banned User1
[+] Banned User2
[-] Skipped Admin (whitelisted)
```

### 🌀 Auto Raid

```
[?] Choose: 11
[!] AUTO RAID - Parallel Execution
[+] Deleted 15 channels
[+] Created 20 channels
[+] Sent 5 messages per channel
```

---

## 📄 License

<div align="center">

**Copyright (c) 2026 Khazix-911**

**All Rights Reserved**

</div>

```
This software and its source code are proprietary and confidential.
No part of this software may be reproduced, distributed, or transmitted
in any form or by any means, without the prior written permission
of the copyright holder.

❌ NO selling
❌ NO modification
❌ NO redistribution without permission
```

---

## 👥 Credits

| Role | Name | GitHub |
|:---|:---|:---|
| **Developer** | **Khazix-911** | [@khazix-911](https://github.com/khazix-911) |

---

## 📞 Contact & Support

| Platform | Link |
|:---|:---|
| 💬 **Discord Server** | [Join Server](https://discord.gg/zrdYErmU6S) |
| 🐙 **GitHub** | [Repository](https://github.com/khazix-911/K.H.X-NUKER) |
| 🐛 **Issues** | [Report Bug](https://github.com/khazix-911/K.H.X-NUKER/issues) |
| ⭐ **Star** | [Star Repository](https://github.com/khazix-911/K.H.X-NUKER) |

---

## 🗳️ Suggest Features

Have an idea for the next version? Open an **Issue** or **Discussion** on GitHub!

**Features being considered for v2.0:**
- [ ] Brainfuck - Infinite channel creation
- [ ] Stealth Mode
- [ ] Multi-token support
- [ ] Server Backup before nuke
- [ ] PDF reports
- [ ] More spam methods

---

<div align="center">

## ⭐ Star this repository if you found it useful!

### Made with ❤️ by Khazix-911

**© 2026 All Rights Reserved**

</div>
