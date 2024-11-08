# -*- coding: Latin-1 -*-
import tkinter as tk
from tkinter import messagebox

def est_bissextile(annee):
    """
    V�rifie si une ann�e est bissextile.
    :param annee: L'ann�e � v�rifier
    :return: True si l'ann�e est bissextile, sinon False
    """
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def dernier_bissextile(annee):
    """Retourne l'ann�e bissextile pr�c�dente � l'ann�e donn�e."""
    while not est_bissextile(annee):
        annee -= 1
    return annee

def prochain_bissextile(annee):
    """Retourne l'ann�e bissextile suivante � l'ann�e donn�e."""
    while not est_bissextile(annee):
        annee += 1
    return annee

class LeapYearApp:
    def __init__(self, master):
        self.master = master
        master.title("V�rificateur d'Ann�e Bissextile")

        # Center the window
        self.center_window(300, 210)

        self.label = tk.Label(master, text="Veuillez entrer une ann�e (nombre entier) :")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(master, text="V�rifier", command=self.check_year)
        self.submit_button.pack(pady=10)

        self.result_text = tk.Text(master, height=5, width=40)
        self.result_text.pack(pady=10)


    def center_window(self, width, height):
        """Centers the Tkinter window on the screen."""
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.master.geometry(f"{width}x{height}+{x}+{y}")

    def check_year(self):
        try:
            annee = int(self.entry.get())
            if est_bissextile(annee):
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, f"L'ann�e {annee} est bissextile.\n")
            else:
                dernier = dernier_bissextile(annee)
                prochain = prochain_bissextile(annee)
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, f"L'ann�e {annee} n'est pas bissextile.\n")
                self.result_text.insert(tk.END, f"La derni�re ann�e bissextile �tait {dernier}.\n")
                self.result_text.insert(tk.END, f"La prochaine ann�e bissextile sera {prochain}.\n")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre entier valide.")


def tp1_5_tkinter_app():
    root = tk.Tk()
    app = LeapYearApp(root)
    root.mainloop()