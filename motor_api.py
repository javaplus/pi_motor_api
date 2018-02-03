import serial
import time
from flask import Flask
app = Flask(__name__)

ser = serial.Serial('/dev/ttyACM0', 9600)


@app.route("/")
def hello():
    ser.write('3')
    return "Hello World!"



if __name__ == '__main__':
    app.run(host='0.0.0.0')