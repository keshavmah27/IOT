from thing import PiThing
import time

pi_thing = PiThing()

switch = pi_thing.read_switch()
print("Switch :{0}".format(switch))

def switch_changed(state):
    if state:
        print("Switch is on");
    else:
        print("Switch is off")
        
pi_thing.on_switch_change(switch_changed)

print("Blinking LED (Use Ctrl+c to Stop)...")
while True:
      pi_thing.set_led(True)
      time.sleep(0.5)
      switch = pi_thing.read_switch()
      pi_thing.set_led(False)
      time.sleep(0.5)
      
