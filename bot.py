import asyncio
from telegram import Bot
from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, GiftEvent

TOKEN = "8298214673:AAHZj-eLb43e3FpqLIxb1s5g8e29smcn0x0"
CHANNEL = "@Babekinbotu"

USERS = [
    "username1",
    "username2",
    "username3"
]

bot = Bot(token=TOKEN)

async def start_client(username):
    client = TikTokLiveClient(unique_id=username)

    @client.on(ConnectEvent)
    async def on_connect(event: ConnectEvent):
        await bot.send_message(
            chat_id=CHANNEL,
            text=f"🔴 {username} TikTok live başladı!\nhttps://www.tiktok.com/@{username}/live"
        )

    @client.on(GiftEvent)
    async def on_gift(event: GiftEvent):
        if "Treasure" in event.gift.name:
            await bot.send_message(
                chat_id=CHANNEL,
                text=f"🎁 {username} live-də sandıq çıxdı!\nhttps://www.tiktok.com/@{username}/live"
            )

    await client.start()

async def main():
    tasks = []
    for user in USERS:
        tasks.append(asyncio.create_task(start_client(user)))
    await asyncio.gather(*tasks)

asyncio.run(main())
