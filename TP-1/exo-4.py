# Chaîne de caractères à analyser
chaine = "python est amusant"


# Création du dictionnaire pour stocker les fréquences
frequences = {}

# Parcours de chaque caractère de la chaîne
for caractere in chaine:
    # Ignorer les espaces
    if caractere != ' ':
        # Si le caractère existe déjà, on incrémente sa fréquence
        # Sinon, on l'initialise à 1
        frequences[caractere] = frequences.get(caractere, 0) + 1

# Affichage du résultat
print("Fréquence des lettres :", frequences)
