# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot('Здесь должен быть Ваш токен бота')


@bot.message_handler(content_types=["text"])
def repeat_all(message):
    bot.send_message(message.chat.id, message.text)
    print(message)


bot.polling(none_stop=True, interval=0)
