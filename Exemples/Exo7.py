# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 08:52:51 2015

@author: Maher
"""

import pythymio as pt

# Genere x combinaisons
def hasardComb(x):

    lettres = ['U', 'D', 'L', 'R']
    lettresOut = []

    for i in range(x):
        lettresOut.append(lettres[random.randint(0,x-1)])

    return lettresOut

with pt.thymio(["acc"],[]) as Thym:
    def progression (idnum, evt, data):
        if evt == "fwd.acc":
                print(data[0])

    Thym.loop(progression)
