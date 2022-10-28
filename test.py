import random
joueurs = ["Quentin", "Nicolas", "Romain", "Olivier", "Pascale"]
paquet = [5,8,6,3,2,1,4,5,6,9,8,7,6,3,25]

def bataillesimple(listejoueurs):
    """Fonction permettant d'initialiser une bataille simple de 2 à n joueurs."""
    joueur = {}
    for n in listejoueurs:
        random.shuffle(paquet)
        joueur[n] = paquet
    return joueur

print(bataillesimple(joueurs))