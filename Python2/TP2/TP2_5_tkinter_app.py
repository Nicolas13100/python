# -*-coding: Latin-1 -*

import random
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


def simuler_lancers_de(n, nombre_de_dés):
    # Dictionnaire pour stocker les fréquences des faces du dé
    frequences = {i: 0 for i in range(1, 7)}  # Faces du dé (1 à 6)

    # Effectuer les lancers de dés
    for _ in range(n):
        for _ in range(nombre_de_dés):
            lancer = random.randint(1, 6)  # Lancer un dé à six faces
            frequences[lancer] += 1  # Augmenter la fréquence de la face obtenue

    return frequences


def afficher_resultats(frequences, total_lancers):
    # Création du graphique
    faces = list(frequences.keys())
    valeurs = list(frequences.values())

    plt.bar(faces, valeurs, color='skyblue')
    plt.xlabel('Faces du dé')
    plt.ylabel('Fréquence')
    plt.title(f'Fréquence d\'apparition des faces du dé après {total_lancers} lancers')
    plt.xticks(faces)  # Pour afficher toutes les faces sur l'axe x
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Ajouter les pourcentages sous chaque barre
    for i, frequence in enumerate(valeurs):
        pourcentage = (frequence / total_lancers) * 100
        plt.text(faces[i], frequence + 1, f"{pourcentage:.2f}%", ha='center')  # Positionnement du texte

    plt.show()  # Affiche le graphique

    # Mettre à jour les pourcentages dans le GUI
    afficher_pourcentages(frequences, total_lancers)


def afficher_pourcentages(frequences, total_lancers):
    # Effacer le contenu précédent
    text_area.delete(1.0, tk.END)

    # Afficher les pourcentages dans le GUI
    for face in range(1, 7):
        frequence = frequences[face]
        pourcentage = (frequence / total_lancers) * 100
        text_area.insert(tk.END, f"Face {face}: {frequence} fois ({pourcentage:.2f}%)\n")


def lancer_de():
    # Nombre maximum de lancers pour éviter les crashs
    MAX_LANCERS = 100000

    try:
        total_lancers = int(entry_lancers.get())
        if total_lancers < 1 or total_lancers > MAX_LANCERS:
            messagebox.showerror("Erreur", f"Veuillez entrer un nombre entre 1 et {MAX_LANCERS}.")
            return
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")
        return

    # Simuler les lancers de dés
    frequences = simuler_lancers_de(total_lancers, 1)

    # Afficher les résultats
    afficher_resultats(frequences, total_lancers)

def tp2_5_tkinter_app():
    root = tk.Tk()
    root.title("Simulation de Lancers de Dés")

    # Center the window on the screen
    window_width = 400
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create label and entry for user input
    tk.Label(root, text="Entrez le nombre de lancers (max 100000) :").pack(pady=10)

    global entry_lancers
    entry_lancers = tk.Entry(root, width=10)
    entry_lancers.pack(pady=5)

    # Create button to start simulation
    tk.Button(root, text="Lancer les dés", command=lancer_de).pack(pady=10)

    # Create a text area to display results
    global text_area
    text_area = tk.Text(root, height=10, width=40)
    text_area.pack(pady=10)

    root.mainloop()
