import os
from pandas import array
from typing import List
import pydantic
import schedule
import telebot
from threading import Thread
from time import sleep, strptime
from aiogram import types
import json
TOKEN = "5539956122:AAGVPjHYFI5-mN0OXuVmkNpO3wzruU-8uuU"

bot = telebot.TeleBot(TOKEN)


class remainder_everyday(pydantic.BaseModel):
    id_chat:int
    remiand_text: str
    activation_time: str
    

@bot.message_handler(content_types='text')
def copypast(message:types.message):
    text_split=str(message.text).split()
    if(strptime(text_split[0],'%H:%M')): #setter of remainder in format time + text
        remaind_text=message.text.replace(text_split[0],'',1)
        if(remaind_text[0]==' '):  remaind_text=remaind_text[1:]
        file=open('remainds.json','a+')
        if(os.stat('remainds.json').st_size!=0):
            # file.seek(file.tell()-1, os.SEEK_END)
            # file.write('')
            file.write(',')
        # else: file.write('[')
        file.write  (remainder_everyday(id_chat=message.chat.id,remiand_text= remaind_text,activation_time= text_split[0]).json())
        # file.write(']')
        file.close()
    
    else: bot.send_message(message.chat.id,message.text)
    


def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

def function_to_run():
    return bot.send_message(687088043, "bob")
def function_to_run2():
    return bot.send_message(687088043, "suck")    
def morning_mess():
    return bot.send_message(687088043,'Доброе утро)')
def sport_mess():
    return bot.send_message(687088043,'Займись спортом')
def schedules():
    # reminds_file=open('remainds.json','r')
    if os.stat('remainds.json').st_size!=0:
        file=open('remainds.json','r')
        strjson='['+file.read()+']'
        file.close()
        reminds=pydantic.parse_obj_as(List[remainder_everyday],json.loads(strjson))
        schedule.every().day.at('23:27').do(bot.send_message,rem.id_chat,'дешевка')
        for rem in reminds:
            
            schedule.every().day.at(rem.activation_time).do(bot.send_message,rem.id_chat,rem.remiand_text)

    
    # schedule.every(5).seconds.do(function_to_run)
    # schedule.every(10).seconds.do(function_to_run2)
    schedule.every().day.at('07:00').do(morning_mess)
    schedule.every().day.at('14:00').do(sport_mess) 
    
if __name__ == "__main__":
    # Create the job in schedule.
    
    schedules()
    # Spin up a thread to run the schedule check so it doesn't block your bot.
    # This will take the function schedule_checker which will check every second
    # to see if the scheduled job needs to be ran.
    Thread(target=schedule_checker).start() 

    # And then of course, start your server.
    # server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
bot.polling(none_stop=True)