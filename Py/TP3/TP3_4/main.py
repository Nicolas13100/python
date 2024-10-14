# -*-coding:Latin-1 -*

import unittest
from io import StringIO
from unittest import TestLoader, TextTestRunner
from unittest.mock import patch

from TP3.TP3_1.main import Bibliotheque
# Importing classes from other modules
from TP3.TP3_1.main import Livre
from TP3.TP3_2.main import Bateau
from TP3.TP3_3.main import Port


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
        self.livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
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

        self.assertEqual(output.strip(), "La bibliothèque est vide.")

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
        self.assertEqual(str(context.exception), "Le nombre de passagers à ajouter doit être positif.")

    def test_retirer_passagers_negatif(self):
        """Test removing a negative number of passengers."""
        with self.assertRaises(ValueError) as context:
            self.bateau.retirer_passagers(-5)
        self.assertEqual(str(context.exception), "Le nombre de passagers à retirer doit être positif.")

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
        self.assertIn("Longueur du bateau : 269.1 mètres", output)
        self.assertIn("Capacité maximale : 2200 passagers", output)
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

        self.assertIn("Bateaux présents dans le port Marseille :", output)
        self.assertIn("Nom du bateau : Bateau1", output)
        self.assertIn("Nom du bateau : Bateau2", output)

    def test_afficher_bateaux_vide(self):
        """Test displaying boats when the port is empty."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.port.afficher_bateaux()
            output = mock_stdout.getvalue()

        self.assertEqual(output.strip(), "Aucun bateau n'est présent dans le port Marseille.")

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

        self.assertEqual(output.strip(), "Aucun bateau à faire naviguer dans le port Marseille.")

def menu():
    """Display a menu for test selection."""
    print("Choisissez le test à exécuter :")
    print("1. Test du Livre")
    print("2. Test de la Bibliothèque")
    print("3. Test du Bateau")
    print("4. Test du Port")
    print("5. Exécuter tous les tests")
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
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
