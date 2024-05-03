import os


class VérificateurPalindrome:
    BONJOUR = "Bonjour"
    AU_REVOIR = "Au revoir !"

    def __init__(self, langue):
        self.__langue = langue
        pass

    def vérifier(self, chaîne):
        reverse = chaîne[::-1]
        félicitations = self.__langue.féliciter()
        if (reverse == chaîne):
            return self.BONJOUR + os.linesep + chaîne[::-1] + os.linesep + félicitations + os.linesep + self.AU_REVOIR
        else:
            return self.BONJOUR + os.linesep + reverse + os.linesep + self.AU_REVOIR
