from scan import *
from movement import *

# Mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

avancer(5)
getPosX()
print(str(scan()))


# Clean GPIOs
GPIO.cleanup()
