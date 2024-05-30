import os


class VérificateurPalindrome:

    def __init__(self, langue):
        self.__langue = langue
        pass

    def vérifier(self, chaîne):
        reverse = chaîne[::-1]

        félicitations = self.__langue.féliciter()
        salutations = self.__langue.saluer()
        acquittance = self.__langue.acquitter()


        if (reverse == chaîne):
            return salutations + os.linesep + chaîne[::-1] + os.linesep + félicitations + os.linesep + acquittance
        else:
            return salutations + os.linesep + reverse + os.linesep + acquittance
