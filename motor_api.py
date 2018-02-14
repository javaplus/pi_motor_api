import serial
import time
import json
import motor_controller
from flask import Flask, request
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
    responseMsg = {}
    responseMsg['message'] = 'Speed set to %s' % speed 
    return json.dumps(responseMsg)


@app.route('/test/<string:input>')
def test(input):
    data = {}
    data['name'] = input
    return json.dumps(data) 

@app.route('/move', methods = ['POST'])
def move():
    runTime = request.json["time"]
    speed = request.json["speed"]
    direction = request.json["direction"]
    motor_controller.doTimedMove(runTime, speed, direction)
    data = {}
    data['message'] = 'Moving for %s seconds' % runTime
    return json.dumps(data) 



if __name__ == '__main__':
    app.run(host='0.0.0.0')
