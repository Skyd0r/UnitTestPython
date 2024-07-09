from moment_de_la_journée import MomentDeLaJournée
from verificateur_palindrome import VérificateurPalindrome
from langue_systeme import LangueSystème

from datetime import datetime
heure_actuelle = datetime.now().hour
if 6 <= heure_actuelle < 12:
    Time = 1
elif 12 <= heure_actuelle < 18:
    Time = 2
elif 18 <= heure_actuelle < 22:
    Time = 3
else:
    Time = 0



if __name__ == '__main__':
    langue = LangueSystème()
    moment = MomentDeLaJournée(Time)

    verificateur = VérificateurPalindrome(langue, moment)

    resultat = verificateur.vérifier("test")

    print(resultat)