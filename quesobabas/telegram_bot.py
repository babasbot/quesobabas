import logging

logging.basicConfig(level=logging.INFO)

from chatbot      import fetch_conversation
from chatbot      import quesobabas
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

import os

def handle_message(bot, update):
    conversation_id = fetch_conversation(update.message.chat_id)

    statement = quesobabas.get_response(update.message.text, conversation_id)

    bot.send_message(chat_id=update.message.chat_id, text=statement.text)

if __name__ == "__main__":
    updater = Updater(token=os.environ["TELEGRAM_API_KEY"])

    message_handler = MessageHandler(Filters.all, handle_message)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()
