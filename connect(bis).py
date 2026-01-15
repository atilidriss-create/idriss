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
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent toujours dans le bateau.",
    "Pourquoi les poissons détestent l'ordinateur ? Parce qu'ils ont peur du net.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Pourquoi les moutons ne racontent jamais de blagues ? Parce qu'ils ont peur de se faire tondre.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent toujours dans le bateau.",
    "Pourquoi les poissons détestent l'ordinateur ? Parce qu'ils ont peur du net.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Pourquoi les moutons ne racontent jamais de blagues ? Parce qu'ils ont peur de se faire tondre.",
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent toujours dans le bateau.",
    "Pourquoi les poissons détestent l'ordinateur ? Parce qu'ils ont peur du net.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Pourquoi les moutons ne racontent jamais de blagues ? Parce qu'ils ont peur de se faire tondre.",
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent toujours dans le bateau.",
    "Pourquoi les poissons détestent l'ordinateur ? Parce qu'ils ont peur du net.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Pourquoi les moutons ne racontent jamais de blagues ? Parce qu'ils ont peur de se faire tondre.",
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent toujours dans le bateau.",
    "Pourquoi les poissons détestent l'ordinateur ? Parce qu'ils ont peur du net.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Pourquoi les moutons ne racontent jamais de blagues ? Parce qu'ils ont peur de se faire tondre.",
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent toujours dans le bateau.",
    "Pourquoi les poissons détestent l'ordinateur ? Parce qu'ils ont peur du net.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Pourquoi les moutons ne racontent jamais de blagues ? Parce qu'ils ont peur de se faire tondre.",
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent toujours dans le bateau.",
    "Pourquoi les poissons détestent l'ordinateur ? Parce qu'ils ont peur du net.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Pourquoi les moutons ne racontent jamais de blagues ? Parce qu'ils ont peur de se faire tondre.",
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent toujours dans le bateau.",
    "Pourquoi les poissons détestent l'ordinateur ? Parce qu'ils ont peur du net.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Pourquoi les moutons ne racontent jamais de blagues ? Parce qu'ils ont peur de se faire tondre.",
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent toujours dans le bateau.",
    "Pourquoi les poissons détestent l'ordinateur ? Parce qu'ils ont peur du net.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Pourquoi les moutons ne racontent jamais de blagues ? Parce qu'ils ont peur de se faire tondre.",
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent toujours dans le bateau.",
    "Pourquoi les poissons détestent l'ordinateur ? Parce qu'ils ont peur du net.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Pourquoi les moutons ne racontent jamais de blagues ? Parce qu'ils ont peur de se faire tondre.",
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent toujours dans le bateau.",
    "Pourquoi les poissons détestent l'ordinateur ? Parce qu'ils ont peur du net.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Pourquoi les moutons ne racontent jamais de blagues ? Parce qu'ils ont peur de se faire tondre.",
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent toujours dans le bateau."
]
