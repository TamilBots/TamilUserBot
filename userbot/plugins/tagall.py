""".tagall Plugin for @UniBorg"""
from telethon import events
from userbot.utils import admin_cmd
from userbot import CMD_HELP

@borg.on(admin_cmd(pattern="tagall"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "@tagall"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, 100):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()


CMD_HELP.update(
    {
        "tagall": """**Plugin : **`tagall`  

   •  **Syntax : **`.tagall`
   •  **Function : **__tags recent 100 persons in the group may not work for all__ 
 """
    }
)
