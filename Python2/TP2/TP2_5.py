# -*-coding: Latin-1 -*

import random
import matplotlib.pyplot as plt


def simuler_lancers_de(n, nombre_de_d�s):
    # Dictionnaire pour stocker les fr�quences des faces du d�
    frequences = {i: 0 for i in range(1, 7)}  # Faces du d� (1 � 6)

    # Effectuer les lancers de d�s
    for _ in range(n):
        for _ in range(nombre_de_d�s):
            lancer = random.randint(1, 6)  # Lancer un d� � six faces
            frequences[lancer] += 1  # Augmenter la fr�quence de la face obtenue

    return frequences


def afficher_resultats(frequences, total_lancers):
    print("Fr�quence d'apparition de chaque face du d� :")
    for face, frequence in frequences.items():
        pourcentage = (frequence / total_lancers) * 100
        print(f"Face {face}: {frequence} fois ({pourcentage:.2f}%)")

    # Cr�ation du graphique
    faces = list(frequences.keys())
    valeurs = list(frequences.values())

    plt.bar(faces, valeurs, color='skyblue')
    plt.xlabel('Faces du d�')
    plt.ylabel('Fr�quence')
    plt.title('Fr�quence d\'apparition des faces du d� apr�s {} lancers'.format(total_lancers))
    plt.xticks(faces)  # Pour afficher toutes les faces sur l'axe x
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()  # Affiche le graphique


# Fonction principale
def tp2_5_menu():
    # Nombre maximum de lancers pour �viter les crashs
    MAX_LANCERS = 100000

    # Demande � l'utilisateur combien de lancers effectuer
    try:
        total_lancers = int(input("Combien de lancers souhaitez-vous effectuer ? (max {}): ".format(MAX_LANCERS)))
        if total_lancers < 1 or total_lancers > MAX_LANCERS:
            print(f"Veuillez entrer un nombre entre 1 et {MAX_LANCERS}.")
            return
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return

    # Simuler les lancers de d�s
    frequences = simuler_lancers_de(total_lancers, 1)

    # Afficher les r�sultats
    afficher_resultats(frequences, total_lancers)


# Ex�cuter le programme principal
if __name__ == "__main__":
    main()
