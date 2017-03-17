#!/usr/bin/env python

"""

Le loup criait


Le loup criait sous les feuilles
En crachant les belles plumes
De son repas de volailles :
Comme lui je me consume.

Les salades, les fruits
N'attendent que la cueillette ;
Mais l'araignée de la haie
Ne mange que des violettes.

Que je dorme ! que je bouille
Aux autels de Salomon.
Le bouillon court sur la rouille,
Et se mêle au Cédron.

"""

def greetings():
    """salut les amis"""
    print("helloo resif people 3")

def repeat(x, callback):
    """call x times callback"""
    for _ in range(x):
        callback()

if __name__ == "__main__":
    # blabla
    repeat(3, greetings)
    
