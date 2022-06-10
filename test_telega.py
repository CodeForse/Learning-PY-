from email import message
from msilib import type_binary
import telebot as tl
import requests

bot=tl.TeleBot('5491627246:AAEOdKhGPXH5ny_Gh6xQIQbl76NKrD8PWeI')

#decorator
@bot.message_handler(commands=['hello','help'])

def hello(message):
    mess=f'<b>hi, {message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id,mess, parse_mode='html')
    
# def help(message):
#     bot.send_message(message.chat.id,'list of commands:',parse_mode='html')
@bot.message_handler(content_types=['text'])
def getUserText(message):
    if(message.text=='full info'): bot.send_message(message.chat.id,message, parse_mode='html' )
    elif(message.text=='hello' or message.text=='hi' or message.text=='привет'):
        bot.send_message(message.chat.id,f'И тебе привет, {message.from_user.first_name}', parse_mode='html' )
    elif(message.text=='photo'):
        photo=open('D:/Users/Аслан/Desktop/программирование/001-Tatsu3.png','rb')
        bot.send_photo(message.chat.id, photo)
    elif(message.text=='video'):
        video=open('C:/Users/User/Videos/vlc-record-2022-06-01-00h54m04s-Destiny 2 2022.06.01 - 00.37.12.68.DVR.mp4-.mp4','rb')
        bot.send_video(message.chat.id, video)

@bot.message_handler(content_types=['photo'])#text,sticker,sharedtext,photo,audio
def getUserPhoto(message):
        bot.send_message(message.chat.id,'Не плохо, я одолжу')

bot.polling(none_stop=True)