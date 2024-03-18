class livres:
    def __init__(self, titre, auteur, genre, prix): 
        self.__titre = titre
        self.__auteur = auteur
        self.genre = genre
        self.__prix = prix 
    #Methode Get
    # Acceder a l'attribut titre
    def get_titre (self):
        return self.__titre
    #Acceder a l'attribut auteur
    def get_auteur(self):
        return self.__auteur
    # Acceder a l'attribut genre
    def get_genre(self):
        return self.genre
    # Acceder a l'attribut prix
    def get_prix(self):
        return self.prix
    # Methode Set 
    #Attribut titre
    def set_titre(self, titre):
        self.titre = titre
    #Attribut auteur
    def set_auteur(self, auteur):
        self.auteur = auteur
    #Attribut genre
    def set_genre(self, genre):
        self.genre = genre
    #Attribut prix
    def set_prix(self, prix):
        self.prix = prix
   
#print ("livre cree : cela veut dire qu'un livre est presenté, instanciation de la classe livre")
    def infos(self):
        print(f"Titre: {self.titre}, auteur: {self.auteur}, genre:{self.genre}, prix:{self.prix}")


