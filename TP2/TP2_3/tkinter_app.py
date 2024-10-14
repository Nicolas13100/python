# -*-coding: Latin-1 -*

import statistics
import tkinter as tk
from tkinter import filedialog

import matplotlib.pyplot as plt


def calculer_statistiques(prix):
    """Calcul des statistiques pour une liste de prix."""
    moyenne = sum(prix) / len(prix)
    variance = sum((x - moyenne) ** 2 for x in prix) / len(prix)
    ecart_type = variance ** 0.5
    mediane = statistics.median(prix)
    return moyenne, variance, ecart_type, mediane


def afficher_graphique(prix, moyenne, mediane, ecart_type):
    """Affiche un histogramme des prix avec des lignes pour les statistiques."""
    plt.figure(figsize=(10, 6))
    plt.hist(prix, bins=10, alpha=0.7, color='blue', edgecolor='black')

    plt.axvline(moyenne, color='red', linestyle='dashed', linewidth=2, label='Moyenne')
    plt.axvline(mediane, color='green', linestyle='dashed', linewidth=2, label='Médiane')
    plt.axvline(moyenne + ecart_type, color='orange', linestyle='dotted', linewidth=2, label='Écart-Type (+1)')
    plt.axvline(moyenne - ecart_type, color='orange', linestyle='dotted', linewidth=2, label='Écart-Type (-1)')

    plt.title('Distribution des Prix des Produits')
    plt.xlabel('Prix')
    plt.ylabel('Fréquence')
    plt.legend()
    plt.grid(axis='y', alpha=0.75)

    plt.show()


def load_from_file():
    """Charge les prix depuis un fichier et met à jour l'interface utilisateur."""
    nom_fichier = filedialog.askopenfilename(title="Sélectionnez un fichier", filetypes=[("Text files", "*.txt")])
    if nom_fichier:
        try:
            with open(nom_fichier, 'r') as fichier:
                prix = [float(x) for x in fichier.read().split()]
            # Update the input field with the loaded prices
            input_prix.delete(0, tk.END)  # Clear existing input
            input_prix.insert(tk.END, ' '.join(map(str, prix)))  # Insert loaded prices as a string

            # Automatically call calculer to compute and display the results
            calculer()

            return prix
        except FileNotFoundError:
            afficher_message(f"Le fichier {nom_fichier} est introuvable.")
        except ValueError:
            afficher_message("Erreur de format dans le fichier. Assurez-vous que les prix sont des nombres valides.")
    return []


def calculer():
    """Calculer les statistiques et afficher les résultats."""
    try:
        prix_input = input_prix.get().strip()
        if prix_input:
            prix = [float(x) for x in prix_input.split()]
        else:
            prix, erreur = load_from_file()
            if erreur:
                afficher_message(erreur)
                return

        if not prix:
            afficher_message("Erreur : Aucune donnée de prix valide n'a été fournie.")
            return

        # Calcul des statistiques
        moyenne, variance, ecart_type, mediane = calculer_statistiques(prix)

        # Affichage des résultats
        resultats = (
            f"Moyenne des prix : {moyenne:.2f}\n"
            f"Variance des prix : {variance:.2f}\n"
            f"Écart-type des prix : {ecart_type:.2f}\n"
            f"Médiane des prix : {mediane:.2f}"
        )
        afficher_resultats(resultats)

        # Afficher le graphique
        afficher_graphique(prix, moyenne, mediane, ecart_type)

    except ValueError:
        afficher_message("Veuillez entrer uniquement des nombres valides.")


def afficher_message(message):
    """Affiche un message d'erreur dans la zone de texte."""
    output_text.delete(1.0, tk.END)  # Efface le texte précédent
    output_text.insert(tk.END, message)  # Insère le nouveau message


def afficher_resultats(resultats):
    """Affiche les résultats dans la zone de texte."""
    output_text.delete(1.0, tk.END)  # Efface le texte précédent
    output_text.insert(tk.END, resultats)  # Insère les résultats


# Créer la fenêtre principale
root = tk.Tk()
root.title("Analyse des Prix des Produits")

# Center the window on the user's screen
window_width = 500
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Interface utilisateur
frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text="Entrez les prix des produits (ou choisissez un fichier) :")
label.pack()

input_prix = tk.Entry(frame, width=50)
input_prix.pack(pady=10)

button_calculer = tk.Button(frame, text="Calculer les Statistiques", command=calculer)
button_calculer.pack()

button_load_file = tk.Button(frame, text="Charger depuis un Fichier", command=load_from_file)
button_load_file.pack(pady=10)

# Text widget for displaying output
output_text = tk.Text(frame, height=10, width=50)
output_text.pack(pady=10)

# Lancer l'application
root.mainloop()
