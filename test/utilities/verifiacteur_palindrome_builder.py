from utilities.langue_de_base import langueDeBase
from verificateur_palindrome import VérificateurPalindrome


class VérificateurPalindromeBuilder:
    def build(self) -> VérificateurPalindrome:
        return VérificateurPalindrome(langueDeBase())

    @classmethod
    def par_defaut(cls):
        return VérificateurPalindromeBuilder().build()

    def ayant_pour_langue(self, langue):
        self.__langue = langue
        return self