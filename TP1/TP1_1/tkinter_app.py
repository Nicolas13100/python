# -*- coding: Latin-1 -*-

import math
import tkinter as tk
from tkinter import messagebox


class App:
    def __init__(self, master):
        self.master = master
        master.title("Calculateur de Nombres Pairs")

        # Center the window
        self.center_window(450, 400)  # width, height

        # Frame for user input
        self.frame = tk.Frame(master)
        self.frame.pack(pady=10)

        self.label = tk.Label(self.frame, text="Entrez un entier positif < 1000:")
        self.label.pack()

        self.entry = tk.Entry(self.frame)
        self.entry.pack()

        self.submit_button = tk.Button(self.frame, text="Soumettre", command=self.process_input)
        self.submit_button.pack(pady=5)

        self.result_text = tk.Text(master, height=10, width=50)
        self.result_text.pack(pady=10)

        self.restart_button = tk.Button(master, text="Recommencer", command=self.restart)
        self.restart_button.pack(pady=5)

        self.exit_button = tk.Button(master, text="Quitter", command=master.quit)
        self.exit_button.pack(pady=5)

    def center_window(self, width, height):
        """Centers the Tkinter window on the screen."""
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Calculate x, y coordinates
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Set the window size and position
        self.master.geometry(f"{width}x{height}+{x}+{y}")

    def process_input(self):
        user_input = self.entry.get()
        if user_input.lower() == 'exit':
            self.master.quit()

        try:
            N = int(user_input)
            if 0 < N < 1000:
                somme, produit, nombres_pairs = self.calculer_somme_et_produit_pairs(N)
                self.afficher_resultats(somme, produit, nombres_pairs)
            else:
                messagebox.showerror("Erreur", "L'entier doit être positif et inférieur à 1000.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre entier valide.")

    def calculer_somme_et_produit_pairs(self, N):
        """Calcule la somme et le produit des nombres pairs jusqu'à N."""
        somme = 0
        produit = 1
        nombres_pairs = []

        for i in range(2, N + 1, 2):
            somme += i
            nombres_pairs.append(i)

            try:
                produit = math.prod(nombres_pairs)  # Utilisation de math.prod pour gérer le produit
            except OverflowError:
                messagebox.showerror("Erreur", "Le produit des nombres pairs est trop grand pour être calculé.")
                produit = None
                break

        return somme, produit, nombres_pairs

    def afficher_resultats(self, somme, produit, nombres_pairs):
        """Affiche les résultats de la somme et du produit."""
        self.result_text.delete(1.0, tk.END)  # Clear previous results
        self.result_text.insert(tk.END, "--- Résultats ---\n")
        self.result_text.insert(tk.END, f"Somme des pairs: {' + '.join(map(str, nombres_pairs))} = {somme}\n")

        if produit is not None and nombres_pairs:  # To avoid multiplying an empty list
            self.result_text.insert(tk.END, f"Produit des pairs: {' * '.join(map(str, nombres_pairs))} = {produit}\n")
        else:
            self.result_text.insert(tk.END, "Aucun nombre pair pour le produit ou produit trop grand à calculer.\n")

        self.result_text.insert(tk.END, f"Nombre de nombres pairs: {len(nombres_pairs)}\n")

    def restart(self):
        """Reset the application state for new input."""
        self.entry.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
