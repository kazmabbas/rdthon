from telethon import events
import phoenix.client
client = phoenix.client.client
import random

gn = ["""
🌙.     *       ☄️      
🌟   .  *       .         
                       *   .      🛰     .        ✨      *
  .     *   روح نام         🚀     
      .              . . احلام سعيدة 🌙
. *       🌏 بيباي         *
                     🌙.     *       ☄️      
🌟   .  *       .         
                       *   .      🛰     .        ✨      *
"""]

@events.register(events.NewMessage(outgoing=True,  pattern="\.نام"))
async def goodnight(event):
  ggn = random.choice(gn)
  return await event.edit(ggn)
