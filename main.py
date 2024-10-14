# -*-coding: Latin-1 -*

import subprocess
import os


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
            run_tp_menu("TP1")
        elif choice == '2':
            run_tp_menu("TP2")
        elif choice == '3':
            run_tp_menu("TP3")
        elif choice == '0':
            print("Exiting the menu.")
            break
        else:
            print("Invalid choice. Please try again.")


def run_tp_menu(tp_folder):
    """Run the menu.py of the selected TP."""
    # Get the current script directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the TP's menu.py
    script_path = os.path.join(current_dir, tp_folder, 'menu.py')

    # Make sure the script exists before trying to run it
    if os.path.exists(script_path):
        subprocess.run(['python', script_path], check=True)
    else:
        print(f"Error: {script_path} does not exist.")


if __name__ == "__main__":
    main()
