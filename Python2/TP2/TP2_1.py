# Fonction pour vérifier si un nombre est parfait et afficher les détails
def est_nombre_parfait(n):
    # Initialiser la somme des diviseurs propres
    somme_diviseurs = 0
    diviseurs = []  # Liste pour stocker les diviseurs propres

    # Calculer la somme des diviseurs propres
    for i in range(1, n):
        if n % i == 0:  # Si 'i' est un diviseur de 'n'
            somme_diviseurs += i
            diviseurs.append(i)  # Ajouter le diviseur à la liste

    # Comparer la somme des diviseurs au nombre et afficher les détails
    if somme_diviseurs == n:
        print(f"{n} est un nombre parfait.")
    else:
        print(f"{n} n'est pas un nombre parfait.")

    # Afficher les diviseurs propres
    print(f"Les diviseurs propres de {n} sont : {diviseurs}")
    print(f"La somme des diviseurs propres est : {somme_diviseurs}")


def tp2_1_menu():
    # Demander à l'utilisateur d'entrer un nombre entier
    try:
        nombre = int(input("Entrez un nombre entier: "))

        # Vérifier si le nombre est parfait
        est_nombre_parfait(nombre)

    except ValueError:
        print("Veuillez entrer un nombre entier valide.")
