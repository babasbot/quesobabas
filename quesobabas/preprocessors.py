import logging

logging.basicConfig(level=logging.INFO)

def clean_screen_name(chatbot, statement):
    statement.text = statement.text.replace("@ilovequesobabas", "")
    statement.text = statement.text.replace("@QuesoBabasBot ", "")

    return statement
