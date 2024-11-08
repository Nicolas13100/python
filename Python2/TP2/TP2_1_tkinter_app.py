# -*- coding: Latin-1 -*-
import tkinter as tk
from tkinter import messagebox

def est_nombre_parfait(n):
    """Vérifie si un nombre est parfait et retourne la somme des diviseurs."""
    somme_diviseurs = 0
    diviseurs = []

    # Calculer la somme des diviseurs propres
    for i in range(1, n):
        if n % i == 0:
            somme_diviseurs += i
            diviseurs.append(i)

    return somme_diviseurs, diviseurs

class PerfectNumberApp:
    def __init__(self, master):
        self.master = master
        master.title("Vérificateur de Nombre Parfait")

        # Center the window
        self.center_window(400, 300)

        self.label = tk.Label(master, text="Entrez un nombre entier :")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(master, text="Vérifier", command=self.check_perfect_number)
        self.submit_button.pack(pady=10)

        self.result_text = tk.Text(master, height=10, width=50)
        self.result_text.pack(pady=10)

    def center_window(self, width, height):
        """Center the Tkinter window on the screen."""
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.master.geometry(f"{width}x{height}+{x}+{y}")

    def check_perfect_number(self):
        try:
            nombre = int(self.entry.get())
            somme_diviseurs, diviseurs = est_nombre_parfait(nombre)

            self.result_text.delete(1.0, tk.END)  # Clear previous results
            if somme_diviseurs == nombre:
                self.result_text.insert(tk.END, f"{nombre} est un nombre parfait.\n")
            else:
                self.result_text.insert(tk.END, f"{nombre} n'est pas un nombre parfait.\n")

            self.result_text.insert(tk.END, f"Les diviseurs propres de {nombre} sont : {diviseurs}\n")
            self.result_text.insert(tk.END, f"La somme des diviseurs propres est : {somme_diviseurs}\n")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre entier valide.")

def tp2_1_tkinter_app():
    root = tk.Tk()
    app = PerfectNumberApp(root)
    root.mainloop()