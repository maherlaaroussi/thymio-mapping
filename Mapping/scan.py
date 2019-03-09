# -*- coding: utf-8 -*-

from ultrasonic import *
from servomotor import *
from math import *

# GPIOs sensors
t1 = 20
e1 = 21
t2 = 19
e2 = 26
servo = 4

# Text form
bold = "\033[1m"
underline = "\033[4m"
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
normal = "\033[0m"

def scan(mode, verbose=False) :

    #Functions
    def p(text):
        if (verbose):
            print(text)

    # Précision du scan
    if (mode == "fast"):
        step = 10
    elif (mode == "normal"):
        step = 5
    elif (mode == "slow"):
        step = 2
    else:
        step = 10

    # Angle de base
    angle = 0

    # Stockage des données
    values = []

    # Save
    t = str(int(time.time())) + ".txt"
    f = open("data/" + t, "w+")
    p(bold + green + "Create file: " + t)

    # For fun
    p(bold + red + "Initialisation du servo-motor ...")
    rotate(servo, 180)
    p(normal + "------------------------------")

    # Début du scan
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

        p(normal + bold + str(angle) + "°" + normal + "")
        p(yellow + "F:" +  str(vb) + " cm \nB: " + str(vf) + " cm")
        p(normal + "----------------------------------")
        time.sleep(0.01)

        angle = angle + step

    rotate(servo, 0)
    p(bold + "Values :")
    p(str(values))

    f.close()

    return values
