import asyncio
from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, TreasureBoxEvent
from telegram import Bot

TELEGRAM_TOKEN = "8298214673:AAHZj-eLb43e3FpqLIxb1s5g8e29smcn0x0"
CHAT_ID = "@Babekinbotu"

USERS = [
"sandiq.orusu.gldi",
"aynur1335"
]

bot = Bot(token=TELEGRAM_TOKEN)

async def start_client(username):
    try:
        client = TikTokLiveClient(unique_id=username)

        @client.on(ConnectEvent)
        async def on_connect(event):
            print(f"{username} live qoşuldu")

        @client.on(TreasureBoxEvent)
        async def on_treasure(event):
            msg = f"""
🎁 TikTok Sandıq Tapıldı

👤 User: {username}
⏱ Vaxt: {event.treasure_box.duration} saniyə
👥 İştirak: {event.treasure_box.user_count}

🔗 https://www.tiktok.com/@{username}/live
"""
            await bot.send_message(chat_id=CHAT_ID, text=msg)
            print("Sandıq göndərildi")

        await client.start()

    except Exception as e:
        print(f"Xəta: {e}")

async def main():
    tasks = []
    for user in USERS:
        tasks.append(start_client(user))

    await asyncio.gather(*tasks)

asyncio.run(main())
