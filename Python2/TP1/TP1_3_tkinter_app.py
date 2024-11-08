# -*- coding: Latin-1 -*-

import os
import random
import tkinter as tk
from tkinter import filedialog, messagebox

# Define global variables for the entry fields and text area
entry_fichier_noms = None
entry_fichier_messages = None
text_area = None


def saluer_utilisateurs_depuis_fichier(fichier_noms, fichier_messages):
    try:
        # Vérifier l'existence du fichier de noms
        if not os.path.exists(fichier_noms):
            messagebox.showerror("Erreur",
                                 f"Le fichier {fichier_noms} est introuvable. Veuillez vérifier le chemin du fichier.")
            return

        # Ouvrir et lire le fichier de noms
        with open(fichier_noms, 'r', encoding='latin-1') as fichier:
            contenu = fichier.read()

        # Diviser le contenu en noms
        noms = [nom.strip() for nom in contenu.replace('\n', ',').split(',') if nom.strip()]

        # Vérifier l'existence du fichier de messages
        if not os.path.exists(fichier_messages):
            messagebox.showerror("Erreur", f"Le fichier {fichier_messages} est introuvable.")
            return

        # Lire les messages d'accueil
        with open(fichier_messages, 'r', encoding='latin-1') as fichier1:
            messages = fichier1.read()
            messages_accueil = [message.strip() for message in messages.replace('\n', ',').split(',') if
                                message.strip()]

        # Créer une liste pour stocker les messages d'accueil
        messages_affiches = []

        # Parcourir la liste des noms et afficher un message d'accueil personnalisé
        for nom in noms:
            if nom:
                message_choisi = random.choice(messages_accueil)
                messages_affiches.append(f"{message_choisi}, {nom} !")
            else:
                messages_affiches.append("Un nom vide a été détecté, veuillez entrer un nom valide.")

        # Afficher les messages dans la zone de texte
        text_area.delete(1.0, tk.END)  # Effacer le contenu précédent
        text_area.insert(tk.END, "\n".join(messages_affiches))

    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")


def choisir_fichier_noms():
    chemin_fichier_noms = filedialog.askopenfilename(title="Choisissez le fichier contenant les noms",
                                                     filetypes=[("Text Files", "*.txt")])
    entry_fichier_noms.delete(0, tk.END)  # Effacer l'entrée précédente
    entry_fichier_noms.insert(0, chemin_fichier_noms)  # Afficher le chemin sélectionné


def choisir_fichier_messages():
    chemin_fichier_messages = filedialog.askopenfilename(title="Choisissez le fichier contenant les messages",
                                                         filetypes=[("Text Files", "*.txt")])
    entry_fichier_messages.delete(0, tk.END)  # Effacer l'entrée précédente
    entry_fichier_messages.insert(0, chemin_fichier_messages)  # Afficher le chemin sélectionné


def lancer_salutations():
    chemin_fichier_noms = entry_fichier_noms.get()
    chemin_fichier_messages = entry_fichier_messages.get()
    saluer_utilisateurs_depuis_fichier(chemin_fichier_noms, chemin_fichier_messages)


def tp1_3_tkinter_app():
    global entry_fichier_noms, entry_fichier_messages, text_area

    # Créer la fenêtre principale
    root = tk.Tk()
    root.title("Application de Salutations")

    # Set window size (width x height)
    window_width = 400
    window_height = 300

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate x and y coordinates to center the window
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Set the geometry of the window
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Créer les widgets
    label_fichier_noms = tk.Label(root, text="Fichier contenant les noms:")
    label_fichier_noms.pack(pady=5)

    entry_fichier_noms = tk.Entry(root, width=50)
    entry_fichier_noms.pack(pady=5)

    button_fichier_noms = tk.Button(root, text="Choisir fichier", command=choisir_fichier_noms)
    button_fichier_noms.pack(pady=5)

    label_fichier_messages = tk.Label(root, text="Fichier contenant les messages d'accueil:")
    label_fichier_messages.pack(pady=5)

    entry_fichier_messages = tk.Entry(root, width=50)
    entry_fichier_messages.pack(pady=5)

    button_fichier_messages = tk.Button(root, text="Choisir fichier", command=choisir_fichier_messages)
    button_fichier_messages.pack(pady=5)

    button_saluer = tk.Button(root, text="Saluer les utilisateurs", command=lancer_salutations)
    button_saluer.pack(pady=10)

    text_area = tk.Text(root, height=10, width=70)
    text_area.pack(pady=10)

    root.mainloop()
