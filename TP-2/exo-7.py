# Import du module math_operations
from modules import math_operations

# Test de la fonction carré
nombre = 5
resultat_carre = math_operations.carre(nombre)
print(f"Le carré de {nombre} est : {resultat_carre}")

# Test de la fonction somme
a, b = 10, 20
resultat_somme = math_operations.somme(a, b)
print(f"La somme de {a} et {b} est : {resultat_somme}")

# Test de la fonction puissance
nombre = 3
exposant = 4
resultat_puissance = math_operations.puissance(nombre, exposant)
print(f"{nombre} à la puissance {exposant} est : {resultat_puissance}")

# Test avec l'exposant par défaut
nombre = 6
resultat_puissance_defaut = math_operations.puissance(nombre)
print(f"Le carré de {nombre} (puissance par défaut) est : {resultat_puissance_defaut}")
