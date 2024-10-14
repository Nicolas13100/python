# -*-coding:Latin-1 -*

import math


def obtenir_entier_positif():
    """Demande à l'utilisateur de saisir un entier positif inférieur à 1000."""
    essais = 0
    print("Bienvenue! Veuillez entrer un entier positif inférieur à 1000.")
    print("Vous avez un maximum de 15 essais. Tapez 'exit' pour quitter à tout moment.\n")

    while essais < 15:  # Limite d'essais
        try:
            user_input = input("Entrez un entier positif inférieur à 1000 (ou 'exit' pour quitter): ")
            if user_input.lower() == 'exit':
                print("Merci d'avoir utilisé le programme!")
                exit()
            N = int(user_input)
            if 0 < N < 1000:  # Vérification de la validité
                return N
            else:
                print("Erreur : L'entier doit être positif et inférieur à 1000.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")

        essais += 1
        print(f"Essais restants: {15 - essais}")

    # Trop d'essais - confirmation avant de quitter
    confirm_exit = input(
        "Vous avez atteint la limite de 15 essais. Voulez-vous vraiment quitter? (oui/non): ").strip().lower()
    if confirm_exit in ['oui', 'o']:
        print("Merci d'avoir utilisé le programme!")
        exit()
    else:
        return obtenir_entier_positif()  # Restart the input process after confirmation


def calculer_somme_et_produit_pairs(N):
    """Calcule la somme et le produit des nombres pairs jusqu'à N."""
    somme = 0
    produit = 1
    nombres_pairs = []

    for i in range(2, N + 1, 2):
        somme += i
        nombres_pairs.append(i)

        try:
            produit = math.prod(nombres_pairs)  # Utilisation de math.prod pour gérer le produit
        except OverflowError:
            print("Erreur : Le produit des nombres pairs est trop grand pour être calculé.")
            produit = None
            break

    return somme, produit, nombres_pairs


def afficher_resultats(somme, produit, nombres_pairs):
    """Affiche les résultats de la somme et du produit."""
    print("\n--- Résultats ---")
    print(f"Somme des pairs: {' + '.join(map(str, nombres_pairs))} = {somme}")

    if produit is not None and nombres_pairs:  # To avoid multiplying an empty list
        print(f"Produit des pairs: {' * '.join(map(str, nombres_pairs))} = {produit}")
    else:
        print("Aucun nombre pair pour le produit ou produit trop grand à calculer.")

    print(f"Nombre de nombres pairs: {len(nombres_pairs)}")


def start():
    while True:
        N = obtenir_entier_positif()  # Obtention d'un entier valide
        somme, produit, nombres_pairs = calculer_somme_et_produit_pairs(N)
        afficher_resultats(somme, produit, nombres_pairs)

        # Demander à l'utilisateur s'il veut recommencer
        recommencer = input("Voulez-vous recommencer? (oui/non): ").strip().lower()
        if recommencer not in ['oui', 'o']:
            print("Merci d'avoir utilisé le programme!")
            break

if __name__ == "__main__":
    start()