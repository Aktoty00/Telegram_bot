import telebot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


keyboardL = [[InlineKeyboardButton("г. Астана", callback_data='г. Астана'),
                InlineKeyboardButton("г. Алматы", callback_data='г. Алматы')],
                [InlineKeyboardButton("Акмолинская область", callback_data='Акмолинская область'),
                InlineKeyboardButton("Актюбинская область", callback_data='Актюбинская область')],
                [InlineKeyboardButton("Алматинская область", callback_data='Алматинская область'),
                InlineKeyboardButton("Атырауская область", callback_data='Атырауская область')]
                ]
keyboardG = [[InlineKeyboardButton("101001", callback_data='101001'),
                InlineKeyboardButton("101002", callback_data='101002')],
                [InlineKeyboardButton("101003", callback_data='101003'),
                InlineKeyboardButton("101004", callback_data='101004')],
                [InlineKeyboardButton("101006", callback_data='101005'),
                InlineKeyboardButton("101007", callback_data='101006')]
                ]

keyboard = [[InlineKeyboardButton("Безопасность", callback_data='Безопасность'),
                InlineKeyboardButton("Бизнес", callback_data='Бизнес')],
                [InlineKeyboardButton("ЖКХ", callback_data='ЖКХ'),
                InlineKeyboardButton("Коррупция", callback_data='Коррупция')],
                [InlineKeyboardButton("Образование", callback_data='Образование'),
                InlineKeyboardButton("Экология", callback_data='Экология')]
                ]