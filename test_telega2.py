
import schedule
import telebot
from threading import Thread
from time import sleep, strptime
from aiogram import types
TOKEN = "5539956122:AAGVPjHYFI5-mN0OXuVmkNpO3wzruU-8uuU"

bot = telebot.TeleBot(TOKEN)


class remainder_everyday():
    

@bot.message_handler(content_types='text')
def copypast(message:types.message):
    text_split=str(message.text).split()
    if(strptime(text_split[0],'%H:%M')): #setter of remainder in format time + text
        remaind_text=message.text.replace(text_split[0],'',1)
        if(remaind_text[0]==' '):  remaind_text=remaind_text[1:]

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