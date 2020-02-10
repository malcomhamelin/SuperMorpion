from Model.Case import Case


def initCases():
    cases = []
    for ligne in range(3):
        cases.append([])
        for colonne in range(3):
            cases[ligne].append(Case(colonne, ligne))

    return cases


class Grille:

    def __init__(self, x, y):
        self.cases = initCases()
        self.x = x
        self.y = y
        self.gagnant = None

    def __str__(self):
        grille = ''
        for i in range(3):
            for j in range(3):
                grille = grille + self.cases[i][j].__str__() + ' '
            if i < 2:
                grille = grille + '\n'

        return grille

    def estValide(self, colonne, ligne):
        if colonne < 3 and ligne < 3:
            return True if self.cases[ligne][colonne].estVide() else False

        return False

    def estPleine(self):
        for i in range(3):
            for j in range(3):
                if self.cases[i][j] == Case(0, 0):
                    return False

        return True

    def placerSigne(self, colonne, ligne, signe):
        self.cases[ligne][colonne].signe = signe

    def victoire(self):
        return self.victoireLigne() or self.victoireColonne() or self.victoireDiagonale()

    def egalite(self):
        return True if self.victoire() is False and self.estPleine() else False

    def victoireLigne(self):
        for i in range(3):
            ligne = self.cases[i]
            if all(case == ligne[0] and case != Case(0, 0) for case in ligne):
                return True

        return False

    def victoireColonne(self):
        for i in range(3):
            colonne = [self.cases[0][i], self.cases[1][i], self.cases[2][i]]
            if all(case == colonne[0] and case != Case(0, 0) for case in colonne):
                return True

        return False

    def victoireDiagonale(self):
        diagonale1 = [self.cases[0][0], self.cases[1][1], self.cases[2][2]]
        diagonale2 = [self.cases[0][0], self.cases[1][1], self.cases[2][2]]

        if all(case == diagonale1[0] and case != Case(0, 0) for case in diagonale1):
            return True

        if all(case == diagonale2[0] and case != Case(0, 0) for case in diagonale2):
            return True

        return False
