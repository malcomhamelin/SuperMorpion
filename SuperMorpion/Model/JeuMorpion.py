from Model.SuperGrille import SuperGrille


class JeuMorpion:

    def __init__(self, grille):
        self.grille = grille

    def jouer(self, joueur):
        aJoue = False
        while aJoue is False:
            colonne = int(input(joueur.__str__() + ' colonne : '))
            ligne = int(input(joueur.__str__() + ' ligne : '))

            if self.grille.estValide(colonne, ligne):
                self.grille.placerSigne(colonne, ligne, joueur.signe)
                aJoue = True

        return colonne, ligne