from gpytranslate import Translator
from telethon import events

translator = Translator()
tr_status = {}

@events.register(events.NewMessage(outgoing=True, pattern=".مترجم (.*)"))
async def start_translate(event):
    if event.fwd_from:
        return
    lang = event.pattern_match.group(1).strip()
    tr_status[event.sender_id] = lang
    await event.edit(f"**تم تفعيل المترجم إلى اللغة: {lang}**", parse_mode="md")

@events.register(events.NewMessage)
async def auto_translate(event):
    if event.fwd_from:
        return
    sender_id = event.sender_id
    if sender_id in tr_status:
        lang = tr_status[sender_id]
        try:
            translated = await translator(event.message.message, targetlang=lang)
            await event.edit(translated.text, parse_mode="md")
        except Exception as exc:
            print(f"خطأ في الترجمة: {exc}")

@events.register(events.NewMessage(outgoing=True, pattern=r"\.ايقاف المترجم$"))
async def stop_translate(event):
    if event.fwd_from:
        return
    sender_id = event.sender_id
    if sender_id in tr_status:
        del tr_status[sender_id]
        await event.edit("**تم إيقاف المترجم.**", parse_mode="md")
