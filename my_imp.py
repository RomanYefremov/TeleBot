import telebot
from binance.client import Client

bot = telebot.TeleBot('BOTID', parse_mode='HTML')
client = Client(
    'SECRET KEY',
    'TOKEN')
users = [ID USER]
token_weather = 'd309e1237aaeb338ad8555f203411d8e'

dict_city = []
with open('ua.csv', 'r') as file:
    dict_city += [i for i in file.read().split()]

symbols = ["BTC", "LTC", "ETH", "NEO", "BNB", "QTUM", "EOS", "SNT", "BNT", "GAS", "BCC", "USDT", "HSR", "OAX", "DNT",
           "MCO", "ICN", "ZRX", "OMG", "WTC", "YOYO", "LRC", "TRX", "SNGLS", "STRAT", "BQX", "FUN", "KNC", "CDT", "XVG",
           "IOTA", "SNM", "LINK", "CVC", "TNT", "REP", "MDA", "MTL", "SALT", "NULS", "SUB", "STX", "MTH", "ADX", "ETC",
           "ENG", "ZEC", "AST", "GNT", "DGD", "BAT", "DASH", "POWR", "BTG", "REQ", "XMR", "EVX", "VIB", "ENJ", "VEN",
           "ARK", "XRP", "MOD", "STORJ", "KMD", "RCN", "EDO", "DATA", "DLT", "MANA", "PPT", "RDN", "GXS", "AMB", "ARN",
           "BCPT", "CND", "GVT", "POE", "BTS", "FUEL", "XZC", "QSP", "LSK", "BCD", "TNB", "ADA", "LEND", "XLM", "CMT",
           "WAVES", "WABI", "GTO", "ICX", "OST", "ELF", "AION", "WINGS", "BRD", "NEBL", "NAV", "VIBE", "LUN", "TRIG",
           "APPC", "CHAT", "RLC", "INS", "PIVX", "IOST", "STEEM", "NANO", "AE", "VIA", "BLZ", "SYS", "RPX", "NCASH",
           "POA", "ONT", "ZIL", "STORM", "XEM", "WAN", "WPR", "QLC", "GRS", "CLOAK", "LOOM", "BCN", "TUSD", "ZEN",
           "SKY", "THETA", "IOTX", "QKC", "AGI", "NXS", "SC", "NPXS", "KEY", "NAS", "MFT", "DENT", "IQ", "ARDR", "HOT",
           "VET", "DOCK", "POLY", "VTHO", "ONG", "PHX", "HC", "GO", "PAX", "RVN", "DCR", "USDC", "MITH", "BCHABC",
           "BCHSV", "REN", "BTT", "USDS", "FET", "TFUEL", "CELR", "MATIC", "ATOM", "PHB", "ONE", "FTM", "BTCB", "USDSB",
           "CHZ", "COS", "ALGO", "ERD", "DOGE", "BGBP", "DUSK", "ANKR", "WIN", "TUSDB", "COCOS", "PERL", "TOMO", "BUSD",
           "BAND", "BEAM", "HBAR", "XTZ", "NGN", "DGB", "NKN", "GBP", "EUR", "KAVA", "RUB", "UAH", "ARPA", "TRY",
           "CTXC", "AERGO", "BCH", "TROY", "BRL", "VITE", "FTT", "AUD", "OGN", "DREP", "BULL", "BEAR", "ETHBULL",
           "ETHBEAR", "XRPBULL", "XRPBEAR", "EOSBULL", "EOSBEAR", "TCT", "WRX", "LTO", "ZAR", "MBL", "COTI", "BKRW",
           "BNBBULL", "BNBBEAR", "HIVE", "STPT", "SOL", "IDRT", "CTSI", "CHR", "BTCUP", "BTCDOWN", "HNT", "JST", "FIO",
           "BIDR", "STMX", "MDT", "PNT", "COMP", "IRIS", "MKR", "SXP", "SNX", "DAI", "ETHUP", "ETHDOWN", "ADAUP",
           "ADADOWN", "LINKUP", "LINKDOWN", "DOT", "RUNE", "BNBUP", "BNBDOWN", "XTZUP", "XTZDOWN", "AVA", "BAL", "YFI",
           "SRM", "ANT", "CRV", "SAND", "OCEAN", "NMR", "LUNA", "IDEX", "RSR", "PAXG", "WNXM", "TRB", "EGLD", "BZRX",
           "WBTC", "KSM", "SUSHI", "YFII", "DIA", "BEL", "UMA", "EOSUP", "TRXUP", "EOSDOWN", "TRXDOWN", "XRPUP",
           "XRPDOWN", "DOTUP", "DOTDOWN", "NBS", "WING", "SWRV", "LTCUP", "LTCDOWN", "CREAM", "UNI", "OXT", "SUN",
           "AVAX", "BURGER", "BAKE", "FLM", "SCRT", "XVS", "CAKE", "SPARTA", "UNIUP", "UNIDOWN", "ALPHA", "ORN", "UTK",
           "NEAR", "VIDT", "AAVE", "FIL", "SXPUP", "SXPDOWN", "INJ", "FILDOWN", "FILUP", "YFIUP", "YFIDOWN", "CTK",
           "EASY", "AUDIO", "BCHUP", "BCHDOWN", "BOT", "AXS", "AKRO", "HARD", "KP3R", "RENBTC", "SLP", "STRAX", "UNFI",
           "CVP", "BCHA", "FOR", "FRONT", "ROSE", "HEGIC", "AAVEUP", "AAVEDOWN", "PROM", "BETH", "SKL", "GLM", "SUSD",
           "COVER", "GHST", "SUSHIUP", "SUSHIDOWN", "XLMUP", "XLMDOWN", "DF", "JUV", "PSG", "BVND", "GRT", "CELO",
           "TWT", "REEF", "OG", "ATM", "ASR", "1INCH", "RIF", "BTCST", "TRU", "DEXE", "CKB", "FIRO", "LIT", "PROS",
           "VAI", "SFP", "FXS", "DODO", "AUCTION", "UFT", "ACM", "PHA", "TVK", "BADGER", "FIS", "OM", "POND", "ALICE",
           "DEGO", "BIFI", "LINA"]

to_day = [[f'\U0001F525 TO DO LIST! \U0001F525\n '
           f'8:00 Wake up\U000023F0\n '
           f'8:20 Drink coffee\U00002615\n '
           f'9:00 Go do harder\U0001F3CB\n']]
