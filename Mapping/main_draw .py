# -*- coding: utf-8 -*-

from ultrasonic import *
from servomotor import *
import turtle
from math import *

# Mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIOs sensors
t1 = 20
e1 = 21
t2 = 19
e2 = 26
servo = 4
angle = 0
step = 10

x = 0
y = 0

# =========================================================

turtle.setup(300, 300)
turtle.title("Cartographie")
turtle.bgcolor("blue")
turtle.hideturtle()
turtle.pencolor("white")

# For fun)
print("Initialisation du servo-motor ...")
rotate(servo, 180)

print("-------------------")

for i in range(18) :

    c1 = 0
    c2 = 0
    xold = x
    yold = y
    rotate(servo, angle)

    # 1st scan
    c1 = scan(t1, e1)
    c2 = scan(t2, e2)

    # 2nd scan
    cb1 = scan(t1, e1)
    cb2 = scan(t2, e2)

    # Selected values
    vf = min(c2, cb2)
    vb = min(c1, cb1)

    x = vf * cos(angle)
    y = vf * sin(angle)

    print("x: " + str(x) + " y: " + str(y))
    print("cos: " + str(cos(angle)) + " sin: " + str(sin(angle)))

    turtle.up()
    turtle.goto(xold, yold)
    turtle.down()
    turtle.goto(x, y)

    print(str(angle) + "° : B:" + str(vb) + " cm - F:" + str(vf) + " cm")
    print("----------------------------------")
    time.sleep(0.5)

    angle = angle + step

rotate(servo, 0)
time.sleep(500)


# Clean GPIOs
GPIO.cleanup()
