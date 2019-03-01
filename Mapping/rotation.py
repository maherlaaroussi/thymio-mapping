# -*- coding: utf-8 -*-

from ultrasonic import *
from servomotor import *

# Mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIOs sensors
t1 = 20
e1 = 21
t2 = 19
e2 = 26
servo = 4
angle = 0

# =========================================================
print(str(scan(t1, e1)))
rotate(servo, 180)
print(str(scan(t1, e1)))
rotate(servo, 0)


# Clean GPIOs
GPIO.cleanup()
