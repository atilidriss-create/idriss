import mysql.connector
from classes import Pile, File


def connecter(requete):
    try:
        # Connexion à la base de données
        mydb = mysql.connector.connect(
            host='localhost',
            database= "commandes_vocales",
            user='root',
            password=None
        )
        mydb.autocommit = True  # Autocommit pour éviter de devoir faire un commit

        curseur = mydb.cursor()
        curseur.execute(requete)
        resultat = curseur
        
        p = Pile()
        if resultat:
            for row in resultat:
                p.empiler(row)
        else:
             print("Aucun résultat trouvé.")
        

        return p

         

        # Récupérer tous les résultats
        

        # Vérifier et afficher les résultats
        #Affiche chaque ligne retournée par la requête

    except mysql.connector.Error as err:
        print(f"Erreur lors de la connexion ou de l'exécution de la requête : {err}")

    finally:
        # Toujours fermer la connexion à la base de données
        if mydb.is_connected():
            curseur.close()
            mydb.close()

        
