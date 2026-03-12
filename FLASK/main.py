from random import randint 
from Actions import Action
from utilisateur import Utilisateur
import datetime
from commande import Commande



#L'utilisateur fait une requête à l'opérateur.
Idriss = Utilisateur("Atil", "Idriss", "thekiller72")
requete = "Le nombre d'habitants à Marseille."
print(Idriss.saisir_commande(requete))


villes = [
    "Gap","Marseille", "Paris", "Lyon", "Toulouse", "Nice", "Nantes",
    "Montpellier", "Strasbourg", "Bordeaux", "Lille", "Rennes",
    "Reims", "Toulon", "Saint-Étienne", "Le Havre", "Grenoble",
    "Dijon", "Angers", "Nîmes", "Clermont-Ferrand", "Villeurbanne",
    "Saint-Denis", "Aix-en-Provence", "Besançon", "Limoges"
]

utilisateurs = ["thekiller72","mdupont","tartempion_95","grumpy_cat","pierre_the_terrible","sophie_les_pates",        
"soda_fantome","claire_qui_rigole","super_héros_de_lombre","la_chieuse","chasseur_de_croissants","les_pommes_de_terre","king_burger",
"mama_bear", "super_nana_01","max_power_up","darth_vador_94","princesse_mignon","le_chef_de_lombre","fanny_le_fantome"]

def requeter(requete):
    a = Action()
    if "habitant" in requete or "population" in requete:
        for ville in villes:
            if ville in requete:
                population = a.afficher_population_ville(ville).sommet()[0]
                return(f"Le nombre d'habitants à {ville} est {population}.")


    elif "date" in requete:
        for ville in villes:
            if ville in requete:
                date = a.afficher_date_construction_ville(ville).sommet()[0]
                return(f"La date de construction de {ville} est {date}.")

    elif "mot de passe" in requete:
        for utilisateur in utilisateurs:
            if utilisateur in requete:
                motdepasse = a.afficher_motdepasse_utilisateur(utilisateur).sommet()[0]
                return(f"Le mot de passe de {utilisateur} est {motdepasse}.")


    elif "pays" in requete:
        for ville in villes:
            if ville in requete:
                pays = a.afficher_pays_ville(ville).sommet()[0]
                return(f"La ville de {ville} se situe en {pays}.")


    elif "nom" in requete and not("prénom" in requete):
        for utilisateur in utilisateurs:
            if utilisateur in requete:
                nom = a.afficher_nom_utilisateur(utilisateur).sommet()[0]
                return(f"Le nom de {utilisateur} est {nom}")
                
    elif "prénom" in requete:
        for utilisateur in utilisateurs:
            if utilisateur in requete:
                prenom = a.afficher_prenom_utilisateur(utilisateur).sommet()[0]
                return(f"Le prénom de {utilisateur} est {prenom}")            


    elif "blague" in requete:
        return(a.raconter_blague())
    



c = Commande()
if "addition" in requete or "somme" in requete:
    liste = []
    for element in requete.split():
        if element.isdigit() == True:
            liste.append(element)
    result = c.addition(liste[0], liste[1])
    print(f"Le résultat de la somme entre {liste[0]} et {liste[1]} est {result}")


elif "soustraction" in requete or "différence" in requete:
    liste = []
    for element in requete.split():
        if element.isdigit() == True:
            liste.append(element)
    result = c.soustraction(liste[0], liste[1])
    print(f"Le résultat de la soustraction entre {liste[0]} et {liste[1]} est {result}.")

elif "produit" in requete or "multiplication" in requete:
    liste = []
    for element in requete.split():
        if element.isdigit() == True:
            liste.append(element)
    result = c.multiplication(liste[0], liste[1])
    print(f"Le résultat du produit entre {liste[0]} et {liste[1]} est {result}")


elif "division" in requete:
    liste = []
    for element in requete.split():
        if element.isdigit() == True:
            liste.append(element)
    result = c.division(liste[0], liste[1])
    print(f"Le résultat de la division {liste[0]} et {liste[1]} est {result}")
    
    
    
    
