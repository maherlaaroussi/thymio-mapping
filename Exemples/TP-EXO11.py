
# 
from robosim import *
from math import *

init()

horizon = 50
alpha = 0.1
beta = 0.01

# Fonction get prox
def get_prox():
    global horizon

    a = orientation()
    angles = [ a + x for x in [-40,20,0,20,40]]
    
    prox = telemetre_coords_list(*position(),angle_list=angles,show_rays=False)
    
    for i in range(len(prox)):
        if (prox[i] > 50):
            prox[i] = horizon
            
        
    return prox
    
# Conversion radians et degrees
def convdr(x,c):
    if (c == "r"):
        return radians(x)
        
    elif (c == "d"):
        return degrees(x)
        
# Pour langle de destination en fonction de la  pos de destination
def cap (x, y):
    
    x0,y0 = position()
    xn = x - x0
    yn = y - y0
    
    # On fais la conversion en degrees du resultat
    # X et Y sont inverses dans la fonction atan2
    vers = convdr(atan2(yn,xn), 'd')
     
    return vers

# Fonction pour se diriger vers une pos x y
def aller_a(x,y):
    angle = 0
    xto,yto = x, y
    cap2 = 0
    cp = 0
    pos = position()
    
    # Alpha quon appelle adouciceur
    global alpha
    
    for i in range(500):
        angle = alpha * cap (x,y) + (1 - alpha) * cap_evitement()
        
        # Des modif fait par le prof qui marchent a moitie
        if (pos == position() ):
            cp+=1
            if cp==5:
                angle=220
        else:
            cp=0
            
        pos = position()
        
        if angle > 0:
            tg(angle)
        else:
            td(-angle)
        av(5)
        
        # Pour checker le resultat
        print(cap_evitement())
        
# Pour eviter les obstacles en calculant un angle dechappement
def cap_evitement():
    total = 0
    global beta
    
    prox = get_prox()
    angles = [-40,-20,0,20,40]
    
    for i in range(len(angles)):
        total += prox[i] * (40 - 20 * i)
        
    
    total *= beta
    
    return total + orientation()
    
# On teste en allant au coin en bas a droite
aller_a(460,460)