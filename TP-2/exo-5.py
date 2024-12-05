def superieur_a_n(n):
    #Retourne une fonction lambda qui vérifie si un nombre est supérieur à n
    return lambda x: x > n

def creer_multiplicateur(n):
    #Retourne une fonction lambda qui multiplie un nombre par n
    return lambda x: x * n

# Tests de superieur_a_n
sup_5 = superieur_a_n(5)
nombres_test = [3, 5, 7, 10]
print("Test de superieur_a_5 :")
for nombre in nombres_test:
    print(f"{nombre} est supérieur à 5 : {sup_5(nombre)}")

# Tests de creer_multiplicateur
double = creer_multiplicateur(2)
triple = creer_multiplicateur(3)
print("\nTest des multiplicateurs :")
for nombre in [1, 2, 3, 4]:
    print(f"Double de {nombre} : {double(nombre)}")
    print(f"Triple de {nombre} : {triple(nombre)}")
