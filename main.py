from thing import PiThing
from flask import *
import time
import random
import json
from flask_socketio import SocketIO

app = Flask(__name__)
pi_thing = PiThing()
socketio = SocketIO(app)

@app.route('/')
def index():
    devicesStatus = pi_thing.read_devices_status()
    return render_template('index.html', devicesStatus=devicesStatus)

@socketio.on('send_status')
def send_status(message):
    devicesStatus = pi_thing.read_devices_status()
    str = {'bulb': devicesStatus[0],'fan': devicesStatus[1],'ac': devicesStatus[2],'tv': devicesStatus[3]}
    socketio.emit('devices_status',str)
    print(message)
    
@socketio.on('change_bulb')
def change_bulb(bulb_state):
    if bulb_state == 'off':
        pi_thing.set_bulb(False)
    elif bulb_state == 'on':
        pi_thing.set_bulb(True)
    bulb_status = {'bulb' : bulb_state}    
    status_changed(bulb_status)

@socketio.on('change_fan')
def change_fan(fan_state):
    if fan_state == 'off':
        pi_thing.set_fan(False)
    elif fan_state == 'on':
        pi_thing.set_fan(True)
    fan_status = {'fan' : fan_state}    
    status_changed(fan_status)

@socketio.on('change_ac')
def change_ac(ac_state):
    if ac_state == 'off':
        pi_thing.set_ac(False)
    elif ac_state == 'on':
        pi_thing.set_ac(True)
    ac_status = {'ac' : ac_state}    
    status_changed(ac_status)

@socketio.on('change_tv')
def change_tv(tv_state):
    if tv_state == 'off':
        pi_thing.set_tv(False)
    elif tv_state == 'on':
        pi_thing.set_tv(True)
    tv_status = {'tv' : tv_state}    
    status_changed(tv_status)


def status_changed(state):
    socketio.emit('status_changed',state)
    

if __name__ == "__main__":
    socketio.run(app,host='0.0.0.0',debug=True)