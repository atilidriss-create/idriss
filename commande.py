class Commande:
    def __init__(self):
        """
        Initialisation de Commande.
        """
        self.commande = None

    def addition(self, nb1, nb2):
        """
        Réalise et renvoie une addition entre un nombre nb1 et un nombre nb2.
        """
        return int(nb1) + int(nb2)


    def soustraction(self, nb1, nb2):
        """
        Réalise et renvoie une soustraction entre un nombre nb1 et un nombre nb2.
        """
        return int(nb1) - int(nb2)


    def multiplication(self, nb1, nb2):
        """
        Réalise et renvoie une multiplication entre un nombre nb1 et un nombre nb2.
        """
        return int(nb1)* int(nb2)

    def division(self, nb1, nb2):
        """
        Réalise une division entre un nombre nb1 et un nombre nb2.
        """
        return int(nb1)/int(nb2)