from moment_de_la_journée import MomentDeLaJournée

class LangueFrançaise:
    BONSOIR = "Bonsoir"
    BIEN_DIT = "Bien dit !"
    BONJOUR = "Bonjour"
    BON_MATIN = "Bon Matin"
    BONNE_SOIREE = "Bonne soirée"
    AU_REVOIR = "Au revoir"
    BONNE_NUIT = "Bonne nuit"
    BONNE_JOURNEE = "Bonne journée"
    BONNE_FIN_DE_JOURNEE = "Bonne fin de journée"

    @classmethod
    def féliciter(cls):
        return cls.BIEN_DIT

    @classmethod
    def saluer(cls, moment):
        if moment == MomentDeLaJournée.Nuit:
            return cls.BONSOIR
        elif moment == MomentDeLaJournée.Matin:
            return cls.BON_MATIN
        elif moment == MomentDeLaJournée.Soiree:
            return cls.BONNE_SOIREE
        else:
            return cls.BONJOUR

    @classmethod
    def acquitter(cls, moment):
        if moment == MomentDeLaJournée.Nuit:
            return cls.BONNE_NUIT
        elif moment == MomentDeLaJournée.Matin:
            return cls.BONNE_JOURNEE
        elif moment == MomentDeLaJournée.ApresMidi:
            return cls.BONNE_FIN_DE_JOURNEE
        elif moment == MomentDeLaJournée.Soiree:
            return cls.BONNE_SOIREE
        else:
            return cls.AU_REVOIR

    def __str__(self):
        return "Langue Française"
