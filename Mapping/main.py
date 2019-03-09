from scan import *

# Mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



first = scan("fast")
print(str(first))

# Clean GPIOs
GPIO.cleanup()
