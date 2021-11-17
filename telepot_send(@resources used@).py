import telepot

my_token = '853853898:AAG-x35dFGIsbmUJCX2ZyLUhoXhcwO9yZHk'
bot = telepot.Bot(my_token)

msg = 'BBSW User is !DANGER!'
telegram_id = '700008506'

bot.sendMessage(chat_id = telegram_id, text = msg)

