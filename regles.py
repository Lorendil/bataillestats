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
        return ("Nom: {}, Rareté: {}, Attaque: {}, Defense: {}, Agilité: {}, Intelligence: {}, Vitesse: {}"
                .format(self.nom, self.rarete, self.attaque, self.defense, self.agilite, self.intelligence, self.vitesse))

    def __repr__(self):
        """On indique ce que l'on veut voir apparaître en cas de print avec conditions"""
        return ("Nom: {}, Rareté: {}, Attaque: {}, Defense: {}, Agilité: {}, Intelligence: {}, Vitesse: {}"
                .format(self.nom, self.rarete, self.attaque, self.defense, self.agilite, self.intelligence, self.vitesse))
    
    def __ge__(self, other):
        """On indique que deux cartes sont identiques si elles portent le même nom"""
        if self.nom == other.nom:
            return True
        else:
            return False

    def compare(self, other, statistique):
        """Compare deux cartes selon la statistique donnée, retourne la carte supérieure, en cas d'égalité retourne 'False'."""
        if statistique == "attaque":
            if self.attaque > other.attaque:
                return True
            elif self.attaque == other.attaque:
                return "Egal"
            else:
                return False

        if statistique == "defense":
            if self.defense > other.defense:
                return True
            elif self.defense == other.defense:
                return "Egal"
            else:
                return False

        if statistique == "agilite":
            if self.agilite > other.agilite:
                return True
            elif self.agilite == other.agilite:
                return "Egal"
            else:
                return False       

        if statistique == "intelligence":
            if self.intelligence > other.intelligence:
                return True
            elif self.intelligence == other.intelligence:
                return "Egal"
            else:
                return False 

        if statistique == "vitesse":
            if self.vitesse > other.vitesse:
                return True
            elif self.vitesse == other.vitesse:
                return "Egal"
            else:
                return False


class Jeudecartestats(object):
    """Classe permettant de jouer à différents modes de jeux à l'aide d'un paquet de carte"""
    def __init__(self):
        """On importe le fichier contenant l'ensemble des cartes"""
        paquet = importtsv()
        self.paquet = paquet

    def createdeck(self, jeu):
        """Fonction permettant de créer les decks selon le mode de jeu choisi"""
        if jeu == "courseauscore":
            deck = []
            while len(deck) < 10:
                deck.append(self.paquet[(random.randrange(1, len(self.paquet)))])
        return deck


    def melange(self):
        """Fonction permettant de mélanger un deck"""
        random.shuffle(self.paquet)
        return self.paquet


    def preparation(self, jeu):
        """Fonction permettant d'initialiser une bataille simple à partir de 2 joueurs"""
        if jeu == "courseauscore":
            listejoueurs = []
            repeat = True
            #On demande à l'utilisateur de rentrer le nom des joueurs qui souhaitent jouer
            while repeat:
                joueur = {}
                try :
                    newjoueur = str(input("Entrez le nom d'un nouveau joueur, laisser vide pour arrêter\n"))
                except:
                    print("Ce n'est pas valide")

                #On ajoute le nouveau joueur à la liste et son deck si l'utilisateur ne renvoie pas rien et on vérifie qu'il y a bien au moins 2 joueurs
                if newjoueur != "":
                    joueur["nomjoueur"] = newjoueur
                    joueur["cartes"] = self.createdeck(jeu)
                    listejoueurs.append(joueur)
                elif len(listejoueurs) >= 2:
                    repeat = False
                else:
                    print("Il faut au moins 2 joueurs\n")
        return listejoueurs

    def courseauscore(self, x):
        """Jeu où il faut remporter le plus de cartes en x tours"""
        listedesjoueurs = self.preparation("courseauscore")
        tour = 0
        score = 0
        scoremax = 10 * x * (len(listedesjoueurs)-1)

        #On initie la boucle qui ira jusqu'au nombre de tours indiqué par x
        while tour < x:
            verif = False
            

            #verif permet de vérifier que l'utilisateur a bien renseigné un choix possible, tant que la vérification n'est pas faite, on lui demande de faire un choix
            while verif == False:
                choixstats = str(input("\n{}, voici votre carte :\n {} \n Indiquez quelle statistique jouer ('attaque', 'defense', 'agilite', 'intelligence', 'vitesse')."
                                        .format(listedesjoueurs[0]["nomjoueur"], listedesjoueurs[0]["cartes"][tour])))
                
                #Si on ne reconnait pas la réponse, la vérification reste False, sinon elle passe en True 
                if choixstats != "attaque" and choixstats != "defense" and choixstats != "agilite" and choixstats != "intelligence" and choixstats != "vitesse":
                    print(choixstats)
                    print("\nNous n'avons pas compris votre réponse. \n")
                else:
                    verif = True

            #On va comparer la carte du joueur avec les cartes de tous les autres joueurs
            for n in range(len(listedesjoueurs)):
                print("\nCarte de {}: {}".format(listedesjoueurs[n]["nomjoueur"],listedesjoueurs[n]["cartes"][tour]))

                if n != 0:
                    # print(listedesjoueurs[0]["cartes"][tour], (listedesjoueurs[n]["cartes"][tour]), choixstats)
                    result = listedesjoueurs[0]["cartes"][tour].compare(listedesjoueurs[n]["cartes"][tour], choixstats)
                    print("Le resultat de la comparaison est: {}".format(result))
                    if result == True:
                        score += 10
                    elif result == "Egal":
                        score += 1
                    else:
                        continue
            

            tour += 1
            if x == tour:
                print("{}, vous avez un score de {} points sur {} points possibles, soit {}/100 du maximum".format(listedesjoueurs[0]["nomjoueur"], score, scoremax, score/scoremax*100))


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
partie.courseauscore(3)
