# -*- coding: utf-8 -*-
"""
Maher LAAROUSSI
Groupe 5
11504011

"""

import pythymio as pt
import random
import time

# Etats
etat = {'ready' : 1, 'read' : 0, 'compare' : 0, 'won' : 0, 'lost' : 0}

# Nombre de combinaisaons de base a generer
nbrC = 3

# Le tableau jeu qui contient les combinaisons
jeu = []

# nbr de combinaison tape par lutilisateur
nbrUser = 0

# Genere x combinaisons
def hasardComb(x):
    
    lettres = ['U', 'D', 'L', 'R']
    lettresOut = []
    
    for i in range(x):
        lettresOut.append(lettres[random.randint(0,x-1)])
        
    return lettresOut
    
# Mettre un etat a 1 et tout les autres a 0
def etatUp(x):

    etat['ready'] == 0
    etat['compare'] == 0
    etat['read'] == 0
    etat['lost'] == 0
    etat['won'] == 0
    
    if x == 'ready':
        etat['ready'] == 1
    if x == 'read':
        etat['read'] == 1
    if x == 'compare':
        etat['compare'] == 1
    if x == 'won':
        etat['won'] == 1
    if x == 'lost':
        etat['lost'] == 1

# Le programme
with pt.thymio(["button.center", "button.right", "button.left", "button.forward", "button.backward"], pt.customEvents('circle')) as Thym:
    def progression (idnum, evt, data):
        
        global nbrC
        global nbrUser
        global jeu
        global jeuUser
                        
                # Pour generer les combinaisons et les jouer
        if etat['ready']:
            # On genere la serie
            jeu = hasardComb(nbrC)
            
            print("Jeu : %d\n" % jeu)
            
            jeuUser = []
            
            # On joue les combinaisons
            for i in jeu:
                
                if i == 'R':
                    Thym.send_event('custom.right')
                if i == 'L':
                    Thym.send_event('custom.left')
                if i == 'U':
                    Thym.send_event('custom.front')
                if i == 'B':
                    Thym.send_event('custom.back')
                    
                # Delai dattente de 1 seconde
                time.sleep(1)
                
            # Met read a 1
            etatUp('read')
            
        # Pour save la combinaison de lutilisateur
        if etat['read']:
        
            jeuUser = []
            nbrUser = 0
            
            # On attends les entrees
            while nbrUser < nbrC:
                
                if evt == "fwd.button.right":
                    jeuUser.append['R']
                    nbrUser += 1
                if evt == "fwd.button.left":
                    jeuUser.append['L']
                    nbrUser += 1
                if evt == "fwd.button.forward":
                    jeuUser.append['U']
                    nbrUser += 1
                if evt == "fwd.button.backward":
                    jeuUser.append['D']
                    nbrUser += 1

                print("\nJeu : %d\n" % jeuUser)                
                
                # On passe a la comparaison
                etatUp('compare')
                    
        # Compare ce que la personne a jouer avec les combinaisons
        if etat['compare']:
        
            # On considere le joueur deja comme gagnant
            etatUp('won')
            
            # Mais sil y a une seule mauvaise combinaison il perd
            for i in jeu:
                if jeuUser[i] != jeu[i]:
                    etatUp('lost')
                    
        # Sil a gagné, on augmente la difficulte
        if etat['won']:
            nbrC += 1
            etatUp('ready')
        
        if etat['lost']:
            # Si lutilisateur a perdu, il reessaye
            etatUp('read')
            

Thym.loop(progression)