import os
class VérificateurPalindrome:

    BIEN_DIT = "Bien dit !"
    BONJOUR = "Bonjour"
    AU_REVOIR = "Au revoir !"
    @classmethod
    def vérifier(cls, chaîne):
        reverse = chaîne[::-1]
        if (reverse == chaîne):
            return cls.BONJOUR + os.linesep + chaîne[::-1] + os.linesep + cls.BIEN_DIT
        else:
            return cls.BONJOUR + os.linesep + reverse