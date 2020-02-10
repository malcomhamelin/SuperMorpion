class Joueur:

    def __init__(self, nom, signe):
        self.nom = nom
        self.signe = signe

    def __str__(self):
        return self.nom