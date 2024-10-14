# -*-coding:Latin-1 -*

from TP3_4 import main as tp3_4


def main():
    """Display a menu and run the selected TP."""
    while True:
        print("Please select an option:")
        print("1. Run TP3_4 ")
        print("0. Exit")

        choice = input("Enter your choice (0-1): ")

        if choice == '1':
            tp3_4.main()
        elif choice == '0':
            print("Exiting the menu.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
