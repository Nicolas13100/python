# -*-coding:Latin-1 -*

import random
import threading
import json
import os

# Constants for difficulty levels
DIFFICULTY_LEVELS = {
    '1': {'range_min': 1, 'range_max': 10, 'time_limit': 20, 'level': 'Facile'},
    '2': {'range_min': 1, 'range_max': 50, 'time_limit': 15, 'level': 'Moyen'},
    '3': {'range_min': 1, 'range_max': 100, 'time_limit': 10, 'level': 'Difficile'}
}

# Supported operations
OPERATIONS = {
    '1': {'name': 'Addition', 'symbol': '+', 'func': lambda x, y: x + y},
    '2': {'name': 'Soustraction', 'symbol': '-', 'func': lambda x, y: x - y},
    '3': {'name': 'Multiplication', 'symbol': 'x', 'func': lambda x, y: x * y},
    '4': {'name': 'Division', 'symbol': '�', 'func': lambda x, y: round(x / y, 2) if y != 0 else None}
}

def timer_decompte(limit, reponse, event):
    """
    Waits for the user to respond within the time limit.
    If the user does not respond in time, appends None to the response list.
    """
    if not event.wait(timeout=limit):
        reponse.append(None)

def save_score_to_json(name, score, filename="scores.json"):
    """
    Saves the user's name and score to a JSON file.
    If the file exists, it appends the new score; otherwise, it creates a new file.
    """
    data = {"name": name, "score": score}
    try:
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                scores = json.load(file)
        else:
            scores = []

        scores.append(data)

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(scores, file, indent=4)
    except IOError as e:
        print(f"Erreur lors de la sauvegarde du score: {e}")

def tp1_4_menu():
    """
    Main function to conduct the math quiz game.
    Handles difficulty selection, question generation, timing, scoring, and score saving.
    """
    score = 0

    print("Bienvenue au jeu de calculs !")
    print("Choisissez un niveau de difficult� :")
    for key, value in DIFFICULTY_LEVELS.items():
        print(f"{key}. {value['level']} (nombres entre {value['range_min']} et {value['range_max']}, {value['time_limit']} secondes)")

    # S�lection du niveau de difficult�
    while True:
        difficulte = input("Entrez votre choix de difficult� (1-3) : ")
        if difficulte in DIFFICULTY_LEVELS:
            settings = DIFFICULTY_LEVELS[difficulte]
            break
        else:
            print("Choix invalide. Veuillez entrer 1, 2 ou 3.")

    range_min = settings['range_min']
    range_max = settings['range_max']
    temps = settings['time_limit']

    # Demander le nombre maximum de questions
    while True:
        try:
            max_questions = int(input("Combien de questions voulez-vous r�pondre ? "))
            if max_questions > 0:
                break
            else:
                print("Veuillez entrer un nombre sup�rieur � z�ro.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    questions_repondues = 0

    while questions_repondues < max_questions:
        print(f"\nQuestion {questions_repondues + 1}/{max_questions}")
        print("Choisissez une op�ration :")
        for key, op in OPERATIONS.items():
            print(f"{key}. {op['name']}")

        # Ajouter l'option pour quitter
        print("5. Quitter")

        choix = input("Entrez votre choix (1-5) : ")

        if choix == '5':
            print(f"Merci d'avoir jou� ! Votre score final est : {score}")
            break

        if choix not in OPERATIONS:
            print("Choix invalide. Veuillez entrer un chiffre entre 1 et 5.")
            continue

        # G�n�rer deux nombres al�atoires selon le niveau de difficult�
        nombre1 = random.randint(range_min, range_max)
        nombre2 = random.randint(range_min, range_max)

        # Initialiser la question et la r�ponse correcte
        operation = OPERATIONS[choix]
        if choix == '4':  # Division
            while nombre2 == 0:
                nombre2 = random.randint(range_min, range_max)
            reponse_correcte = operation['func'](nombre1, nombre2)
            question = f"Combien fait {nombre1} {operation['symbol']} {nombre2} (arrondi � deux d�cimales) ?"
        else:
            reponse_correcte = operation['func'](nombre1, nombre2)
            question = f"Combien fait {nombre1} {operation['symbol']} {nombre2} ?"

        print(question)

        # Pr�parer une liste pour stocker la r�ponse utilisateur
        reponse_utilisateur = []
        event = threading.Event()

        # D�marrer le timer dans un thread
        timer_thread = threading.Thread(target=timer_decompte, args=(temps, reponse_utilisateur, event))
        timer_thread.start()

        try:
            reponse_input = input(f"Votre r�ponse (vous avez {temps} secondes) : ")
            event.set()
            if reponse_input.strip() == "":
                raise ValueError
            if choix == '4':
                reponse_utilisateur_input = round(float(reponse_input), 2)
            else:
                reponse_utilisateur_input = float(reponse_input)
            reponse_utilisateur.append(reponse_utilisateur_input)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            reponse_utilisateur.append(None)

        # Attendre que le thread du timer se termine
        timer_thread.join()

        # V�rifier si le temps a expir� ou la r�ponse est invalide
        if not reponse_utilisateur or reponse_utilisateur[0] is None:
            print("Temps �coul� ou r�ponse invalide ! Vous n'avez pas r�pondu � temps.")
            print(f"La bonne r�ponse �tait {reponse_correcte}.")
        else:
            # Comparer la r�ponse de l'utilisateur � la r�ponse correcte
            if reponse_utilisateur[0] == reponse_correcte:
                print("Bonne r�ponse !")
                score += 1
            else:
                print(f"Mauvaise r�ponse. La bonne r�ponse �tait {reponse_correcte}.")

        questions_repondues += 1
        print(f"Votre score actuel est : {score}")

    # Demander le nom du joueur � la fin du jeu
    while True:
        nom = input("\nEntrez votre nom pour sauvegarder votre score : ").strip()
        if nom:
            break
        else:
            print("Le nom ne peut pas �tre vide.")

    save_score_to_json(nom, score)
    print(f"Score de {score} enregistr� pour {nom} !")
