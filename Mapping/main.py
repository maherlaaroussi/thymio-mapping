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

for x in range(18) :
    rotate(servo, angle)
    angle = angle + 10
    scan(t1, e1)
    scan(t2, e2)
    print("----------------")
    time.sleep(0.5)

rotate(servo, 0)


# Clean GPIOs
GPIO.cleanup()
