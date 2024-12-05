from functools import reduce

# Liste de test
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liste_base = [1, 2, 3, 4, 5]

# a. Filtrer les nombres pairs avec filter et lambda
nombres_pairs = list(filter(lambda x: x % 2 == 0, nombres))
print("Nombres pairs :", nombres_pairs)

# b. Élever au cube avec map et lambda
cubes = list(map(lambda x: x ** 3, liste_base))
print("Nombres au cube :", cubes)

# c. Calculer le produit avec reduce et lambda
produit = reduce(lambda x, y: x * y, liste_base)
print("Produit des nombres :", produit)
