import telebot
from telebot import types
token = "5539956122:AAGVPjHYFI5-mN0OXuVmkNpO3wzruU-8uuU"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def any_msg(message):
    if(message.text.lower()=='remind me to'):
        keyboardmain = types.InlineKeyboardMarkup(row_width=2)
        period_button = types.InlineKeyboardButton(text='Every Period', callback_data='every')
        once_button = types.InlineKeyboardButton(text='One time', callback_data='once')
        keyboardmain.add(period_button, once_button)
        bot.send_message(message.chat.id, "testing kb", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "mainmenu":#for going back

        keyboardmain = types.InlineKeyboardMarkup(row_width=2)
        period_button = types.InlineKeyboardButton(text='Every Period', callback_data='every')
        once_button = types.InlineKeyboardButton(text='One time', callback_data='once')
        keyboardmain.add(period_button, once_button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="menu",reply_markup=keyboardmain)

    if call.data == "every":
        keyboard = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="1t", callback_data="1")
        rele2 = types.InlineKeyboardButton(text="2t", callback_data="2")
        rele3 = types.InlineKeyboardButton(text="3t", callback_data="3")
        backbutton = types.InlineKeyboardButton(text="back", callback_data="mainmenu")
        keyboard.add(rele1, rele2, rele3, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="replaced text",reply_markup=keyboard)

    elif call.data == "once":
        keyboard = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="another layer", callback_data="gg")
        backbutton = types.InlineKeyboardButton(text="back", callback_data="mainmenu")
        keyboard.add(rele1,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="replaced text",reply_markup=keyboard)

    elif call.data == "1" or call.data == "2" or call.data == "3":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="alert")
        keyboard3 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="lastlayer", callback_data="ll")
        keyboard3.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="last layer",reply_markup=keyboard3)


if __name__ == "__main__":
    bot.polling(none_stop=True)