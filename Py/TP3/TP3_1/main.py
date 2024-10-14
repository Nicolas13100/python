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
        """Ajoute un livre � la biblioth�que."""
        self.livres.append(livre)
        print(f'Livre ajout� : {livre}')

    def retirer_livre(self, titre):
        """Retire un livre de la biblioth�que par son titre."""
        for livre in self.livres:
            if livre.titre == titre:
                self.livres.remove(livre)
                print(f'Livre retir� : {livre}')
                return
        print(f'Livre avec le titre "{titre}" non trouv�.')

    def afficher_livres(self):
        """Affiche tous les livres pr�sents dans la biblioth�que."""
        if not self.livres:
            print("La biblioth�que est vide.")
            return
        print("Livres dans la biblioth�que :")
        for livre in self.livres:
            print(livre)

