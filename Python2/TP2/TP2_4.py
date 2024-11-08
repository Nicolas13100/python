# -*-coding: Latin-1 -*

import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plotly.graph_objects import Bar, Figure

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
        print("No valid ages to analyze.")
        return

    # Calculate statistics
    median_age = np.median(ages)
    mean_age = np.mean(ages)
    mode_age = pd.Series(ages).mode()[0]
    std_dev_age = np.std(ages)
    print(f"\nStatistiques des âges :")
    print(f"- Médiane : {median_age}")
    print(f"- Moyenne : {mean_age:.2f}")
    print(f"- Mode : {mode_age}")
    print(f"- Écart-type : {std_dev_age:.2f}")

    # Group ages and calculate frequencies
    bins = [0, 18, 30, 50, 70, 90, 120]  # Extended age bins
    labels = ['0-18', '19-30', '31-50', '51-70', '71-90', '91+']
    age_groups = pd.cut(ages, bins=bins, labels=labels, right=False)
    age_group_counts = age_groups.value_counts().sort_index()
    print("\nFréquence des groupes d'âge :")
    print(age_group_counts)

    # Use provided weights or fallback to default if none are provided
    if weights is None:
        weights = {'0-18': 1, '19-30': 2, '31-50': 3, '51-70': 4, '71-90': 5, '91+': 6}

    weighted_average = np.average(
        [age_group_counts[label] for label in labels],
        weights=[weights[label] for label in labels]
    )
    print(f"\nMoyenne pondérée des groupes d'âge : {weighted_average:.2f}")

    # Save Analysis to File
    save_analysis_to_file("age_analysis_results.txt", age_group_counts, median_age, mean_age, mode_age, std_dev_age)
    print("\nLes résultats de l'analyse ont été enregistrés dans 'age_analysis_results.txt'.")

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
        print(f"Le fichier '{filename}' n'a pas été trouvé.")
        return None
    except ValueError:
        print("Le fichier contient des données non valides.")
        return None


# Random Age Generation
def generate_random_ages(count):
    return [random.randint(0, 120) for _ in range(count)]  # Adjusted to include 0-120


# Main Menu for Interactive User Input
def tp2_4_menu():
    while True:
        print("\nChoisissez une méthode d'entrée des âges :")
        print("1. Entrer un nom de document pour lire les âges.")
        print("2. Saisir les âges manuellement.")
        print("3. Générer des âges aléatoires.")
        print("4. Choisir un ensemble de poids prédéfinis.")
        print("5. Quitter.")

        choice = input("Entrez votre choix (1, 2, 3, 4, ou 5) : ")

        ages = []
        selected_weights = None  # Variable to hold the chosen weights

        if choice == '1':  # Read from a file
            filename = input("Entrez le nom du document (avec l'extension, ex. ages.txt) : ")
            ages = read_ages_from_file(filename)
        elif choice == '2':  # Input manually
            user_input = input("Entrez une liste d'âges séparés par des virgules (ex. 15,22,34,45) : ")
            try:
                ages = list(map(int, user_input.split(',')))
            except ValueError:
                print("Entrée invalide. Assurez-vous que les âges sont des nombres entiers séparés par des virgules.")
                continue
        elif choice == '3':  # Generate random ages
            try:
                count = int(input("Combien d'âges aléatoires souhaitez-vous générer ? "))
                ages = generate_random_ages(count)
            except ValueError:
                print("Veuillez entrer un nombre entier pour la quantité d'âges à générer.")
                continue
        elif choice == '4':  # Choose weight preset
            print("Choisissez un ensemble de poids :")
            print("1. Poids incrémentaux")
            print("2. Accent sur la jeunesse")
            print("3. Équilibre sur les jeunes groupes")
            print("4. Poids plus élevés pour les personnes âgées")
            preset_choice = input("Entrez votre choix (1, 2, 3, ou 4) : ")
            if preset_choice in weight_presets:
                selected_weights = weight_presets[preset_choice]
                print(f"Vous avez choisi l'ensemble de poids : {selected_weights}")
            else:
                print("Choix non valide. Veuillez réessayer.")
                continue
        elif choice == '5':  # Exit option
            print("Merci d'avoir utilisé le programme.")
            break
        else:
            print("Choix non valide. Veuillez réessayer.")
            continue

        # Proceed if ages were successfully retrieved
        if ages:
            analyze_ages(ages, selected_weights)  # Pass the selected weights to the analysis function

