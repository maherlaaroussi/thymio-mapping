from scan import *

# Mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



scan("normal", false)

# Clean GPIOs
GPIO.cleanup()
