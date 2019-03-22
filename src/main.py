from scan import *
from movement import *

# Mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

sound("start")
avancer(5)
td(270)
avancer(9)
allerA(0,0,True)
print(str(getPosX()) + ":" + str(getPosY()))

sound("scan")
print(str(scan()))


# Clean GPIOs & Stop
sound("stop")
quit()
GPIO.cleanup()
