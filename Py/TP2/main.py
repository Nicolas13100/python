# -*-coding:Latin-1 -*

from TP2_1 import main as tp2_1
from TP2_2 import main as tp2_2
from TP2_3 import main as tp2_3
from TP2_4 import main as tp2_4
from TP2_5 import main as tp2_5


def main():
    """Display a menu and run the selected TP."""
    while True:
        print("Please select an option:")
        print("1. Run TP2_1 : Nombre parfait")
        print("2. Run TP2_2 : Calcul de la moyenne et de la médiane")
        print("3. Run TP2_3 : Calcul de la variance et de l'écart-type")
        print("4. Run TP2_4 : Analyse de données d'âge")
        print("5. Run TP2_5 : Simulation de lancers de dés")
        print("0. Exit")

        choice = input("Enter your choice (0-5): ")

        if choice == '1':
            tp2_1.main()
        elif choice == '2':
            tp2_2.main()
        elif choice == '3':
            tp2_3.main()
        elif choice == '4':
            tp2_4.main()
        elif choice == '5':
            tp2_5.main()
        elif choice == '0':
            print("Exiting the menu.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
