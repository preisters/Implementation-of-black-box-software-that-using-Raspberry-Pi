from multiprocessing import Process
import RPi.GPIO as GPIO
import time
import picamera
import time
import datetime

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


def func3():
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
     
        if distance < 30 :
            while (i <= 1):
                pwm_so.ChangeDutyCycle(10)
                time.sleep(0.1)
                pwm_so.ChangeDutyCycle(0)
                time.sleep(0.1)
                i = i + 1
            i=0
        if distance >= 100 and distance < 200 :
            while (i <= 1):
                pwm_so.ChangeDutyCycle(10)
                time.sleep(0.2)
                pwm_so.ChangeDutyCycle(0)
                time.sleep(1)
                i = i + 1
            i=0
        if distance >= 30 and distance < 100 :
            while (i <=1):
                pwm_so.ChangeDutyCycle(10)
                time.sleep(0.2)
                pwm_so.ChangeDutyCycle(0)
                time.sleep(0.5)
                i = i+1
            i=0
        else:
            pwm_so.ChangeDutyCycle(0)
        print (' Dist = ', distance)
        time.sleep(0.3)


p1 = Process(target=recording) 
p2 = Process(target=ultrasonic) 
p3 = Process(target=func3) 


p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()


