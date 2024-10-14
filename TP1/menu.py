# -*-coding: Latin-1 -*

import subprocess
import os

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
            run_tp_script("TP1_1")
        elif choice == '2':
            run_tp_script("TP1_2")
        elif choice == '3':
            run_tp_script("TP1_3")
        elif choice == '4':
            run_tp_script("TP1_4")
        elif choice == '5':
            run_tp_script("TP1_5")
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

def run_tp_script(tp_folder):
    """Run the start.py of the selected TP1 task."""
    # Get the current script directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the start.py script in the selected TP folder
    script_path = os.path.join(current_dir, tp_folder, 'start.py')

    # Make sure the script exists before trying to run it
    if os.path.exists(script_path):
        subprocess.run(['python', script_path], check=True)
    else:
        print(f"Error: {script_path} does not exist.")

if __name__ == "__main__":
    main()
