from binance import Client
import pandas as pd


def main():
    client = Client('zMXWG9fRsJOsHNPUHuvgC1Tvwr9Gvfu76fIt4Mfu47icnmEIBVanMsyCJwIVLnCT',
                    'UKXPwlwaCVQbjoh86cG8AmRF2kq0pA0MJVq9ia5BR3YQ5HVKXcnCkzVDZQx5I8zE')

    posframe = pd.read_csv('positionchack')

    def gethourlydata(symbol):
        frame = pd.DataFrame(client.get_historical_klines(symbol,
                                                          '1h',
                                                          '75 hours ago UTC'))
        frame = frame[[0, 4]]
        frame.columns = ['Time', 'Close']
        frame.Close = frame.Close.astype(float)
        frame.Time = pd.to_datetime(frame.Time, unit='ms')
        return frame

    temp = gethourlydata('BTCUSDT')

    def applytechnicals(df):
        df['FastSMA'] = df.Close.rolling(5).mean()
        df['SlowSMA'] = df.Close.rolling(75).mean()

    applytechnicals(temp)

    def changepos(curr, order, buy=True):
        if buy:
            posframe.loc[posframe.Currency == curr, 'position'] = 1
            posframe.loc[posframe.Currency == curr, 'quantity'] = float(order['executedQty'])
        else:
            posframe.loc[posframe.Currency == curr, 'position'] = 0
            posframe.loc[posframe.Currency == curr, 'quantity'] = 0


    def trader(investment=100):
        for coin in posframe[posframe.position == 1].Currency:
            df = gethourlydata(coin)
            applytechnicals(df)
            lastrow = df.iloc[-1]
            if lastrow.SlowSMA > lastrow.FastSMA:
                order = client.create_order(symbol=coin,
                                            side='SELL',
                                            type='MARKET',)
            quantity = posframe[posframe.Currency == coin].quantity.values[0]
            changepos(coin, order, buy=False)
            print(order)


    for coin in posframe[posframe.Position == 0].Currency:
        df = gethourlydata(coin)
        applytechnicals(df)
        lastrow = df.iloc[-1]
        if lastrow.FastSMA > lastrow.SlowSMA:
            order = client.create_order(symbol=coin,
                                        side='BUY',
                                        type='MARKET',)
            print(order)
            changepos(coin, order, buy=True)
        else:
            print(f'Buying Conditions for {coin} is not fulfilled')

    while True:
        try:
            trader()
        except:
            continue


if __name__ == '__main__':
    main()
