# -*-coding: Latin-1 -*

import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

def analyze_ages(ages):
    # Calculate the median
    median_age = np.median(ages)
    print(f"M�diane des �ges : {median_age}")

    # Grouping ages and calculating frequencies
    bins = [0, 18, 30, 50, 100]
    labels = ['0-18', '19-30', '31-50', '51+']
    age_groups = pd.cut(ages, bins=bins, labels=labels, right=False)
    age_group_counts = age_groups.value_counts().sort_index()
    print("\nFr�quence des groupes d'�ge :")
    print(age_group_counts)

    # Calculate the weighted average
    weights = {'0-18': 1, '19-30': 2, '31-50': 3, '51+': 4}
    weighted_average = np.average(
        [age_group_counts[label] for label in labels],
        weights=[weights[label] for label in labels]
    )
    print(f"\nMoyenne pond�r�e des groupes d'�ge : {weighted_average:.2f}")

    # Plotting
    plt.figure(figsize=(10, 6))
    bars = plt.bar(age_group_counts.index, age_group_counts.values, color='skyblue', alpha=0.7)
    plt.axhline(y=median_age, color='r', linestyle='--', label=f'M�diane d\'�ge : {median_age}')

    # Adding annotations
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')

    plt.title('Distribution des �ges par groupes')
    plt.xlabel('Groupes d\'�ge')
    plt.ylabel('Fr�quence')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Function to read ages from a file
def read_ages_from_file(filename):
    try:
        with open(filename, 'r') as file:
            # Read ages and convert them to a list of integers
            ages = list(map(int, file.read().strip().split(',')))
        return ages
    except FileNotFoundError:
        print(f"Le fichier '{filename}' n'a pas �t� trouv�.")
        return None
    except ValueError:
        print("Le fichier contient des donn�es non valides.")
        return None

# Function to generate random ages
def generate_random_ages(count):
    return [random.randint(0, 100) for _ in range(count)]

#

def main():
        #Main interaction
    print("Choisissez une m�thode d'entr�e des �ges :")
    print("1. Entrer un nom de document pour lire les �ges.")
    print("2. Saisir les �ges manuellement.")
    print("3. G�n�rer des �ges al�atoires.")

    choice = input("Entrez votre choix (1, 2, ou 3) : ")

    ages = []

    if choice == '1': # Get the current script directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        filename = current_dir + input("Entrez le nom du document (avec l'extension, ex. ages.txt) : ")
        ages = read_ages_from_file(filename)
    elif choice == '2':
        user_input = input("Entrez une liste d'�ges s�par�s par des virgules (ex. 15,22,34,45) : ")
        ages = list(map(int, user_input.split(',')))
    elif choice == '3':
        count = int(input("Combien d'�ges al�atoires souhaitez-vous g�n�rer ? "))
        ages = generate_random_ages(count)
    else:
        print("Choix non valide. Veuillez red�marrer le programme.")

    # Proceed if ages were successfully retrieved
    if ages:
        analyze_ages(ages)

if __name__ == "__main__":
    main()