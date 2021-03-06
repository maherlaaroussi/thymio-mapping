# -*- coding: utf-8 -*-

from package.ultrasonic import *
from package.servomotor import *
from math import *

# Nombre de mesure de distance à chaque step
s = 14

# Text form
bold = "\033[1m"
underline = "\033[4m"
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
normal = "\033[0m"

def scan(filename="nothing", mode="fast", verbose=False) :

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
    t = str(filename) + ".txt"
    f = open("data/" + t, "w+")
    p(bold + green + "Create file: " + t)

    # For fun
    p(bold + red + "Initialisation du servo-motor ...")
    p(normal + "------------------------------")

    # Début du scan
    for i in range(int((180 / step) + 1)) :

        rotate(angle)

        # For scans
        c1 = []
        c2 = []

        # DISTANCEs ----------------------------------------------

        for i in range (s):
            c1.append(distance("front"))
            c2.append(distance("back"))

        # Selected values
        vf = max(c1)
        vb = max(c2)

        # -------------------------------------------------

        # Save data
        f.write(str(angle) + ":" + str(vf) + ":" + str(vb) + "\n")

        # Stockage des données
        values.append([angle, vf, vb])

        p(normal + bold + str(angle) + "°" + normal + "")
        p(yellow + "F:" +  str(vf) + " cm\nB: " + str(vb) + " cm\n")
        p(normal + "----------------------------------")
        time.sleep(0.001)

        angle = angle + step

    rotate(0)
    p(bold + "Values :")
    p(str(values))

    f.close()

    return values
