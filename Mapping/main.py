from scan import *

# Mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



print(str(scan("fast")))

# Clean GPIOs
GPIO.cleanup()
