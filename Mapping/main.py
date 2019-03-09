from scan import *

# Mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



scan("normal", False)

# Clean GPIOs
GPIO.cleanup()
