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
x2 = 0
y2 = 0
fx = 0
fy = 0
fx2 = 0
fy2 = 0

# =========================================================

turtle.setup(500, 500)
turtle.title("Cartographie")
turtle.bgcolor("blue")
turtle.hideturtle()
turtle.pencolor("white")

# For fun)
print("Initialisation du servo-motor ...")
rotate(servo, 180)

print("-------------------")

for i in range(int(180 / step)) :

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

    # 2nd scan
    cb1 = scan(t1, e1)
    cb2 = scan(t2, e2)

    # Selected values
    vf = min(c2, cb2)
    vb = min(c1, cb1)

    x = vf * cos(angle / 180. * pi)
    y = vf * sin(angle / 180. * pi)
    print("x: " + str(x) + " y: " + str(y))

    if (xold != 0 and yold != 0):
        turtle.up()
        turtle.goto(xold, yold)
        turtle.down()
        turtle.goto(x, y)
    else:
        fx = x
        fy = y


    x2 = vb * cos((angle + 180) / 180. * pi)
    y2 = vb * sin((angle + 180) / 180. * pi)
    print("x2: " + str(x2) + " y2: " + str(y2))

    if (x2old != 0 and y2old != 0):
        turtle.up()
        turtle.goto(x2old, y2old)
        turtle.down()
        turtle.goto(x2, y2)
    else:
        fx2 = x2
        fy2 = y2

    print(str(angle) + "° : B:" + str(vb) + " cm - F:" + str(vf) + " cm")
    print("----------------------------------")
    time.sleep(0.5)

    angle = angle + step

rotate(servo, 0)

turtle.up()
turtle.goto(x, y)
turtle.down()
turtle.goto(fx2, fy2)

turtle.up()
turtle.goto(x2, y2)
turtle.down()
turtle.goto(fx, fy)
time.sleep(500)


# Clean GPIOs
GPIO.cleanup()
