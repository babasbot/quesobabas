import logging

logging.basicConfig(level=logging.INFO)

from chatbot     import quesobabas
from twitter_api import api
from random      import choice

if __name__ == "__main__":
    follower_id = choice(api.followers_ids())
    follower    = api.get_user(follower_id)
    statement   = quesobabas.storage.get_random()

    new_status = "@{} {} #AlbureandoFollowers".format(
        follower.screen_name,
        statement.text
    )

    api.update_status(new_status)
