# -*-coding:Latin-1 -*
import os
import random


def saluer_utilisateurs_depuis_fichier(fichier_noms):

    try:
        # Vérifier l'existence du fichier de noms
        if not os.path.exists(fichier_noms):
            print(f"Le fichier {fichier_noms} est introuvable. Veuillez vérifier le chemin du fichier.")
            return

        # 1. Ouvrir et lire le fichier de noms
        with open(fichier_noms, 'r', encoding='latin-1') as fichier:
            contenu = fichier.read()

        # 2. Diviser le contenu en noms
        noms = [nom.strip() for nom in contenu.replace('\n', ',').split(',') if nom.strip()]

        # Get the current script directory
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Vérifier l'existence du fichier ListeMessagesDAccueil
        fichier_messages = current_dir + '\\ListeMessagesDAccueil.txt'
        if not os.path.exists(fichier_messages):
            print(f"Le fichier {fichier_messages} est introuvable.")
            return

        # 3. Lire les messages d'accueil
        with open(fichier_messages, 'r', encoding='latin-1') as fichier1:
            messages = fichier1.read()
            messages_accueil = [message.strip() for message in messages.replace('\n', ',').split(',') if
                                message.strip()]

        # 4. Parcourir la liste des noms et afficher un message d'accueil personnalisé
        for nom in noms:
            if nom:
                message_choisi = random.choice(messages_accueil)
                print(f"{message_choisi}, {nom} !")
            else:
                print("Un nom vide a été détecté, veuillez entrer un nom valide.")

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


def start():
    # Get the current script directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Demander à l'utilisateur d'entrer le chemin du fichier contenant les nom
    chemin_fichier = current_dir + '\\' + input("Veuillez entrer le chemin du fichier contenant les noms ( ListeDeNom.txt ): ")
    saluer_utilisateurs_depuis_fichier(chemin_fichier)

# Exécution du programme
if __name__ == "__main__":
    start()
