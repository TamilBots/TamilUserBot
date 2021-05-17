# Userbot module for getiing info about any user on Telegram(including you!).

# Copyright (C) 2019 The Raphielscape Company LLC.(who is from raphielscape)

# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.

import html
import os

from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
from userbot.manager.utils import edit_or_reply

from ..utils import admin_cmd, sudo_cmd
from userbot import CMD_HELP

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="whois(?: |$)(.*)"))
async def who(event):
    cat = await edit_or_reply(event, "`Fetching userinfo wait....`")
    if not os.path.isdir(TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user(event)
    try:
        photo, caption = await fetch_info(replied_user, event)
    except AttributeError:
        await edit_or_reply(cat, "`Could not fetch info of that user.`")
        return
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await cat.delete()
    except TypeError:
        await cat.edit(caption, parse_mode="html")


async def get_user(event):
    """ Get the user from argument or replied message. """
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return replied_user


async def fetch_info(replied_user, event):
    """ Get details from the User object. """
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(
            user_id=replied_user.user.id, offset=42, max_id=0, limit=80
        )
    )
    replied_user_profile_photos_count = "User haven't set profile pic"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError:
        pass
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except:
        dc_id = "Couldn't fetch DC ID!"
    common_chat = replied_user.common_chats_count
    username = replied_user.user.username
    user_bio = replied_user.about
    is_bot = replied_user.user.bot
    restricted = replied_user.user.restricted
    verified = replied_user.user.verified
    photo = await event.client.download_profile_photo(
        user_id, TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg", download_big=True
    )
    first_name = (
        first_name.replace("\u2060", "")
        if first_name
        else ("This User has no First Name")
    )
    last_name = last_name.replace("\u2060", "") if last_name else (" ")
    username = "@{}".format(username) if username else ("This User has no Username")
    user_bio = "This User has no About" if not user_bio else user_bio
    caption = "<b><i>USER INFO from Durov's Database :</i></b>\n\n"
    caption += f"<b>👤 First Name:</b> {first_name} {last_name}\n"
    caption += f"<b>🤵 Username:</b> {username}\n"
    caption += f"<b>🔖 ID:</b> <code>{user_id}</code>\n"
    caption += f"<b>🌏 Data Centre ID:</b> {dc_id}\n"
    caption += f"<b>🖼 Number of Profile Pics:</b> {replied_user_profile_photos_count}\n"
    caption += f"<b>🤖 Is Bot:</b> {is_bot}\n"
    caption += f"<b>🔏 Is Restricted:</b> {restricted}\n"
    caption += f"<b>🌐 Is Verified by Telegram:</b> {verified}\n\n"
    caption += f"<b>✍️ Bio:</b> \n<code>{user_bio}</code>\n\n"
    caption += f"<b>👥 Common Chats with this user:</b> {common_chat}\n"
    caption += f"<b>🔗 Permanent Link To Profile:</b> "
    caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
    return photo, caption


@bot.on(admin_cmd(pattern="link(?: |$)(.*)"))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(mention, f"[{tag}](tg://user?id={user.id})")


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj

CMD_HELP.update(
    {
        "Info": """**Plugin : ** `Info`

  ╼•∘ 🅲🅼🅽🅳 ∘•╾  :`.info`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Get User Info__

  ╼•∘ 🅲🅼🅽🅳 ∘•╾  :`.link`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Get User Link__
"""
    }
)


