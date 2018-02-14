import threading
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

def doTimedMove(runTime,speed, direction):
    print("runtime:" + runTime + " speed:" + speed + " direction:" + direction)
    t = threading.Thread(target=worker, args=(runTime,speed,direction,))
    t.start()
	
        
def worker(runTime, speed, direction):
    vector = direction + speed + 'E'
    ser.write(vector.encode())
    time.sleep(runTime)
    print("Waking up to stop")
    vector = direction + '0E'
    ser.write(vector.encode())
