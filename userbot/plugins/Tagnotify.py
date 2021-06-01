from telethon import custom, events
from telethon.tl.types import Channel
from telethon.utils import get_display_name

from userbot.uniborgConfig import Config

if Config.PRIVATE_GROUP_ID:
    NEEDTOLOG = int(Config.PRIVATE_GROUP_ID)
    
if Var.PRIVATE_GROUP_ID is not none:
    @borg.on(
        events.NewMessage(
            incoming=True,
            blacklist_chats=Config.UB_BLACK_LIST_CHAT,
            func=lambda e: (e.mentioned),
        )
    )
    async def all_messages_catcher(e):
        await event.forward_to(Var.TG_BOT_USERNAME)
        x = await borg.get_entity(e.sender_id)
        if x.bot or x.verified:
            return
        y = await borg.get_entity(e.chat_id)
        if y.username:
            yy = f"[{get_display_name(y)}](https://t.me/{y.username})"
        else:
            yy = f"[{get_display_name(y)}](https://t.me/c/{y.id}/{e.id})"
        xx = f"[{get_display_name(x)}](tg://user?id={x.id})"
        msg = f"https://t.me/c/{y.id}/{e.id}"
        if e.text:
            cap = f"{xx} tagged you in {yy}\n\n```{e.text}```\nㅤ"
        else:
            cap = f"{xx} tagged you in {yy}"

        btx = "📨 View Message"

        try:
            if e.text:
                cap = get_string("tagnot_1").format(xx, yy, e.text, msg)
            else:
                cap = get_string("tagnot_2").format(xx, yy, msg)
            await borg.send_message(
                NEEDTOLOG,
                cap,
                link_preview=False,
                buttons=[[custom.Button.url(btx, msg)]],
            )
        except BaseException:
            if e.text:
                cap = get_string("tagnot_1").format(xx, yy, e.text, msg)
            else:
                cap = get_string("tagnot_2").format(xx, yy, msg)
            try:
                await borg.send_message(NEEDTOLOG, cap, link_preview=False)
            except BaseException:
                pass
       else: 
           return
