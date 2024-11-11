from telethon import events
import time

import phoenix.client
client = phoenix.client.client

@events.register(events.NewMessage(outgoing=True, pattern='\.التنصيب'))
async def alive(event):
		client = event.client
		me = await client.get_me()
		username = me.username
		img = await client.download_profile_photo(username)
		time.sleep(0.5)
		await event.respond(f"""**Foydalanuvchi:** @{username}
**RDTHON USERBOT:** https://t.me/rdthon 

**Developer:** @qqzqqx 
			
v.1.2.0

📥 التثبيت 

$ `pkg update && pkg upgrade`

$ `apt update && apt upgrade`

$ `pkg install git`

$ `pkg install python`

$ `git clone https://github.com/kazmabbas/rdthon.git`

$ `python setup.py`

$ `python main.py`""", file=img)
		await event.message.delete()
