from time import sleep
import schedule
from threading import Thread
from my_imp import bot, client, users, to_day


def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)


token = client.get_avg_price(symbol='BTCUSDT')
price_now = token['price']


def monday(to_day):
    token = client.get_avg_price(symbol='BTCUSDT')
    token1 = token['price']
    token2 = client.get_avg_price(symbol='USDTUAH')
    token3 = token2['price']
    for i in users:
        print(i)
        return bot.send_message(i, f'{to_day}\n'
                                f'Bitcoin today cost {token1}\U0001F4B0\n'
                                f'USD/UAH {token3}\n'
                                f'and remember everything will be magnificently')


def prices(price_now):
    token = client.get_avg_price(symbol='BTCUSDT')
    token1 = token['price']
    if float(token1) < float(price_now):
        current_price1 = float(price_now) - float(token1)
        for k in users:
            return bot.send_message(k, f'BTC drops -{round(current_price1)}')
    elif float(token1) > float(price_now):
        current_price2 = float(token1) - float(price_now)
        for j in users:
            return bot.send_message(j, f'BTC rise +{round(current_price2)}')
    price_now = token['price']
    return price_now


schedule.every().day.at("10:00").do(monday, to_day=to_day[0][0])
schedule.every().day.at("12:21").do(prices, price_now=price_now)
schedule.every().day.at("16:10").do(prices, price_now=price_now)
schedule.every().day.at("21:12").do(prices, price_now=price_now)
Thread(target=schedule_checker).start()
