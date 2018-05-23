from constants import TOKEN
from messages import HELLO, CURRENT_WEATHER
from telebot import types
import messages
import database
# pytelegrambotapi
import telebot
import requests


bot = telebot.TeleBot(TOKEN)

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('Breakfast')
itembtn2 = types.KeyboardButton('Lunch')
itembtn3 = types.KeyboardButton('Dinner')
itembtn4 = types.KeyboardButton('Dessert')
markup.row(itembtn1, itembtn2)
markup.row(itembtn3, itembtn4)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, messages.HELLO)
    msg = ''
    for i in database.get():
        msg += str(i)
    bot.send_message(message.chat.id, msg)


#@bot.message_handler(commands=['weather'])
def get_recipe(message):
    # bot.reply_to(message, CURRENT_WEATHER)
    # print(message)
    # bot.send_message(message.chat.id, CURRENT_WEATHER)
    my_message = str(message)
    database.insert({'msg': my_message})
    print('inserted')
    bot.send_message(message.chat.id, "Choose:", reply_markup=markup)


#@bot.message_handler(commands=['photo'])
#def send_photo(message):
#    photo = open('photos/liverpool.jpg', 'rb')
#    bot.send_photo(message.chat.id, photo)
#    photo.close()s

if __name__ == '__main__':
    print('Starting recipe_bot')
    bot.polling()