class VérificateurPalindrome:

    @classmethod
    def vérifier(cls, chaîne):
        reverse = chaîne[::-1]
        if (reverse == chaîne):
            return "Bonjour\n" + chaîne[::-1] + "\nBien dit !"
        else:
            return "Bonjour\n" +reverse