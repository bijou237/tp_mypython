def remplir_liste():
    # Définition de la taille de la liste
    taille = int(input("Entrez la taille de la liste : "))
    # Initialisation de la liste à vide
    liste = []
    # Remplissage des elements de la liste
    for i in range(taille):
        # l'utilisateur va rentrer les elements de la liste
        element =int(input("Entrez l'élément {}: ".format(i+1)))
        # inserer l'element dans la liste en derniere position
        liste.append(element)
    # la liste remplie sera retournée 
    return liste

# Appel de la fonction pour remplir une liste
ma_liste = remplir_liste()
print("Liste remplie par l'utilisateur :", ma_liste)

# fonctio pour cqlculer la moyenne des notes des éleves
def calculer_moyenne(ma_liste): 
    # calculer la somme des notes 
    total= sum(ma_liste)
    # calculer la taille de la liste
    taille = len(ma_liste)
    # Calculer la moyenne
    moyenne = total/taille 
    return moyenne 
moyennegene = calculer_moyenne(ma_liste)
print("la moyenne génerale de la classe est : ", moyennegene)

