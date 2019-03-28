# -*- coding: utf-8 -*-
from package.movement import *
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
            #print(m,cm)
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

#Le but de cete methode est de faire un zigzag pour la detection d'obstacle afin de contourner celui-ci
#return
#test=0: test non reussi
#test=1: test reussi
#tracker: Tableau de suivre, deplacement du robot celon l'axe x ou y
def zigzag_d():
    cp0=0
    cp1=1
    cp2=2
    cp3=3
    cp4=4
    tracker = [[0 for i in range(2)] for j in range(3)]
    tracker[0][0]='x'
    tracker[1][0]='y'
    tracker[2][0]='x'
    etape=0
    reussi=1
    x=0
    y=0
    #Etape1: On se position
    #codition:le robot doit etre face a l'ostacle
    while(obstacle_existe(cp2)==1 and reussi==1):
        td(90)
        if(obstacle_existe(cp2)==0): #pas d'ostacle
            avancer(3)
            x=x+3
            tracker[0][1]=x
            tg(90)
            reussi=1
        else: #presence d'obstacle
            reculer(x)
            tg(90)
            reussi=0
            return [reussi,tracker]
    #Configuration
    td(90)
    avancer(12)
    x=x+12
    tg(90)
    avancer(22)
    y=y+22
    tg(90)
    distance_obstacle=reperer_dist_obstacle(2, 1) #positionnement par defaut
    dinst_3=distance_obstacle-3
    avancer(dinst_3)
    #Etape2
    while(obstacle_existe(cp2)==1 and reussi==1):
        td(90)
        if(obstacle_existe(cp2)==0): #pas d'ostacle
            avancer(3)
            y=y+3
            tracker[1][1]=y
            tg(90)
            reussi=1
        else:
            reculer(y)
            td(90)
            recule(tracker[0][1])
            tg(90)
            reussi=0
            return [reussi,tracker]
    #Configuration
    td(90)
    avancer(12)
    y=y+12
    tg(90)
    avancer(22)
    x=x+22
    tg(90)
    distance_obstacle=reperer_dist_obstacle(2, 1) #positionnement par defaut
    dinst_3=distance_obstacle-3
    avancer(dinst_3)
    #Etape3
    td(90)
    avancer(tracker[0][1])
    td(90)
    x=x+tracker[0][1]
    tracker[2][1]=x
    reussi=1
    return [reussi,tracker]

def zigzag_g():
    cp0=0
    cp1=1
    cp2=2
    cp3=3
    cp4=4
    tracker = [[0 for i in range(2)] for j in range(3)]
    tracker[0][0]='x'
    tracker[1][0]='y'
    tracker[2][0]='x'
    etape=0
    reussi=1
    x=0
    y=0
    #le robot doit etre face a l'ostacle droite
    while(obstacle_existe(cp2)==1 and reussi==1):
        tg(90)
        if(obstacle_existe(cp2)==0):
            avancer(3)
            x=x+3
            tracker[0][1]=x
            td(90)
            reussi=1
        else:
            reculer(x)
            td(90)
            reussi=0
            return [reussi, tracker]
    #Configuration
    tg(90)
    avancer(12)
    x=x+12
    td(90)
    avancer(22)
    y=y+22
    td(90)
    distance_obstacle=reperer_dist_obstacle(2, 1) #positionnement par defaut
    dinst_3=distance_obstacle-3
    avancer(dinst_3)
    #Etape2
    while(obstacle_existe(cp2)==1 and reussi==1):
        tg(90)
        if(obstacle_existe(cp2)==0): #pas d'ostacle
            avancer(3)
            y=y+3
            tracker[1][1]=y
            td(90)
            reussi=1
        else:
            reculer(y)
            tg(90)
            reculer(x)
            td(90)
            reussi=0
            return [reussi,tracker]
    #Configuration
    tg(90)
    avancer(12)
    y=y+12
    td(90)
    avancer(22)
    x=x+22
    td(90)
    distance_obstacle=reperer_dist_obstacle(2, 1) #positionnement par defaut
    dinst_3=distance_obstacle-3
    avancer(dinst_3)
    #Etape3
    tg(90)
    avancer(tracker[0][1])
    tg(90)
    x=x+tracker[0][1]
    tracker[2][1]=x
    reussi=1
    return [reussi,tracker]


#Cette methode permet dans un premeir temps de detecter un obstacle, puis de l'evite et le contourner_obstacle
#par la droite si possible sinon par la gauche.
#assurer que le capteur le plus a droite et a gauche n'a aps dobstale trop prche pour contourne
def contourner_obstacle():
    parcour_droite=1
    parcour_gauche=0
    test=0
    x=0
    y=0
    while(obstacle_existe(2)==0):
        avancer(3)
        y=y+3
    distance_obstacle=reperer_dist_obstacle(2, 1)
    dinst_3=distance_obstacle-3
    avancer(dinst_3)#Avancer jusqu'a 3cm de l'ostacle
    y=y+dinst_3
    if(parcour_droite==1 and parcour_gauche==0):
        test=zigzag_d()
        if(test[0]==1):
            print("Parcour possible a droite")
            x=x+test[1][0][1]+test[1][2][1]
            y=y+test[1][1][1]
            return 1
        else:
            parcour_droite=0
            parcour_gauche=1
    elif(parcour_droite==0 and parcour_gauche==1):
        test=zigzag_d()
            if(test[0]==1):
                print("Parcour possible a gauche")
                x=x+test[1][0][1]+test[1][2][1]
                y=y+test[1][1][1]
                return 1
            else:
                parcour_droite=0
                parcour_gauche=0
    else:
        print("Echec du parcour droite et gauche")
        return 0

################ MAIN CONTOURNER ################
#print(zigzag_d())
print(zigzag_g())
quitter()
