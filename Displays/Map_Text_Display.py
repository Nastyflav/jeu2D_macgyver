import os

from Packages.Map import Map


class Map_Text_Display():
    def __init__(self):
        pass
    ##
    ## Display map stored in Map class
    ##
    def display_map(self, map):
        for line in map._paths:
            for character in line:
                print(character, end="")
        print()

    # POUR chaque numéro_de_ligne de 0 à 14 FAIRE:
    # POUR chaque numéro_de_colonne de 0 à 14 FAIRE:
    #     position <- Position(numéro_de_ligne, numéro_de_colonne)
    #     SI position est la position de MacGyver FAIRE:
    #         Afficher le caractère de MacGyver
    #     SINON SI position est la position du garde FAIRE:
    #         Afficher le caractère du garde
    #     SINON SI position est une position dans la liste des objets à ramasser:
    #         Afficher le caractère de l'objet
    #     SINON SI position est une position dans les chemins FAIRE:
    #         Afficher le caractère d'un chemin
    #     SINON:
    #         Afficher le caractère d'un mur