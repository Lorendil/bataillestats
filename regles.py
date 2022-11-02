#Dans ce script j'initialise une classe pour créer des cartes et leur règles, c'est vraiment inutile, je pourrais tout gérer avec juste un dictionnaire et une liste, je cherche à manipuler au mieux les classes

import random
import csv

class Cartestats(object):
    """Classe permettant de créer des cartes personnalisées"""
    def __init__(self, nom, rarete, attaque, defense, agilite, intelligence, vitesse):
        self.nom = nom
        self.rarete = rarete
        self.attaque = attaque
        self.defense = defense
        self.agilite = agilite
        self.intelligence = intelligence
        self.vitesse = vitesse

    def __str__(self):
        """On indique ce que l'on veut voir apparaître en cas de print"""
        return ("Nom: {}, Rareté: {}, Attaque: {}, Defense: {}, Agilité: {}, Intelligence: {}, Vitesse: {}".format(self.nom, self.rarete, self.attaque, self.defense, self.agilite, self.intelligence, self.vitesse))

    def __repr__(self):
        """On indique ce que l'on veut voir apparaître en cas de print avec conditions"""
        return ("Nom: {}, Rareté: {}, Attaque: {}, Defense: {}, Agilité: {}, Intelligence: {}, Vitesse: {}".format(self.nom, self.rarete, self.attaque, self.defense, self.agilite, self.intelligence, self.vitesse))

    def compare(self, other, statistique):
        """Compare deux cartes selon la statistique donnée, retourne la carte supérieure, en cas d'égalité retourne 'False'."""
        if statistique == "attaque":
            if self.attaque > other.attaque:
                return self
            elif self.attaque == other.attaque:
                return False
            else:
                return other

        if statistique == "defense":
            if self.defense > other.defense:
                return self
            elif self.defense == other.defense:
                return False
            else:
                return other

        if statistique == "agilite":
            if self.agilite > other.agilite:
                return self
            elif self.agilite == other.agilite:
                return False
            else:
                return other       

        if statistique == "intelligence":
            if self.intelligence > other.intelligence:
                return self
            elif self.intelligence == other.intelligence:
                return False
            else:
                return other 

        if statistique == "vitesse":
            if self.vitesse > other.vitesse:
                return self
            elif self.vitesse == other.vitesse:
                return False
            else:
                return other


class Jeudecartestats(object):
    """Classe permettant de jouer à différents modes de jeux à l'aide d'un paquet de carte"""
    def __init__(self):
        """On importe le fichier contenant l'ensemble des cartes"""
        paquet = importtsv()
        self.paquet = paquet

    def melange(self):
        """Fonction permettant de mélanger un deck"""
        random.shuffle(self.paquet)
        return self.paquet


    def bataillesimple(self):
        """Fonction permettant d'initialiser une bataille simple à partir de 2 joueurs"""
        joueur = {}
        listejoueurs = []
        repeat = True
        j = 0
        #On deamnde à l'utilisateur de rentrer le nom des joueurs qui souhaitent jouer
        while repeat:
            try :
                newjoueur = str(input("Entrez le nom d'un nouveau joueur, laisser vide pour arrêter\n"))
            except:
                print("Ce n'est pas valide")

            #On ajoute le nouveau joueur à la liste si l'utilisateur ne renvoie pas rien et on vérifie qu'il y a bien au moins 2 joueurs
            if newjoueur != "":
                listejoueurs.append(newjoueur)
            elif len(listejoueurs) >= 2:
                repeat = False
            else:
                print("Il faut au moins 2 joueurs\n")

        for n in listejoueurs:
            joueur[n] = self.melange()
            print(joueur[n][0])
        return joueur


def importtsv():
    """Fonction permettant d'extraire les données des jeux vers des fichiers. Retourne un dictionnaire avec la liste de carte pour chaque rareté."""
    #On declare les différents types de cartes pouvant être appelées
    unique = []
    rare = []
    peucommun = []
    commun = []
    paquetdecarte = {}
    listepaquetdecarte = []
    with open("listedescartes.csv", newline='', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter = '\t', lineterminator="\n")
        for row in reader:
            if row[1] == "Commun" :
                newcarte = Cartestats(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                commun.append(newcarte)
                listepaquetdecarte.append(newcarte)
            elif row[1] == "Peu Commun":
                newcarte = Cartestats(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                peucommun.append(newcarte)
                listepaquetdecarte.append(newcarte)
            elif row[1] == "Rare":
                newcarte = Cartestats(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                rare.append(newcarte)
                listepaquetdecarte.append(newcarte)
            elif row[1] == "Unique":
                newcarte = Cartestats(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                unique.append(newcarte)
                listepaquetdecarte.append(newcarte)
            else:
                continue
    
    #On ajoute les listes de cartes dans leur dico respectifs et on retourne 
    paquetdecarte["Commun"], paquetdecarte["Peu Commun"], paquetdecarte["Rare"], paquetdecarte["Unique"] = commun, peucommun, rare, unique
    return listepaquetdecarte

# if __name__ == __main__:
partie = Jeudecartestats()
partie.bataillesimple()
