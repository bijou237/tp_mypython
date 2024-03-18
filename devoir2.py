# Début controle de saisie 
while True: 
    
    try:
        aage = int(input("Quel age avez vous?: "))
        # On teste si l'age est positif 
        if age > 0:
            break
    except ValueError:
        print("Nous ne voulons que des nombres entiers positifs")

#- Fin controle de saisie

if age >= 18:
    print("Vous êtes majeur.")

else:
    print("Vous êtes mineur.")

# Demander à l'utilisateur son âge
age = int(input("Quel est votre âge ? "))

# Vérifier si l'âge est supérieur ou égal à 18
if age >= 18:
    print("Vous êtes majeur.")
# Vérifier si l'âge est strictement inférieur à zéro
elif age < 0:
    print("Erreur : L'âge ne peut pas être négatif.")
# Si l'âge est compris entre 0 et 17
else:
    print("Vous êtes mineur.")
# Dans le cas d'une chaine de caratere
    