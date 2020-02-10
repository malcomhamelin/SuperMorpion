from Model.JeuMorpion import JeuMorpion


class JeuSuperMorpion:

    def __init__(self, superGrille):
        self.superGrille = superGrille

    def jouer(self, joueur, colonne, ligne):
        grilleCourante = self.superGrille.grilles[ligne][colonne]
        morpionCourant = JeuMorpion(grilleCourante)

        print('Grille : ')
        print(grilleCourante)

        colonne, ligne = morpionCourant.jouer(joueur)

        while self.superGrille.estValide(colonne, ligne) is False:
            colonne = int(input('Veuillez choisir une colonne (grille) : '))
            ligne = int(input('Veuillez choisir une ligne (grille) : '))

        return colonne, ligne