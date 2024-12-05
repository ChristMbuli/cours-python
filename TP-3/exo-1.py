class Personne:
    def __init__(self, nom, age, sexe):
        self.nom = nom
        self.age = age
        self.sexe = sexe
    
    def grandir(self, annees=1):
        """
        Ajoute un certain nombre d'années à l'âge de la personne
        Par défaut, ajoute 1 an si aucun paramètre n'est spécifié
        """
        self.age += annees

# Exemple d'utilisation
p1 = Personne("Jean", 25, "M")
print(p1.age) 
p1.grandir()   
print(p1.age)  
p1.grandir(3)  
print(p1.age) 