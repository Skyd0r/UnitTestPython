import unittest
import random
import string

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
                résultat = VérificateurPalindrome.vérifier(chaîne)

                # ALORS la chaîne est renvoyée en miroir
                attendu = chaîne[::-1]
                self.assertEqual(attendu, résultat)

    def test_BienDit(self):
        # ETANT DONNE un palindrome
        palindrome = "kayak"

        # QUAND on saisit un palindrome
        résultat = VérificateurPalindrome.vérifier(palindrome)

        # ALORS celui - ci est renvoyé ET « Bien dit » est envoyé ensuite
        attendu = palindrome + "\nBien dit !"
        self.assertEqual(attendu, résultat)

if __name__ == '__main__':
    unittest.main()
