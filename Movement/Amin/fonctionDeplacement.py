#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 10:14:41 2019

@author: Ralagane
@author: TImmy
"""

import sys
import time
from pythymiodw import *
import math as m
################################################################################################################
"""
Variables globales
"""
r = ThymioReal()
vitesseG = 200
vitesseD = 205
tempsRotation = 0.011
tempsAvancer = 8.5
x= 0
y= 0
rotationRobot=0
################################################################################################################
"""
Fonction de calcul
"""
def obstacle(distance1,distance2,distance3,distance4,distance5,distance6):
    if r.prox_horizontal[0] > distance1 or r.prox_horizontal[1] > distance2 or r.prox_horizontal[2] > distance3 or r.prox_horizontal[3] > distance4 or r.prox_horizontal[4] > distance5 or r.prox_horizontal[5] > distance6:
        r.sound_system(3)   
        #r.sound_freq()
        return 1
    else:
        return 0

def avancerTemps(temps):
    r.wheels(200,200)
    time.sleep(temps)
    r.wheels(0,0)

def calculTempsAvancement(distance):
    global tempsAvancer
    
    temps = distance/tempsAvancer
    print("Avec une distance de "+str(distance)+" cm, le robot a avancé pendant "+str(temps)+" s.\8n")
    time.sleep((temps))
   

def calculTempsRotation(degree):
    global tempsRotation
    
    rotation = degree*tempsRotation
    print("Avec une rotation de "+str(degree)+" degree(s), le robot a tourné pendant "+str(rotation)+" s.\n")
    time.sleep(rotation)
    
def distanceParcourue(distance):
    global rotationRobot
    global x
    global y
    
    if rotationRobot == 90:
        x = x + distance
        
    if rotationRobot == 270:
        x = x-distance
      
    if rotationRobot == 180:
        y = y- distance
    
    if rotationRobot == 0:
        y = y + distance
    
    if rotationRobot == 360:
        y = y+distance
    
    if rotationRobot >270 and rotationRobot < 360:
        tmp1 = m.cos(360-rotationRobot) * distance
        tmp2 = m.sin(360-rotationRobot) * distance
        x = x-distance
        y = y + distance
        
    if rotationRobot >0 and rotationRobot <90:
        tmp1 = m.cos(90-rotationRobot) * distance
        tmp2 = m.sin(90-rotationRobot) * distance
        x = x+tmp1
        y = y+tmp2
        
    if rotationRobot >90 and rotationRobot < 180:
        tmp1 = m.cos(rotationRobot-90) * distance
        tmp2 = m.sin(rotationRobot-90) * distance
        x = x+tmp1
        y = y - tmp2
        
    if rotationRobot >180 and rotationRobot <270:
        tmp1 = m.cos(270-rotationRobot) * distance
        tmp2 = m.sin(270-rotationRobot) * distance
        x = x-tmp1
        y = y-tmp2

def incrementerRotationRobot(degree):
    global rotationRobot

    tmp = rotationRobot + degree
    if tmp > 360: #rotation droite
        tmp = tmp-360

    if tmp < 0:  #rotation gauche
        tmp = 360 +tmp

    rotationRobot = tmp
    

    
################################################################################################################s
"""
Fonc#tion de mouvement
"""

def avancer(distance):
    r.wheels(vitesseG,vitesseD)
    calculTempsAvancement(distance)
    r.wheels(0,0)
    distanceParcourue(distance)


def reculer(distance):
    r.wheels(-vitesseG,-vitesseD)
    calculTempsAvancement(distance-0.05)
    distanceParcourue(-distance)

def stop():
    r.wheels(0,0)
 
def attend(secondes):
    time.sleep(secondes)

def td(degree):
    r.wheels(vitesseG,-vitesseD)
    calculTempsRotation(degree)
    incrementerRotationRobot(degree)
    stop()


def tg(degree):
    r.wheels(-vitesseG,vitesseD)
    calculTempsRotation(degree) # 1 sec = presque 180 --> supp a 180
    incrementerRotationRobot(-degree)
    stop()

def changerRotation(nouvelleRotation):
    tmps = rotationRobot - nouvelleRotation
    if tmps >=0:
        td(tmps)
        incrementerRotationRobot(tmps)
    else:
        tg(-tmps)
        incrementerRotationRobot(-tmps)

def allerA(cordX,cordY):
    global x,y,rotationRobot
    tmp = rotationRobot
    if cordY > y : #on va en haut
        if cordX > x : #On va en haut à droite
            
            coteAdjacent = abs(cordX - x)
            coteOppose   = abs(cordY - y)
            hypotenus    = m.hypot(coteAdjacent,coteOppose)
            angle = m.acos(coteAdjacent/hypotenus)
            changerRotation(90)
            tg(angle)
            avancer(hypotenus)
            changerRotation(tmp)
            x = cordX
            y = cordY
            
        if cordX < x: #On va en haut à gauche
            
            coteAdjacent = abs(x - cordX)
            coteOppose   = abs(cordY - y)
            hypotenus    = m.hypot(coteAdjacent,coteOppose)
            angle = m.acos(coteAdjacent/hypotenus)
            changerRotation(270)
            td(angle)
            avancer(hypotenus)
            changerRotation(tmp)
            x = cordX
            y = cordY
            
    if cordY < y: #On va en bas
        if cordX > x: #On va en bas à droite
            
            coteAdjacent = abs(cordX - x)
            coteOppose   = abs(y - cordY)
            hypotenus    = m.hypot(coteAdjacent,coteOppose)
            angle        = m.acos(coteAdjacent/hypotenus)
            changerRotation(90)
            td(angle)
            avancer(hypotenus)
            changerRotation(tmp)
            x = cordX
            y = cordY
            
        if cordX < x: #On va en bas à gauche
            
            coteAdjacent = abs(x - cordX)
            coteOppose   = abs(cordY - y)
            hypotenus    = m.hypot(coteAdjacent,coteOppose)
            angle        = m.acos(coteAdjacent/hypotenus)
            changerRotation(270)
            tg(angle)
            avancer(hypotenus)
            changerRotation(tmp)
            x = cordX
            y = cordY




#def eviterUnObstacle(distance):

################################################################################################################
if __name__ == "__main__":
    r.sound_freq()
    attend(1)
    print()
    print("###########################################################\n")
    print("Bonjour ! Il est temps de vous montrer ma vraie puissance !\n")
    print("###########################################################\n") 
    
    print("###########################################################\n")
    print("Initialisation : x vaut : "+str(x)+" y vaut : "+str(y)+" et ma rotation actuelle est :"+str(rotationRobot)+" degrée(s)\n")
    print("###########################################################\n")
    print("Commençons soft : j'avance de 5 centimètres !\n")
    print("###########################################################\n")
    attend(1)
    avancer(5)
    print("###########################################################\n")
    print("Mes valeurs : x vaut : "+str(x)+" y vaut : "+str(y)+" et ma rotation actuelle est :"+str(rotationRobot)+" degrée(s)\n")
    print("###########################################################\n")
    print("Ensuite tournons à gauche de 20 degrée(s) et avancons de 3 centimetres...\n")
    print("###########################################################\n")
    attend(1)
    td(90)
    attend(1)
    avancer(4)
    print("###########################################################\n")
    print("Mes valeurs : x vaut : "+str(x)+" y vaut : "+str(y)+" et ma rotation actuelle est :"+str(rotationRobot)+" degrée(s)\n")
    print("###########################################################\n")
    print("Enfin, je retourne à mon point de départ et je m'arrête..\n")
    print("###########################################################\n")
    attend(1)
    allerA(0,0)
    print("###########################################################\n")
    print("Mes valeurs : x vaut : "+str(x)+" y vaut : "+str(y)+" et ma rotation actuelle est :"+str(rotationRobot)+" degrée(s)\n")
    print("###########################################################\n")
    print("Fin de mon petit voyage, ai-je réussi ?")
    print("###########################################################\n")
    attend(1)
    r.quit()