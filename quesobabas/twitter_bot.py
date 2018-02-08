import logging

logging.basicConfig(level=logging.INFO)

from chatbot     import fetch_conversation
from chatbot     import quesobabas
from tweepy      import StreamListener
from tweepy      import Stream
from twitter_api import api
from twitter_api import auth

class BotStreamListener(StreamListener):
    def on_status(self, status):
        conversation_id = fetch_conversation(status.user.id)
        statement       = quesobabas.get_response(status.text, conversation_id)

        status_reply = "@{} {}".format(status.user.screen_name, statement.text)

        api.update_status(status_reply, in_reply_to_status_id=status.id)

if __name__ == '__main__':
    listener = Stream(auth, BotStreamListener())
    listener.filter(track=["@ilovequesobabas"])
