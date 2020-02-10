from Model.JeuSuperMorpion import JeuSuperMorpion
from Model.Joueur import Joueur
from Model.SuperGrille import SuperGrille

nomJ1 = input('Nom j1 : ')
nomJ2 = input('Nom j2 : ')
joueur1 = Joueur(nomJ1, 'X')
joueur2 = Joueur(nomJ2, 'O')
joueurCourant = True

partie = JeuSuperMorpion(SuperGrille())

print(partie.superGrille)
colonneGrilleCourante = int(input('colonne grille de début : '))
ligneGrilleCourante = int(input('ligne grille de début : '))

while partie.superGrille.victoire() is False and partie.superGrille.egalite() is False:
    print('Super grille : ')
    print(partie.superGrille)

    if joueurCourant:
        colonneGrilleCourante, ligneGrilleCourante = partie.jouer(joueur1, colonneGrilleCourante, ligneGrilleCourante)
    else:
        colonneGrilleCourante, ligneGrilleCourante = partie.jouer(joueur2, colonneGrilleCourante, ligneGrilleCourante)

    joueurCourant = not joueurCourant

if partie.grille.egalite():
    print('egalite')
else:
    print('Bravo ', end='')
    print(joueur1 if not joueurCourant else joueur2)