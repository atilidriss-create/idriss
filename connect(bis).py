import mysql.connector
import datetime

def connecter(requete):
    try:
        # Connexion à la base de données
        mydb = mysql.connector.connect(
            host='0504-srv-sig',
            database= "nsi_eleve3",
            user='nsi_eleve3',
            password='eleve3'
        )
        mydb.autocommit = True  # Autocommit pour éviter de devoir faire un commit

        curseur = mydb.cursor()
        
        if resultat:
            for row in resultat:
                print(row[0])
        else:
             print("Aucun résultat trouvé.")

        curseur.execute(requete) 

        # Récupérer tous les résultats
        resultat = curseur.fetchall()

        # Vérifier et afficher les résultats
        #Affiche chaque ligne retournée par la requête

    except mysql.connector.Error as err:
        print(f"Erreur lors de la connexion ou de l'exécution de la requête : {err}")

    finally:
        # Toujours fermer la connexion à la base de données
        if mydb.is_connected():
            curseur.close()
            mydb.close()
        
class base_de_donnees:
    def __init__(self):
        """
        
        """      

class MotCle:
    def __init__(self, mot, id_commande, description=""):
        """
        Initialisation de Motcle.
        """
        self.mot = mot
        self.id_commande = id_commande
        self.description = description
        
        
        
class Commande:
    def __init__(self, nom, description=""):
        """
        Initialisation de Commande.
        """
        self.commande = commande

    def addition(self, nb1, nb2):
        """
        Réalise et renvoie une addition entre un nombre nb1 et un nombre nb2.
        """
        return nb1 + nb2


    def soustraction(self, nb1, nb2):
        """
        Réalise et renvoie une soustraction entre un nombre nb1 et un nombre nb2.
        """
        return nb1 - nb2


    def multiplication(self, nb1, nb2):
        """
        Réalise et renvoie une multiplication entre un nombre nb1 et un nombre nb2.
        """
        return nb1*nb2

    def division(self, nb1, nb2):
        """
        Réalise une division entre un nombre nb1 et un nombre nb2.
        """
        return nb1/nb2



class Categorie:
    
    def __init__(self, nom, description=""):
        """
        Initialisation de Categorie.
        """
        self.nom = nom
        self.description = description

class Action:
    def __init__(self):
        """
        Initialisation de Action.
        """
        self.action = None


    def afficher_population_ville(self, ville):
        """
        Interroge la base de données pour afficher la ville demandée.
        """
        return base_de_donnees(f"SELECT nb_population FROM ville WHERE nom = '{ville}'")
        
    
    
    
    def afficher_date_construction_ville(self,ville):
        """
        Affiche la date de construction de la ville prise en argument.
        """
        return base_de_donnees(f"SELECT date_construction FROM ville WHERE nom = '{ville}'")
    
    
    
    def afficher_motdepasse_utilisateur(self, utilisateur):
        """
        Affiche le mot de passe de l'utilisateur demandé.
        """
        return base_de_donnees(f"SELECT mot_de_passe FROM utilisateur WHERE surnom = '{utilisateur}'")
    

    def afficher_pays_ville(self, ville):
        """
        Prend en argument une ville et affiche le pays associé.
        """
        return base_de_donnees(f"SELECT pays FROM ville WHERE ville={ville}")


    def raconter_une_blague(self):
        """
        Renvoie une blague aléatoire
        """
        return random.choice(blagues)


    def afficher_aide(self):
        """
        Donne toutes les informations concernant ce que peut faire la base de données. 
        """
        return base_de_données(f"SELECT description FROM action")


    def afficher_mail_utilisateur(self, utilisateur):
        """
        Renvoie l'adresse mail de l'utilisateur entré en argument
        """
        
        
        
a = Action()
print(a.raconter_une_blague())        


class Utilisateur:
    def __init__(self, nom, prenom, surnom):
        """
        Initialisation de Utilisateur.
        """
        self.nom = nom
        self.prenom = prenom
        self.surnom = surnom
        
        

#programme principal.
a = Action()
print(a.afficher_population_ville("Gap"))
print(a.afficher_date_construction_ville("Marseille"))
print(a.afficher_motdepasse_utilisateur("cr7legoat"))
print(a.afficher)

print(base_de_donnees(f"SELECT * FROM utilisateur"))



def choisir_message(blagues):
    

# Liste des messages
blagues = [
    "Quelle mamie fait peur aux voleurs ? Mamie Traillette.",
    "Pourquoi est-ce si difficile de conduire dans le Nord ? Parce que les voitures n’arrêtent pas de caler (Pas-de-Calais).",
    "Pourquoi est-ce qu'on dit que les bretons sont tous frères et sœurs ? Parce qu’ils n’ont Quimper.",
    "Pourquoi faut-il mettre tous les crocos en prison ? Parce que les crocos dealent.",
    "Comment fait-on pour allumer un barbecue breton ? On utilise des breizh.",
    "Pourquoi dit-on que les poissons travaillent illégalement ? Parce qu’ils n’ont pas de FISH de paie.",
    "Quel fruit est assez fort pour couper des arbres ? Le citron.",
    "Que fait un cendrier devant un ascenseur ? Il veut des cendres.",
    "Que dit une imprimante dans l'eau ? J’ai papier.",
    "Pourquoi les girafes n'existent pas ? Parce que c’est un coup monté.",
    "Comment appelle-t-on un jeudi vraiment nul ? Une trajeudi.",
    "Que fait un geek quand il a peur ? Il URL.",
    "Quel est le carburant le plus détendu ? Le kérozen.",
    "Quel est le sport préféré des insectes ? Le cricket.",
    "Pourquoi est-ce que les éoliennes n'ont pas de copain ? Parce qu’elles se prennent toujours des vents.",
    "Pourquoi les cordonniers sont-ils curieux ? Parce qu’ils se mêlent de tout (semelle).",
    "Que dit le citron quand il braque une banque ? « Pas un zeste, ze suis pressé ! »",
    "Comment appelle-t-on une manifestation d'aveugles ? Un festival de cannes.",
    "Que risque-t-on à lancer de l'ail sur un mur ? Le retour du jet d’ail.",
    "Quelle est la fée la plus paresseuse ? La fée Néante.",
    "Que dit une noisette qui tombe à l'eau ? « Au secours, je me noix ! »",
    "Tu connais l'histoire de l'armoire ? Elle est pas commode.",
    "Tu connais l'histoire de la feuille de papier ? Elle déchire !",
    "Comment appelle-t-on un chat tout-terrain ? Un cat cat.",
    "Quelle est l'info la plus tirée par les cheveux ? Il n’y a pas de chauve à Bastia, mais à Calvi si.",
    "Que disaient les apôtres à Jésus quand il racontait une blague de ce top ? « C’est naze, arrête. »",
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent toujours dans le bateau.",
    "Pourquoi les poissons détestent l'ordinateur ? Parce qu'ils ont peur du net.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Pourquoi les moutons ne racontent jamais de blagues ? Parce qu'ils ont peur de se faire tondre.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent toujours dans le bateau.",
    "Pourquoi les poissons détestent l'ordinateur ? Parce qu'ils ont peur du net.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Pourquoi les moutons ne racontent jamais de blagues ? Parce qu'ils ont peur de se faire tondre."
]


