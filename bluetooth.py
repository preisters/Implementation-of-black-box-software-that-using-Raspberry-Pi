#import PyBBIO library:
from bbio import *
import serial
import time

BLED = GPIO3_21
TEMP = AIN5
bl = serial.Serial("/dev/ttyUSB0", baudrate=115200)

def loop():
 data = bl.readline()
 if data == 'T\n':
  val1 = analogRead(TEMP)

  bl.write(str(TEMP))


run(setup, loop)