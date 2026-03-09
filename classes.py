class Pile:
    def __init__(self):
        """
        Initialisation de la Pile.
        """
        self.p =[]

    def __str__(self):
        """
        Méthode de représentation sous forme de chaînes de caractères.
        """
        return str(self.p)
    
    def empiler(self, element):
        """
        Prend en argument un élément et l'ajoute à la fin de la Pile
        """
        return self.p.append(element)
    
    def depiler(self):
        """
        Retire le dernier élément de la Pile et le renvoie.
        """
        return self.p.pop(-1)
    

    def sommet(self):
        """
        Renvoie le dernier élément de la Pile.
        """
        return self.p[-1]
    

    def taille(self):
        """
        Renvoie la taille de la Pile.
        """
        return len(self.p)
    

    def est_vide(self):
        """
        Renvoie un booléen : teste la vacuité de la Pile.
        """
        return self.p == []
    

class File:
    def __init__(self):
        """
        Initialisation de la File.
        """
        self.f = []


    def __str__(self):
        """
        Méthode de représentation sous forme de chaînes de caractères.
        """
        return str(self.f)
    

    def enfiler(self, element):
        """
        Prend en argument un élément et l'ajoute à la fin de la File.
        """
        return self.f.append(element)
    

    def defiler(self):
        """
        Retire le premier élément de la File et le renvoie.
        """
        return self.f.pop(0)
    

    def est_vide(self):
        """
        Renvoie un booléen : teste la vacuité de la File.
        """
        return self.f == []
    

    def sommet(self):
        """
        Renvoie le premier élément de la File.
        """
        return self.f[0]
    

    def taille(self):
        """
        Renvoie la taille de la File.
        """
        return len(self.f)
    

    