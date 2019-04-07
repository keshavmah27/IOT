import threading
import RPi.GPIO as GPIO

BULB_PIN  = 12 #Physical Pin 32
FAN_PIN   = 16 #Physical Pin 36
AC_PIN    = 20 #Physical Pin 38
TV_PIN    = 21 #Physical Pin 40

class PiThing():
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BULB_PIN,GPIO.OUT)
        GPIO.setup(FAN_PIN,GPIO.OUT)
        GPIO.setup(AC_PIN,GPIO.OUT)
        GPIO.setup(TV_PIN,GPIO.OUT)
        self._lock=threading.Lock()
                
    def read_devices_status(self):
        with self._lock:
            return [GPIO.input(BULB_PIN),GPIO.input(FAN_PIN),GPIO.input(AC_PIN),GPIO.input(TV_PIN)]

    def set_bulb(self, value):
        with self._lock:
            GPIO.output(BULB_PIN,value)

    def set_fan(self, value):
        with self._lock:
            GPIO.output(FAN_PIN,value)

    def set_ac(self, value):
        with self._lock:
            GPIO.output(AC_PIN,value)

    def set_tv(self, value):
        with self._lock:
            GPIO.output(TV_PIN,value)