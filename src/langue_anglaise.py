from moment_de_la_journée import MomentDeLaJournée

class LangueAnglaise:
    GOOD_NIGHT = "Good night"
    WELL_DONE = "Well done!"
    GOOD_MORNING = "Good morning"
    GOOD_AFTERNOON = "Good afternoon"
    GOOD_EVENING = "Good evening"
    GOODBYE = "Goodbye"
    HAVE_A_GOOD_DAY = "Have a good day"
    HAVE_A_GOOD_AFTERNOON = "Have a good afternoon"
    HAVE_A_GOOD_EVENING = "Have a good evening"
    WELL_SAID = "Well said !"
    HELLO = "Hello"


    @classmethod
    def féliciter(cls):
        return cls.WELL_SAID

    @classmethod
    def saluer(cls, moment):
        if moment == MomentDeLaJournée.Nuit:
            return cls.GOOD_NIGHT
        elif moment == MomentDeLaJournée.Matin:
            return cls.GOOD_MORNING
        elif moment == MomentDeLaJournée.Soiree:
            return cls.GOOD_AFTERNOON
        else:
            return cls.HELLO

    @classmethod
    def acquitter(cls, moment):
        if moment == MomentDeLaJournée.Nuit:
            return cls.GOOD_NIGHT
        elif moment == MomentDeLaJournée.Matin:
            return cls.HAVE_A_GOOD_DAY
        elif moment == MomentDeLaJournée.ApresMidi:
            return cls.HAVE_A_GOOD_AFTERNOON
        elif moment == MomentDeLaJournée.Soiree:
            return cls.HAVE_A_GOOD_EVENING
        else:
            return cls.GOODBYE



    def __str__(self):
        return "Langue Anglaise"
