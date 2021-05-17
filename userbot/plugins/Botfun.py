# rewritten by @saravanakrish

from telegraph import Telegraph
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP
from userbot.utils import admin_cmd
from userbot.manager.utils import edit_delete, edit_or_reply

telegraph = Telegraph()
mee = telegraph.create_account(short_name="tamilbot")


@borg.on(admin_cmd(pattern="purl ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply("**Reply to any document.**")
        return
    reply_message = await event.get_reply_message()
    chat = "@FiletolinkTGbot"
    reply_message.sender
    await eor(event, "**Making public url...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1011636686)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await eor(event, "```Please unblock me (@FiletolinkTGbot) u Nigga```")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )


@borg.on(admin_cmd(pattern="reader ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await eor(event, "**Reply to a URL.**")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await eor(event, "**Reply to a url message.**")
        return
    chat = "@chotamreaderbot"
    reply_message.sender
    await eor(event, "**Making instant view...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=272572121)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await eor(event, "```Please unblock me (@chotamreaderbot) u Nigga```")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )


@borg.on(admin_cmd(pattern="aud ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await eor(event, "```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await eor(event, "```reply to media message```")
        return
    chat = "@audiotubebot"
    reply_message.sender
    if reply_message.sender.bot:
        await eor(event, "```Reply to actual users message.```")
        return
    await event.reply("```Processing```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=507379365)
            )
            await event.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await eor(event, "```Please unblock @AudioTubeBot and try again```")
            return
        await event.delete()
        await event.client.send_file(event.chat_id, response.message.media)


@borg.on(admin_cmd(pattern="instadl ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply("**Reply to a instagram url.**")
        return
    reply_message = await event.get_reply_message()
    chat = "@instadownloadingbot"
    reply_message.sender
    await eor(event, "**Downloading the post...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1310260390)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await eor(event, "```Please unblock me (@instadownloadingbot) u Nigga```")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )


@borg.on(admin_cmd(pattern="xogame$"))
async def gamez(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()


@borg.on(admin_cmd(pattern="whisper ?(.*)"))
async def wspr(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr)
    await tap[0].click(event.chat_id)
    await event.delete()


@borg.on(admin_cmd(pattern="checkspam ?(.*)"))
async def _(event):
    bot = "@SpamBot"
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/start")
                audio = await conv.get_response()
                final = ("See if you are limited..\n(c)@TamilSupport", "")
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await eor(event, "**Error:** `unblock` @spambot `and retry!")


@borg.on(admin_cmd(pattern="gitdl ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply("**Reply to a github repo url.**")
        return
    reply_message = await event.get_reply_message()
    chat = "@gitdownloadbot"
    reply_message.sender
    await eor(event, "**Downloading the repository...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1282593576)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await eor(event, "```Please unblock me (@gitdownloadbot) u Nigga```")
            return
        await event.delete()
        x = await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )
        await x.edit(
            "Downloaded by [TeleBot](t.me/TeleBotSupport), via @gitdownloadbot"
        )


@borg.on(admin_cmd(pattern="imusic ?(.*)"))
async def tel(event):
    if event.fwd_from:
        return
    botusername = "@vkmusic_bot"
    tele = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, tele)
    await tap[0].click(event.chat_id)
    await event.delete()


@borg.on(admin_cmd(pattern="font ?(.*)"))
async def _(event):
    bot = "@fontsgenbot"
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        await event.edit("Give me a text to sylize pero")
    else:
        async with borg.conversation(bot) as conv:
            try:
                x = await edit_or_reply(event, "`Making the text stylish..`")
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message(sysarg)
                audio = await conv.get_response()
                title = "Stylish Fonts"
                topaste = audio.text
                topaste = topaste.replace("\n", "<br>")
                response = telegraph.create_page(title, html_content=topaste)
                link = response["path"]
                await x.edit(
                    f"**Normal Text** - {sysarg}\n**Stylised text** - [here](https://telegra.ph/{link})",
                    link_preview=False,
                )
            except YouBlockedUserError:
                await x.edit("**Error:** `unblock` @fontsgenbot `and retry!")


                
CMD_HELP.update(
    {
        "Botfun": """**Plugin : ** `Botfun`

  ╼•∘ 🅲🅼🅽🅳 ∘•╾  :`.purl <reply to file>`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __ Get a direct download link of that file/doc/pic/vid\__
  
  ╼•∘ 🅲🅼🅽🅳 ∘•╾  :`.reader <reply to url>`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Get an instant view of that site.__
  
  ╼•∘ 🅲🅼🅽🅳 ∘•╾  :`.aud <reply to youtube link>`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Get audio from that youtube video__
  
  ╼•∘ 🅲🅼🅽🅳 ∘•╾  :`.instadl <reply to instagram url>`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Download that instagram post__
  
  ╼•∘ 🅲🅼🅽🅳 ∘•╾  :`.xogame`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __XO-Game__
  
  ╼•∘ 🅲🅼🅽🅳 ∘•╾  :`.whisper <message> <target username/id>`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Send a whisper message to that person.__
  
  ╼•∘ 🅲🅼🅽🅳 ∘•╾  :`.checkspam`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __ Check if you are limited.__
  
  ╼•∘ 🅲🅼🅽🅳 ∘•╾  :`.gitdl <reply to github link>`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Download the main branch of that git repo.__
  
  ╼•∘ 🅲🅼🅽🅳 ∘•╾  :`.imusic <song name>`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Get the song.__
  
  ╼•∘ 🅲🅼🅽🅳 ∘•╾  :`.font`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __Generate some stylish fonts.__
