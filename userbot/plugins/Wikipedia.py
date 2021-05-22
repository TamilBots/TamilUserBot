"""WikiPedia.ORG
Syntax: .wikipedia Query"""
"""WikiMedia.ORG
Syntax: .wikimedia Query"""
from telethon import events
import wikipedia
import requests
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="wikipedia (.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Processing ...")
    input_str = event.pattern_match.group(1)
    result = ""
    results = wikipedia.search(input_str)
    for s in results:
        page = wikipedia.page(s)
        url = page.url
        result += f"> [{s}]({url}) \n"
    await event.edit("WikiPedia **Search**: {} \n\n **Result**: \n\n{}".format(input_str, result))
    
    
@borg.on(admin_cmd(pattern="wikimedia (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    url = "https://commons.wikimedia.org/w/api.php?action={}&generator={}&prop=imageinfo&gimlimit={}&redirects=1&titles={}&iiprop={}&format={}".format(
        "query",
        "images",
        "5",
        input_str,
        "timestamp|user|url|mime|thumbmime|mediatype",
        "json"
    )
    r = requests.get(url).json()
    result = ""
    for key in results:
        current_value = results[key]
        pageid = current_value["pageid"]
        title = current_value["title"]
        imageinfo = current_value["imageinfo"][0]
        timestamp = imageinfo["timestamp"]
        user = imageinfo["user"]
        descriptionurl = imageinfo["descriptionurl"]
        mime = imageinfo["mime"]
        mediatype = imageinfo["mediatype"]
        result += """\n
        pageid: {}
        title: {}
        timestamp: {}
        user: [{}]({})
        mime: {}
        mediatype: {}
        """.format(pageid, title, timestamp, user, descriptionurl, mime, mediatype)
    await event.edit("**Search**: {} \n\n **Results**: {}".format(input_str, result))
