
from numpy import number
from pydantic import BaseModel
import telebot as tl
from telebot import types
from threading import Thread
import schedule
import time

bot=tl.TeleBot('5491627246:AAEOdKhGPXH5ny_Gh6xQIQbl76NKrD8PWeI')

class Reminder(BaseModel):
    chat_id: int 
    text:str #text reminded
    periodicityDays: int #execute in n days (hard to obtain it from user)
    exactTimeHours: str #0->7:00->24:00 by defualt
    repeations: int #every executed time do -1 until 0, then remove
    

    def executeReminding(self,bot: tl.TeleBot):
         if(self.periodicityDays==0):
             schedule.every().day.at(self.exactTimeHours).do(bot.send_message,self.chat_id,self.text)
         else:    
             schedule.every(self.periodicityDays).days.at(self.exactTimeHours).do(bot.send_message,self.chat_id,self.text)
    @staticmethod
    def schedule_checker():
         while(True):
             schedule.run_pending()
             time.sleep(100)
            
        

input_json="""
{
    "chat_id": 687088043,
    "text": "do sport",
    "periodicityDays": 0,
    "exactTimeHours": "15:36",
    "repeations":1
}
"""
bot.send_message(687088043,'lovi')
rem=Reminder.parse_raw(input_json)
rem.executeReminding(bot) 
@bot.message_handler(content_types='text')
def getUserText(message):
    bot.send_message(message.chat.id, 'copy that')
    

#decorator
# @bot.message_handler(commands=['hello'])

# def hello(message):
#     mess=f'<b>hi, {message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
#     bot.send_message(message.chat.id,mess, parse_mode='html')
    
# # def help(message):
# #     bot.send_message(message.chat.id,'list of commands:',parse_mode='html')
# # @bot.message_handler(content_types=['text'])
# # def getUserText(message):
# #     if(message.text=='full info'): bot.send_message(message.chat.id,message, parse_mode='html' )
# #     elif(message.text=='hello' or message.text=='hi' or message.text=='привет'):
# #         bot.send_message(message.chat.id,f'И тебе привет, {message.from_user.first_name}', parse_mode='html' )
# #     elif(message.text=='photo'):
# #         photo=open('D:/Users/Аслан/Desktop/программирование/001-Tatsu3.png','rb')
# #         bot.send_photo(message.chat.id, photo)
# #     elif(message.text=='video'):
# #         video=open('C:/Users/User/Videos/vlc-record-2022-06-01-00h54m04s-Destiny 2 2022.06.01 - 00.37.12.68.DVR.mp4-.mp4','rb')
# #         bot.send_video(message.chat.id, video)

# @bot.message_handler(content_types=['photo'])#text,sticker,sharedtext,photo,audio
# def getUserPhoto(message):
#     bot.send_message(message.chat.id,'Не плохо, я одолжу')

# @bot.message_handler(commands=['website'])
# def website(message):
#     markup= types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('посетить вебсайт',url='https://youtu.be/eqCGwblJKIs'))
#     bot.send_message(message.chat.id, 'Работает. Заходи', reply_markup=markup)

# @bot.message_handler(commands=['help'])
# def website(message):
#     markup= types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     websiteButton=types.KeyboardButton('Website')
#     startButton=types.KeyboardButton('Start')
#     markup.add(websiteButton,startButton)
#     bot.send_message(message.chat.id, 'Работает. Заходи', reply_markup=markup)

# Thread(target=Reminder.schedule_checker()).start()
bot.polling(none_stop=True)
