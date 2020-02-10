class Case:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.signe = ''

    def __str__(self):
        return self.signe

    def __eq__(self, other):
        return True if self.signe == other.signe else False

    def estVide(self):
        return True if self.signe == '' else False
