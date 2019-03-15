# -*- coding: utf-8 -*-
import sys
from pythymiodw import *
import time

r=ThymioReal()

mesure_capteur=[[0,4300],[0.5,4289],[1.0,4250],
        [1.5,4168],[2.0,3975],[2.5,3547],
        [3.0,3283],[3.5,3050],[4.0,2809],
        [4.5,2665],[5.0,2495],[5.5,2366],
        [6.0,2212],[6.5,2105],[7.0,1984],
        [7.5,1860],[8.0,1750],[8.5,1658],
        [9.0,1540],[9.5,1410],[10.0,1232],
        [10.5,0]]

pos_init=[0,0]
pos_actuel=[0,0]

#convertie mesure thymio en cm 
def convert_cm(dist_thy):
    i=0
    for i in range (0,22):
        if(mesure_capteur[i][1]>=dist_thy):
            res=mesure_capteur[i][0]
    return res

# Permet de mesurer la distance d'un obstacle
#Capteur accepter 0 à 5
def reperer_dist_obstacle(num_capteur):
    m=0
    for i in range(0,2): #premier boucle pour initialiser
        m=r.prox_horizontal[num_capteur]
        time.sleep(0.5)
    print(m)
    return convert_cm(m);

#Cette focntion retourne un obstacle, elle prend en argument 4 int,
def contourner_obstacle(cdx,cdy):
    return 1

############## Main ###############
res=reperer_dist_obstacle(2)
print(res)
r.quit()