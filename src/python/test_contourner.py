# -*- coding: utf-8 -*-
from package.movement import *
from package.contourner import *
#import sys
#from pythymiodw import *
#import time

#Cette methode permet dans un premeir temps de detecter un obstacle, puis de l'evite et le contourner_obstacle
#par la droite si possible sinon par la gauche.
#assurer que le capteur le plus a droite et a gauche n'a aps dobstale trop prche pour contourne

def contourner_obstacle():
    while(obstacle_existe(2)==0):
        avancer(2)
    distance_obstacle=reperer_dist_obstacle(2, 1)
    dinst_3=distance_obstacle-3
    avancer(dinst_3)#Avancer jusqu'a 3cm de l'ostacle
"""
    impossible=False
    objectif=False
    while(reussite != True and objectif != True):
        if(DROITE() == True):
            if(DROITE() == True):
                td(180)
                objectif=True
            else:
                GAUCHE()
                y=y-10
                if(GAUCHE()==True):
                    if(GAUCHE()==True):
                        rg(180)
                        objectif=True
                    elif(GAUCHE()==False):
                        impossible=True
                        DROITE()
                    else:
                        impossible=True
        else:
            if(GAUCHE() == True):
                if(GAUCHE() == True):
                    tg(180)
                    objectif=True
                else:
                    impossible=True
                    DROITE()
                    y=y-10
            else:
                impossible=True
    if(impossible==False and objectif==True):
        return True
    else:
        return False
"""


################ MAIN CONTOURNER ################
contourner_obstacle()
#avancer(3)
quitter()
