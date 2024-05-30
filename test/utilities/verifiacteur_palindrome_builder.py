from utilities.langue_de_base import langueDeBase
from verificateur_palindrome import VérificateurPalindrome


class VérificateurPalindromeBuilder:
    __langue = langueDeBase()
    __moment = None

    @classmethod
    def par_defaut(cls):
        return VérificateurPalindromeBuilder().build()

    def ayant_pour_langue(self, langue):
        self.__langue = langue
        return self

    def build(self) -> VérificateurPalindrome:
        return VérificateurPalindrome(self.__langue, self.__moment)

    def ayant_pour_moment_de_la_journée(self, moment):
        self.__moment = moment
        return self