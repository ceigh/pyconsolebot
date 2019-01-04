import telebot

import config
from core import get_output

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def console(message):
    response = get_output(message.text)
    bot.send_message(message.chat.id, response)


if __name__ == '__main__':
    bot.polling(none_stop=True)
