import time
import telepot
from telepot.loop import MessageLoop

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if content_type == 'text':
        if msg['text'] == 'locate':
            bot.sendMessage(chat_id, 'GPS location')
        elif msg['text'] == '/start':
            pass
        else:
            bot.sendMessage(chat_id, 'Please choose the RIGHT COMMAND!')
            
TOKEN = '853853898:AAG-x35dFGIsbmUJCX2ZyLUhoXhcwO9yZHk'

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

print ('Listening ...')
while True:
    time.sleep(1000)