    #Devoir4
jours_semaines=["lundi", "Mardi", "Mercredi", "jeudi", "Vendredi", "Samedi", "Dimanche"]
for jour in jours_semaines:
    print(jour)

mois_annee = ("Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre")

# Initialisation de l'index pour parcourir les éléments du tuple
index = 0

# Boucle while pour parcourir les mois de l'année
while index < len(mois_annee):
    print(mois_annee[index])
    index += 1

    