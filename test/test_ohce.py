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

            # QUAND on vérifie si c'est un palindrome
            résultat = VérificateurPalindrome.vérifier(chaîne)

            # ALORS la chaîne est renvoyée en miroir
            attendu = chaîne[::-1]
            self.assertEqual(attendu, résultat)



if __name__ == '__main__':
    unittest.main()
