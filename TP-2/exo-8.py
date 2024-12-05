import math
import random

def racine(x):
    #Calcule la racine carrée d'un nombre en utilisant math.sqrt
    if x < 0:
        raise ValueError("Impossible de calculer la racine carrée d'un nombre négatif")
    return math.sqrt(x)

def nombre_aleatoire(a, b):
    #Retourne un nombre aléatoire entre a et b inclus
    return random.randint(a, b)

# Tests de la fonction racine
nombres_test = [16, 25, 100]
print("Test de la fonction racine :")
for n in nombres_test:
    print(f"La racine carrée de {n} est : {racine(n)}")

# Tests de la fonction nombre_aleatoire
print("\nTest de la fonction nombre_aleatoire :")
for _ in range(5):  # Génère 5 nombres aléatoires
    a, b = 1, 10
    nombre = nombre_aleatoire(a, b)
    print(f"Nombre aléatoire entre {a} et {b} : {nombre}")
