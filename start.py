from webhook.webhook import app
from telebot import TeleBot
import os

# Установка webhook Telegram-бота
bot = TeleBot(os.getenv("TELEGRAM_TOKEN"))
url = "https://kolega-tv-bot-railway.up.railway.app/webhook"
bot.set_webhook(url=url, secret_token=os.getenv("WEBHOOK_SECRET"))

# Запуск Flask сервера
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
