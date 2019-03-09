from scan import *

# Mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

scan("fast")

# Clean GPIOs
GPIO.cleanup()
