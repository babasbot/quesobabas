import logging

logging.basicConfig(level=logging.INFO)

from chatterbot.trainers import ChatterBotCorpusTrainer
from chatbot             import quesobabas

if __name__ == '__main__':
    quesobabas.set_trainer(ChatterBotCorpusTrainer)
    quesobabas.train("./data/spanish/conversations.yml")
