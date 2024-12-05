import math

class Point:
    def __init__(self, x=0, y=0):
        self.x_coord = x
        self.y_coord = y
    
    def deplacer(self, dx, dy):
        #Déplace le point de dx et dy
        self.x_coord += dx
        self.y_coord += dy
    
    def distance_origine(self):
        #Calcule la distance entre le point et l'origine
        return math.sqrt(self.x_coord**2 + self.y_coord**2)
    
    def afficher(self):
        #Affiche la position du point
        print(f"Position: ({self.x_coord}, {self.y_coord})")
    
    def x(self):
        #Renvoie la coordonnée x
        return self.x_coord
    
    def y(self):
        #Renvoie la coordonnée y
        return self.y_coord
    
    def rho(self):
        #Renvoie la coordonnée polaire rho (distance à l'origine)
        return self.distance_origine()
    
    def theta(self):
        #Renvoie la coordonnée polaire theta (angle en radians)
        return math.atan2(self.y_coord, self.x_coord)
    
    def homoth(self, R):
        #Applique une homothétie de centre O et de rapport R
        self.x_coord *= R
        self.y_coord *= R


# Création d'un point
p = Point(3, 4)
p.afficher()  # Position: (3, 4)

# Distance à l'origine
print(f"Distance à l'origine: {p.distance_origine()}")  # 5.0

# Coordonnées cartésiennes
print(f"x: {p.x()}, y: {p.y()}")  # x: 3, y: 4

# Coordonnées polaires
print(f"rho: {p.rho()}, theta: {p.theta()}")

# Application d'une homothétie
p.homoth(2)
p.afficher()  # Position: (6, 8)