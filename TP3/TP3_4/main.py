# -*-coding:Latin-1 -*

import unittest
from io import StringIO
from unittest import TestLoader, TextTestRunner
from unittest.mock import patch


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


class TestLivre(unittest.TestCase):

    def setUp(self):
        """Setup a Livre instance for testing."""
        self.livre = Livre("1984", "George Orwell")

    def test_initialization(self):
        """Test that the Livre class initializes correctly."""
        self.assertEqual(self.livre.titre, "1984")
        self.assertEqual(self.livre.auteur, "George Orwell")

    def test_str(self):
        """Test the string representation of the Livre class."""
        self.assertEqual(str(self.livre), '"1984" par George Orwell')

    def test_titre_change(self):
        """Test changing the title of the book."""
        self.livre.titre = "Animal Farm"
        self.assertEqual(self.livre.titre, "Animal Farm")
        self.assertEqual(str(self.livre), '"Animal Farm" par George Orwell')

    def test_auteur_change(self):
        """Test changing the author of the book."""
        self.livre.auteur = "Orwell"
        self.assertEqual(self.livre.auteur, "Orwell")
        self.assertEqual(str(self.livre), '"1984" par Orwell')

class TestBibliotheque(unittest.TestCase):

    def setUp(self):
        """Setup a Bibliotheque instance for testing."""
        self.bibliotheque = Bibliotheque()
        self.livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exup�ry")
        self.livre2 = Livre("1984", "George Orwell")

    def test_ajouter_livre(self):
        """Test adding a book to the library."""
        self.bibliotheque.ajouter_livre(self.livre1)
        self.assertIn(self.livre1, self.bibliotheque.livres)

    def test_retirer_livre(self):
        """Test removing a book from the library."""
        self.bibliotheque.ajouter_livre(self.livre1)
        self.bibliotheque.retirer_livre(self.livre1.titre)
        self.assertNotIn(self.livre1, self.bibliotheque.livres)

    def test_retirer_livre_non_existant(self):
        """Test removing a non-existing book from the library."""
        self.bibliotheque.ajouter_livre(self.livre1)
        original_count = len(self.bibliotheque.livres)
        self.bibliotheque.retirer_livre("Inconnu")
        self.assertEqual(len(self.bibliotheque.livres), original_count)

    def test_afficher_livres(self):
        """Test displaying books in the library."""
        self.bibliotheque.ajouter_livre(self.livre1)
        self.bibliotheque.ajouter_livre(self.livre2)

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.bibliotheque.afficher_livres()
            output = mock_stdout.getvalue()

        self.assertIn(str(self.livre1), output)
        self.assertIn(str(self.livre2), output)

    def test_afficher_livres_vide(self):
        """Test displaying books when library is empty."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.bibliotheque.afficher_livres()
            output = mock_stdout.getvalue()

        self.assertEqual(output.strip(), "La biblioth�que est vide.")

class TestBateau(unittest.TestCase):

    def setUp(self):
        """Setup a Bateau instance for testing."""
        self.bateau = Bateau("Titanic", 269.1, 2200)

    def test_ajouter_passagers(self):
        """Test adding passengers to the boat."""
        self.bateau.ajouter_passagers(10)
        self.assertEqual(self.bateau.passagers_actuels, 10)

        # Test adding passengers exceeding max capacity
        self.bateau.ajouter_passagers(2210)
        self.assertEqual(self.bateau.passagers_actuels, 10)  # Should still be 10

        # Test adding exactly max capacity
        self.bateau.ajouter_passagers(2190)
        self.assertEqual(self.bateau.passagers_actuels, 2200)  # Should be at max capacity

    def test_retirer_passagers(self):
        """Test removing passengers from the boat."""
        self.bateau.ajouter_passagers(50)
        self.bateau.retirer_passagers(20)
        self.assertEqual(self.bateau.passagers_actuels, 30)

        # Test removing more passengers than are currently on board
        self.bateau.retirer_passagers(50)
        self.assertEqual(self.bateau.passagers_actuels, 30)  # Should still be 30

        # Test removing all passengers
        self.bateau.retirer_passagers(30)
        self.assertEqual(self.bateau.passagers_actuels, 0)  # Should be 0 now

    def test_ajouter_passagers_negatif(self):
        """Test adding a negative number of passengers."""
        with self.assertRaises(ValueError) as context:
            self.bateau.ajouter_passagers(-5)
        self.assertEqual(str(context.exception), "Le nombre de passagers � ajouter doit �tre positif.")

    def test_retirer_passagers_negatif(self):
        """Test removing a negative number of passengers."""
        with self.assertRaises(ValueError) as context:
            self.bateau.retirer_passagers(-5)
        self.assertEqual(str(context.exception), "Le nombre de passagers � retirer doit �tre positif.")

    def test_retirer_passagers_aucun(self):
        """Test removing passengers when there are none on board."""
        self.bateau.retirer_passagers(10)  # No passengers to remove
        self.assertEqual(self.bateau.passagers_actuels, 0)  # Should still be 0

    def test_afficher_informations(self):
        """Test displaying boat information."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.bateau.afficher_informations()
            output = mock_stdout.getvalue()

        self.assertIn("Nom du bateau : Titanic", output)
        self.assertIn("Longueur du bateau : 269.1 m�tres", output)
        self.assertIn("Capacit� maximale : 2200 passagers", output)
        self.assertIn("Passagers actuels : 0", output)

    def test_naviguer(self):
        """Test navigating the boat."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.bateau.naviguer()
            output = mock_stdout.getvalue()

        self.assertIn("Le bateau Titanic est en train de naviguer.", output)

class TestPort(unittest.TestCase):

    def setUp(self):
        """Setup a Port instance for testing."""
        self.port = Port("Marseille")
        self.bateau1 = Bateau("Bateau1", 50, 100)
        self.bateau2 = Bateau("Bateau2", 75, 200)

    def test_ajouter_bateau(self):
        """Test adding a boat to the port."""
        self.port.ajouter_bateau(self.bateau1)
        self.assertIn(self.bateau1, self.port.bateaux)

    def test_retirer_bateau(self):
        """Test removing a boat from the port."""
        self.port.ajouter_bateau(self.bateau1)
        self.port.retirer_bateau(self.bateau1)
        self.assertNotIn(self.bateau1, self.port.bateaux)

    def test_retirer_bateau_non_present(self):
        """Test trying to remove a boat that is not in the port."""
        self.port.ajouter_bateau(self.bateau1)
        self.port.retirer_bateau(self.bateau2)  # This boat has not been added
        self.assertIn(self.bateau1, self.port.bateaux)  # Should still be present

    def test_afficher_bateaux(self):
        """Test displaying the boats in the port."""
        self.port.ajouter_bateau(self.bateau1)
        self.port.ajouter_bateau(self.bateau2)

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.port.afficher_bateaux()
            output = mock_stdout.getvalue()

        self.assertIn("Bateaux pr�sents dans le port Marseille :", output)
        self.assertIn("Nom du bateau : Bateau1", output)
        self.assertIn("Nom du bateau : Bateau2", output)

    def test_afficher_bateaux_vide(self):
        """Test displaying boats when the port is empty."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.port.afficher_bateaux()
            output = mock_stdout.getvalue()

        self.assertEqual(output.strip(), "Aucun bateau n'est pr�sent dans le port Marseille.")

    def test_faire_naviguer_tous_les_bateaux(self):
        """Test making all boats navigate."""
        self.port.ajouter_bateau(self.bateau1)
        self.port.ajouter_bateau(self.bateau2)

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.port.faire_naviguer_tous_les_bateaux()
            output = mock_stdout.getvalue()

        self.assertIn("Navigation de tous les bateaux dans le port Marseille :", output)
        self.assertIn("Le bateau Bateau1 est en train de naviguer.", output)
        self.assertIn("Le bateau Bateau2 est en train de naviguer.", output)

    def test_faire_naviguer_tous_les_bateaux_vide(self):
        """Test trying to navigate boats when none are present."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.port.faire_naviguer_tous_les_bateaux()
            output = mock_stdout.getvalue()

        self.assertEqual(output.strip(), "Aucun bateau � faire naviguer dans le port Marseille.")

def menu():
    """Display a menu for test selection."""
    print("Choisissez le test � ex�cuter :")
    print("1. Test du Livre")
    print("2. Test de la Biblioth�que")
    print("3. Test du Bateau")
    print("4. Test du Port")
    print("5. Ex�cuter tous les tests")
    print("0 Quitter")

def main():
    while True:
        menu()
        choice = input("Entrez votre choix (1-5) : ")

        if choice == '1':
            # Run TestLivre
            suite = TestLoader().loadTestsFromTestCase(TestLivre)
            TextTestRunner(verbosity=2).run(suite)
        elif choice == '2':
            # Run TestBibliotheque
            suite = TestLoader().loadTestsFromTestCase(TestBibliotheque)
            TextTestRunner(verbosity=2).run(suite)

        elif choice == '3':
            # Run TestBateau
            suite = TestLoader().loadTestsFromTestCase(TestBateau)
            TextTestRunner(verbosity=2).run(suite)

        elif choice == '4':
            # Run TestPort
            suite = TestLoader().loadTestsFromTestCase(TestPort)
            TextTestRunner(verbosity=2).run(suite)

        elif choice == '5':
            # Run all tests
            suite = unittest.TestSuite()
            loader = unittest.TestLoader()
            suite.addTests(loader.loadTestsFromTestCase(TestLivre))
            suite.addTests(loader.loadTestsFromTestCase(TestBibliotheque))
            suite.addTests(loader.loadTestsFromTestCase(TestBateau))
            suite.addTests(loader.loadTestsFromTestCase(TestPort))
            TextTestRunner(verbosity=2).run(suite)

        elif choice == '0':
            print("Fin des tests.")
            break

        else:
            print("Choix invalide. Veuillez r�essayer.")

if __name__ == "__main__":
    main()
