from telethon import events
import asyncio

@events.register(events.NewMessage(pattern=".(احم|غبي)"))  # Match either .احم or .غبي
async def sexy(event):
    if event.fwd_from:
        return

    if event.pattern_match.group(1) == "احم":
        animation_interval = 2
        animation_ttl = range(0, 15)
        await event.edit("تنبيه العرض اباحي")
        animation_chars = [
            "قصة 💘 قصيرة ",
            "  😐             😕 \n/👕\         <👗\ \n 👖               /|",    
            "  😉          😳 \n/👕\       /👗\ \n  👖            /|",
            "  😚            😒 \n/👕\         <👗> \n  👖             /|",
            "  😍         ☺️ \n/👕\      /👗\ \n  👖          /|",
            "  😍          😍 \n/👕\       /👗\ \n  👖           /|",
            "  😘   😊 \n /👕\/👗\ \n   👖   /|",
            " 😳  😁 \n /|\ /👙\ \n /     / |",    
            "😈    /😰\ \n<|\      👙 \n /🍆    / |",
            "😅 \n/(),✊😮 \n /\         _/\\/|",
            "😎 \n/\\_,__😫 \n  //    //       \\",
            "😖 \n/\\_,💦_😋  \n  //         //        \\",
            "  😭      ☺️ \n  /|\   /(👶)\ \n  /!\   / \ ",
            "النهاية ترااااا 😂..."
        ]
    elif event.pattern_match.group(1) == "غبي":
        animation_interval = 1
        animation_ttl = range(14)
        await event.edit("`الزم هذا عقلك و اشمرة بالزبل`")
        animation_chars = [
            "᯽︙ عقلك ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
            "᯽︙ عقلك ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
            "᯽︙ عقلك ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
            "᯽︙ عقلك ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
            "᯽︙ عقلك ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
            "᯽︙ عقلك ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
            "᯽︙ عقلك ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
            "᯽︙ عقلك ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
            "᯽︙ عقلك ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
            "᯽︙ عقلك ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
            "᯽︙ عقلك ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
            "᯽︙ عقلك ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
            "᯽︙ عقلك ➡️ 🧠\n\n           (> ^_^)>🗑",
            "᯽︙ عقلك ➡️ 🧠\n\n           <(^_^ <)🗑",
        ]
    else:
        return  # Ignore any other commands

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % len(animation_chars)])
