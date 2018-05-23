import logging
from breakfast import * 
from lunch import *
from dinner import *
from dessert import *
from drink import *
from salad import *
from additional import *

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Hello, I am a recipe-bot. Please choose on of the item below:', reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query
    
    reply_markup1 = InlineKeyboardMarkup(keyboard1)
    reply_markup2 = InlineKeyboardMarkup(keyboard2)
    reply_markup3 = InlineKeyboardMarkup(keyboard3) 
    reply_markup4 = InlineKeyboardMarkup(keyboard4)
    reply_markup5 = InlineKeyboardMarkup(keyboard5)
    reply_markup6 = InlineKeyboardMarkup(keyboard6)

    if query.data == 'Breakfast':
        query.edit_message_reply_markup(reply_markup = reply_markup1)
    if query.data == 'Lunch':
        query.edit_message_reply_markup(reply_markup = reply_markup2)
    if query.data == 'Dinner':
        query.edit_message_reply_markup(reply_markup = reply_markup3)
    if query.data == 'Dessert':
        query.edit_message_reply_markup(reply_markup = reply_markup4)
    if query.data == 'Drink':
        query.edit_message_reply_markup(reply_markup = reply_markup5)
    if query.data == 'Salad':
        query.edit_message_reply_markup(reply_markup = reply_markup6)

    #BREAKFAST_MEALS
    for i in range (0, 7):
        if query.data == breakfast_meals[i]:
            query.edit_message_text(BF_TEXT[i])
    #LUNCH_MEALS
    for i in range (0, 7):
        if query.data == lunch_meals[i]:
            query.edit_message_text(LUNCH_TEXT[i])
    #DINNER__MEALS
    for i in range (0, 7):
        if query.data == dinner_meals[i]:
            query.edit_message_text(DINNER_TEXT[i])
    #DESSERT__MEALS
    for i in range (0, 7):
        if query.data == dessert_meals[i]:
            query.edit_message_text(DESSERT_TEXT[i])
    #DRINK__MEALS
    for i in range (0, 7):
        if query.data == drink_meals[i]:
            query.edit_message_text(DRINK_TEXT[i])
    #SALAD__MEALS
    for i in range (0, 7):
        if query.data == salad_meals[i]:
            query.edit_message_text(SALAD_TEXT[i])

def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")

def main():
    updater = Updater("606072390:AAGHAH7LFwLSqKjaPze27U3arh4h7vT3bHI")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))

    updater.start_polling()
    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()