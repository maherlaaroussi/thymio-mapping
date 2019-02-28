import RPi.GPIO as GPIO
import time

def rotate(data, angle) :

    GPIO.setup(data, GPIO.OUT)
    pwm = GPIO.PWM(data,100)

    ajoutAngle = 5
    angle = float(angle)

    pwm.start(5)

    angleChoisi = angle/10 + ajoutAngle
    pwm.ChangeDutyCycle(angleChoisi)
    time.sleep(10)
