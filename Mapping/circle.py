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
corps = 15

# Précision du scan
step = 5

# Vars de pos
x = 0
y = 0
x2 = 0
y2 = 0
fx = 0
fy = 0
fx2 = 0
fy2 = 0

# =========================================================

turtle.setup(500, 500)
turtle.title("Cartographie")
turtle.bgcolor("black")
turtle.hideturtle()
turtle.pencolor("white")

turtle.home()
turtle.setheading(0)

# For fun)
print("Initialisation du servo-motor ...")
rotate(servo, 180)

print("-------------------")

for i in range(int((180 / step) + 1)) :

    c1 = 0
    c2 = 0
    xold = x
    yold = y
    x2old = x2
    y2old = y2
    rotate(servo, angle)

    # 1st scan
    c1 = scan(t1, e1)
    c2 = scan(t2, e2)

    time.sleep(0.01)

    # 2nd scan
    cb1 = scan(t1, e1)
    cb2 = scan(t2, e2)

    # Selected values
    vf = min(c2, cb2) - 2 + corps
    vb = min(c1, cb1) - 3 + corps

    turtle.up()
    turtle.forward(corps)

    turtle.down()
    turtle.forward(vf)

    turtle.up()
    turtle.backward(corps + vf)

    turtle.backward(corps)
    turtle.down()
    turtle.backward(vb)

    turtle.up()
    turtle.forward(vb + corps)

    turtle.left(step)

    print(str(angle) + "° : B:" + str(vb) + " cm - F:" + str(vf) + " cm")
    print("----------------------------------")
    time.sleep(0.01)

    angle = angle + step

rotate(servo, 0)

time.sleep(500)


# Clean GPIOs
GPIO.cleanup()
