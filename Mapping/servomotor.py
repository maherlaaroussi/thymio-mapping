import RPi.GPIO as GPIO
import time

def rotate(data, angle) :

    GPIO.setup(data, GPIO.OUT)
    pwm = GPIO.PWM(data,100)

    addAngle = 5
    ang = float(angle)

    pwm.start(5)

    angleChoisi = ang/10 + addAngle
    pwm.ChangeDutyCycle(angleChoisi)
    time.sleep(10)
