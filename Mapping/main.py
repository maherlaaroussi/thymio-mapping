from ulrasonic import *
from servomotor import *

# Mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIOs sensors
t1 = 23
e1 = 24
t2 = 21
e2 = 20

# =========================================================

trigger = input("GPIO Trigger : ")
echo = input("GPIO Echo : ")

servo = input("GPIO Servo : ")

for x in range(5) :
   scan(trigger, echo)
   rotate(servo, 180)

# Clean GPIOs
GPIO.cleanup()
