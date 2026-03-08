import requests
import time
import threading
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8278790899:AAGTdU-Jysjl4ALt9dwOOyhX5J_HolnaE_A"
CHANNEL = "@babekinbotu"

bot = Bot(token=TOKEN)

admins = [8120551479]

tiktok_users = [
"tiktok",
"livecreator",
"gaminglive"
]

def check_live(username):

    try:
        url = f"https://www.tiktok.com/@{username}/live"

        r = requests.get(url, timeout=10)

        if r.status_code == 200:
            return True

    except:
        return False


def auto_scan():

    while True:

        for user in tiktok_users:

            if check_live(user):

                link = f"https://www.tiktok.com/@{user}/live"

                text = f"""
🔥 TikTok CANLI

👤 {user}

🎁 Sandıq ola bilər

🔗 {link}
"""

                try:
                    bot.send_message(chat_id=CHANNEL, text=text)
                except:
                    pass

        time.sleep(300)


async def sandig(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = "🔥 Tapılan canlılar:\n\n"

    for user in tiktok_users:

        text += f"https://www.tiktok.com/@{user}/live\n"

    await update.message.reply_text(text)


async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id not in admins:
        return

    try:

        username = context.args[0]

        tiktok_users.append(username)

        await update.message.reply_text("TikTok hesab əlavə edildi")

    except:

        await update.message.reply_text("İstifadə: /add username")


async def users(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = "Yoxlanan TikTok hesabları:\n\n"

    for u in tiktok_users:
        text += u + "\n"

    await update.message.reply_text(text)


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("sandig", sandig))
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("users", users))

threading.Thread(target=auto_scan).start()

app.run_polling()
