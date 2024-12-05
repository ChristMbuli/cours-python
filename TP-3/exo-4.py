from exo_2 import Point
import math

class Cercle:
    def __init__(self, centre, rayon, couleur="noir"):
 
        if isinstance(centre, tuple):
            self._centre = Point(centre[0], centre[1])
        else:
            self._centre = centre
        self._rayon = rayon
        self._couleur = couleur
    
    # Getters
    def get_centre(self):
        return self._centre
    
    def get_rayon(self):
        return self._rayon
    
    def get_couleur(self):
        return self._couleur
    
    # Setters
    def set_rayon(self, rayon):
        self._rayon = rayon
    
    def set_couleur(self, couleur):
        self._couleur = couleur
    
    def set_surface(self, surface):
        #Modifie le rayon pour obtenir la surface désirée"""
        self._rayon = math.sqrt(surface / math.pi)
    
    def deplacer(self, dx, dy):
        #Déplace le centre du cercle
        self._centre.deplacer(dx, dy)
    
    def surface(self):
        #Calcule la surface du cercle
        return math.pi * self._rayon ** 2
    
    def afficher(self):
        #Affiche l'état complet du cercle
        print(f"Cercle de centre ({self._centre.x()}, {self._centre.y()})")
        print(f"Rayon: {self._rayon}")
        print(f"Couleur: {self._couleur}")
        print(f"Surface: {self.surface():.2f}")


# Création d'un cercle avec un Point
centre = Point(1, 2)
c1 = Cercle(centre, 5, "rouge")
c1.afficher()

# Création d'un cercle avec un tuple
c2 = Cercle((0, 0), 3, "bleu")
c2.afficher()

# Modification de la surface
c2.set_surface(50)
print(f"Nouveau rayon après modification de la surface: {c2.get_rayon():.2f}")

# Déplacement
c2.deplacer(2, 3)
c2.afficher()

# Modification de la couleur
c2.set_couleur("vert")
print(f"Nouvelle couleur: {c2.get_couleur()}")