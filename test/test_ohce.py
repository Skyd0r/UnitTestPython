import unittest
import random
import string
import os

from langue_anglaise import LangueAnglaise
from langue_francaise import LangueFrançaise
from utilities.verifiacteur_palindrome_builder import VérificateurPalindromeBuilder

from verificateur_palindrome import VérificateurPalindrome
from moment_de_la_journée import MomentDeLaJournée



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
        vérificateur = VérificateurPalindromeBuilder().ayant_pour_langue(langue).build()

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
        vérificateur = VérificateurPalindromeBuilder().ayant_pour_langue(langue).build()

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
        vérificateur = VérificateurPalindromeBuilder().ayant_pour_langue(langue).build()
        résultat = vérificateur.vérifier(chaine)

        #ALORS « Bonjour » est envoyé avant toute réponse
        attendu = LangueFrançaise.BONJOUR + os.linesep + chaine[::-1]
        self.assertIn(attendu, résultat)

    def test_Hello(self):
        # ETANT DONNE une chaine
        chaine = "voiture"

        # ET que l'utilisateur parle anglais
        langue = LangueAnglaise()
        moment = MomentDeLaJournée.Matin

        # QUAND on saisit une chaîne
        vérificateur = VérificateurPalindromeBuilder().ayant_pour_langue(langue).ayant_pour_moment_de_la_journée(moment).build()
        résultat = vérificateur.vérifier(chaine)

        # ALORS « Bonjour » est envoyé avant toute réponse
        attendu = LangueAnglaise.GOOD_MORNING + os.linesep + chaine[::-1]
        self.assertIn(attendu, résultat)

    def test_Au_Revoir(self):


        # ETANT DONNE une chaine
        chaine = "voiture"

        # ET que l'utilisateur parle français
        langue = LangueFrançaise()
        moment = MomentDeLaJournée.Nuit

        #QUAND on saisit une chaîne
        vérificateur = VérificateurPalindromeBuilder().ayant_pour_langue(langue).ayant_pour_moment_de_la_journée(moment).build()
        résultat = vérificateur.vérifier(chaine)

        # ALORS « Bonjour » est envoyé avant toute réponse
        attendu = chaine[::-1] + os.linesep + LangueFrançaise.BONNE_NUIT
        self.assertIn(attendu, résultat)

    def test_Goodnight(self):
        # ETANT DONNE une chaine
        chaine = "voiture"

        # ET que l'utilisateur parle français
        langue = LangueAnglaise()
        moment = MomentDeLaJournée.Nuit


        # QUAND on saisit une chaîne
        vérificateur = VérificateurPalindromeBuilder().ayant_pour_langue(langue).ayant_pour_moment_de_la_journée(moment).build()
        résultat = vérificateur.vérifier(chaine)

        # ALORS « Bonjour » est envoyé avant toute réponse
        attendu = chaine[::-1] + os.linesep + LangueAnglaise.GOOD_NIGHT
        self.assertIn(attendu, résultat)


    def test_bonjour_nuit(self):
        cas = [
            ["kayak", LangueAnglaise(), LangueAnglaise.GOOD_NIGHT],
            ["voiture", LangueAnglaise(), LangueAnglaise.GOOD_NIGHT],
            ["kayak", LangueFrançaise(), LangueFrançaise.BONSOIR],
            ["voiture", LangueFrançaise(), LangueFrançaise.BONSOIR],
        ]

        for test in cas:
            chaîne = test[0]
            langue = test[1]
            salutations = test[2]

            with self.subTest(f"{chaîne} - {langue}"):
                # ETANT DONNE une <chaîne>
                # ET que l'utilisateur parle <langue>
                # ET que le moment de la journée est la nuit
                moment = MomentDeLaJournée.Nuit

                # QUAND on vérifie si c'est un palindrome
                vérificateur = VérificateurPalindromeBuilder().ayant_pour_langue(langue).ayant_pour_moment_de_la_journée(moment).build()

                résultat = vérificateur.vérifier(chaîne)

                # ALORS la chaîne renvoyée est précédée des salutations de cette langue
                lignes = résultat.split(os.linesep)
                self.assertEqual(salutations, lignes[0])

    def test_saut_de_ligne_finale(self):

        # ETANT DONNE une chaine
        chaine = "voiture"

        # ET que l'utilisateur parle anglais
        langue = LangueAnglaise()

        # QUAND on saisit une chaîne
        vérificateur = VérificateurPalindromeBuilder().ayant_pour_langue(langue).build()
        résultat = vérificateur.vérifier(chaine)

        # ALORS il y a un saut de ligne final
        attendu = LangueAnglaise.HELLO + os.linesep + chaine[::-1] + os.linesep + LangueAnglaise.GOODBYE + os.linesep
        self.assertTrue(attendu.endswith(os.linesep), résultat)



if __name__ == '__main__':
    unittest.main()
