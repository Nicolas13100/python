# -*-coding: Latin-1 -*

import subprocess
import os

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
            run_tp_script("TP2_1")
        elif choice == '2':
            run_tp_script("TP2_2")
        elif choice == '3':
            run_tp_script("TP2_3")
        elif choice == '4':
            run_tp_script("TP2_4")
        elif choice == '5':
            run_tp_script("TP2_5")
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
