# Création du dictionnaire des notes
notes = {
    'Alice': 15,
    'Bob': 12,
    'Claire': 17,
    'David': 9,
    'Emma': 18
}

# Ajout d'un nouvel élève
notes['Frank'] = 14
print("ajout de Frank:", notes)

# Modification de la note de Bob
notes['Bob'] = 16
print("modification de la note de Bob:", notes)

#Suppression de David
del notes['David']
print("suppression de David:", notes)

#Calcul et affichage de la moyenne de la classe
moyenne = sum(notes.values()) / len(notes)
print(f"La moyenne de la classe est : {moyenne:.2f}/20")
