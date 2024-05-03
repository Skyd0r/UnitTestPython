import unittest

from verificateur_palindrome import VérificateurPalindrome

class PalindromeTest(unittest.TestCase):
    def test_miroir(self):
        # ETANT DONNE un non-palindrome
        cas = ["epsi", "romain"]

        for chaîne in cas:

            # QUAND on vérifie si c'est un palindrome
            résultat = VérificateurPalindrome.vérifier(chaîne)

            # ALORS la chaîne est renvoyée en miroir
            attendu = chaîne[::-1]
            self.assertEqual(attendu, résultat)



if __name__ == '__main__':
    unittest.main()
