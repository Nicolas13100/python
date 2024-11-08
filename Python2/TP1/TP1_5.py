# -*- coding: Latin-1 -*-

def est_bissextile(annee):
    """
    Vérifie si une année est bissextile.
    :param annee: L'année à vérifier
    :return: True si l'année est bissextile, sinon False
    """
    # Vérification selon les règles des années bissextiles
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def dernier_bissextile(annee):
    """Retourne l'année bissextile précédente à l'année donnée."""
    while not est_bissextile(annee):
        annee -= 1
    return annee

def prochain_bissextile(annee):
    """Retourne l'année bissextile suivante à l'année donnée."""
    while not est_bissextile(annee):
        annee += 1
    return annee

def tp1_5_menu():
    # Demander à l'utilisateur d'entrer une année
    try:
        annee = int(input("Veuillez entrer une année (nombre entier) : "))

        # Vérification si l'année est bissextile ou non
        if est_bissextile(annee):
            print(f"L'année {annee} est bissextile.")
        else:
            dernier = dernier_bissextile(annee)
            prochain = prochain_bissextile(annee)
            print(f"L'année {annee} n'est pas bissextile.")
            print(f"La dernière année bissextile était {dernier}.")
            print(f"La prochaine année bissextile sera {prochain}.")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre entier valide.")

