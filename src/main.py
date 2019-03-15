from scan import *
#from movement import *

# Mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

angle = 0

for i in range(50):
	print("F: " + str(distance("front")))
	print("L: " + str(distance("left")))
	print("B: " + str(distance("back")))
	print("R: " + str(distance("right")))
	rotate(angle)
	print("============")
	time.sleep(1)
	angle = angle + 5
# Clean GPIOs & Stop
GPIO.cleanup()
