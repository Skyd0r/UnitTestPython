import unittest
import random
import string
import os

from langue_anglaise import LangueAnglaise
from langue_francaise import LangueFrançaise
from utilities.verifiacteur_palindrome_builder import VérificateurPalindromeBuilder

from verificateur_palindrome import VérificateurPalindrome


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return(result_str)
class PalindromeTest(unittest.TestCase):

    def test_miroir(self):

        # ETANT DONNE un non-palindrome
        cas = ["epsi", "romain", get_random_string(10), get_random_string(100)]

        for chaîne in cas:
            with self.subTest(chaîne):
                # QUAND on vérifie si c'est un palindrome
                vérificateur = VérificateurPalindromeBuilder.par_defaut()
                résultat = vérificateur.vérifier(chaîne)

                # ALORS la chaîne est renvoyée en miroir
                attendu = chaîne[::-1]
                self.assertIn(attendu, résultat)

    def test_BienDit(self):
        # ETANT DONNE un palindrome
        palindrome = "kayak"

        # ET que l'utilisateur parle français
        langue = LangueFrançaise()
        vérificateur = VérificateurPalindrome(langue)

        # QUAND on saisit un palindrome
        résultat = vérificateur.vérifier(palindrome)


        # ALORS celui - ci est renvoyé ET « Bien dit » est envoyé ensuite
        attendu = palindrome + os.linesep + LangueFrançaise.BIEN_DIT
        self.assertIn(attendu, résultat)

    def test_WellSaid(self):
        # ETANT DONNE un palindrome
        palindrome = "kayak"

        # ET que l'utilisateur parle anglais
        langue = LangueAnglaise()
        vérificateur = VérificateurPalindrome(langue)

        # QUAND on saisit un palindrome
        résultat = vérificateur.vérifier(palindrome)

        # ALORS celui - ci est renvoyé ET « Bien dit » est envoyé ensuite
        attendu = palindrome + os.linesep + LangueAnglaise.WELL_SAID
        self.assertIn(attendu, résultat)

    def test_Bonjour(self):

        # ETANT DONNE une chaine
        chaine = "voiture"

        # ET que l'utilisateur parle français
        langue = LangueFrançaise()

        #QUAND on saisit une chaîne
        vérificateur = VérificateurPalindrome(langue)
        résultat = vérificateur.vérifier(chaine)

        #ALORS « Bonjour » est envoyé avant toute réponse
        attendu = LangueFrançaise.BONJOUR + os.linesep + chaine[::-1]
        self.assertIn(attendu, résultat)

    def test_Hello(self):
        # ETANT DONNE une chaine
        chaine = "voiture"

        # ET que l'utilisateur parle anglais
        langue = LangueAnglaise()

        # QUAND on saisit une chaîne
        vérificateur = VérificateurPalindrome(langue)
        résultat = vérificateur.vérifier(chaine)

        # ALORS « Bonjour » est envoyé avant toute réponse
        attendu = LangueAnglaise.HELLO + os.linesep + chaine[::-1]
        self.assertIn(attendu, résultat)

    def test_Au_Revoir(self):


        # ETANT DONNE une chaine
        chaine = "voiture"

        # ET que l'utilisateur parle français
        langue = LangueFrançaise()

        #QUAND on saisit une chaîne
        vérificateur = VérificateurPalindrome(langue)
        résultat = vérificateur.vérifier(chaine)

        # ALORS « Bonjour » est envoyé avant toute réponse
        attendu = chaine[::-1] + os.linesep + LangueFrançaise.AU_REVOIR
        self.assertIn(attendu, résultat)

    def test_Goodbye(self):
        # ETANT DONNE une chaine
        chaine = "voiture"

        # ET que l'utilisateur parle français
        langue = LangueAnglaise()

        # QUAND on saisit une chaîne
        vérificateur = VérificateurPalindrome(langue)
        résultat = vérificateur.vérifier(chaine)

        # ALORS « Bonjour » est envoyé avant toute réponse
        attendu = chaine[::-1] + os.linesep + LangueAnglaise.GOODBYE
        self.assertIn(attendu, résultat)

if __name__ == '__main__':
    unittest.main()
