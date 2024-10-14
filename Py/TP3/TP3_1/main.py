# -*-coding:Latin-1 -*

class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def __str__(self):
        return f'"{self.titre}" par {self.auteur}'


class Bibliotheque:
    def __init__(self):
        self.livres = []  # Liste vide pour stocker les livres

    def ajouter_livre(self, livre):
        """Ajoute un livre à la bibliothèque."""
        self.livres.append(livre)
        print(f'Livre ajouté : {livre}')

    def retirer_livre(self, titre):
        """Retire un livre de la bibliothèque par son titre."""
        for livre in self.livres:
            if livre.titre == titre:
                self.livres.remove(livre)
                print(f'Livre retiré : {livre}')
                return
        print(f'Livre avec le titre "{titre}" non trouvé.')

    def afficher_livres(self):
        """Affiche tous les livres présents dans la bibliothèque."""
        if not self.livres:
            print("La bibliothèque est vide.")
            return
        print("Livres dans la bibliothèque :")
        for livre in self.livres:
            print(livre)

