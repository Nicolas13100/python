# -*-coding:Latin-1 -*

import tkinter as tk
from tkinter import messagebox


def calculate_even_numbers(entry):
    """Calculate sum and product of even numbers up to the entered value."""
    try:
        # Get the user input
        N = int(entry.get())

        # Check if the input is valid
        if N < 0 or N >= 1000:
            messagebox.showerror("Input Error", "Veuillez entrer un entier positif inférieur à 1000.")
            return

        somme = 0
        produit = 1
        nombres_pairs = []

        # Calculate the sum and product of even numbers
        for i in range(2, N + 1, 2):
            somme += i
            produit *= i
            nombres_pairs.append(i)

        # Display the results
        sum_result = f"Somme: {' + '.join(map(str, nombres_pairs))} = {somme}"
        product_result = f"Produit: {' * '.join(map(str, nombres_pairs))} = {produit}"

        # Show the results in a message box
        messagebox.showinfo("Results", f"{sum_result}\n{product_result}")

    except ValueError:
        messagebox.showerror("Input Error", "Veuillez entrer un nombre entier valide.")


def restart(entry):
    """Clear the input field."""
    entry.delete(0, tk.END)


def tp1_2_tkinter_app():
    # Create the main window
    root = tk.Tk()
    root.title("Sum and Product of Even Numbers")

    # Set window size (width x height)
    window_width = 400
    window_height = 200

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate x and y coordinates to center the window
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Set the geometry of the window
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create a label
    label = tk.Label(root, text="Entrez un entier positif inférieur à 1000:")
    label.pack(pady=10)

    # Create an entry widget
    entry = tk.Entry(root)
    entry.pack(pady=10)

    # Create a button to calculate
    calculate_button = tk.Button(root, text="Calculer", command=lambda: calculate_even_numbers(entry))
    calculate_button.pack(pady=10)

    # Create a button to restart
    restart_button = tk.Button(root, text="Recommencer", command=lambda: restart(entry))
    restart_button.pack(pady=10)

    root.mainloop()

