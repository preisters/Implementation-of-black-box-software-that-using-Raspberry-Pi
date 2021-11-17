from multiprocessing import Process
import RPi.GPIO as GPIO
import time
import picamera
import time
import datetime
import telepot
import subprocess
from telepot.loop import MessageLoop

savepath = '/home/pi/Desktop/BlackBox'




def recording():
    while True:
        
        with picamera.PiCamera() as camera:
            camera.resolution = (640,480)
            now = datetime.datetime.now()
            filename = now.strftime('%d-%H:%M:%S')
            camera.start_recording(output = savepath + '/' + filename + '.h264')
            camera.start_preview()
            camera.wait_recording(60)
            camera.stop_preview()
            camera.stop_recording()

def ultrasonic():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings (False)

    vcc = 21
    trig = 20
    echo = 16
    sound = 26
    num = 0

    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)
    GPIO.setup(sound, GPIO.OUT)
    GPIO.setup(vcc, GPIO.OUT, initial=GPIO.HIGH)

    pwm_so = GPIO.PWM(26, 1500)
    pwm_so.start(0)
    i=0
    x=0
    
    my_token = '853853898:AAG-x35dFGIsbmUJCX2ZyLUhoXhcwO9yZHk'
    bot = telepot.Bot(my_token)
    
    while True:
        GPIO.output(trig,False)
        time.sleep(0.5)
        
        GPIO.output(trig, True)
        time.sleep(0.000001)
        GPIO.output(trig, False)
        
        while GPIO.input(echo) == 0:
            pulse_start = time.time()
            
        while GPIO.input(echo) == 1:
            pulse_end = time.time()
            
        pulst_duration = pulse_end - pulse_start
        distance = pulst_duration * 17000

        if x > 20 :
            msg = 'BBSW User is !DANGER!'
            telegram_id = '700008506'

            bot.sendMessage(chat_id = telegram_id, text = msg)

        if distance < 30 :
            while (i <= 1):
                pwm_so.ChangeDutyCycle(10)
                time.sleep(0.1)
                pwm_so.ChangeDutyCycle(0)
                time.sleep(0.1)
                i = i + 1
                x = x + 1
            i=0
            
        if distance >= 100 and distance < 200 :
            while (i <= 1):
                pwm_so.ChangeDutyCycle(10)
                time.sleep(0.2)
                pwm_so.ChangeDutyCycle(0)
                time.sleep(1)
                i = i + 1
            i=0
            x=0
        if distance >= 30 and distance < 100 :
            while (i <=1):
                pwm_so.ChangeDutyCycle(10)
                time.sleep(0.2)
                pwm_so.ChangeDutyCycle(0)
                time.sleep(0.5)
                i = i+1
            i=0
            x=0
        else:
            pwm_so.ChangeDutyCycle(0)
        print (' Dist = ', distance)
        print (' x = ' , x )
        
def func3():
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

def func4():
    subprocess.call ('cat /dev/ttyUSB0>log.txt', shell=True)


p1 = Process(target=recording) 
p2 = Process(target=ultrasonic) 
p3 = Process(target=func3) 
p4 = Process(target=func4)

p1.start()
p2.start()
p3.start()
p4.start()

p1.join()
p2.join()
p3.join()
p4.join()

