import RPi.GPIO as GPIO
import time

# GPIOs sensors
t1 = 20
e1 = 21
t2 = 23
e2 = 24
t3 = 5
e3 = 6
t4 = 13
e4 = 19
# SCAN =================================================
def distance(capteur):
    d = 0
    if (capteur == "left"):
        d = dist(t1, e1)
    elif (capteur == "back"):
        d = dist(t2, e2)
    elif (capteur == "right"):
        d = dist(t3, e3)
    elif (capteur == "front"):
        d = dist(t4, e4)
    return d

def dist(t, e) :

    # Initialisation
    GPIO.setup(t, GPIO.OUT)
    GPIO.setup(e, GPIO.IN)
    GPIO.output(t, False)

    # Envoie de l'onde
    GPIO.output(t, True)
    time.sleep(0.00001)
    GPIO.output(t, False)

    while (GPIO.input(e) == 0):
        pulse_start = time.time()
    while (GPIO.input(e) == 1):
        pulse_end = time.time()

    time.sleep(0.01)

    # Calculs
    pulse_duration = pulse_end - pulse_start
    distance = round(pulse_duration * 17150, 1)

    return distance

# =========================================================
