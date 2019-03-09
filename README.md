# &#x1F53A; Thymio Mapping Project &#x1F53A;

### La demande :
Le client ne nous impose pas de contraintes particulières dans la mesure où il veut
juste un résultat: le Thymio doit pouvoir cartographier un lieu et visualiser le résultat
en temps réel. Le client souhaite également qu’il puisse interagir avec le robot.
L’équipe en charge du projet à l’aval du client pour rajouter des composants.

### Membres :
* Amin JELLAD
* Maher LAAROUSSI
* Hamid OUFKIR
* Lucky RAHERINIAINA
* Arnaud COSTA

### Matériels :
* Thymio
* Raspberry Pi Zero WH
* 2x Capteurs Ultrason
* Servo-motor
* Batterie


## GitLab :
#### 1ère étape : Configuration
Avant toute chose, commencez par configurer votre git en mettant votre nom d'utilisateur gitlab et votre adresse mail, la même que celle présente dans votre compte GitLab.  
`git config user.name "maherlaaroussi"`  
`git config user.email "maher@outlook.fr"`

#### 2e étape : Clonage
Ensuite, vous pourrez cloner ce dépot :  
`git clone https://gitlab.com/maherlaaroussi/thymio-mapping.git`

#### 3e étape : Commit & Push
Puis faites votre vie en modifiant ou en ajoutant des fichiers et ensuite à chaque fois que vous voulez commit & push ces changements/ajouts/modifications/suppressions, faites ces 3 commandes en vous plaçant à la racine de votre répertoire :  
`git add *`  
`git commit -m "Un message ici"`  
`git push`

#### Conseil : Même obligation
N'oubliez pas de faire un pull à chaque fois que vous commencez à travailler pour ainsi télécharger toutes les modifications faite au dépot.  
`git pull`  


## PyThymioDW

### Lien :
`https://www.mediafire.com/file/a5n1jkpxgy2xre8/pythymiodw-master.zip/file`

C'est pour avoir accès aux exemples et à la documentation de la bibliothèque.
### Installation
#### Avec le fichier
Il suffit de le télécharger et de le décompresser.  
Seul le fichier pythymiodw.py nous intéresse. Il suffira de le mettre à coté de vos autres fichiers qui importent cette bibliothèque pour pouvoir l'utiliser.

#### En ligne de commande
Par chance la bibliothèque est incorporée en python et on peut donc l'installer et comme je suis quelqu'un de bien je vais décrire les étapes.

Commençons par installer pip ou pip3 si ce n'est pas déjà fait :  
Pour python  : `sudo apt-get install python-pip`  
Pour python3 : `sudo apt-get install python3-pip`  

Sinon mettez le à jour.

Ensuite il faut installer la bibliotèque libdw.  
Pour python  : `sudo pip install libdw`  
Pour python3 :  `sudo pip3 install libdw`  

Puis il suffit d'installer notre bibliothèque adorée :   
Pour Python  : `sudo pip install pythymiodw`  
Pour Python3 : `sudo pip3 install pythymiodw`    

Dernière étape, il vous faut deux bibliotèques supplémentaires.  
Il faut la bibliotèque tk  
Pour Python   : `sudo apt-get install python-tk`  
Pour Python3  : `sudo apt-get install python3-tk`  

Et image tk  
Pour Python   : `sudo apt-get install python-imaging-tk`  
Pour Python3  : `sudo apt-get install python3-pil.imagetk`  

### Executer un fichier
Pour executer le fichier :  
Pour Python   : `sudo python votreFichier.py`  
Pour Pyhton3  : `sudo python3 votreFichier.py`

## Connexion SSH avec le Wifi CThymio :
#### 1ère étape : SSH
`ssh -2 -Y pi@10.3.141.1`

#### 2e étape : Thymio
`asebamedulla "ser:name=Thymio-II" &`
