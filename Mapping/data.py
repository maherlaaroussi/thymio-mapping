# -*- coding: utf-8 -*-

from ultrasonic import *
from servomotor import *
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

# Précision du scan
step = 2

values = []

# Text
bold = "\033[1m"
underline = "\033[4m"
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
normal = "\033[0m"

# Save
t = str(int(time.time())) + ".txt"
f = open("data/" + t, "w+")
print(bold + green + "Create file: " + t) 
# =========================================================

# For fun)
print(bold + red + "Initialisation du servo-motor ...")
rotate(servo, 180)

print(normal + "------------------------------")

for i in range(int((180 / step) + 1)) :

    rotate(servo, angle)

    # 1st scan
    c1 = distance(t1, e1)
    c2 = distance(t2, e2)

    time.sleep(0.01)

    # 2nd scan
    cb1 = distance(t1, e1)
    cb2 = distance(t2, e2)

    # Selected values
    vf = min(c2, cb2) - 2
    vb = min(c1, cb1) - 3

    # Save data
    f.write(str(angle) + ":" + str(vf) + ":" + str(vb) + "\n")

    # Stockage des données
    values.append([angle, vb, vf])

    print(normal + bold + str(angle) + "°" + normal + "")
    print(yellow + "F:" +  str(vb) + " cm \nB: " + str(vf) + " cm")
    print(normal + "----------------------------------")
    time.sleep(0.01)

    angle = angle + step

rotate(servo, 0)
print(bold + "Values :")
print(str(values))

f.close()

# Clean GPIOs
GPIO.cleanup()

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
