class VérificateurPalindrome:
    @classmethod
    def vérifier(cls, chaîne):
        reverse = chaîne[::-1]
        if (reverse == chaîne):
            return chaîne[::-1] + "\nBien dit !"
        else:
            return reverse