from Model.Grille import Grille
from Model.JeuMorpion import JeuMorpion
from Model.Joueur import Joueur

nomJ1 = input('Nom j1 : ')
nomJ2 = input('Nom j2 : ')
joueur1 = Joueur(nomJ1, 'X')
joueur2 = Joueur(nomJ2, 'O')
joueurCourant = True

partie = JeuMorpion(Grille(0, 0))

while partie.grille.victoire() is False and partie.grille.egalite() is False:
    print(partie.grille)

    if joueurCourant:
        partie.jouer(joueur1)
    else:
        partie.jouer(joueur2)

    joueurCourant = not joueurCourant

if partie.grille.egalite():
    print('egalite')
else:
    print('Bravo ', end='')
    print(joueur1 if not joueurCourant else joueur2)
