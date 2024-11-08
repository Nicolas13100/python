# -*-coding:Latin-1 -*


class Bateau:
    def __init__(self, nom: str, longueur: float, capacite_max: int):
        """Constructeur pour initialiser le bateau avec son nom, sa longueur et sa capacit� maximale."""
        if longueur < 0:
            raise ValueError("La longueur doit �tre positive.")
        if capacite_max < 0:
            raise ValueError("La capacit� maximale doit �tre positive.")

        self.nom = nom
        self.longueur = longueur
        self.capacite_max = capacite_max
        self.passagers_actuels = 0

    def ajouter_passagers(self, nombre: int) -> None:
        """Ajoute des passagers � bord, si la capacit� maximale le permet."""
        if nombre < 0:
            raise ValueError("Le nombre de passagers � ajouter doit �tre positif.")

        if self.passagers_actuels + nombre > self.capacite_max:
            message = "Impossible d'ajouter des passagers : d�passement de la capacit� maximale."
            print(message)
            return

        self.passagers_actuels += nombre
        message = f"{nombre} passagers ont �t� ajout�s. Passagers actuels : {self.passagers_actuels}."
        print(message)

    def retirer_passagers(self, nombre: int) -> None:
        """Retire des passagers du bateau, sans descendre en dessous de z�ro."""
        if nombre < 0:
            raise ValueError("Le nombre de passagers � retirer doit �tre positif.")

        if self.passagers_actuels - nombre < 0:
            message = "Impossible de retirer autant de passagers : pas assez de passagers � bord."
            print(message)
            return

        self.passagers_actuels -= nombre
        message = f"{nombre} passagers ont �t� retir�s. Passagers actuels : {self.passagers_actuels}."
        print(message)

    def afficher_informations(self) -> None:
        """Affiche les informations du bateau."""
        messages = [
            f"Nom du bateau : {self.nom}",
            f"Longueur du bateau : {self.longueur} m�tres",
            f"Capacit� maximale : {self.capacite_max} passagers",
            f"Passagers actuels : {self.passagers_actuels}"
        ]
        for msg in messages:
            print(msg)

    def naviguer(self) -> None:
        """Simule la navigation du bateau."""
        message = f"Le bateau {self.nom} est en train de naviguer."
        print(message)

    def reset_passagers(self) -> None:
        """R�initialise le nombre de passagers � z�ro."""
        self.passagers_actuels = 0
