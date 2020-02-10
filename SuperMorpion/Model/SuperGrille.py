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

    def __str__(self):
        superGrille = ''
        for i in range(3):
            for j in range(3):
                superGrille = superGrille + self.grilles[i][j].__str__() + "|"

        return superGrille

    def estValide(self, colonne, ligne):
        if colonne < 3 and ligne < 3:
            return False if self.grilles[ligne][colonne].estPleine() else True

        return False

    def estPleine(self):
        for i in range(3):
            for j in range(3):
                if self.grilles[i][j].estPleine() is False:
                    return False

        return True

    def selectionnerGrille(self, colonne, ligne):
        return self.grilles[ligne][colonne]

    def victoire(self):
        return self.victoireLigne() or self.victoireColonne() or self.victoireDiagonale()

    def egalite(self):
        return True if self.victoire() is False and self.estPleine() else False

    def victoireLigne(self):
        for i in range(3):
            gagnantsLigne = [self.grilles[i][0].gagnant, self.grilles[i][1].gagnant, self.grilles[i][2].gagnant]
            if all(joueurGagnant is not None and gagnantsLigne[0] is not None and
                   joueurGagnant == gagnantsLigne[0] for joueurGagnant in gagnantsLigne):
                return True

        return False

    def victoireColonne(self):
        for i in range(3):
            gagnantsColonne = [self.grilles[0][i].gagnant, self.grilles[1][i].gagnant, self.grilles[2][i].gagnant]
            if all(joueurGagnant is not None and gagnantsColonne[0] is not None and
                   joueurGagnant == gagnantsColonne[0] for joueurGagnant in gagnantsColonne):
                return True

        return False

    def victoireDiagonale(self):
        gagnantsDiagonale1 = [self.grilles[0][0].gagnant, self.grilles[1][1].gagnant, self.grilles[2][2].gagnant]
        gagnantsDiagonale2 = [self.grilles[0][0].gagnant, self.grilles[1][1].gagnant, self.grilles[2][2].gagnant]

        if all(joueurGagnant is not None and gagnantsDiagonale1[0] is not None and
               joueurGagnant == gagnantsDiagonale1[0] for joueurGagnant in gagnantsDiagonale1):
            return True

        if all(joueurGagnant is not None and gagnantsDiagonale2[0] is not None and
               joueurGagnant == gagnantsDiagonale2[0] for joueurGagnant in gagnantsDiagonale2):
            return True

        return False
