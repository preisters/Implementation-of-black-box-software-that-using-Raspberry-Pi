import serial
import pynmea2

port = '/dev/ttyAMA0'
ser = serial.Serial(port, baudrate=9600)
print("serial connect")

while True:
    data = ser.readline()
    if data[0:6] == '$GPGGA':
        msg = pynmea2.parse(data)
        print("latitude: "+msg.lat+msg.lat_dir)
        print("longitude: "+msg.lon+msg.lon_dir)
        print("altitude: "+str(msg.altitude)+msg.altitude_units)