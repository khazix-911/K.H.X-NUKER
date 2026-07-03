# ============================================================
# K.H.X NUKER v1.0 - Settings File
# Copyright (c) 2026 Khazix-911
# All Rights Reserved
# ============================================================
# ⚠️ IMPORTANT:
# This tool is for EDUCATIONAL PURPOSES only.
# Redistribution, selling, or modification is STRICTLY PROHIBITED.
# ============================================================

# ============================================================
# 1. Server Icon
# ============================================================
# Put your image file name here (must be in the same folder)
# Example: "my-icon.png"
NUKE_ICON_URL = ""

# ============================================================
# 2. Embedded Message (The fancy message sent to channels)
# ============================================================
EMBED_CONFIG = {
    "title": "",  # Big bold text at the top
    "description": "",  # Main message text
    "color": 0xFF0000,  # Color of the embed (red by default)
    "fields": [],  # Small boxes with text (leave empty)
    "image": "",  # Image URL to show in the embed
    "footer": "",  # Small text at the bottom
    "message": "",  # Extra text before the embed
}

# ============================================================
# 3. Server Changes (Rename, Change Icon, Change Description)
# ============================================================
SERVER_CONFIG = {
    "new_name": "",  # New server name
    "new_icon": "",  # New server icon (image URL)
    "new_description": "",  # New server description (shown at the top)
}

# ============================================================
# 4. Webhook Settings
# ============================================================
WEBHOOK_CONFIG = {"default_name": ""}  # Name that appears on webhook messages

# ============================================================
# 5. Auto Raid Settings (Automatic attack)
# ============================================================
AUTO_RAID_CONFIG = {
    "num_channels": 20,  # How many channels to create
    "channel_type": "text",  # "text" or "voice"
    "channel_name": "name",  # Name of the new channels
    "num_messages": 5,  # How many messages to send per channel
    "message_content": "test @here @everyone",  # The message to send
}

# ============================================================
# 6. Protected Members (These users will NOT be banned/kicked)
# ============================================================
# Put Discord User IDs here, separated by commas
# Example: [123456789, 987654321]
NO_BAN_KICK_ID = []

# ============================================================
# 7. Admin Members (These users will get admin role)
# ============================================================
# Put Discord User IDs here
ADMIN_IDS = []

# ============================================================
# 8. Bot Status (What appears under the bot's name)
# ============================================================
BOT_PRESENCE = {"type": "playing", "text": ""}  # "watching", "listening", "playing"

# ============================================================
# 9. Performance Settings
# ============================================================
RATE_LIMIT_DELAY = 0  # Wait time between actions (0 = fastest)
MAX_CONCURRENT_TASKS = 100  # How many things to do at once

# ============================================================
# 10. Channel Names (For creating multiple channels with different names)  (its very important btw :)
# ============================================================
CHANNELS_CONFIG = {
    "names": [
        "name",
        "name",
        "name",
        "name",
        "name",
    ]
}

# ============================================================
# 11. Role Names (For creating multiple roles)
# ============================================================
ROLES_CONFIG = {"names": []}  # Example: ["Admin", "Mod", "VIP"]
