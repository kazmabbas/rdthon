from telethon import events
import phoenix.client
client = phoenix.client.client

@events.register(events.NewMessage(outgoing=True,  pattern="\.فاك"))
async def fuck(event):
	await event.edit("┏━┳┳┳━┳┳┓\n┃━┫┃┃┏┫━┫┏┓\n┃┏┫┃┃┗┫┃┃┃┃\n┗┛┗━┻━┻┻┛┃┃\n┏┳┳━┳┳┳┓┏┫┣┳┓\n┣┓┃┃┃┃┣┫┃┏┻┻┫\n┃┃┃┃┃┃┃┃┣┻┫┃┃\n┗━┻━┻━┻┛┗━━━┛")
