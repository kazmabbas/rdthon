from telethon import events 
import phoenix.client
from phoenix import emojify
client = phoenix.client.client


@events.register(events.NewMessage(outgoing=True, pattern="\.ايموجي"))
async def itachi(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit_or_reply(event, "اكتب في النص..")
        return
    result = ""
    for a in args:
        a = a.lower()
        if a in emojify.oofman:
            char = emojify.offman[emojify.oofman.index(a)]
            result += char
        else:
            result += a
    await event.edit(result)
    
