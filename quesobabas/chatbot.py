import logging

logging.basicConfig(level=logging.INFO)

from chatterbot import ChatBot

import os
import redis_storage

def fetch_conversation(uuid):
    conversation_id = redis_storage.connection.get(uuid)

    if conversation_id == None:
        conversation_id = quesobabas.storage.create_conversation()
        redis_storage.connection.set(uuid, conversation_id)

    return int(conversation_id)

quesobabas = ChatBot(
    "quesobabas",
    database=os.environ["DATABASE_PATH"],
    preprocessors=[
        'preprocessors.clean_screen_name'
    ]
)
