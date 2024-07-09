import os


class VérificateurPalindrome:

    def __init__(self, langue, moment):
        self.__moment = moment
        self.__langue = langue
        pass

    def vérifier(self, chaîne):
        reverse = chaîne[::-1]

        félicitations = self.__langue.féliciter()
        salutations = self.__langue.saluer(self.__moment)
        acquittance = self.__langue.acquitter(self.__moment)


        if (reverse == chaîne):
            #return salutations + os.linesep + chaîne[::-1] + os.linesep + félicitations + os.linesep + acquittance
            ReturnPalindrome = salutations + os.linesep + chaîne[::-1] + os.linesep + félicitations + os.linesep + acquittance
            if ReturnPalindrome.endswith(os.linesep):
                return ReturnPalindrome
            else:
                return ReturnPalindrome + os.linesep
        else:
            #return salutations + os.linesep + reverse + os.linesep + acquittance
            ReturnPasPalindrome = salutations + os.linesep + reverse + os.linesep + acquittance
            if ReturnPasPalindrome.endswith(os.linesep):
                return ReturnPasPalindrome
            else:
                return ReturnPasPalindrome + os.linesep

