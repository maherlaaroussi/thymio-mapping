from scan import *
from movement import *

# Mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

avancer(5)
getPoxS()
print(str(scan()))


# Clean GPIOs
GPIO.cleanup()
