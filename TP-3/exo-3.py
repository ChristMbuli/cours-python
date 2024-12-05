from exo_2 import Point
import math

class Segment:
    def __init__(self, p1, p2):
      #Constructeur prenant deux Points comme paramètres
        #Si des tuples sont fournis, les convertit en Points
       
        if isinstance(p1, tuple):
            p1 = Point(p1[0], p1[1])
        if isinstance(p2, tuple):
            p2 = Point(p2[0], p2[1])
            
        self.point1 = p1
        self.point2 = p2
    
    def afficher(self):
        #Affiche les coordonnées des deux points du segment
        print(f"Segment: [({self.point1.x()}, {self.point1.y()}) -> ({self.point2.x()}, {self.point2.y()})]")
    
    def translation(self, dx, dy):
        #Effectue une translation du segment
        self.point1.deplacer(dx, dy)
        self.point2.deplacer(dx, dy)
    
    def longueur(self):
        #Calcule la longueur du segment
        dx = self.point2.x() - self.point1.x()
        dy = self.point2.y() - self.point1.y()
        return math.sqrt(dx**2 + dy**2)

# Création d'un segment avec des Points
p1 = Point(0, 0)
p2 = Point(3, 4)
seg1 = Segment(p1, p2)
seg1.afficher()  # Segment: [(0, 0) -> (3, 4)]
print(f"Longueur: {seg1.longueur()}")  # Longueur: 5.0

# Création d'un segment avec des tuples
seg2 = Segment((1, 1), (4, 5))
seg2.afficher()  # Segment: [(1, 1) -> (4, 5)]

# Translation
seg2.translation(2, -1)
seg2.afficher()  # Segment: [(3, 0) -> (6, 4)]