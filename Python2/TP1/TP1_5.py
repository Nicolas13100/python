# -*- coding: Latin-1 -*-

def est_bissextile(annee):
    """
    V�rifie si une ann�e est bissextile.
    :param annee: L'ann�e � v�rifier
    :return: True si l'ann�e est bissextile, sinon False
    """
    # V�rification selon les r�gles des ann�es bissextiles
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def dernier_bissextile(annee):
    """Retourne l'ann�e bissextile pr�c�dente � l'ann�e donn�e."""
    while not est_bissextile(annee):
        annee -= 1
    return annee

def prochain_bissextile(annee):
    """Retourne l'ann�e bissextile suivante � l'ann�e donn�e."""
    while not est_bissextile(annee):
        annee += 1
    return annee

def tp1_5_menu():
    # Demander � l'utilisateur d'entrer une ann�e
    try:
        annee = int(input("Veuillez entrer une ann�e (nombre entier) : "))

        # V�rification si l'ann�e est bissextile ou non
        if est_bissextile(annee):
            print(f"L'ann�e {annee} est bissextile.")
        else:
            dernier = dernier_bissextile(annee)
            prochain = prochain_bissextile(annee)
            print(f"L'ann�e {annee} n'est pas bissextile.")
            print(f"La derni�re ann�e bissextile �tait {dernier}.")
            print(f"La prochaine ann�e bissextile sera {prochain}.")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre entier valide.")

