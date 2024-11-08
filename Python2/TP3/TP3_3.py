# -*-coding:Latin-1 -*

class Port:
    def __init__(self, nom):
        """Constructeur pour initialiser le port avec son nom et une liste vide de bateaux."""
        self.nom = nom  # Nom du port
        self.bateaux = []  # Liste vide pour stocker les bateaux pr�sents dans le port

    def ajouter_bateau(self, bateau):
        """Ajoute un bateau � la liste des bateaux du port."""
        self.bateaux.append(bateau)
        print(f'Bateau {bateau.nom} ajout� au port {self.nom}.')

    def retirer_bateau(self, bateau):
        """Retire un bateau de la liste des bateaux du port."""
        if bateau in self.bateaux:
            self.bateaux.remove(bateau)
            print(f'Bateau {bateau.nom} retir� du port {self.nom}.')
        else:
            print(f'Le bateau {bateau.nom} n\'est pas pr�sent dans le port {self.nom}.')

    def afficher_bateaux(self):
        """Affiche les informations de tous les bateaux pr�sents dans le port."""
        if not self.bateaux:
            print(f"Aucun bateau n'est pr�sent dans le port {self.nom}.")
            return
        print(f"Bateaux pr�sents dans le port {self.nom} :")
        for bateau in self.bateaux:
            bateau.afficher_informations()

    def faire_naviguer_tous_les_bateaux(self):
        """Fait naviguer tous les bateaux du port."""
        if not self.bateaux:
            print(f"Aucun bateau � faire naviguer dans le port {self.nom}.")
            return
        print(f"Navigation de tous les bateaux dans le port {self.nom} :")
        for bateau in self.bateaux:
            bateau.naviguer()
