from telebot import types
import requests
import datetime
from my_imp import bot, client, dict_city, symbols, users
import random
import json
import re
import random_responses
# from main import main


def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)


response_data = load_json("chat_bot.json")


@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id not in users:
        users.append(message.from_user.id)
        print(users)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Что бы посмотреть?\U0001F3A6')
    item2 = types.KeyboardButton('Полезная информация\U0001F4C8')
    item3 = types.KeyboardButton('Хочу анекдот\U0001F605')
    item4 = types.KeyboardButton('Книги?\U0001F4DA')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} you are my Bro?', reply_markup=markup)
    bot.send_message(message.chat.id,
                     f'Ну конечно же да {message.from_user.first_name} Я твой маленький помощник\U0001F601\n'
                     f'если ты хочешь проверить криптографик, отправь сообщения в верхнем регистре.\n'
                     f'Так же я буду отправлять тебе в 8:00утра сообщения с делами:-)\n'
                     f'И список с курсами валют')
    bot.send_message(message.chat.id, f'Если что то не понятно пиши /help')


@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, f'Бро вот все что есть!\U0001F601\n'
                                      f'/start\n'
                                      f'/help\n'
                                      f'/token\n'
                                      f'/weather\n')


@bot.message_handler(commands=['token'])
def token(message):
    bot.send_message(message.chat.id, 'Просто напиши мне какая крипта тебе интерестна')


@bot.message_handler(commands=['weather'])
def token(message):
    bot.send_message(message.chat.id, 'Напиши свой город')


# @bot.message_handler(commands=['traider'])
# def token(message):
#     bot.send_message(message.chat.id, 'Okay i begin trading')
#     main()


@bot.message_handler(content_types=['text'])
def text(message):
    if message.chat.type == 'private':
        if message.text == 'Что бы посмотреть?\U0001F3A6':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Фильм?\U0001F3AC')
            item2 = types.KeyboardButton('Сериал?\U0001F3AC')
            back = types.KeyboardButton('Меню\U0001F30C')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, 'Что хочешь?', reply_markup=markup)

        elif message.text == 'Фильм?\U0001F3AC':
            with open('films.csv', 'r') as f:
                a = f.read().split('\n')
                bot.send_message(message.chat.id, random.choice(a))

        elif message.text == 'Сериал?\U0001F3AC':
            with open('serials.csv', 'r') as f:
                b = f.read().split('\n')
                bot.send_message(message.chat.id, random.choice(b))
        elif message.text == 'Полезная информация\U0001F4C8':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton(text='Tradingview', url='https://tradingview.com/symbols/BTCUSDT/')
            item2 = types.InlineKeyboardButton(text='Coinbase', url='https://www.coinbase.com/price')
            item3 = types.InlineKeyboardButton(text='psy-practice', url='https://psy-practice.com/publications/')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, 'Может быть полезным', reply_markup=markup)
        elif message.text == 'Хочу анекдот\U0001F605':
            with open('anecdote.csv', 'r') as jok:
                s = [i for i in jok.read().split('.')]
            bot.send_message(message.chat.id, random.choice(s))
        elif message.text == 'Книги?\U0001F4DA':
            with open('Books.csv', 'r') as book:
                d = book.read().split('\n')
            bot.send_message(message.chat.id, random.choice(d))

        elif message.text == 'Меню\U0001F30C':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Что бы посмотреть?\U0001F3A6')
            item2 = types.KeyboardButton('Полезная информация\U0001F4C8')
            item3 = types.KeyboardButton('Хочу анекдот\U0001F605')
            item4 = types.KeyboardButton('Книги?\U0001F4DA')

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, 'Меню\U0001F30C', reply_markup=markup)

    if message.text in symbols:
        try:
            token = client.get_avg_price(symbol=f'{message.text}USDT')
            bot.reply_to(message, token['price'])
        except Exception as ex:
            print(ex)
            bot.send_message(message.chat.id, 'Что то не так\U0001F914\n '
                                              'Попробуй снова')

    if message.text in dict_city:
        city = message.text
        code_to_emoji = {
            'Clear': 'Ясно \U00002600',
            'Clouds': 'Облака \U00002601',
            'Rain': 'Дождь \U00002614',
            'Drizzle': 'Мелкий дождь \U00002614',
            'Thunderstorm': 'Гроза \U000026A1',
            'Snow': 'Снег \U0001F328',
            'Mist': 'Туман \U0001F32B'}
        try:

            req = requests.get(
                url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d309e1237aaeb338ad8555f203411d8e&units=metric')
            data = req.json()

            name = data['name']
            cur_weather1 = data['main']['temp']
            cur_weather2 = data['wind']['speed']
            weather_description = data['weather'][0]['main']
            if weather_description in code_to_emoji:
                wd = code_to_emoji[weather_description]
            else:
                wd = 'Выгляни в окно и посмотри сам, я не понимаю'

            sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
            sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])

            bot.send_message(message.chat.id, f'Погода в {name}\n'
                                              f'Температура {cur_weather1}C°{wd}\n'
                                              f'Скорость ветра {cur_weather2}\n'
                                              f'Восход {sunrise}\U0001F31D\n'
                                              f'Заход {sunset}\U0001F31A\n'
                                              f'Have a great day!')

        except Exception as ex:
            print(ex)

    split_message = re.split(r'\s+|[,;?!.-]\s*', message.text.lower())
    score_list = []

    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        if required_score == len(required_words):
            for word in split_message:
                if word in response["user_input"]:
                    response_score += 1

        score_list.append(response_score)

    best_response = max(score_list)
    response_index = score_list.index(best_response)

    if best_response != 0:
        return bot.send_message(message.chat.id, response_data[response_index]["bot_response"])


bot.polling(non_stop=True)
