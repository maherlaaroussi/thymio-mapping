# -*- coding: utf-8 -*-
"""

@Auteur: Maher LAAROUSSI
TP Thymio


"""

import pythymio, time, math
    
# ---------------------------------------------------------------

# Fonction pour avancer de x centimetres
def avance(xTarget):
    
    with pythymio.thymio([], []) as Thym:
            
        x = 0.0 # Position
        t = time.time() # Time
        v = 0.0
        posTarget = (xTarget * 500) / 16
        
        # Faire pendant 4 secondes
        while time.time() - t < 4.0:
        
            # Marge derreur
            e =  posTarget - x
            
            
            # Vitesse a laquelle avancer
            u = max(-500, min(500, e/3))
            
            
            # MAJ de la vitesse des moteurs
            Thym.set('motor.left.target', [u])
            Thym.set('motor.right.target', [u])
            
            # Get de la vitesse actuelle des deux moteurs
            v = (Thym.get("motor.left.speed") + Thym.get("motor.right.speed")) / 2
            
            # MAJ de la position
            x += v
            
            # Sleep de 0.1 sec
            time.sleep(1)
            
        # On coupe les moteurs
        Thym.set('motor.left.target', [0])
        Thym.set('motor.right.target', [0])
        time.sleep(0.5)
        Thym.stop()
        
# ---------------------------------------------------------------
        
# Fonction pour tourner le robot
def tourne(a):
    
    with pythymio.thymio([], []) as Thym:
        
        x = 0
        t = time.time()
        
        
        s = (a * 2.0) / 360.0
    
        
        # Si langle est superieur a 0
        if a > 0:
            while time.time() - t < s:
                Thym.set('motor.left.target', [500])
                Thym.set('motor.right.target', [-500])
                time.sleep(0.1)
            
        else: # Sinon on tourne a gauche
            while time.time() - t < s:
                Thym.set('motor.left.target', [-500])
                Thym.set('motor.right.target', [500])
                time.sleep(0.1)
                    
        # On coupe les moteurs
        Thym.set('motor.left.target', [0])
        Thym.set('motor.right.target', [0])
        time.sleep(0.5)
        Thym.stop()
    
# ---------------------------------------------------------------

#Affiche les obstacles
def afficheObs():
    t = time.time() # Temps now
    
    with pythymio.thymio([], []) as Thym:
        while 1: # Refait endant 5 sec
            print(max(Thym.get("prox.horizontal"))) # Affiche les obstacles
            time.sleep(0.01) # 10 fois par seconde
        
# ---------------------------------------------------------------

# Fonction avance tout droit
def avancetoutdroit():
    with pythymio.thymio([], []) as Thym:
        while afficheObs() == 0 :
            print("AVANCE")
            avance(100)
        
# ---------------------------------------------------------------

avancetoutdroit()