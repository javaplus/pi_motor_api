import serial
import time
from flask import Flask
from flask_cors import CORS
from flask import Response

app = Flask(__name__)
CORS(app)


ser = serial.Serial('/dev/ttyACM0', 9600)


@app.route("/test")
def hello():
    #ser.write('0')
    return Response('{"name" : "value"}', mimetype='application/json')

@app.route('/forward/<string:speed>')
def go_forward(speed):
    ser.write(speed.encode())
    return 'Speed set to %s' % speed


@app.route('/test/<string:input>')
def test(input):
    return '{"name" : "${input}"'



if __name__ == '__main__':
    app.run(host='0.0.0.0')