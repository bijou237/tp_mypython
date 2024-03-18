# Ce programme permet de resoudre une equation de la forme ax+b=0
#  avec a different de 0; EXemple : 2x+5=0 => 2x=-5 => x=-5/2 ;
# x=-b/a; x=-5/2
#Algo : etape 1: on transpose +5 dans le second membre (2x=-5)
#      etape 2: on divise le second membre par le coef de x (x=-5/2)
a = 6 #6x+12=0 => x=-12/6=-2
b = 12
x =-b/a
# Le resultat de votre equation est 

print(x)

a = int(input("enterz la valeur de a: "))
b = int(input("entrez la valeur de b: "))
x=-b/a
print("le resultat de l'opération est =", x)
