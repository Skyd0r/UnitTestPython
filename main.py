import datetime

heure = datetime.datetime.now().hour


if (heure < 10):
    print("Bon matin !")
else:
    print("Bonjour")

mot = input("Entrer un mot: \n")

reverse = mot[::-1]

if(reverse == mot):
    print(mot + " , bien dit !")

else:
    print(reverse)


if (heure < 8):
    print("Bonne matinée !")
else:
    print("Bonne journée")
