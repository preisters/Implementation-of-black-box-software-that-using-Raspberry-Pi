import serial

port = "/dev/ttyUSB0"

def GPS(data):

    if data[0:6] == "$GPGGA":
        sdata = data.split(",")

        time = sdata[1][0:2] + ":" + sdata[1][2:4] + ":" + sdata[1][4:6]
        used = sdata[2]
        used2 = sdata[4]

        print(time)
        print(used)
        print(used2)
#
ser = serial.Serial(port, timeout = 0.5)
#
while True :
    data = ser.readline()
    GPS(data)