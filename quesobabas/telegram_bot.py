import logging

logging.basicConfig(level=logging.INFO)

from chatbot      import fetch_conversation
from chatbot      import quesobabas
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram     import ChatAction

import os
import re

def handle_message(bot, update):
    if update.message.chat.type != "private" and re.search(r'@QuesoBabasBot', update.message.text) is None:
        return()

    bot.send_chat_action(
        chat_id=update.message.chat_id,
        action=ChatAction.TYPING
    )

    conversation_id = fetch_conversation(update.message.chat_id)
    statement = quesobabas.get_response(update.message.text, conversation_id)

    bot.send_message(
        chat_id=update.message.chat_id,
        text=statement.text,
        reply_to_message_id=update.message.message_id
    )

if __name__ == "__main__":
    updater = Updater(token=os.environ["TELEGRAM_API_KEY"])

    message_handler = MessageHandler(Filters.all, handle_message)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()
