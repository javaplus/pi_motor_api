import serial
import time
from flask import Flask
app = Flask(__name__)

ser = serial.Serial('/dev/ttyACM0', 9600)


@app.route("/")
def hello():
    ser.write('0')
    return "Hello World!"

@app.route('/forward/<int:speed>')
def go_forward(speed):
    ser.write(speed.encode())
    # show the post with the given id, the id is an integer
    return 'Speed set to %s' % speed


if __name__ == '__main__':
    app.run(host='0.0.0.0')