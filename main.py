from blagues import choisir_message, blagues
from random import randint 
from Actions import Action
from utilisateur import Utilisateur
import datetime


#L'utilisateur fait une requête à l'opérateur.
Idriss = Utilisateur("Atil", "Idriss", "cr7legoat")
requete = "Quel est le pays de Gap ?"
print(Idriss.saisir_commande(requete))


a= Action()

villes = [
    "Gap","Marseille", "Paris", "Lyon", "Toulouse", "Nice", "Nantes",
    "Montpellier", "Strasbourg", "Bordeaux", "Lille", "Rennes",
    "Reims", "Toulon", "Saint-Étienne", "Le Havre", "Grenoble",
    "Dijon", "Angers", "Nîmes", "Clermont-Ferrand", "Villeurbanne",
    "Saint-Denis", "Aix-en-Provence", "Besançon", "Limoges"
]

utilisateurs = ["cr7legoat","mdupont","tartempion_95","grumpy_cat","pierre_the_terrible","sophie_les_pates",        
"soda_fantome","claire_qui_rigole","super_héros_de_lombre","la_chieuse","chasseur_de_croissants","les_pommes_de_terre","king_burger",
"mama_bear", "super_nana_01","max_power_up","darth_vador_94","princesse_mignon","le_chef_de_lombre","fanny_le_fantome"]


if "habitant" in requete:
    for ville in villes:
        if ville in requete:
            population = a.afficher_population_ville(ville).sommet()[0]
            print(f"Le nombre d'habitants à {ville} est {population}.")


elif "date" in requete:
    for ville in villes:
        if ville in requete:
            date = a.afficher_date_construction_ville(ville).sommet()[0]
            print(f"La date de construction de {ville} est {date}.")

elif "mot de passe" in requete:
    for utilisateur in utilisateurs:
        if utilisateur in requete:
            motdepasse = a.afficher_motdepasse_utilisateur(utilisateur).sommet()[0]
            print(f"Le mot de passe de {utilisateur} est {motdepasse}.")


elif "pays" in requete:
    for ville in villes:
        if ville in requete:
            pays = a.afficher_pays_ville(ville).sommet()[0]
            print(f"La ville de {ville} se situe en {pays}.")


    
    

