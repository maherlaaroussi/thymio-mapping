from scan import *
import sys
#from movement import *

# Mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print(str(sys.argv[1]))
print(str(scan(sys.argv[1])))

# Clean GPIOs & Stop
GPIO.cleanup()
