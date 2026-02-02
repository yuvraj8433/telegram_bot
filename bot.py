import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

HF_API = "https://yuvraj8433-autocomplete-model.hf.space//run/predict"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    response = requests.post(
        HF_API,
        json={"data": [user_text]},
        timeout=30
    )

    result = response.json()["data"][0]
    await update.message.reply_text(result)

if __name__ == "__main__":
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    app.add_handler(MessageHandler(filters.TEXT, reply))
    app.run_polling()
