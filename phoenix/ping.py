from telethon import events
from datetime import datetime
import phoenix.client
client = phoenix.client.client

@events.register(events.NewMessage(pattern='\.بنك'))
async def ping(event):
    client.parse_mode = "html" 
    start = datetime.now()
    msg = await event.edit("سرعة الانترنيت!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await msg.edit(f"<b>سرعة انترنيتك!!<b/>\n`{ms} ms`")
