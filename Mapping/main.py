from ulrasonic import *

# Mode GPIO
GPIO.setmode(GPIO.BCM)

# GPIOs sensors
t1 = 23
e1 = 24
t2 = 21
e2 = 20

# =========================================================

trigger = input("GPIO Trigger : ")
echo = input("GPIO Echo : ")

for x in range(100) :
   scan(trigger, echo)

# Clean GPIOs
GPIO.cleanup()
