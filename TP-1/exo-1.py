students = []

#Ajout des étudiants
students.append("Deo")
students.append("Marie")
students.append("Clement")
students.append("Zeze")
students.append("Toto")
students.append("Marha")

print(students)

#Suppression d'un étudiant
students.remove("Marie")
print(students)

#Trier la liste des étudiants
students.sort()
print(students)

#Compter le nombre des etudiantes
print(len(students))
print("Il y a", len(students), "étudiants.")
