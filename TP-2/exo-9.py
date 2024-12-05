# Import des modules du package calculations
from modules import math_operations as math_ops
from modules import string_operations as str_ops

# Test des fonctions de math_operations
print("Tests des opérations mathématiques :")
print(f"Carré de 5 : {math_ops.carre(5)}")
print(f"Somme de 10 et 20 : {math_ops.somme(10, 20)}")
print(f"2 à la puissance 3 : {math_ops.puissance(2, 3)}")

# Test des fonctions de string_operations
print("\nTests des opérations sur les chaînes :")
print(f"Inverse de 'Python' : {str_ops.inverse('Python')}")
print(f"Salutation : {str_ops.saluer('Alice')}")
print(f"Salutation personnalisée : {str_ops.saluer('Bob', 'Bonsoir')}")
