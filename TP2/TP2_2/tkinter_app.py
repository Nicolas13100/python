# -*- coding: Latin-1 -*-
import tkinter as tk
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt

def lire_notes_depuis_fichier(nom_fichier):
    """Lit les notes depuis un fichier et les retourne sous forme de liste."""
    try:
        with open(nom_fichier, 'r') as fichier:
            contenu = fichier.read()
            notes = list(map(float, contenu.split()))
            return notes
    except FileNotFoundError:
        messagebox.showerror("Erreur", "Le fichier spécifié n'a pas été trouvé.")
        return []
    except ValueError:
        messagebox.showerror("Erreur", "Erreur dans le format des notes dans le fichier.")
        return []

def entrer_notes(notes_input):
    """Convertit les entrées utilisateur en notes."""
    try:
        return list(map(float, notes_input.split()))
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des notes valides.")
        return []

def calculer_moyenne(notes):
    """Calcule la moyenne des notes."""
    return sum(notes) / len(notes) if notes else 0

def calculer_mediane(notes):
    """Calcule la médiane des notes."""
    notes_triees = sorted(notes)
    n = len(notes_triees)
    if n == 0:
        return 0
    elif n % 2 == 1:
        return notes_triees[n // 2]
    else:
        return (notes_triees[n // 2 - 1] + notes_triees[n // 2]) / 2

def afficher_histogramme(notes):
    """Affiche un histogramme des notes."""
    plt.figure(figsize=(10, 6))
    plt.hist(notes, bins=10, alpha=0.7, color='blue', edgecolor='black')
    plt.title('Histogramme des Notes des Étudiants')
    plt.xlabel('Notes')
    plt.ylabel('Nombre d\'Étudiants')
    plt.axvline(calculer_moyenne(notes), color='red', linestyle='dashed', linewidth=1, label='Moyenne')
    plt.axvline(calculer_mediane(notes), color='green', linestyle='dashed', linewidth=1, label='Médiane')
    plt.legend()
    plt.grid(axis='y', alpha=0.75)
    plt.show()

def afficher_boite_a_moustaches(notes):
    """Affiche une boîte à moustaches des notes."""
    plt.figure(figsize=(8, 5))
    plt.boxplot(notes, vert=False)
    plt.title('Boîte à Moustaches des Notes des Étudiants')
    plt.xlabel('Notes')
    plt.grid(axis='x', alpha=0.75)
    plt.show()

class GradeAnalysisApp:
    def __init__(self, master):
        self.master = master
        master.title("Analyse des Notes des Étudiants")

        # Center the window
        self.center_window(600, 400)

        self.label = tk.Label(master, text="Entrez les notes des étudiants (séparées par des espaces) :")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, width=50)
        self.entry.pack(pady=5)

        self.file_button = tk.Button(master, text="Charger les notes depuis un fichier", command=self.charger_fichier)
        self.file_button.pack(pady=5)

        self.submit_button = tk.Button(master, text="Calculer", command=self.calculer_notes)
        self.submit_button.pack(pady=10)

        self.result_text = tk.Text(master, height=10, width=70)
        self.result_text.pack(pady=10)

        self.exit_button = tk.Button(master, text="Quitter", command=master.quit)
        self.exit_button.pack(pady=5)

    def center_window(self, width, height):
        """Center the Tkinter window on the screen."""
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.master.geometry(f"{width}x{height}+{x}+{y}")

    def charger_fichier(self):
        """Permet à l'utilisateur de charger un fichier contenant des notes."""
        nom_fichier = filedialog.askopenfilename(title="Choisir un fichier de notes", filetypes=[("Text Files", "*.txt")])
        if nom_fichier:
            notes = lire_notes_depuis_fichier(nom_fichier)
            if notes:
                self.afficher_resultats(notes)

    def calculer_notes(self):
        """Calcule les notes à partir de l'entrée utilisateur."""
        notes_input = self.entry.get()
        if notes_input:
            notes = entrer_notes(notes_input)
            if notes:
                self.afficher_resultats(notes)
        else:
            messagebox.showerror("Erreur", "Veuillez entrer des notes ou charger un fichier.")

    def afficher_resultats(self, notes):
        """Affiche les résultats de la moyenne et de la médiane."""
        moyenne = calculer_moyenne(notes)
        mediane = calculer_mediane(notes)

        self.result_text.delete(1.0, tk.END)  # Clear previous results
        self.result_text.insert(tk.END, f"La moyenne des notes est : {moyenne:.2f}\n")
        self.result_text.insert(tk.END, f"La médiane des notes est : {mediane:.2f}\n")

        afficher_histogramme(notes)
        afficher_boite_a_moustaches(notes)

if __name__ == "__main__":
    root = tk.Tk()
    app = GradeAnalysisApp(root)
    root.mainloop()
