import logging
from breakfast import text_bf1,text_bf2,text_bf3, text_bf4,text_bf5
from lunch import text_l1,text_l2,text_l3,text_l4,text_l5
from dinner import text_d1,text_d2,text_d3,text_d4, text_d5
from dessert import text_ds1,text_ds2,text_ds3,text_ds4, text_ds5

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    keyboard = [[InlineKeyboardButton("Breakfast", callback_data='Breakfast'),
                InlineKeyboardButton("Lunch", callback_data='Lunch'),
                InlineKeyboardButton("Dinner", callback_data='Dinner'),
                InlineKeyboardButton("Dessert", callback_data='Dessert')]
                ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Hello, I am a recipe-bot. Please choose on of the item below:', reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query
    keyboard1 = [[InlineKeyboardButton('Omelette', callback_data = 'Omelette')],
                 [InlineKeyboardButton('Mini super-fruit breakfast wraps', callback_data = 'Mini super-fruit breakfast wraps')],
                 [InlineKeyboardButton('One-cup pancakes with blueberries', callback_data = 'One-cup pancakes with blueberries')],
                 [InlineKeyboardButton('Egg & mango chutney flatbreads', callback_data = 'Egg & mango chutney flatbreads')],
                 [InlineKeyboardButton('Apple & pecan porridge', callback_data = 'Apple & pecan porridge')]
                  ]
    keyboard2 = [[InlineKeyboardButton('Pasta', callback_data = 'Pasta')],
                 [InlineKeyboardButton('Carrot soup', callback_data = 'Carrot soup')],
                 [InlineKeyboardButton('Spicy avocado wraps', callback_data = 'Spicy avocado wraps')],
                 [InlineKeyboardButton('Barney-Monday night rice', callback_data = 'Barney-Monday night rice')],
                 [InlineKeyboardButton('Chicken gumbo', callback_data = 'Chicken gumbo')]
                  ]
    keyboard3 = [[InlineKeyboardButton('Pot-roast beef', callback_data = 'Pot-roast beef')],
                 [InlineKeyboardButton('Moroccan chickpea soup', callback_data = 'Moroccan chickpea soup')],
                 [InlineKeyboardButton('Spanish rice & prawn one-pot', callback_data = 'Spanish rice & prawn one-pot')],
                 [InlineKeyboardButton('Mild chilli & bean pasta bake', callback_data = 'Mild chilli & bean pasta bake')],
                 [InlineKeyboardButton('Spicy root & lentil casserole', callback_data = 'Spicy root & lentil casserole')]
                  ]
    keyboard4 = [[InlineKeyboardButton('Pumpkin pie with pecan crumble', callback_data = 'Pumpkin pie with pecan crumble')],
                 [InlineKeyboardButton('Blackcurrant ombré cheesecake', callback_data = 'Blackcurrant ombré cheesecake')],
                 [InlineKeyboardButton('Almond pastry puff', callback_data = 'Almond pastry puff')],
                 [InlineKeyboardButton('Brigadeiros', callback_data = 'Brigadeiros')],
                 [InlineKeyboardButton('Lamingtons', callback_data = 'Lamingtons')]
                  ]
    reply_markup1 = InlineKeyboardMarkup(keyboard1)
    reply_markup2 = InlineKeyboardMarkup(keyboard2)
    reply_markup3 = InlineKeyboardMarkup(keyboard3)
    reply_markup4 = InlineKeyboardMarkup(keyboard4)

    if query.data == 'Breakfast':
        query.edit_message_reply_markup(reply_markup = reply_markup1)
    if query.data == 'Lunch':
        query.edit_message_reply_markup(reply_markup = reply_markup2)
    if query.data == 'Dinner':
        query.edit_message_reply_markup(reply_markup = reply_markup3)
    if query.data == 'Dessert':
        query.edit_message_reply_markup(reply_markup = reply_markup4)

    if query.data == 'Omelette':
        query.edit_message_text(text_bf1)
    if query.data == 'One-cup pancakes with blueberries':
        query.edit_message_text(text_bf2)
    if query.data == 'Egg & mango chutney flatbreads':
        query.edit_message_text(text_bf3)
    if query.data == 'Apple & pecan porridge':
        query.edit_message_text(text_bf4)
    if query.data == 'Mini super-fruit breakfast wraps':
        query.edit_message_text(text_bf5)

    if query.data == 'Pasta':
        query.edit_message_text(text_l1)
    if query.data == 'Carrot soup':
        query.edit_message_text(text_l2)
    if query.data == 'Spicy avocado wraps':
        query.edit_message_text(text_l3)
    if query.data == 'Barney-Monday night rice':
        query.edit_message_text(text_l4)
    if query.data == 'Chicken gumbo':
        query.edit_message_text(text_l5)

    if query.data == 'Pot-roast beef':
        query.edit_message_text(text_d1)
    if query.data == 'Moroccan chickpea soup':
        query.edit_message_text(text_d2)
    if query.data == 'Spanish rice & prawn one-pot':
        query.edit_message_text(text_d3)
    if query.data == 'Mild chilli & bean pasta bake':
        query.edit_message_text(text_d4)
    if query.data == 'Spicy root & lentil casserole':
        query.edit_message_text(text_d5)

    if query.data == 'Pumpkin pie with pecan crumble':
        query.edit_message_text(text_ds1)
    if query.data == 'Blackcurrant ombré cheesecake':
        query.edit_message_text(text_ds2)
    if query.data == 'Almond pastry puff':
        query.edit_message_text(text_ds3)
    if query.data == 'Brigadeiros':
        query.edit_message_text(text_ds4)
    if query.data == 'Lamingtons':
        query.edit_message_text(text_ds5)

def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("606072390:AAGHAH7LFwLSqKjaPze27U3arh4h7vT3bHI")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()