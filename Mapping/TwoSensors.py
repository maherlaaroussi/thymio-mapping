import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

print "+------------------+"
print "|   Cartographie   |"
print "+------------------+"

Trig1 = 23
Echo1 = 24

Trig2 = 25
Echo2 = 22

# 1er capteur
GPIO.setup(Trig1,GPIO.OUT)
GPIO.setup(Echo1,GPIO.IN)
GPIO.output(Trig1, False)

# 2e capteur
GPIO.setup(Trig2,GPIO.OUT)
GPIO.setup(Echo2,GPIO.IN)
GPIO.output(Trig2, False)

repet = input("Combien de fois ? ")

for x in range(repet):

    time.sleep(1)

    GPIO.output(Trig1, True)
    time.sleep(0.00001)
    GPIO.output(Trig1, False)

    while GPIO.input(Echo1)==0:
      debutImpulsion1 = time.time()

    while GPIO.input(Echo1)==1:
      finImpulsion1 = time.time()

    distance1 = round((finImpulsion1 - debutImpulsion1) * 340 * 100 / 2, 1)

    print "Capteur 1 : ", distance1," cm"

    time.sleep(0.00001)

    GPIO.output(Trig2, True)
    time.sleep(0.00001)
    GPIO.output(Trig2, False)

    while GPIO.input(Echo2)==0:
      debutImpulsion2 = time.time()

    while GPIO.input(Echo2)==1:
      finImpulsion2 = time.time()

    distance2 = round((finImpulsion2 - debutImpulsion2) * 340 * 100 / 2, 1)

    print "Capteur 2 : ", distance2," cm"

    GPIO.cleanup()
