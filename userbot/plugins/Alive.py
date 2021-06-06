"""Check if tamilBot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# CREDITS: @WhySooSerious, @Sur_vivor

# modified by @saravanakrish
# Re-written by @iMvEtRi
from userbot.utils import admin_cmd
from userbot.uniborgConfig import Config
from userbot import ALIVE_NAME, CMD_HELP

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "TamilUserBot"

PM_IMG = Config.ALIVE_IMAGE
pm_caption = "🤖 **тαмιℓвσт ιѕ:** `ᴏɴʟɪɴᴇ`\n\n"
pm_caption += "⨠ **ѕуѕтємѕ ѕтαтѕ 💻:**\n"
pm_caption += "⨠ **тєℓєтнση νєяѕιση :** `1.15.0` \n"
pm_caption += "⨠ **ρутнση :** `3.7.4` \n"
pm_caption += "⨠ **∂αтαвαѕє ѕтαтυѕ :**  `ꜰᴜɴᴄᴛɪᴏɴᴀʟ`\n"
pm_caption += "⨠ **¢υяяєηт вяαη¢н** : `ᴍᴀꜱᴛᴇʀ`\n"
pm_caption += f"⨠ **νєяѕιση** : `6.5`\n"
pm_caption += f"⨠ **му вσѕѕ** : {DEFAULTUSER} \n\n"
# pm_caption += "⨠ **Heroku Database** : `AWS -\nWorking Properly`💥\n\n"
# pm_caption += "⫸ **License** : [MIT License](github.com/ivetri/tamilbot/blob/master/LICENSE) ✔\n"
# pm_caption += "⫸ **Copyrights** : © By [TAMIL🤖BOT](https://github.com/IVETRI/TamilBot) 👨🏻‍💻\n\n"
pm_caption += "•☆•»»**[🇮🇳 тαмιℓвσтѕ 🇮🇳]**(https://t.me/TamilBots)««•☆•"


@borg.on(admin_cmd(pattern=r"alive"))
async def tamilbot(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()

@borg.on(admin_cmd(pattern=r"sudoalive", allow_sudo=True))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`என்னைப் பயன்படுத்தியதற்கு நன்றி🤖")

@borg.on(admin_cmd(outgoing=True, pattern="repo"))
async def repo(event):
    if event.fwd_from:
        return
    tgbotname = Var.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(tgbotname, "repo")
    await response[0].click(event.chat_id)
    await event.delete()

CMD_HELP.update(
    {
        "Alive":
        """╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.alive`\
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  Check your bot is alive or not.\
  ╼•∘ 🅲🅼🅽🅳 ∘•╾  : `.repo`\
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  get repository of TamilBot.\
  """

    }
)
