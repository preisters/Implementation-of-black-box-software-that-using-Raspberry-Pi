import time
from time import strftime

def dms_to_dec(value, dir):
    mPos = value.find(".")-2
    
    degree = float(value[:mPos])
    minute = float(value[mPos:])
    
    converted_degree = float(degree) + float(minute)/float(60)
    
    if dir == "W":
    converted_degree = -converted_degree