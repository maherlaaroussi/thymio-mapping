# -*- coding: utf-8 -*-

from ultrasonic import *
from servomotor import *
from math import *
import curses

# Nombre de mesure de distance à chaque step
scan = 5

# Text form
bold = "\033[1m"
underline = "\033[4m"
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
normal = "\033[0m"

def scan(mode="fast", verbose=False) :

    # Verbose
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
    p(normal + "------------------------------")

    # Début du scan
    for i in range(int((90 / step) + 1)) :

        rotate(angle)

        # For scans
        c1 = []
        c2 = []
        c3 = []
        c4 = []

        # DISTANCEs ----------------------------------------------

        for i in range (scan):
            c1.append(distance("front"))
            c2.append(distance("back"))
            c3.append(distance("left"))
            c4.append(distance("right"))

        # -------------------------------------------------

        # Selected values
        vf = min(c1)
        vb = min(c2)
        vl = min(c3)
        vr = min(c4)

        # Save data
        f.write(str(angle) + ":" + str(vf) + ":" + str(vl) + ":" + str(vb) + ":" + str(vr) + "\n")

        # Stockage des données
        values.append([angle, vf, vl, vb, vr])

        p(normal + bold + str(angle) + "°" + normal + "")
        p(yellow + "F:" +  str(vf) + " cm\nL: " + str(vl) + " cm\nB: " + str(vb) + " cm\nR: " + str(vr) + " cm")
        p(normal + "----------------------------------")
        time.sleep(0.001)

        angle = angle + step

    rotate(0)
    p(bold + "Values :")
    p(str(values))

    f.close()

    return values
