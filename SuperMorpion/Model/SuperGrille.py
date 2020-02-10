from Model.Grille import Grille


def initGrilles():
    grilles = []
    for ligne in range(3):
        grilles.append([])
        for colonne in range(3):
            grilles[ligne].append(Grille(colonne, ligne))

    return grilles


class SuperGrille:

    def __init__(self):
        self.grilles = initGrilles()
