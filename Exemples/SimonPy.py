# -*- coding: utf-8 -*-
"""
Maher LAAROUSSI
Groupe 5
11504011

"""

import pythymio as pt
import time
import random

# Etats
etat = {'ready' : 1, 'read' : 0, 'compare' : 0, 'won' : 0, 'lost' : 0}

# Nombre de combinaisaons de base a generer
nbrC = 3

# Le tableau jeu qui contient les combinaisons
jeu = []

# nbr de combinaison tape par lutilisateur
nbrUser = 0

boucle = 1;

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
    
while boucle:
                            
            # Pour generer les combinaisons et les jouer
    if etat['ready']:
        # On genere la serie
        jeu = hasardComb(nbrC)
        
        for x in range(len(jeu)):
            print("Jeu : %s\n" % jeu[x])
        
        jeuUser = []
        
       
            
        # Met read a 1
        etatUp('ready')
        
    # Pour save la combinaison de lutilisateur
    if etat['read']:
    
        jeuUser = []
        nbrUser = 0
        
            
            
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
    