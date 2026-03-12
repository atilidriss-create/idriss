import mysql.connector
from classes import Pile


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
        curseur.execute(requete)
        resultat = curseur
        
        p = Pile()
        if resultat:
            for row in resultat:
                p.empiler(row)
        else:
             print("Aucun résultat trouvé.")
        

        return p


    except mysql.connector.Error as err:
        print(f"Erreur lors de la connexion ou de l'exécution de la requête : {err}")

    finally:
        # Toujours fermer la connexion à la base de données
        if mydb.is_connected():
            curseur.close()
            mydb.close()

        
