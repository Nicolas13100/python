# -*-coding: Latin-1 -*

import TP1
import TP2
import TP3

def main():
    """Display a main menu and run the selected TP."""
    while True:
        print("Please select an option:")
        print("1. Run TP1")
        print("2. Run TP2")
        print("3. Run TP3")
        print("0. Exit")

        choice = input("Enter your choice (0-3): ")

        if choice == '1':

        elif choice == '2':

        elif choice == '3':

        elif choice == '0':
            print("Exiting the menu.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
