# -*- coding: Latin-1 -*-
import random
import threading
import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

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
    '4': {'name': 'Division', 'symbol': '÷', 'func': lambda x, y: round(x / y, 2) if y != 0 else None}
}

def timer_decompte(limit, response, event):
    """
    Waits for the user to respond within the time limit.
    If the user does not respond in time, appends None to the response list.
    """
    if not event.wait(timeout=limit):
        response.append(None)

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

class MathQuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Jeu de Calculs")

        # Set window size (width x height)
        window_width = 400
        window_height = 300

        # Get screen width and height
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Calculate x and y coordinates to center the window
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # Set the geometry of the window
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.score = 0
        self.max_questions = 0
        self.questions_answered = 0
        self.current_question = ""

        # Widgets
        self.start_button = tk.Button(master, text="Démarrer le quiz", command=self.start_quiz)
        self.start_button.pack(pady=10)

        self.question_label = tk.Label(master, text="", font=('Helvetica', 16))
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(master)
        self.answer_entry.pack(pady=5)

        self.submit_button = tk.Button(master, text="Soumettre Réponse", command=self.submit_answer)
        self.submit_button.pack(pady=5)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

        # Timer and threading
        self.event = threading.Event()
        self.timer_thread = None

    def start_quiz(self):
        """Start the quiz and reset variables."""
        self.score = 0
        self.questions_answered = 0
        self.result_label.config(text="")
        self.answer_entry.delete(0, tk.END)

        # Select difficulty
        difficulty = simpledialog.askstring("Sélection de la Difficulté",
                                              "Choisissez une difficulté (1: Facile, 2: Moyen, 3: Difficile):")
        if difficulty in DIFFICULTY_LEVELS:
            settings = DIFFICULTY_LEVELS[difficulty]
            self.range_min = settings['range_min']
            self.range_max = settings['range_max']
            self.time_limit = settings['time_limit']

            # Ask for the number of questions
            self.max_questions = simpledialog.askinteger("Nombre de Questions",
                                                         "Combien de questions voulez-vous répondre ?")
            if self.max_questions and self.max_questions > 0:
                self.ask_question()
            else:
                messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")
        else:
            messagebox.showerror("Erreur", "Choix de difficulté invalide.")

    def ask_question(self):
        """Generate and display a new question."""
        if self.questions_answered < self.max_questions:
            self.questions_answered += 1

            # Generate random numbers and operation
            self.number1 = random.randint(self.range_min, self.range_max)
            self.number2 = random.randint(self.range_min, self.range_max)
            self.operation_choice = random.choice(list(OPERATIONS.keys()))
            operation = OPERATIONS[self.operation_choice]

            # Prepare the question
            if self.operation_choice == '4':  # Division
                while self.number2 == 0:
                    self.number2 = random.randint(self.range_min, self.range_max)
                self.correct_answer = operation['func'](self.number1, self.number2)
                self.current_question = f"Combien fait {self.number1} {operation['symbol']} {self.number2} (arrondi à deux décimales) ?"
            else:
                self.correct_answer = operation['func'](self.number1, self.number2)
                self.current_question = f"Combien fait {self.number1} {operation['symbol']} {self.number2} ?"

            self.question_label.config(text=self.current_question)
            self.result_label.config(text="")
            self.answer_entry.delete(0, tk.END)

            # Start the timer
            self.event.clear()
            self.timer_thread = threading.Thread(target=timer_decompte, args=(self.time_limit, [], self.event))
            self.timer_thread.start()

            # Set a timeout for user input
            self.master.after(self.time_limit * 1000, self.timeout)

        else:
            self.end_quiz()

    def submit_answer(self):
        """Check the user's answer and proceed to the next question."""
        user_answer = self.answer_entry.get().strip()
        self.event.set()  # Stop the timer

        if user_answer == "":
            messagebox.showwarning("Avertissement", "Veuillez entrer une réponse.")
            return

        try:
            user_answer = float(user_answer)
            if user_answer == self.correct_answer:
                self.score += 1
                self.result_label.config(text="Bonne réponse !")
            else:
                self.result_label.config(text=f"Mauvaise réponse. La bonne réponse était {self.correct_answer}.")
            self.ask_question()  # Ask the next question
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")

    def timeout(self):
        """Handle the timeout situation."""
        self.result_label.config(text="Temps écoulé !")
        self.ask_question()  # Ask the next question

    def end_quiz(self):
        """End the quiz and save the score."""
        name = simpledialog.askstring("Nom", "Entrez votre nom pour sauvegarder votre score :")
        if name:
            save_score_to_json(name, self.score)
            messagebox.showinfo("Score", f"Votre score final est {self.score}.\nScore enregistré pour {name} !")
        else:
            messagebox.showwarning("Avertissement", "Le nom ne peut pas être vide.")

        # Reset the quiz state
        self.score = 0
        self.questions_answered = 0
        self.max_questions = 0
        self.question_label.config(text="")
        self.result_label.config(text="")
        self.answer_entry.delete(0, tk.END)

        # Optionally, reset the start button to allow a new game
        self.start_button.config(state=tk.NORMAL)

def tp1_4_tkinter_app():
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()
