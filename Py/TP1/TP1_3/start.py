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

        # Vérifier l'existence du fichier ListeMessagesDAccueil
        fichier_messages = 'TP1\\TP1_3\\ListeMessagesDAccueil.txt'
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
    # Demander à l'utilisateur d'entrer le chemin du fichier contenant les noms
    chemin_fichier = 'TP1\\TP1_3\\' + input("Veuillez entrer le chemin du fichier contenant les noms : ")
    saluer_utilisateurs_depuis_fichier(chemin_fichier)

# Exécution du programme
if __name__ == "__main__":
    start()
