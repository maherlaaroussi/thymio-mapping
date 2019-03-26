from package.scan import *
import sys
#from package.movement import *

# Mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print(str(scan(sys.argv[1], "normal")))

# Clean GPIOs & Stop
GPIO.cleanup()
