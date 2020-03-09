import socketio
# import PWM
import json

sio = socketio.Client()


@sio.event
def connect():
    print('connection established')


@sio.event
def success(data):
    print('message received with ', data)


@sio.on('throttle', namespace='/car')
def throttle(data):
    print('message received with ', data)


@sio.on('steer', namespace='/car')
def steer(data):
    print('message received with ', data)
    # jsonData = json.loads(data)
    print(data['degree'])
    # PWM.steer(bool(jsonData["dir"]), bool(jsonData["degree"]))


@sio.on('changeSpeed', namespace='/car')
def changeSpeed(data):
    # PWM.changeSpeed(data)
    print('message received with ', data)


@sio.on('idle', namespace='/car')
def idle(data):
    # PWM.idleSpeed()
    print('message received with ', data)


@sio.event
def stop():
    # PWM.stop()
    print('disconnected from server')


@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('http://10.31.26.40:8020', namespaces=["/car"])
sio.wait()
