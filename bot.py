from telethon import TelegramClient, events
import asyncio
import logging
logging.basicConfig(level=logging.WARNING)

api_id = 21562655 # replace numbers with your api_id
api_hash = '82a353e4cf209ae679b537c1fff17c9c' # replace numbers with your api_hash

client = TelegramClient("Upload", api_id, api_hash) # replace yourbotname
client.start()

from_chat1 = 4085915110 # replace with your chat ID
to_chat1 = 4017435093 # replace with your chat ID
from_chat2 = 4085915110 # replace with your chat ID
to_chat2 = 1886369052 # replace with your chat ID
from_chat3 = 4085915110 # replace with your chat ID
to_chat3 = 4099212202 # replace with your chat ID
from_chat4 = 4085915110 # replace with your chat ID
to_chat4 = 4090020882 # replace with your chat ID
from_chat5 = 4085915110 # replace with your chat ID
to_chat5 = 4092111681 # replace with your chat ID
from_chat6 = 4085915110 # replace with your chat ID
to_chat6 =  4092111681 # replace with your chat ID
from_chat7 = 4085915110 # replace with your chat ID
to_chat7 =  4092111681 # replace with your chat ID

async def get_chat_id(title):
  async for dialog in client.iter_dialogs():
    if dialog.title == title:
      return dialog.id

@client.on(events.NewMessage)
async def my_event_handler(event):
  chat = await event.get_chat()
  if chat.id == from_chat1:
    await client.forward_messages(to_chat1, event.message)
  if chat.id == from_chat2:
    await client.forward_messages(to_chat2, event.message)
  if chat.id == from_chat3:
    await client.forward_messages(to_chat3, event.message)
  if chat.id == from_chat4:
    await client.forward_messages(to_chat4, event.message)
  if chat.id == from_chat5:
    await client.forward_messages(to_chat5, event.message)
  if chat.id == from_chat6:
    await client.forward_messages(to_chat6, event.message)
  if chat.id == from_chat7:
    await client.forward_messages(to_chat7, event.message)
asyncio.get_event_loop().run_forever()