from connect import connecter

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
        return connecter(f"SELECT nb_population FROM ville WHERE nom = '{ville}'")
        
    
    
    
    def afficher_date_construction_ville(self,ville):
        """
        Affiche la date de construction de la ville prise en argument.
        """
        return connecter(f"SELECT date_construction FROM ville WHERE nom = '{ville}'")
    
    
    
    def afficher_motdepasse_utilisateur(self, utilisateur):
        """
        Affiche le mot de passe de l'utilisateur demandé.
        """
        return connecter(f"SELECT mot_de_passe FROM utilisateur WHERE surnom = '{utilisateur}'")
    

    def afficher_pays_ville(self, ville):
        """
        Prend en argument une ville et affiche le pays associé.
        """
        return connecter(f"SELECT pays FROM ville WHERE nom='{ville}'")
    

    def afficher_nom_utilisateur(self, utilisateur):
        """
        Renvoie le nom de l'utilisateur entré en argument.
        """
        return connecter(f"SELECT nom FROM utilisateur WHERE surnom = '{utilisateur}'")
    



