import mysql.connector

try:
    # Connexion à la base de données
    mydb = mysql.connector.connect(
        host='0504-srv-sig',
        database='nsi_eleve3',
        user='nsi_eleve3',
        password='eleve3'
    )
    mydb.autocommit = True  # Autocommit pour éviter de devoir faire un commit

    curseur = mydb.cursor()

    # Correction de la requête SQL
    requete = "SELECT nom_commande FROM commande"
    curseur.execute(requete)

    # Récupérer tous les résultats
    resultat = curseur.fetchall()

    # Vérifier et afficher les résultats
    if resultat:
        for row in resultat:
            print(row)  # Affiche chaque ligne retournée par la requête
    else:
        print("Aucun résultat trouvé.")

except mysql.connector.Error as err:
    print(f"Erreur lors de la connexion ou de l'exécution de la requête : {err}")

finally:
    # Toujours fermer la connexion à la base de données
    if mydb.is_connected():
        curseur.close()
        mydb.close()