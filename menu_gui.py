# -*-coding: Latin-1 -*

import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os


def run_script(script_name):
    """Function to run an external Python script."""
    try:
        # Construct the full path to the script
        script_path = os.path.join(os.getcwd(), script_name)
        # Run the script using subprocess
        subprocess.run(["python", script_path], check=True)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run script: {str(e)}")

def button_click(tab_name, button_number):
    # Define the mapping between buttons and their corresponding scripts
    scripts = {
        "TP1": [
            "TP1/TP1_1/tkinter_app.py",
            "TP1/TP1_2/tkinter_app.py",
            "TP1/TP1_3/tkinter_app.py",
            "TP1/TP1_4/tkinter_app.py",
            "TP1/TP1_5/tkinter_app.py"
        ],
        "TP2": [
            "TP2/TP2_1/tkinter_app.py",
            "TP2/TP2_2/tkinter_app.py",
            "TP2/TP2_3/tkinter_app.py",
            "TP2/TP2_4/tkinter_app.py",
            "TP2/TP2_5/tkinter_app.py"
        ],
        "TP3": [
            "TP3/TP3_4/tkinter_app.py",  # Only one script for TP3
        ],
    }

    script_name = scripts[tab_name][button_number - 1]  # Get the script name based on tab and button number
    run_script(script_name)  # Call the function to run the script

# Create the main window
root = tk.Tk()
root.title("Tabbed Menu Example")

# Set the size of the window (width x height)
window_width = 400
window_height = 300
root.geometry(f"{window_width}x{window_height}")

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to position the window in the center
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the geometry to include position
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a tab control
tab_control = ttk.Notebook(root)

# Create tabs
tabs = ["TP1", "TP2", "TP3"]
for tab in tabs:
    frame = ttk.Frame(tab_control)
    tab_control.add(frame, text=tab)

    # Create buttons in each tab
    if tab == "TP3":
        # Only one button for TP3
        button_name = f"{tab}_4"  # Name format: TP3_1
        button = ttk.Button(frame, text=button_name, command=lambda t=tab, b=1: button_click(t, b))
        button.pack(pady=10)
    else:
        # Create five buttons for TP1 and TP2
        for i in range(1, 6):
            button_name = f"{tab}_{i}"  # Name format: TP1_1, TP1_2, etc.
            button = ttk.Button(frame, text=button_name, command=lambda t=tab, b=i: button_click(t, b))
            button.pack(pady=10)

# Pack the tab control
tab_control.pack(expand=1, fill="both")

# Run the application
root.mainloop()
