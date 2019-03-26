# -*- coding: utf-8 -*-
import sys
from pythymiodw import *
import time

r = ThymioReal()

############ COUTOURNER ###############

mesure_capteur=[[0,4300],[0.5,4289],[1.0,4250],
        [1.5,4168],[2.0,3975],[2.5,3547],
        [3.0,3283],[3.5,3050],[4.0,2809],
        [4.5,2665],[5.0,2495],[5.5,2366],
        [6.0,2212],[6.5,2105],[7.0,1984],
        [7.5,1860],[8.0,1750],[8.5,1658],
        [9.0,1540],[9.5,1410],[10.0,1232],
        [10.5,0]]


#convertie mesure thymio en cm
def convert_cm(dist_thy):
    i=0
    for i in range (0,22):
        if(mesure_capteur[i][1]>=dist_thy):
            res=mesure_capteur[i][0]
    return res

# Permet de mesurer la distance d'un obstacle
#num_capteur: numero du capteur souhaitant être utiliser (0 à 4)
#nb_iter: nombre d'iteration
def reperer_dist_obstacle(num_capteur, nb_iter):
    m=0
    nb_iter=nb_iter+1;
    if (num_capteur>4):
        return -1
    else:
        for i in range(0,nb_iter): #premier boucle pour initialiser
            m=r.prox_horizontal[num_capteur]
            time.sleep(0.5)
            cm=convert_cm(m)
            print(m,cm)
        return cm

def reperer_dist_obstacle_bis(num_capteur):
    m=0
    etat=1
    if (num_capteur>4):
        return -1
    else:
        while(etat==1):
            m=r.prox_horizontal[num_capteur]
            cm=convert_cm(m)
            time.sleep(0.5)
            print(m,cm)

def obstacle_existe(num_capteur):
    m=0
    for i in range(0,2): #premier boucle pour initialiser
        m=r.prox_horizontal[num_capteur]
        time.sleep(0.5)
    if(m == 0):
        return 0
    else:
        return 1


def DROITE():
    reussite=0
    cp0=0
    cp1=1
    cp2=2
    cp3=3
    while(reussite == 0):
        td(90)
        if(obstacle_existe==1):
            tg(90)
            return False
        else:
            avancer(5)
            x=x+5
            tg(90)
            if(obstacle_existe==0):
                avancer(5)
                y=y+5
                tg(90)
                reussite=True
                return True
            else:
                allerA(0,0,True) #retour a la position initial avec rotation initialiser
                return False

def GAUCHE():
    reussite=0
    cp0=0
    cp1=1
    cp2=2
    cp3=3
    while(reussite == 0):
        tg(90)
        if(obstacle_existe==1):
            td(90)
            return False
        else:
            avancer(5)
            y=y+5
            td(90)
            if(obstacle_existe==0):
                avancer(5)
                x=x+5
                td(90)
                reussite=True
                return True
            else:
                allerA(0,0,True) #retour a la position initial avec rotation initialiser
                return False
