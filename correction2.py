while True: # condition d'entrée
    # Initialisstion de la variable de la condition d'arret
    # Toujours à l'intérieur de la boucle
    try:
        n = int(input("donnez un entier > 0 : "))
        print("vous avez fourni", n)
        if n > 0: # condition d'arret
            break # arrreter/sortir de la boucle
    except ValueError:
        print("Veuillez entrer un nombre entier SVP")