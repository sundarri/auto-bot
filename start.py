from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.types import InputPeerUser

api_id = '2412645'
api_hash = '5ca8ea018c64028ca8849695de0c315a'
session_name = 'my_telegram_session'

client = TelegramClient(session_name, api_id, api_hash)

async def download_media():
    await client.start()

    try:
        # Get the ID of the target chat (your own chat ID)
        my_id = await client.get_me()

        # Use the chat ID obtained in the previous step to download media files
        chat = await client.get_entity(InputPeerUser(my_id.id, access_hash=my_id.access_hash))
        messages = await client.get_messages(chat, limit=100000)

        # Download media files
        for message in messages:
            if message.media:
                await client.download_media(message.media, file='./downloads')
    finally:
        await client.disconnect()

if __name__ == '__main__':
    import asyncio
    asyncio.run(download_media())