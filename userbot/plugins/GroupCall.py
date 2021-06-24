# TamilBots 2021-22 

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc
from userbot.events import register
from userbot import bot, get_call
from userbot import CMD_HELP


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]

@register(outgoing=True, pattern="^.startvc$")
async def start_voice(event):
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None

    if not admin and not creator:
        await event.edit("*You Are Not An Admin* 👮🏻‍♂️")
        return
    try:
        await event.client(startvc(event.chat_id))
        await event.edit("`Voice Call Started` 🤗")
    except Exception as ex:
        await event.edit(f"Error : `{ex}`")

@register(outgoing=True, pattern="^.stopvc$")
async def stop_voice(event):
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None

    if not admin and not creator:
        await event.edit("*You Are Not An Admin* 👮")
        return
    try:
        await event.client(stopvc(await get_call(event)))
        await event.edit("`The Group Call Was Stopped` 😥")
    except Exception as ex:
        await event.edit(f"Error : `{ex}`")



@register(outgoing=True, pattern="^.vcinvite$")
async def invite_voice(event):
    await event.edit("`Users are called by voice call ...` 😉")
    users = []
    z = 0
    async for x in event.client.iter_participants(e.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await event.client(invitetovc(call=await get_call(event), users=p))
            z += 6
        except BaseException:
            pass
    await event.edit(f"`{z} The User Was Called`")



