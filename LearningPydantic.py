from email import message
from numpy import meshgrid
import pydantic
import telebot

bot=telebot.TeleBot('5491627246:AAEOdKhGPXH5ny_Gh6xQIQbl76NKrD8PWeI')

#@bot.message_handler(content_types='text')
#def getUserText(message):

class City(pydantic.BaseModel):
    city_id: int
    name: str
    population: int

input_json="""
{
   "city_id": 123,
   "name": "almaty",
   "population": "1000" 
}
"""    
try:
    city=City.parse_raw(input_json)
except pydantic.ValidationError as e:
    print(e.json())

print(city)
print(city.name)