import asyncio, subprocess
import time, re, io
from userbot import bot, BOTLOG, BOTLOG_CHATID, CMD_HELP
from telethon import events, functions, types
from telethon.events import StopPropagation
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.channels import LeaveChannelRequest, CreateChannelRequest, DeleteMessagesRequest
from collections import deque
from telethon.tl.functions.users import GetFullUserRequest
from userbot.events import register
from userbot.utils import admin_cmd

@borg.on(admin_cmd("leave"))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`நான் இந்த குழுவை விட்டு வெளியேறுகிறேன்!🚶 🚶 🚶`")
        time.sleep(3)
        if '-' in str(e.chat_id):
            await bot(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('`இது ஒரு குழு அல்ல`')

@borg.on(admin_cmd("hm"))
#@register(outgoing=True, pattern="^;__;$")
async def fun(e):
    t = ";__;"
    for j in range(10):
        t = t[:-1] + "_;"
        await e.edit(t)

@borg.on(admin_cmd("oof"))
#@register(outgoing=True, pattern="^Oof$")
async def Oof(e):
    t = "Oof"
    for j in range(15):
        t = t[:-1] + "of"
        await e.edit(t)

@borg.on(admin_cmd("cry"))
#@register(outgoing=True, pattern="^.cry$")
async def cry(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(;´༎ຶД༎ຶ)")

@borg.on(admin_cmd("fp"))
#@register(outgoing=True, pattern="^.fp$")
async def facepalm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("🤦‍♂")

@borg.on(admin_cmd("moon"))
#@register(outgoing=True, pattern="^.mmoon$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)

@borg.on(admin_cmd("source"))
#@register(outgoing=True, pattern="^.source$")
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("https://github.com/Ivetri/TamilBot")
        
@borg.on(admin_cmd("readme"))
#@register(outgoing=True, pattern="^.readme$")
async def reedme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("https://github.com/Ivetri/TamilBot/blob/master/README.md")



@borg.on(admin_cmd("heart"))		
#@register(outgoing=True, pattern="^.heart$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("❤️🧡💛💚💙💜🖤"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
		
@borg.on(admin_cmd("king"))
#@register(outgoing=True, pattern="^.king$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("👉🤴🏻👉🙂👉😎"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)

		
CMD_HELP.update(
    {
        "Extra":

        """╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.leave`
 ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Leave a Chat__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.hm`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾   __You try it!__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.cry`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Send face palm emoji.__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.moon`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾ __Bot will send a cool moon animation.__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.clock`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾ __Bot will send a cool clock animation.__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.readme`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾ __Reedme.__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.source`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾ __Gives the source of your userbot__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.myusernames`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __List of Usernames owned by you.__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.oof`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Same as ;__; but ooof__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.earth`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Sends Earth animation__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.heart`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Try and you'll get your emotions back__

╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.king`
╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Be The Real King__
"""
    }
)
