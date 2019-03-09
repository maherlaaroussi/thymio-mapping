from scan import *
from fonctionDeplacement import *

# Mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



scan("fast")
avancerTemps(1)

# Clean GPIOs
GPIO.cleanup()
