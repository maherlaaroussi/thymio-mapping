from scan import *
#from movement import *

# Mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print(str(arg[1]))
print(str(scan(arg[1])))

# Clean GPIOs & Stop
GPIO.cleanup()
