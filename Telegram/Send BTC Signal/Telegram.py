import telegram
my_token = 'token'
bot = telegram.Bot(token=my_token)
bot.sendMessage(chat_id=-123456789, text='Pair BTC/USDT\r\nLong at: 90000 \r\nTP: 100000 \r\nSL: 10000')
f = open(os.path.dirname(__file__) + "\\Caption.txt", "r", encoding="utf8")
bot.send_photo(chat_id=-123456789,photo=open(os.path.dirname(__file__) + "\\BTCUSD.jpg", 'rb'),caption=f.read())

