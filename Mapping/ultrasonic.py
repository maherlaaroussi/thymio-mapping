import RPi.GPIO as GPIO
import time

# SCAN =================================================
def scan(t, e) :

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

    # Calculs
    pulse_duration = pulse_end - pulse_start
    distance = round(pulse_duration * 17150, 1)

    return distance

# =========================================================
