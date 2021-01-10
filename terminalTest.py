import serial
import time

ser = serial.Serial("com4")
ser.timeout = 1

buf = [0x14] #reset
ser.write(buf)
time.sleep(1)

buf = [0x17, 0x01] # Enter IEE command mode
ser.write(buf)

buf = [0x1b, 0x74, 0x1b] #char mode
ser.write(buf)

buf = [0x1d, 0x05] 
ser.write(buf)
print(ser.readline())

buf = [0x0E]
ser.write(buf)

for i in range(38):
    start = 0xA0
    if(i%5 == 0):
        buf = [0x06]
        ser.write(buf)
        buf = [start+i]
        ser.write(buf)
        buf = [0x07]
        ser.write(buf)
    else:
        buf = [start+i]
        ser.write(buf)
         
    #time.sleep(0.1)
    #buf = [0x08] # backspace 1 char
    #ser.write(buf)

ser.close()
