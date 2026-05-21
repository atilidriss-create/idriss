from connect import connecter
class Utilisateur:
    def __init__(self, nom, prenom, surnom, email, mot_de_passe):
        """
        Initialisation de Utilisateur.
        """
        self.nom = nom
        self.prenom = prenom
        self.surnom = surnom
        self.email = email
        self.mot_de_passe = mot_de_passe

    def saisir_commande(self, requete):
        """
        Permet de saisir une commande à l'opérateur.
        """
        return f"{self.surnom} a demandé : {requete}"
    
    
    
    def connexion(self):
        """
        Renvoie un booléen : teste si l'utilisateur a bien saisi les données présentes dans la base de données.
        """
        utilisateur = connecter(f"SELECT EXISTS (SELECT 1 FROM utilisateur WHERE surnom = '{self.surnom}')" ).sommet()[0]
        motdepasse = connecter(f"SELECT EXISTS (SELECT 1 FROM utilisateur WHERE mot_de_passe = '{self.mot_de_passe}')" ).sommet()[0]
        if utilisateur == 1 and motdepasse == 1:
            return True
        else:
            return False
        
    
    def inscription(self, nom, prenom, nom_utilisateur, email, mot_de_passe):
        """
        Inscrit l'utilisateur dans la base de données en fonction des données saisies.
        """
        return connecter(f"INSERT INTO utilisateur (nom, prenom,surnom, mail, mot_de_passe) VALUES ('{nom}', '{prenom}', '{nom_utilisateur}', '{email}', '{mot_de_passe}')")
        
    
