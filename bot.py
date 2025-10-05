from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import os

TOKEN = os.environ.get("TOKEN", "8204561199:AAHP0NoLkk1FtChxoehpfC8FRKphF7GUsGo")
PRESIDENT_CHAT_ID = int(os.environ.get("PRESIDENT_CHAT_ID", "1159623437"))

async def start(update: Update, context):
    await update.message.reply_text(
        "👋 Привет! Хочешь, чтобы школа стала лучше?\n"
        "Напиши своё предложение или жалобу — я передам это президенту школы.\n"
        "Всё абсолютно анонимно ✅"
    )

async def handle_message(update: Update, context):
    text = update.message.text
    await context.bot.send_message(chat_id=PRESIDENT_CHAT_ID, text=f"Новое предложение:\n{text}")
    with open("suggestions.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")
    await update.message.reply_text("Спасибо! Твоё предложение отправлено анонимно ✅")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
