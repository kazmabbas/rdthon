from telethon import events
import phoenix.client
client = phoenix.client.client
@events.register(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def help(event):
	await event.delete()
	messagelocation = event.to_id
	await event.client.send_message(messagelocation, ("""
**⋆ـ┄─┄─┄─┄RDTHON─┄─┄─┄┄ـ⋆**\n**`.م1`  ➪ اوامــر اليوتـيوب والتـرفيـه**\n**`.م2`  ➪ اوامــر الذكـاء الاصـطنـاعي**\n**`.م3`  ➪ اوامــر الـوقتــي**\n**`.م4`  ➪ اوامــر المجمــوعــه**\n**`.م5`  ➪ اوامــر الخــاص**\n**.م6  ➪ اوامــر المـسح و النـسخ**\n**`.م7`  ➪ اوامــر المـيمـز والاختصارات**\n**`.م8`  ➪ اوامــر الـانتحـال**\n**`.م9`  ➪ اوامــر التســليـه**\n**`.م10` ➪ اوامــر التـقليد والمحاكاة**\n**`.م11` ➪ اوامــر النشــر التلقــائي **\n**`.م12` ➪ اوامــر الاشتــراك الاجبــاري **\n**`.م13` ➪ اوامــر الـذاتيــة و المـقيد**\n**`.م14` ➪ اوامــر الـخطـوط والترجمة **\n**`.م15` ➪ اوامــر الـنطق والتـحميل**\n**`.م16` ➪ اوامــر الحماية والتحويل**
"""))
