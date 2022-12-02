import pandas as pd

symbols = ['BTCUSDT','ETHUSDT','LUNAUSDT','SOLUSDT','UNIUSDT','AVAXUSDT','QNTUSDT','BNBUSDT','GALAUSDT','XRPUSDT','SHIBUSDT','ENJUSDT','DOTUSDT','SANDUSDT','DOGEUSDT','VETUSDT','NEARUSDT','ONEUSDT','XLMUSDT','MANAUSDT','TRXUSDT','XTZUSDT','BCHUSDT','FILUSDT','ATOMUSDT','KLAYUSDT','AAVEUSDT','HNTUSDT','EGLDUSDT',
           'ADAUSDT','LINKUSDT','MATICUSDT','EOSUSDT','THETAUSDT','LTCUSDT','NEOUSDT','ETCUSDT','XMRUSDT','TFUELUSDT','FTMUSDT','ALGOUSDT','HBARUSDT','FTTUSDT','MKRUSDT','AXSUSDT','GRTUSDT','CAKEUSDT','ICPUSDT','FLOWUSDT','XECUSDT']



posframe = pd.DataFrame(symbols)

posframe.columns = ['Currency']
posframe['Position'] = 0
posframe['quantity'] = 0
posframe.to_csv('positionchack', index=False)
pd.read_csv('positionchack')
