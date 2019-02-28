from ultrasonic import *
from servomotor import *

# Mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIOs sensors
t1 = 21
e1 = 20
t2 = 26
e2 = 19
angle = 0

# =========================================================

for x in range(5) :
   scan(t1, e1)
   scan(t2, e2)
   print("======================")
   rotate(4, angle)
   angle = angle + 30

# Clean GPIOs
GPIO.cleanup()
