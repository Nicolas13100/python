# -*-coding: Latin-1 -*

from TP1.TP1_1 import start as start1
from TP1.TP1_2 import start as start2
from TP1.TP1_3 import start as start3
from TP1.TP1_4 import start as start4
from TP1.TP1_5 import start as start5

def main():
    """Display a menu and run the selected TP."""
    while True:
        print("\nPlease select an option:")
        print("1. Run TP1_1 : Convertit la température entre Celsius et Fahrenheit")
        print("2. Run TP1_2 : La somme et le produit des nombres pairs")
        print("3. Run TP1_3 : Affiche un message d'accueil")
        print("4. Run TP1_4 : Un jeu de calcul mental")
        print("5. Run TP1_5 : Année bissextile")
        print("0. Return to main menu")

        choice = input("Enter your choice (0-5): ")

        if choice == '1':
            start1.start()
        elif choice == '2':
            start2.start()
        elif choice == '3':
            start3.start()
        elif choice == '4':
            start4.poser_question()
        elif choice == '5':
            start5.start()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
