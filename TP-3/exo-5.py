from exo_2 import Point
from exo_4 import Cercle
import random
import math

class Collimateur:
    def __init__(self):
        self.position = Point(0, 0)
    
    def deplacer(self, x, y):
        self.position = Point(x, y)
    
    def tirer(self, cibles):
        """Vérifie si le tir touche une des cibles"""
        for cible in cibles:
            if self.touche_cible(cible):
                return cible
        return None
    
    def touche_cible(self, cible):
        """Vérifie si le tir touche une cible spécifique"""
        distance = math.sqrt((self.position.x() - cible.get_centre().x())**2 + 
                           (self.position.y() - cible.get_centre().y())**2)
        return distance <= cible.get_rayon()

class Jeu:
    SEUIL_MINIMUM = 1.0  # Rayon minimum avant élimination
    REDUCTION_TAILLE = 0.5  # Réduction du rayon à chaque touche
    
    def __init__(self, nb_cibles=3):
        self.collimateur = Collimateur()
        self.cibles = []
        self.score = 0
        
        # Création des cibles aléatoires
        for _ in range(nb_cibles):
            x = random.randint(-10, 10)
            y = random.randint(-10, 10)
            rayon = random.uniform(2, 5)
            self.cibles.append(Cercle((x, y), rayon))
    
    def tour(self, x, y):
        """Effectue un tour de jeu"""
        self.collimateur.deplacer(x, y)
        cible_touchee = self.collimateur.tirer(self.cibles)
        
        if cible_touchee:
            self.score += 1
            self.reduire_cible(cible_touchee)
            return True
        return False
    
    def reduire_cible(self, cible):
        """Réduit la taille d'une cible touchée"""
        nouveau_rayon = cible.get_rayon() - self.REDUCTION_TAILLE
        
        if nouveau_rayon <= self.SEUIL_MINIMUM:
            cible.set_couleur("rouge")
            self.cibles.remove(cible)
            print("Cible éliminée!")
        else:
            cible.set_rayon(nouveau_rayon)
    
    def partie_terminee(self):
        """Vérifie si la partie est terminée"""
        return len(self.cibles) == 0
    
    def afficher_etat(self):
        """Affiche l'état actuel du jeu"""
        print(f"\nScore: {self.score}")
        print(f"Cibles restantes: {len(self.cibles)}")
        for i, cible in enumerate(self.cibles, 1):
            print(f"\nCible {i}:")
            cible.afficher()

# Exemple d'utilisation
def jouer():
    jeu = Jeu(3)  # Création d'une partie avec 3 cibles
    
    while not jeu.partie_terminee():
        jeu.afficher_etat()
        
        # Demande les coordonnées du tir
        try:
            x = float(input("\nEntrez la coordonnée x du tir: "))
            y = float(input("Entrez la coordonnée y du tir: "))
            
            if jeu.tour(x, y):
                print("Touché!")
            else:
                print("Raté!")
                
        except ValueError:
            print("Entrée invalide! Veuillez entrer des nombres.")
    
    print(f"\nPartie terminée! Score final: {jeu.score}")

if __name__ == "__main__":
    jouer()