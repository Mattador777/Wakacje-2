import os
import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import sqlite3

# Pobranie zmiennych środowiskowych
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Konfiguracja logowania
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Witaj! Użyj komend do ustawienia filtrów wyszukiwania.")

def check_offers(update: Update, context: CallbackContext):
    update.message.reply_text("Sprawdzanie ofert...")

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("check", check_offers))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
