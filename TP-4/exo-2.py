class Contact:
    def __init__(self, nom, numero):
        self._nom = nom
        self._numero = numero

    def nom(self):
        return self._nom

    def numero(self):
        return self._numero

    def __str__(self):
        return f"{self._nom}: {self._numero}"


class Repertoire:
    def __init__(self, max_contacts):
        self._max_contacts = max_contacts
        self._contacts = []

    def addContact(self, nom, numero):
        if len(self._contacts) >= self._max_contacts:
            return False
        
        nouveau_contact = Contact(nom, numero)
        self._contacts.append(nouveau_contact)
        return True

    def getNum(self, nom):
        for contact in self._contacts:
            if contact.nom == nom:
                return contact.numero
        return None

    def getNContacts(self):
        return len(self._contacts)

    def getContact(self, indice):
        if 0 <= indice < len(self._contacts):
            return self._contacts[indice]
        return None


# Test du programme
if __name__ == "__main__":
    # Création d'un répertoire avec maximum 3 contacts
    repertoire = Repertoire(3)

    # Ajout de contacts
    print("Ajout de contacts:")
    print(repertoire.addContact("Alice", "0611223344"))  
    print(repertoire.addContact("Bob", "0622334455"))    
    print(repertoire.addContact("Charlie", "0633445566")) 
    print(repertoire.addContact("David", "0644556677"))  

    # Test des autres méthodes
    print(f"\nNombre de contacts: {repertoire.getNContacts()}")  
    print(f"Numéro d'Alice: {repertoire.getNum('Alice')}")      
    
    # Affichage d'un contact par son indice
    contact = repertoire.getContact(1)
    if contact:
        print(f"Contact à l'indice 1: {contact}")
