import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings (False)


sound = 26


GPIO.setup(sound, GPIO.OUT)

pwm_so = GPIO.PWM(26, 1500)
pwm_so.start(0)

while True:
    pwm_so.ChangeDutyCycle(10)
    print ('1')
    time.sleep(1)
    pwm_so.ChangeDutyCycle(0)
    print ('2')
    time.sleep(1)

