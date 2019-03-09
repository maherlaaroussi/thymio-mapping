from scan import *

# Mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


print(str(scan("normal"), True))


# Clean GPIOs
GPIO.cleanup()
