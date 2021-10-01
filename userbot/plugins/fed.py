#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import asyncio

from telethon.errors import ChatAdminRequiredError
from telethon.errors.rpcerrorlist import MessageTooLongError, YouBlockedUserError
from telethon.tl.functions.users import GetFullUserRequest

from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, CMD_HELP

bot = "@MissRose_bot"

naam = str(ALIVE_NAME)

BOTLOG_CHATID = Config.PRIVATE_GROUP_ID

G_BAN_LOGGER_GROUP = os.environ.get("G_BAN_LOGGER_GROUP", None)
if G_BAN_LOGGER_GROUP:
    G_BAN_LOGGER_GROUP = int(G_BAN_LOGGER_GROUP)

PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", None)
if PRIVATE_GROUP_ID:
    PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)

@borg.on(admin_cmd(pattern="fstat ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit("`Checking...`")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        sysarg = str(previous_message.sender_id)
        user = f"[user](tg://user?id={sysarg})"
    else:
        sysarg = event.pattern_match.group(1)
        user = sysarg
    if sysarg == "":
        await ok.edit(
            "`Give me someones id, or reply to somones message to check his/her fedstat.`"
        )
        return
    else:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat " + sysarg)
                audio = await conv.get_response()
                if "Looks like" in audio.text:
                    await audio.click(0)
                    await asyncio.sleep(2)
                    audio = await conv.get_response()
                    await telebot.send_file(
                        event.chat_id,
                        audio,
                        caption=f"List of feds {user} has been banned in.\n\nCollected using TamilBot.",
                    )
                else:
                    await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await ok.edit("**Error**\n `Unblock` @MissRose_Bot `and try again!")


@borg.on(admin_cmd(pattern="fedinfo ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit("`Extracting information...`")
    sysarg = event.pattern_match.group(1)
    async with borg.conversation(bot) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("/fedinfo " + sysarg)
            audio = await conv.get_response()
            await ok.edit(audio.text + "\n\nFedInfo Excracted by TamilBot")
        except YouBlockedUserError:
            await ok.edit("**Error**\n `Unblock` @MissRose_Bot `and try again!")

@borg.on(admin_cmd("roseinfo ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with borg.conversation(bots) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/info")
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @MissRose_bot `and retry!")
    elif "@" in sysarg:
        async with borg.conversation(bots) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/info " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @MissRose_Bot `and try again!")
    elif "" in sysarg:
        async with borg.conversation(bots) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/info " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @MissRose_Bot `and try again!")

@borg.on(admin_cmd("myfeds ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    async with event.client.conversation(bots) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("/myfeds")
            myfed = await conv.get_response()
            if "file" in myfed.text:
                await fedstat.click(0)
                reply = await conv.get_response()
                await event.client.forward_messages(event.chat_id, reply)
            else:
                await event.client.forward_messages(event.chat_id, myfed)
                await event.delete()
        except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @MissRose_Bot `and try again!")


@borg.on(admin_cmd(pattern="bgban ?(.*)"))
async def _(event):
    if G_BAN_LOGGER_GROUP is None:
        await event.edit("ENV VAR is not set. This module will not work.")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        if r.forward:
            r_from_id = r.forward.from_id or r.from_id
        else:
            r_from_id = r.from_id
        await borg.send_message(
            G_BAN_LOGGER_GROUP,
            "/gban [user](tg://user?id={}) {}".format(r_from_id, reason),
        )
    await event.delete()


@borg.on(admin_cmd(pattern="bungban ?(.*)"))
async def _(event):
    if G_BAN_LOGGER_GROUP is None:
        await event.edit("ENV VAR is not set. This module will not work.")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        r_from_id = r.from_id
        await borg.send_message(
            G_BAN_LOGGER_GROUP,
            "/ungban [user](tg://user?id={}) {}".format(r_from_id, reason),
        )
    await event.delete()


@bot.on(admin_cmd("superfban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Starting a Mass-UnFedBan...")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        FBAN = previous_message.sender_id
    else:
        FBAN = event.pattern_match.group(1)

    if PRIVATE_GROUP_ID:
        chat = PRIVATE_GROUP_ID 
    else:
        chat = await event.get_chat()
    fedList = []
    for a in range(3):
        async with event.client.conversation("@MissRose_bot") as bot_conv:
            await bot_conv.send_message("/start")
            await bot_conv.send_message("/myfeds")
            response = await bot_conv.get_response()
            if "make a file" in response.text:
                await asyncio.sleep(1)
                await response.click(0)
                fedfile = await bot_conv.get_response()
                if fedfile.media:
                    downloaded_file_name = await event.client.download_media(
                        fedfile, "fedlist"
                    )
                    file = open(downloaded_file_name, "r")
                    lines = file.readlines()
                    for line in lines:
                        fedList.append(line[:36])
                else:
                    return
                if len(fedList) == 0:
                    await event.edit(f"Something went wrong. Retrying ({a+1}/3)...")
                else:
                    break
    else:
        await event.edit(f"Error")
    if "You can only use fed commands once every 5 minutes" in response.text:
        await event.edit("Try again after 5 mins.")
        return
    In = False
    tempFedId = ""
    for x in response.text:
        if x == "`":
            if In:
                In = False
                fedList.append(tempFedId)
                tempFedId = ""
            else:
                In = True

        elif In:
            tempFedId += x

    await event.edit(f"UnFbaning in {len(fedList)} feds.")
    try:
        await event.client.send_message(chat, f"/start")
    except:
        await event.edit("PRIVATE_GROUP_ID is incorrect.")
        return
    await asyncio.sleep(3)
    for fed in fedList:
        await event.client.send_message(chat, f"/joinfed {fed}")
        await asyncio.sleep(3)
        await event.client.send_message(chat, f"/feddemoteme {FBAN}")
        await asyncio.sleep(3)
    await event.edit(f"SuperUnFBan Completed. Affected {len(fedList)} feds.")


CMD_HELP.update(
    {
        "fed":

        """╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.sendto category_name`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __will send the replied message to all the chats in give category__

  ╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.fwdto category_name`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __will forward the replied message to all the chats in give category__

  ╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.addto category_name`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __It will add this chat/user/channel to the category of the given name__

  ╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.rmfrom category_name`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __To remove the Chat/user/channel from the given category name__

  ╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.list category_name`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Will show the list of all chats in the given category__

  ╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.listall`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Will show the list of all category names__

  ╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.frmfrom category_name chat_id`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __To force remove the given chat_id from the given category name usefull when you left that chat or banned you there__

  ╼•∘ 🅲🅼🅽🅳 ∘•╾  : `delc category_name`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Deletes the category completely in database__
"""
    }
)



