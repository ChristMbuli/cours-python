def saluer(nom, message="Bonjour"):
    #Affiche un message de salutation personnalisé"""
    return f"{message} {nom} !"

def puissance(nombre, exposant=2):
    #Calcule la puissance d'un nombre avec un exposant par défaut de 2
    return nombre ** exposant

# Tests de la fonction saluer
print(saluer("Alice"))                 
print(saluer("Bob", "Bonsoir"))       
print(saluer("Claire", "Bienvenue"))    

# Tests de la fonction puissance
print(f"\n2 au carré = {puissance(2)}")           
print(f"3 au cube = {puissance(3, 3)}")           
print(f"5 à la puissance 4 = {puissance(5, 4)}") 
