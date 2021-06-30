import requests

from userbot.utils import admin_cmd
from userbot.manager.utils import edit_or_reply


newslog = Config.NEWS_CHANNEL_ID


@borg.on(admin_cmd("news (.*)"))
async def _(event):
    if event.fwd_from:
        return
    if Var.NEWS_CHANNEL_ID is None:
        await edit_or_reply(
            event, "`Please ADD NEWS_CHANNEL_ID For This Module To Work`"
        )
        return
    infintyvar = event.pattern_match.group(1)
    main_url = f"https://inshortsapi.vercel.app/news?category={infintyvar}"
    stuber = await edit_or_reply(
        event,
        f"Ok ! Fectching {infintyvar} From inshortsapi Server And Sending To News Channel",
    )
    await stuber.edit("All News Has Been Sucessfully Send To News Channel")
    starknews = requests.get(main_url).json()
    for item in starknews["data"]:
        sedlyf = item["content"]
        img = item["imageUrl"]
        writter = item["author"]
        dateis = item["date"]
        readthis = item["readMoreUrl"]
        titles = item["title"]
        sed1 = img
        sedm = f"**Title : {titles}** \n{sedlyf} \nDate : {dateis} \nAuthor : {writter} \nReadMore : {readthis}"
        await borg.send_file(newslog, sed1, caption=sedm)
