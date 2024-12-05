# Liste de mots à trier
mots = ["banane", "pomme", "cerise", "mangue", "kiwi"]

# Liste de dictionnaires d'étudiants
etudiants = [
    {"nom": "Alice", "note": 85},
    {"nom": "Bob", "note": 72},
    {"nom": "Charlie", "note": 90}
]

# Tri des mots par longueur
mots.sort(key=lambda mot: len(mot))
print("Mots triés par longueur :")
print(mots)

#Tri des étudiants par note (ordre décroissant)
etudiants.sort(key=lambda etudiant: etudiant["note"], reverse=True)
print("\nÉtudiants triés par note (du plus élevé au plus bas) :")
for etudiant in etudiants:
    print(f"{etudiant['nom']}: {etudiant['note']}")
