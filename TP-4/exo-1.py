class Enseignant:
     # Dhs par heure
    TAUX_HEURE_COMPLEMENTAIRE = 300 

    def __init__(self, nom, heures_total):
        self._nom = nom
        self._heures_total = heures_total

    @property
    def nom(self):
        return self._nom

    def heures_complementaires(self):
        pass  

    def retribution_complementaire(self):
        return self.heures_complementaires() * self.TAUX_HEURE_COMPLEMENTAIRE


class EnseignantInterne(Enseignant):
    HEURES_SERVICE = 192

    def heures_complementaires(self):
        return max(0, self._heures_total - self.HEURES_SERVICE)


class IntervenantExterne(Enseignant):
    def heures_complementaires(self):
        return self._heures_total


# Test du programme
if __name__ == "__main__":
    # Création des enseignants
    prof_interne = EnseignantInterne("Ahmed", 200)
    prof_externe = IntervenantExterne("Marie", 100)

    # Tests pour l'enseignant interne
    print(f"Enseignant interne: {prof_interne.nom}")
    print(f"Heures complémentaires: {prof_interne.heures_complementaires()}h")
    print(f"Rétribution: {prof_interne.retribution_complementaire()} Dhs")

    # Tests pour l'intervenant externe
    print(f"\nIntervenant externe: {prof_externe.nom}")
    print(f"Heures complémentaires: {prof_externe.heures_complementaires()}h")
    print(f"Rétribution: {prof_externe.retribution_complementaire()} Dhs")
