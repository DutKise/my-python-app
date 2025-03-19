class Vehicule:
    """Classe de base représentant un véhicule."""
    def __init__(self, marque: str, modele: str, vitesse: int = 0):
        self.marque = marque
        self.modele = modele
        self.vitesse = vitesse
    
    def description(self):
        return f"{self.marque} {self.modele}, vitesse : {self.vitesse} km/h"
    
    def klaxon(self):
        print("Tut Tut!")
    
    def accelerer(self, vitesse: int):
        self.vitesse += vitesse
        return f"Le véhicule accélère de {vitesse} km/h, vitesse actuelle : {self.vitesse} km/h"

class Voiture(Vehicule):
    """Classe représentant une voiture."""
    def __init__(self, marque: str, modele: str, type_moteur: str, vitesse: int = 0):
        super().__init__(marque, modele, vitesse)
        self.type_moteur = type_moteur  # "thermique" ou "électrique"
    
    def description(self):
        return f"Voiture {self.type_moteur} - {super().description()}"

class Scooter(Vehicule):
    """Classe représentant un scooter."""
    def __init__(self, marque: str, modele: str, type_moteur: str, vitesse: int = 0):
        super().__init__(marque, modele, vitesse)
        self.type_moteur = type_moteur  # "thermique" ou "électrique"
    
    def description(self):
        return f"Scooter {self.type_moteur} - {super().description()}"

# Création de quelques voitures
tesla = Voiture("Tesla", "Model S", "électrique", 0)
peugeot = Voiture("Peugeot", "208", "thermique", 0)
audi = Voiture("Audi", "A3", "thermique", 0)

# Affichage des descriptions des voitures
print(tesla.description())
print(peugeot.description())
print(audi.description())
