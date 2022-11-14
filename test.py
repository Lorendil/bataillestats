from enum import Enum
import random
import csv

class Comparaison(Enum):
    """Permet de traiter les égalités, supérieurs et inférieurs dans les comparaisons"""
    INFERIEUR = 0
    EGAL = 1
    SUPERIEUR = 2

class Cartestats(object):
    """Classe permettant de créer des cartes personnalisées"""
    #On définit les statistiques, elles peuvent être aisément modifiées en cas de choix de jeu différent, exemple sur des personnalité, taille, âge, poids, etc... 
    # il faudrait modifier le programme en conséquence pour qu'il soit réutilisable (WIP)
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
        #Dans certains cas de figures, la fonction permettra de vérifier par exemple is une carte est déjà présente dans le deck ou un autre deck
        if self.nom == other.nom:
            return True
        else:
            return False

    def compare(self, other, statistique):
        """Compare deux cartes selon la statistique donnée, retourne une valeur définie dans Comparaison(Enum) selon le résultat supérieur, inférieur ou égal"""
        #On ecrit la règle pour chacune des possibilités, supérieur, égal et sinon, inférieur, le retour est géré par Comparaison, un énumerateur
        if statistique == "attaque":
            if self.attaque > other.attaque:
                return Comparaison.SUPERIEUR
            elif self.attaque == other.attaque:
                return Comparaison.EGAL
            else:
                return Comparaison.INFERIEUR

        if statistique == "defense":
            if self.defense > other.defense:
                return Comparaison.SUPERIEUR
            elif self.defense == other.defense:
                return Comparaison.EGAL
            else:
                return Comparaison.INFERIEUR

        if statistique == "agilite":
            if self.agilite > other.agilite:
                return Comparaison.SUPERIEUR
            elif self.agilite == other.agilite:
                return Comparaison.EGAL
            else:
                return Comparaison.INFERIEUR       

        if statistique == "intelligence":
            if self.intelligence > other.intelligence:
                return Comparaison.SUPERIEUR
            elif self.intelligence == other.intelligence:
                return Comparaison.EGAL
            else:
                return Comparaison.INFERIEUR 

        if statistique == "vitesse":
            if self.vitesse > other.vitesse:
                return Comparaison.SUPERIEUR
            elif self.vitesse == other.vitesse:
                return Comparaison.EGAL
            else:
                return Comparaison.INFERIEUR

class Joueur(object):
    """Classe permettant de définir un joueur et son jeu"""
    def __init__(self, nom = "", deck = []):
        """Permet d'initialiser la classe joueur à l'aide d'un nom et d'un deck de cartes"""
        self.deck = deck
        self.nom = nom
        self.score = 0

    def drawcard(self, cardnum = 0):
        """Permet de tirer une carte selon son numéro dans la liste, sans modification, il s'agira de la première"""
        drawncard = self.deck[cardnum]
        #On veut retirer la carte du paquet quand elle est jouée, on la remettra dans le paquet si le round est gagné
        self.removecard(drawncard)
        return drawncard
    
    def addcarte(self, carte):
        """Permet d'ajouter une carte au deck"""
        self.deck.append(carte)

    def removecard(self, carte):
        """Permet de retirer une carte au deck, attention, retire une fois la carte"""
        self.deck.remove(carte)

    def melange(self):
        """Permet de mélanger le deck du joueur"""
        random.shuffle(self.deck)

class Jeudecartestats(object):
    """Classe permettant de jouer à différents modes de jeux à l'aide d'un paquet de carte"""
    def __init__(self):
        """On importe le fichier contenant l'ensemble des cartes"""
        paquet = importtsv()
        self.paquet = paquet

    def createdeck(self, jeu, cartemain = 10):
        """Fonction permettant de créer les decks selon le mode de jeu choisi"""
        if jeu == "courseauscore":
            deck = []
            while len(deck) < cartemain:
                deck.append(self.paquet[(random.randrange(1, len(self.paquet)))])

        elif jeu == "jeuclassique":
            deck = []
            while len(deck) < cartemain:
                deck.append(self.paquet[(random.randrange(1, len(self.paquet)))])

        return deck

    def melange(self):
        """Fonction permettant de mélanger un deck"""
        #Fonction qui sera probablement amené à disparaitre avec l'apparition de la classe Joueur, avant de transférer les méthodes, on va rédiger le cahier des charges
        random.shuffle(self.paquet)
        return self.paquet

    def preparation(self, jeu, cartemain = 0):
        """Fonction permettant d'initialiser une bataille simple à partir de 2 joueurs"""
        if jeu == "courseauscore":
            listejoueurs = []
            repeat = True
            #On demande à l'utilisateur de rentrer le nom des joueurs qui souhaitent jouer
            while repeat:
                joueur = Joueur()
                try :
                    newjoueur = str(input("Entrez le nom d'un nouveau joueur, laisser vide pour arrêter\n"))
                except:
                    print("Ce n'est pas valide")

                #On ajoute le nouveau joueur à la liste et son deck si l'utilisateur ne renvoie pas rien et on vérifie qu'il y a bien au moins 2 joueurs
                if newjoueur != "":
                    joueur = Joueur(nom = newjoueur, deck = self.createdeck(jeu))
                    listejoueurs.append(joueur)
                elif len(listejoueurs) >= 2:
                    repeat = False
                else:
                    print("Il faut au moins 2 joueurs\n")
        elif jeu == "jeuclassique":
            listejoueurs = []
            repeat = True
            #On demande à l'utilisateur de rentrer le nom des joueurs qui souhaitent jouer
            while repeat:
                joueur = Joueur()
                try :
                    newjoueur = str(input("Entrez le nom d'un nouveau joueur, laisser vide pour arrêter\n"))
                except:
                    print("Ce n'est pas valide")

                #On ajoute le nouveau joueur à la liste et son deck si l'utilisateur ne renvoie pas rien et on vérifie qu'il y a bien au moins 2 joueurs
                if newjoueur != "":
                    joueur = Joueur(nom = newjoueur, deck = self.createdeck(jeu, cartemain))
                    listejoueurs.append(joueur)

                elif len(listejoueurs) >= 2:
                    repeat = False

                else:
                    print("Il faut au moins 2 joueurs\n")

        return listejoueurs

    def jeuclassique(self, x):
        """Jeu où il faut remporter toutes les cartes des adversaires, x le nombre de cartes dans la main d'un joueur"""
        listedesjoueurs = self.preparation("jeuclassique", cartemain = x)
        tour = 0
        scoremax = 10 * x
        equalistcards = []
        jmax = 0

        #On initie la boucle qui ira jusqu'au nombre de tours indiqué par x
        while len(listedesjoueurs) > 1:
            verif = False
            listecartes = []
            scoretour = []
            
            equalstatus = False
            equalistcardsstatus = False
            equallist = []

            

            #On crée la liste des cartes tirées pour le tour la carte indice [0] correspond au joueur [0] de la liste
            for n in range(len(listedesjoueurs)):
                listecartes.append(listedesjoueurs[n].drawcard())
                scoretour.append(0)

            #verif permet de vérifier que l'utilisateur a bien renseigné un choix possible, tant que la vérification n'est pas faite, on lui demande de faire un choix
            while verif == False:
                choixstats = str(input("\n{}, voici votre carte :\n {} \n Indiquez quelle statistique jouer ('attaque', 'defense', 'agilite', 'intelligence', 'vitesse')."
                                        .format(listedesjoueurs[jmax].nom, listecartes[jmax])))
                
                #Si on ne reconnait pas la réponse, la vérification reste False, sinon elle passe en True 
                if choixstats != "attaque" and choixstats != "defense" and choixstats != "agilite" and choixstats != "intelligence" and choixstats != "vitesse":
                    print(choixstats)
                    print("\nNous n'avons pas compris votre réponse. \n")
                else:
                    print("\n")
                    verif = True

            #On va comparer la carte du joueur avec les cartes de tous les autres joueurs
            for n in range(len(listedesjoueurs)):
                

                if n != jmax:
                    # print(listedesjoueurs[0]["cartes"][tour], (listedesjoueurs[n]["cartes"][tour]), choixstats)
                    result = listecartes[jmax].compare(listecartes[n], choixstats)
                    print("Carte de {}: {}".format(listedesjoueurs[jmax].nom, listecartes[jmax]))
                    print("Carte de {}: {}".format(listedesjoueurs[n].nom, listecartes[n]))
                    print("Le resultat de la comparaison est: {}".format(result.name))

                    #Si la carte est supérieure, on attribue au score du joueur jmax 10 uniquement s'il n'est pas en status égalité car il doit garder ses 5 points et au perdant 0
                    if result == Comparaison.SUPERIEUR:
                        if equalstatus != True:
                            scoretour[jmax] = 10
                        scoretour[n] = 0

                    #Si la carte est égale à celle d'un joueur, on attribue aux deux joueurs le score de 5 et on signale une égalité, les joueurs en égalités sont répertoriés dans la liste
                    #equallist, le status est un booléen passant en True
                    elif result == Comparaison.EGAL:
                        scoretour[jmax] = 5
                        scoretour[n] = 5
                        equalstatus = True
                        equallist.append(jmax)
                        equallist.append(n)

                    #Si la carte est inférieure à celle d'un joueur, on attribue au joueur testé 10, le joueur testé devient jmax, le joueur jmax passe à 0
                    #S'il y a un statut equal, on va attribuer le score de 0 à tous les joueurs et effacer les éléments référencés dans la liste equallist et on retire le statut equal
                    else:
                        scoretour[jmax] = 0
                        scoretour[n] = 10
                        jmax = n

                        if equalstatus == True:
                            for y in equallist:
                                scoretour[y] = 0
                            equallist.clear()

                        equalstatus = False
                        


            if equalstatus == False:
                if equalistcardsstatus:
                    for card in equalistcards:
                        listecartes.append(card)
                    equalistcardsstatus = False

                for card in listecartes:
                    listedesjoueurs[jmax].deck.append(card)

                for joueur in range(len(listedesjoueurs)):
                    if not listedesjoueurs[joueur].deck:
                        listedesjoueurs.remove(listedesjoueurs[joueur])
                
                equalistcards.clear()
            
            else:
                for card in listecartes:
                    equalistcards.append(card)
                    equalistcardsstatus = True

            tour += 1
            if x == tour:
                for x in range(len(listedesjoueurs)):

                    print("{}, vous avez un score de {} points sur {} points possibles, soit {}/100 du maximum".format(
                        listedesjoueurs[x].nom, listedesjoueurs[x].score, scoremax, listedesjoueurs[x].score/scoremax*100
                        ))


def importtsv():
    """Fonction permettant d'extraire les données des jeux vers des fichiers. Retourne un dictionnaire avec la liste de carte pour chaque rareté."""
    #On declare les différents types de cartes pouvant être appelées pour qu'elles soient triées d'une manière à être facilement tirées lors de la création d'un deck en rareté aléatoire
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
                newcarte = Cartestats(row[0], row[1], int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]))
                commun.append(newcarte)
                listepaquetdecarte.append(newcarte)
            elif row[1] == "Peu Commun":
                newcarte = Cartestats(row[0], row[1], int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]))
                peucommun.append(newcarte)
                listepaquetdecarte.append(newcarte)
            elif row[1] == "Rare":
                newcarte = Cartestats(row[0], row[1], int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]))
                rare.append(newcarte)
                listepaquetdecarte.append(newcarte)
            elif row[1] == "Unique":
                newcarte = Cartestats(row[0], row[1], int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]))
                unique.append(newcarte)
                listepaquetdecarte.append(newcarte)
            else:
                continue
    
    #On ajoute les listes de cartes dans leur dico respectifs et on le retourne 
    paquetdecarte["Commun"], paquetdecarte["Peu Commun"], paquetdecarte["Rare"], paquetdecarte["Unique"] = commun, peucommun, rare, unique
    return listepaquetdecarte


partie = Jeudecartestats()
partie.jeuclassique(2)
