import RPi.GPIO as GPIO
import time

# GPIOs sensors
t1 = 20
e1 = 21
t2 = 23
e2 = 24

# Timeout input/output : 15s
timeout = 15

# SCAN =================================================
def distance(capteur):
    d = 0
    if (capteur == "back"):
        d = dist(t1, e1)
    elif (capteur == "front"):
        d = dist(t2, e2)
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

    # If fail
    echec = False

    # timeout
    timelimit = time.time() + timeout
    while (GPIO.input(e) == 0):
        pulse_start = time.time()
        if (time.time() > timelimit):
            echec = True
            break

    # timeout
    timelimit = time.time() + timeout
    while (GPIO.input(e) == 1):
        pulse_end = time.time()
        if (time.time() > timelimit):
            echec = True
            break

    time.sleep(0.01)

    # Calculs
    try:
        if (echec):
            distance = 0
        else:
            pulse_duration = pulse_end - pulse_start
            distance = round(pulse_duration * 17150, 1)
    except:
        distance = 0

    if (distance > 400):
        distance = 0

    return distance

# =========================================================
