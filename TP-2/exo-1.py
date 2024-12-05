def carre(x):
    #Retourne le carré d'un nombre
    return x * x

def somme(a, b):
    #Retourne la somme de deux nombres
    return a + b

def inverse(chaine):
    #Retourne une chaîne de caractères inversée
    return chaine[::-1]


# Test de la fonction carre
nombre = 5
resultat_carre = carre(nombre)
print(f"Le carré de {nombre} est : {resultat_carre}")

# Test de la fonction somme
a, b = 10, 20
resultat_somme = somme(a, b)
print(f"La somme de {a} et {b} est : {resultat_somme}")

# Test de la fonction inverse
texte = "Python"
resultat_inverse = inverse(texte)
print(f"L'inverse de '{texte}' est : '{resultat_inverse}'")
