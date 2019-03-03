import telebot
import additional
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler 
from additional import *

def start(bot, update):
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Hello, I am a quiz-bot. Please choose one of the category, then the location below:', reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query
    reply_markupL = InlineKeyboardMarkup(keyboardL)
    reply_markupG = InlineKeyboardMarkup(keyboardG)

#Category
    if query.data == 'Безопасность':
        f= open("save.txt","a+")
        f.write("Безопасность || ")
        f.close()
        query.edit_message_reply_markup(reply_markup = reply_markupG)
    if query.data == 'Бизнес':
        f= open("save.txt","a+")
        f.write("Бизнес || ")
        f.close()
        query.edit_message_reply_markup(reply_markup = reply_markupG)
    if query.data == 'ЖКХ':
        f= open("save.txt","a+")
        f.write("ЖКХ || ")
        f.close()
        query.edit_message_reply_markup(reply_markup = reply_markupG)
    if query.data == 'Коррупция':
        f= open("save.txt","a+")
        f.write("Коррупция || ")
        f.close()
        query.edit_message_reply_markup(reply_markup = reply_markupG)
    if query.data == 'Образование':
        f= open("save.txt","a+")
        f.write("Образование || ")
        f.close()
        query.edit_message_reply_markup(reply_markup = reply_markupG)
    if query.data == 'Экология':
        f= open("save.txt","a+")
        f.write("Экология || ")
        f.close()
        query.edit_message_reply_markup(reply_markup = reply_markupG)

# Gov
    if query.data == '101001':
        f= open("save.txt","a+")
        f.write("101001 || ")
        f.close()
        query.edit_message_reply_markup(reply_markup = reply_markupL)
    if query.data == '101002':
        f= open("save.txt","a+")
        f.write("101002 || ")
        f.close()
        query.edit_message_reply_markup(reply_markup = reply_markupL)
    if query.data == '101003':
        f= open("save.txt","a+")
        f.write("101003 || ")
        f.close()
        query.edit_message_reply_markup(reply_markup = reply_markupL)
    if query.data == '101004':
        f= open("save.txt","a+")
        f.write("101004 || ")
        f.close()
        query.edit_message_reply_markup(reply_markup = reply_markupL)
    if query.data == '101006':
        f= open("save.txt","a+")
        f.write("101006 || ")
        f.close()
        query.edit_message_reply_markup(reply_markup = reply_markupL)
    if query.data == '101007':
        f= open("save.txt","a+")
        f.write("101007 || ")
        f.close()
        query.edit_message_reply_markup(reply_markup = reply_markupL)

#location
    if query.data == 'г. Астана':
        f= open("save.txt","a+")
        f.write("г. Астана || "+str(query.from_user.username)+"\n")        
        f.close()
        query.message.edit_text('Thank you for your answer, bye :)')         
    if query.data == 'г. Алматы':
        f= open("save.txt","a+")
        f.write("г. Алматы || "+str(query.from_user.username)+"\n")
        f.close()
        query.message.edit_text('Thank you for your answer, bye :)')
    if query.data == 'Акмолинская область':
        f= open("save.txt","a+")
        f.write("Акмолинская область || "+str(query.from_user.username)+"\n")        
        f.close()
        query.message.edit_text('Thank you for your answer, bye :)')
    if query.data == 'Актюбинская область':
        f= open("save.txt","a+")
        f.write("Актюбинская область || "+str(query.from_user.username)+"\n")        
        f.close()
        query.message.edit_text('Thank you for your answer, bye :)')
    if query.data == 'Алматинская область':
        f= open("save.txt","a+")
        f.write("Алматинская область || "+str(query.from_user.username)+"\n")        
        f.close()
        query.message.edit_text('Thank you for your answer, bye :)')
    if query.data == 'Атырауская область':
        f= open("save.txt","a+")
        f.write("Атырауская область || "+str(query.from_user.username)+"\n")        
        f.close()
        query.message.edit_text('Thank you for your answer, bye :)')


def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")

def main():
    updater = Updater("748589730:AAFTa5GARrCETSoHBDkVG7TKRmBpniWrSl4")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))

    updater.start_polling()
    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()