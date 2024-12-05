#Expression lambda pour calculer le carré d'un nombre
carre = lambda x: x * x

#Expression lambda pour calculer le produit de deux nombres
produit = lambda a, b: a * b

#Expression lambda pour calculer la longueur d'une chaîne
longueur = lambda chaine: len(chaine)

# Test du carré
nombres_test = [2, 4, 5]
print("Test de la fonction carré :")
for n in nombres_test:
    print(f"Le carré de {n} est : {carre(n)}")

# Test du produit
a, b = 6, 7
print(f"\nLe produit de {a} et {b} est : {produit(a, b)}")

# Test de la longueur
chaines_test = ["Python", "Lambda", "Programmation"]
print("\nTest de la fonction longueur :")
for chaine in chaines_test:
    print(f"Longueur de '{chaine}' : {longueur(chaine)}")
