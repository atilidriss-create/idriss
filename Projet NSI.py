class MotCle:
    def __init__(self, id_motcle, mot, id_commande, description=""):
        self.id_motcle = id_motcle
        self.mot = mot
        self.id_commande = id_commande
        self.description = description
class Commande:
    def __init__(self, id_commande, nom, description=""):
        self.id_commande = id_commande
        self.nom = nom
        self.description = description

class Categorie:
    def __init__(self, id_categorie, nom, description=""):
        self.id_categorie = id_categorie
        self.nom = nom
        self.description = description

class Action:
    def __init__(self, id_action, nom, categorie, fonction):
        self.id_action = id_action
        self.nom = nom
        self.categorie = categorie
        self.fonction = fonction  # faudrait mettre les fonctions python a utiliser ici


class Utilisateur:
    def __init__(self, id_utilisateur, nom, prenom, surnom):
        self.id_utilisateur = id_utilisateur
        self.nom = nom
        self.prenom = prenom
        self.surnom = surnom



class File:
    def __init__(self):
        """
        Initialisation de l'instance File.
        """
        self.f = []

    def __str__(self):
        """
        Méthode de représentation sous forme de chaînes de caractères.
        """
        return str(self.f)

    def enfiler(self, element):
        """
        Prend en argument un élément et l'ajoute à la fin de la file.
        """
        self.f.append(element)

    def defiler(self):
        """
        Retire le premier élément de la file et le renvoie.
        """
        return self.f.pop(0)


    def sommet(self):
        """
        Renvoie le premier élément de la file.
        """
        return self.f[0]


    def taille(self):
        """
        Renvoie la taille de la file
        """
        return len(self.f)

    def est_vide(self):
        """
        Renvoie un booléen : si la file est vide ou non.
        """
        return self.f == []
        
