# -*-coding: Latin-1 -*

import random
import re
import tkinter as tk
from tkinter import messagebox, filedialog

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Global variable for random_entry
random_entry = None
manual_entry = None

def analyze_ages(ages):
    # Calculate the median
    median_age = np.median(ages)
    print(f"Médiane des âges : {median_age}")

    # Grouping ages and calculating frequencies
    bins = [0, 18, 30, 50, 100]
    labels = ['0-18', '19-30', '31-50', '51+']
    age_groups = pd.cut(ages, bins=bins, labels=labels, right=False)
    age_group_counts = age_groups.value_counts().sort_index()
    print("\nFréquence des groupes d'âge :")
    print(age_group_counts)

    # Calculate the weighted average
    weights = {'0-18': 1, '19-30': 2, '31-50': 3, '51+': 4}
    weighted_average = np.average(
        [age_group_counts[label] for label in labels],
        weights=[weights[label] for label in labels]
    )
    print(f"\nMoyenne pondérée des groupes d'âge : {weighted_average:.2f}")

    # Plotting
    plt.figure(figsize=(10, 6))
    bars = plt.bar(age_group_counts.index, age_group_counts.values, color='skyblue', alpha=0.7)
    plt.axhline(y=median_age, color='r', linestyle='--', label=f'Médiane d\'âge : {median_age}')

    # Adding annotations
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')

    plt.title('Distribution des âges par groupes')
    plt.xlabel('Groupes d\'âge')
    plt.ylabel('Fréquence')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def read_ages_from_file(filename):
    try:
        with open(filename, 'r') as file:
            ages = list(map(int, file.read().strip().split(',')))
        return ages
    except FileNotFoundError:
        messagebox.showerror("Erreur", f"Le fichier '{filename}' n'a pas été trouvé.")
        return None
    except ValueError:
        messagebox.showerror("Erreur", "Le fichier contient des données non valides.")
        return None


def generate_random_ages(count):
    return [random.randint(0, 100) for _ in range(count)]


def on_file_select():
    filename = filedialog.askopenfilename(title="Choisissez un fichier", filetypes=[("Text files", "*.txt")])
    if filename:
        ages = read_ages_from_file(filename)
        if ages:
            analyze_ages(ages)


def on_manual_entry():
    user_input = manual_entry.get()
    try:
        # Use regex to split by commas or whitespace
        ages = list(map(int, re.split(r'[,\s]+', user_input.strip())))
        analyze_ages(ages)
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer une liste d'âges valide.")


def on_random_generation():
    try:
        count = int(random_entry.get())
        if count <= 0:
            raise ValueError
        ages = generate_random_ages(count)
        analyze_ages(ages)
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")


def create_gui():
    global random_entry, manual_entry  # Declare as global

    root = tk.Tk()
    root.title("Analyse des âges")

    # Center the window on the screen
    window_width = 400
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create buttons and entry fields
    tk.Label(root, text="Choisissez une méthode d'entrée des âges :").pack(pady=10)

    tk.Button(root, text="Lire les âges d'un fichier", command=on_file_select).pack(pady=5)

    tk.Label(root, text="Ou entrez des âges manuellement :").pack(pady=10)
    manual_entry = tk.Entry(root, width=30)  # Initialize global variable
    manual_entry.pack(pady=5)
    tk.Button(root, text="Analyser", command=on_manual_entry).pack(pady=5)

    tk.Label(root, text="Ou générez des âges aléatoires :").pack(pady=10)
    random_entry = tk.Entry(root, width=10)  # Initialize global variable
    random_entry.pack(pady=5)
    tk.Button(root, text="Générer", command=on_random_generation).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
