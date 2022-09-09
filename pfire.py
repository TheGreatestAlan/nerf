#!/user/bin/env python3 
import serial 
import time 
import os 
from os.path import exists   
if __name__ == '__main__':         
    test = open("started.txt", "w")         
    test.close()         
    try:                 
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    except:
        time.sleep(5)
        try:
            ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)                 except:
            ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
            ser.reset_input_buffer()
            time.sleep(3)
            ser.write(b"FAKE\n")
            while True:
                if(exists('/home/pi/fire.txt')):
                    ser.write(b"FIRE\n")
                    print("SHOOTING")
                    os.remove("fire.txt")
                if(exists('/home/pi/fake.txt')):
                    ser.write(b"FAKE\n")
                    print("FAKING")
                    os.remove("fake.txt")
