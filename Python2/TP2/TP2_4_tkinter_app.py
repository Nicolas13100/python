# -*-coding: Latin-1 -*

import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plotly.graph_objects import Bar, Figure
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog, ttk

# Preset weights for different contexts
weight_presets = {
    "1": {"0-18": 1, "19-30": 2, "31-50": 3, "51-70": 4, "71-90": 5, "91+": 6},  # Incremental weights
    "2": {"0-18": 3, "19-30": 4, "31-50": 3, "51-70": 5, "71-90": 6, "91+": 7},  # Emphasizing youth
    "3": {"0-18": 1, "19-30": 1, "31-50": 2, "51-70": 3, "71-90": 4, "91+": 5},  # Equal emphasis on younger groups
    "4": {"0-18": 2, "19-30": 3, "31-50": 4, "51-70": 5, "71-90": 6, "91+": 8},  # Higher weight for elderly
}


# Data Validation
def validate_ages(ages):
    valid_ages = [age for age in ages if 0 <= age <= 120]
    if len(valid_ages) != len(ages):
        print("Certain ages were out of the valid range (0-120) and have been excluded.")
    return valid_ages


# Analyze Ages Function with Additional Statistics
def analyze_ages(ages, weights=None):
    ages = validate_ages(ages)
    if not ages:
        messagebox.showinfo("Info", "No valid ages to analyze.")
        return

    # Calculate statistics
    median_age = np.median(ages)
    mean_age = np.mean(ages)
    mode_age = pd.Series(ages).mode()[0]
    std_dev_age = np.std(ages)

    result = f"\nStatistiques des âges :\n- Médiane : {median_age}\n- Moyenne : {mean_age:.2f}\n- Mode : {mode_age}\n- Écart-type : {std_dev_age:.2f}\n"

    # Group ages and calculate frequencies
    bins = [0, 18, 30, 50, 70, 90, 120]  # Extended age bins
    labels = ['0-18', '19-30', '31-50', '51-70', '71-90', '91+']
    age_groups = pd.cut(ages, bins=bins, labels=labels, right=False)
    age_group_counts = age_groups.value_counts().sort_index()

    result += "\nFréquence des groupes d'âge :\n" + str(age_group_counts)

    # Use provided weights or fallback to default if none are provided
    if weights is None:
        weights = {'0-18': 1, '19-30': 2, '31-50': 3, '51-70': 4, '71-90': 5, '91+': 6}

    weighted_average = np.average(
        [age_group_counts[label] for label in labels],
        weights=[weights[label] for label in labels]
    )
    result += f"\nMoyenne pondérée des groupes d'âge : {weighted_average:.2f}"

    # Save Analysis to File
    save_analysis_to_file("age_analysis_results.txt", age_group_counts, median_age, mean_age, mode_age, std_dev_age)
    result += "\nLes résultats de l'analyse ont été enregistrés dans 'age_analysis_results.txt'."

    messagebox.showinfo("Results", result)

    # Plotting
    plot_age_distribution(age_group_counts, median_age)
    plot_histogram(ages)


# Function to Save Analysis to a File
def save_analysis_to_file(filename, age_group_counts, median_age, mean_age, mode_age, std_dev_age):
    with open(filename, 'w') as f:
        f.write("Statistiques d'analyse des âges\n")
        f.write(f"Médiane : {median_age}\n")
        f.write(f"Moyenne : {mean_age}\n")
        f.write(f"Mode : {mode_age}\n")
        f.write(f"Écart-type : {std_dev_age}\n")
        f.write("\nFréquence des groupes d'âge:\n")
        f.write(age_group_counts.to_string())


# Plotting Interactive Age Distribution with Plotly
def plot_age_distribution(age_group_counts, median_age):
    fig = Figure(data=[Bar(x=age_group_counts.index, y=age_group_counts.values, marker=dict(color='skyblue'))])
    fig.add_hline(y=median_age, line=dict(color="red", dash="dash"), annotation_text=f"Médiane d'âge : {median_age}")
    fig.update_layout(title="Distribution des âges par groupes", xaxis_title="Groupes d'âge", yaxis_title="Fréquence")
    fig.show()


# Histogram Plot for Detailed Age Distribution
def plot_histogram(ages):
    plt.figure(figsize=(10, 6))
    plt.hist(ages, bins=20, color='skyblue', alpha=0.7)
    plt.axvline(x=np.median(ages), color='r', linestyle='--', label=f"Médiane d'âge : {np.median(ages)}")
    plt.title("Histogramme des âges")
    plt.xlabel("Âge")
    plt.ylabel("Fréquence")
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


# File Reading Function
def read_ages_from_file(filename):
    try:
        with open(filename, 'r') as file:
            ages = list(map(int, file.read().strip().split(',')))
        return ages
    except FileNotFoundError:
        messagebox.showerror("Error", f"Le fichier '{filename}' n'a pas été trouvé.")
        return None
    except ValueError:
        messagebox.showerror("Error", "Le fichier contient des données non valides.")
        return None


# Random Age Generation
def generate_random_ages(count):
    return [random.randint(0, 120) for _ in range(count)]  # Adjusted to include 0-120


# Tkinter GUI
class AgeAnalyzerApp:
    def __init__(self, master):
        self.master = master
        master.title("Analyseur d'âges")

        # Frame for better layout
        self.frame = ttk.Frame(master, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Label
        self.label = ttk.Label(self.frame, text="Choisissez une méthode d'entrée des âges :", font=('Arial', 14))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        # Buttons with styling
        self.load_button = ttk.Button(self.frame, text="Charger des âges depuis un fichier",
                                      command=self.load_from_file)
        self.load_button.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W + tk.E)

        self.input_button = ttk.Button(self.frame, text="Saisir des âges manuellement", command=self.input_ages)
        self.input_button.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W + tk.E)

        self.random_button = ttk.Button(self.frame, text="Générer des âges aléatoires",
                                        command=self.generate_random_ages)
        self.random_button.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W + tk.E)

        self.weight_button = ttk.Button(self.frame, text="Choisir un ensemble de poids", command=self.choose_weights)
        self.weight_button.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W + tk.E)

        self.selected_weights = None

    def load_from_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filename:
            ages = read_ages_from_file(filename)
            if ages is not None:
                self.analyze_ages(ages)

    def input_ages(self):
        user_input = simpledialog.askstring("Input",
                                            "Entrez une liste d'âges séparés par des virgules (ex. 15,22,34,45):")
        if user_input:
            try:
                ages = list(map(int, user_input.split(',')))
                self.analyze_ages(ages)
            except ValueError:
                messagebox.showerror("Error",
                                     "Entrée invalide. Assurez-vous que les âges sont des nombres entiers séparés par des virgules.")

    def generate_random_ages(self):
        count_str = simpledialog.askstring("Input", "Combien d'âges aléatoires souhaitez-vous générer?")
        if count_str:
            try:
                count = int(count_str)
                ages = generate_random_ages(count)
                self.analyze_ages(ages)
            except ValueError:
                messagebox.showerror("Error", "Veuillez entrer un nombre entier pour la quantité d'âges à générer.")

    def choose_weights(self):
        weights = simpledialog.askstring("Choose Weights",
                                         "Choisissez un ensemble de poids:\n1. Standard\n2. Jeune\n3. Égal\n4. Ancien\n\nEntrez le numéro de l'ensemble de poids:")
        if weights in weight_presets:
            self.selected_weights = weight_presets[weights]
            messagebox.showinfo("Info", f"Ensemble de poids sélectionné : {weights}")
        else:
            messagebox.showerror("Error", "Choix non valide. Veuillez réessayer.")

    def analyze_ages(self, ages):
        analyze_ages(ages, self.selected_weights)


def tp2_4_tkinter_app():
    root = tk.Tk()
    app = AgeAnalyzerApp(root)
    root.mainloop()
