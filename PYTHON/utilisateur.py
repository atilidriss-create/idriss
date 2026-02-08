class Utilisateur:
    def __init__(self, nom, prenom, surnom):
        """
        Initialisation de Utilisateur.
        """
        self.nom = nom
        self.prenom = prenom
        self.surnom = surnom

    def saisir_commande(self, requete):
        """
        Permet de saisir une commande à l'opérateur.
        """
        return f"{self.surnom} a demandé : {requete}"
    


    

