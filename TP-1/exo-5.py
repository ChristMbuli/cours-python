# Liste des étudiants avec leurs notes
etudiants = [
    {'nom': 'Alice', 'note': 15},
    {'nom': 'Bob', 'note': 12},
    {'nom': 'Claire', 'note': 17},
    {'nom': 'David', 'note': 9}
]

# Affichage de tous les étudiants
print("Liste des étudiants et leurs notes :")
for etudiant in etudiants:
    print(f"{etudiant['nom']}: {etudiant['note']}/20")

# Recherche de l'étudiant avec la meilleure note
meilleur_etudiant = max(etudiants, key=lambda x: x['note'])
print(f"\nMeilleur étudiant : {meilleur_etudiant['nom']} avec {meilleur_etudiant['note']}/20")

# Calcul de la moyenne de la classe
somme_notes = sum(etudiant['note'] for etudiant in etudiants)
moyenne = somme_notes / len(etudiants)
print(f"\nMoyenne de la classe : {moyenne:.2f}/20")
