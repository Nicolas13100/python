# -*-coding:Latin-1 -*

import subprocess
import os

def main():
    """Display a menu and run the selected TP."""
    while True:
        print("Please select an option:")
        print("1. Run TP3_4 ")
        print("0. Exit")

        choice = input("Enter your choice (0-1): ")

        if choice == '1':
            run_tp_script("TP3_4")
        elif choice == '0':
            print("Exiting the menu.")
            break
        else:
            print("Invalid choice. Please try again.")


def run_tp_script(tp_folder):
    """Run the main.py of the selected TP task."""
    # Get the current script directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the main.py script in the selected TP folder
    script_path = os.path.join(current_dir, tp_folder, 'main.py')

    # Make sure the script exists before trying to run it
    if os.path.exists(script_path):
        try:
            # Run the script and check for errors
            subprocess.run(['python', script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: The script crashed with the following message:\n{e}")
            input("Press Enter to continue...")  # Pause for user input after crash
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            input("Press Enter to continue...")  # Pause for user input after unexpected error
    else:
        print(f"Error: {script_path} does not exist.")
        input("Press Enter to continue...")  # Pause for user input if the script doesn't exist


if __name__ == "__main__":
    main()
