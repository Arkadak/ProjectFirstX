# API key fb0810eec2de4b59b42200541240705
import requests
import datetime
import telebot

bot = telebot.TeleBot('6806105230:AAHVN2QtUlG4yVypohoFEc1SUtHq18I7Z-M')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, вот список команд: \n /weather - посмотреть погоду на сегодня. \n '
                                      '/short - посмотреть погоду на 1-14 дней от сегодняшней даты.\n'
                     '/long - посмотреть погоду на 15-300 дней от сегоднящней даты.\n'
                                      '/help - показать команды.')

@bot.message_handler(commands=['help', 'Help'])
def help(message):
    bot.send_message(message.chat.id, '/weather - посмотреть погоду на сегодня. \n '
                                      '/short - посмотреть погоду на 1-14 дней от сегодняшней даты.\n'
                     '/long - посмотреть погоду на 15-300 дней от сегоднящней даты.')

# def compare_dates():
#     while True:
#         try:
#             global dt
#             dt = input('Введите дату в формате гггг-мм-дд: ')
#             if dt.lower().strip() == 'stop':
#                 break
#             today = datetime.date.today()
#             md = datetime.datetime.strptime(dt, '%Y-%m-%d').date()
#             difference = md - today
#             if difference.days == 0:
#                 weather_for_today()
#             elif 1 <= difference.days <= 14:
#                 two_weeks_weather()
#             elif 14 < difference.days < 300:
#                 future_weather_after_two_weaks()
#         except:
#             print('Пожалуйста, вводите даты.')





@bot.message_handler(commands=['weather'])
def weather_for_today(message):
    bot.send_message(message.chat.id, "Введите город на английском языке, например (Riga): ")
    bot.register_next_step_handler(message, get_city_weather)

def get_city_weather(message):
    try:
        city = message.text.strip().lower().capitalize()
        r = requests.get(
            'https://api.weatherapi.com/v1/current.json?key=fb0810eec2de4b59b42200541240705&q=' + city + '&aqi=no').json()
        bot.send_message(message.chat.id, f"{r['location']['name']} сегодня:")
        bot.send_message(message.chat.id, f"Сейчас температура {r['current']['temp_c']} C")
        bot.send_message(message.chat.id, f"Ощущается как {r['current']['feelslike_c']} C")
        bot.send_message(message.chat.id, f"Ветер: {r['current']['wind_kph']} км/ч.")
        bot.send_message(message.chat.id, f"Сегодня давление: {r['current']['pressure_mb']} мб")
    except KeyError:
        bot.send_message(message.chat.id, 'Убедитесь, что город введён правильно, английскими буквами.\n'
                                          '/weather - посмотреть погоду на сегодня. \n '
                                      '/short - посмотреть погоду на 1-14 дней от сегодняшней даты.\n'
                     '/long - посмотреть погоду на 15-300 дней от сегоднящней даты.')







@bot.message_handler(commands=['long'])
def zapros(message):
    bot.send_message(message.chat.id, "Введите город на английском языке, например (Riga): ")
    bot.register_next_step_handler(message, future_weather_after_two_weeks)

def future_weather_after_two_weeks(message):
    city = message.text.strip().lower().capitalize()
    bot.send_message(message.chat.id, 'Введите дату в формате гггг-мм-дд')
    bot.register_next_step_handler(message, process_date, city)



def process_date(message, city):
    try:
        dt = message.text.strip()
        request = requests.get(
            'https://api.weatherapi.com/v1/future.json?key=fb0810eec2de4b59b42200541240705&q=' + city
            + '&dt=' + dt + '&aqi=no').json()
        bot.send_message(message.chat.id, request['location']['name'])
        bot.send_message(message.chat.id,
                         f"Максимальная температура {dt}: {request['forecast']['forecastday'][0]['day']['maxtemp_c']}")
        bot.send_message(message.chat.id,
                         f"Минимальная температура: {dt}: {request['forecast']['forecastday'][0]['day']['mintemp_c']}")
        bot.send_message(message.chat.id,
                         f"Максимальная скорость ветра: {dt}: {request['forecast']['forecastday'][0]['day']['maxwind_mph']}")
        bot.send_message(message.chat.id, f"Восход в {request['forecast']['forecastday'][0]['astro']['sunrise']}")
        bot.send_message(message.chat.id, f"Заход в {request['forecast']['forecastday'][0]['astro']['sunset']}")
        bot.send_message(message.chat.id,
                         f"Шанс дождя: {request['forecast']['forecastday'][0]['hour'][0]['chance_of_rain']}")
    except IndexError:
        bot.send_message(message.chat.id, 'Убедитесь, что город введён правильно, английскими буквами.\n'
                                          '/weather - посмотреть погоду на сегодня. \n '
                                      '/short - посмотреть погоду на 1-14 дней от сегодняшней даты.\n'
                     '/long - посмотреть погоду на 15-300 дней от сегоднящней даты.')
    except KeyError:
        bot.send_message(message.chat.id, 'Убедитесь, что дата введена верно: \n'
                                          'в формате гггг-мм-дд, \n'
                                          'дата находится в радиусе от 15-300 дней от сегодняшней даты.\n'
                                          '/weather - посмотреть погоду на сегодня. \n '
                                      '/short - посмотреть погоду на 1-14 дней от сегодняшней даты.\n'
                     '/long - посмотреть погоду на 15-300 дней от сегоднящней даты.')







@bot.message_handler(commands=['short'])
def zapros2(message):
    bot.send_message(message.chat.id, 'Введите город английскими буквами, например (Riga): ')
    bot.register_next_step_handler(message, data_z)

def data_z(message):
    city = message.text.strip().lower().capitalize()
    bot.send_message(message.chat.id, 'Введите дату в формате гггг-мм-дд')
    bot.register_next_step_handler(message, two_weeks_weather, city)

def two_weeks_weather(message, city):
    try:
        dt = message.text.strip()
        r = requests.get('https://api.weatherapi.com/v1/forecast.json?key=fb0810eec2de4b59b42200541240705&q=' + city +
                         '&aqi=no&dt=' + dt).json()
        bot.send_message(message.chat.id,
                         f"Максимальная теммпература: {r['forecast']['forecastday'][0]['day']['maxtemp_c']}.")
        bot.send_message(message.chat.id,
                         f"Минимальная теммпература: {r['forecast']['forecastday'][0]['day']['mintemp_c']}.")
        bot.send_message(message.chat.id, f"Ветер: {r['forecast']['forecastday'][0]['day']['maxwind_kph']}км/ч.")
        bot.send_message(message.chat.id,
                         f"Максимальная скорость ветра: {r['forecast']['forecastday'][0]['day']['maxwind_mph']}км/ч")
        bot.send_message(message.chat.id,
                         f"Шанс дождя: {r['forecast']['forecastday'][0]['day']['daily_will_it_rain']}.")
        bot.send_message(message.chat.id, f"Восход в {r['forecast']['forecastday'][0]['astro']['sunrise']}")
        bot.send_message(message.chat.id, f"Заход в {r['forecast']['forecastday'][0]['astro']['sunset']}")
    except KeyError:
        bot.send_message(message.chat.id, 'Я не знаю такой город, либо он введён неправильно.\n'
                                          '/weather - посмотреть погоду на сегодня. \n '
                                      '/short - посмотреть погоду на 1-14 дней от сегодняшней даты.\n'
                     '/long - посмотреть погоду на 15-300 дней от сегоднящней даты.')
    except IndexError:
        bot.send_message(message.chat.id, 'Убедитесь, что дата введена верно: \n'
                                          'в формате гггг-мм-дд, \n'
                                          'дата находится в радиусе от 1-14 дней от сегодняшней даты. \n'
                                          '/weather - посмотреть погоду на сегодня. \n '
                                      '/short - посмотреть погоду на 1-14 дней от сегодняшней даты.\n'
                     '/long - посмотреть погоду на 15-300 дней от сегоднящней даты.')



bot.polling(non_stop=True)
