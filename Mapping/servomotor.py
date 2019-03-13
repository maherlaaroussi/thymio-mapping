import RPi.GPIO as GPIO
import time

servo = 4

def rotate(angle) :

    GPIO.setup(servo, GPIO.OUT)
    pwm = GPIO.PWM(servo,100)

    addAngle = 5
    ang = float(angle)

    pwm.start(5)

    angleChoisi = ang/10 + addAngle
    pwm.ChangeDutyCycle(angleChoisi)
    time.sleep(1.2)
