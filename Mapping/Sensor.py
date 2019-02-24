import RPi.GPIO as GPIO
import time

def scan(t, e) :

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(t, GPIO.OUT)
    GPIO.setup(e, GPIO.IN)

    GPIO.output(t, False)

    time.sleep(1)

    GPIO.output(t, True)
    time.sleep(0.00001)
    GPIO.output(t, False)

    while GPIO.input(e)==0:
        debutImpulsion = time.time()

    while GPIO.input(e)==1:
        finImpulsion = time.time()

    distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)
    temps = finImpulsion - debutImpulsion

    print "La distance est de : ", distance," cm"
    print "Debut : ", temps," ms"

    GPIO.cleanup()


print "+-----------------------------------------------------------+"
print "|   Mesure de distance par le capteur ultrasonore HC-SR04   |"
print "+-----------------------------------------------------------+"

repet = input("Entrez un nombre de repetitions de mesure : ")

for x in range(repet) :
   scan(23, 24)
