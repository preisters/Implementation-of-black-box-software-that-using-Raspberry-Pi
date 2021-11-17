import time
import telepot
from telepot.loop import MessageLoop
import serial

port = "/dev/ttyUSB0"



def GPS(data):
    global kk, kk2
    if data[0:6] == "$GPGGA":
        sdata = data.split(",")

 
        kk2 = sdata[2]
        kk = sdata[4]
        
        print('1234')
        print(kk)
        print('1234')

def handle(msg):
    
    ser = serial.Serial(port, timeout = 0.5)

    data = ser.readline()
    GPS(data)

    content_type, chat_type, chat_id = telepot.glance(msg)    
    if content_type == 'text':
        if msg['text'] == 'locate':
            bot.sendMessage(chat_id, kk2)
            bot.sendMessage(chat_id, kk)            
        elif msg['text'] == '/start':
            pass
        else:
            bot.sendMessage(chat_id, 'Please choose the RIGHT COMMAND!')
    #

    #


            
TOKEN = '853853898:AAG-x35dFGIsbmUJCX2ZyLUhoXhcwO9yZHk'

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()


    
print ('Listening ...')
while True:
    time.sleep(1000)



    