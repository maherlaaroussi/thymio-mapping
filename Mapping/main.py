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

# For fun)
print("Initialisation du servo-motor ...")
rotate(servo, 180)

for x in range(18) :
    c1 = 0
    c2 = 0
    rotate(servo, angle)
    angle = angle + 10
    c1 = scan(t1, e1)
    c2 = scan(t2, e2)
    print(str(angle - 10) + "° : B:" + str(c1) + " -// F:" + str(c2))
    print("-------------------")
    time.sleep(0.5)

rotate(servo, 0)


# Clean GPIOs
GPIO.cleanup()
