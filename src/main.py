from scan import *
#from movement import *

# Mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print(str(scan()))

# Clean GPIOs & Stop
GPIO.cleanup()
