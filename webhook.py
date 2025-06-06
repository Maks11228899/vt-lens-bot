from flask import Flask, request
from core.analyzer import analyze_trade
import os
import telebot

app = Flask(__name__)
bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))
CHAT_ID = int(os.getenv("TELEGRAM_CHAT_ID"))
SECRET = os.getenv("WEBHOOK_SECRET")

@app.route("/webhook", methods=["POST"])
def webhook():
    if request.headers.get("X-Telegram-Bot-Api-Secret-Token") != SECRET:
        return "Unauthorized", 403

    data = request.json
    print("🔄 Получен сигнал от TradingView:", data)
    result = analyze_trade(data)
    bot.send_message(CHAT_ID, result)
    return "OK", 200
