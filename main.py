import telebot
import os
from core.analyzer import analyze_trade

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = int(os.getenv("TELEGRAM_CHAT_ID"))
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я KolegaTVBot. Используй /вход для анализа точки входа.")

@bot.message_handler(commands=["вход"])
def handle_entry(message):
    result = analyze_trade()
    bot.send_message(message.chat.id, result)

# bot.remove_webhook()
# bot.polling()
