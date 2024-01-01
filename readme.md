# Objectif
L'objectif est dans un premier temps d'analyser le mouvement d'un volant de badminton pour en déterminer les caractéristiques, puis de simuler des lancer, et enfin de définir les paramètres d'un lancé de type lob

# Analyse
L'objectif est dans un premier temps d'analyser le mouvement d'un volant de badminton pour en déterminer les caractéristiques.
C'est l'objet de **reverse.py** qui calcule le coéfficient de frottement fluide à partir d'essais où la vitesse initiale, l'angle initial, et la distance parcourue.
Les paramètres à entrer sont :
+ la hauteur du pas de tir
+ l'angle de tir (par rapport à l'horizontale, en degrés)
+ la vitesse initiale
+ la distance parcourue
+ la masse du volant
Le résultat est k, le coefficient de frottement fluide.

# Simulation
Ensuite il est possible de simuler un lancer avec **shot.py**
Les paramètres à entrer sont :
+ la hauteur du pas de tir
+ l'angle de tir (par rapport à l'horizontale, en degrés)
+ la vitesse initiale
+ le coefficient de frottement fluide
+ la masse du volant
Le résultat est le tracé de la trajectoire, les coordonées de l'apogée, et la distance parcourue.

# Résolution

