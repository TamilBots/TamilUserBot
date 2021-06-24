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

@register(pattern="^.startvc$", groups_only=True)
async def apk(e):
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None

    if not admin and not creator:
        await e.edit("*You Are Not An Admin* 👮🏻‍♂️")
        return
    try:
        await e.client(startvc(e.chat_id))
        await e.edit("`Voice Call Started` 🤗")
    except Exception as ex:
        await e.edit(f"Error : `{ex}`")

@register(outgoing=True, pattern="^.stopvc", groups_only=True)
async def apk(e):
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None

    if not admin and not creator:
        await e.edit("*You Are Not An Admin* 👮")
        return
    try:
        await e.client(stopvc(await get_call(e)))
        await e.edit("`The Group Call Was Stopped` 😥")
    except Exception as ex:
        await e.edit(f"Error : `{ex}`")



@register(outgoing=True, pattern="^.vctag", groups_only=True,)
async def apk(e):
    await e.edit("`Users are called by voice call ...` 😉")
    users = []
    z = 0
    async for x in e.client.iter_participants(e.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await e.client(invitetovc(call=await get_call(e), users=p))
            z += 6
        except BaseException:
            pass
    await e.edit(f"`{z} The User Was Called`")

CmdHelp('groupcall').add_command('startvc' , None, 'Səsli söhbət başladar').add_command('stopvc', None, 'Səsli söhbəti dayandırar').add_command('vctag', None, 'İnsanları səsli söhbətə dəvət edər').add()


