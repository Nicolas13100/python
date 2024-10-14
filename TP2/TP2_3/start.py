import statistics
import matplotlib.pyplot as plt


def calculer_statistiques(prix):
    # Calcul de la moyenne
    moyenne = sum(prix) / len(prix)

    # Calcul de la variance
    variance = sum((x - moyenne) ** 2 for x in prix) / len(prix)

    # Calcul de l'écart-type
    ecart_type = variance ** 0.5

    # Calcul de la médiane
    mediane = statistics.median(prix)

    return moyenne, variance, ecart_type, mediane


def afficher_graphique(prix, moyenne, mediane, ecart_type):
    # Création du graphique
    plt.figure(figsize=(10, 6))
    plt.hist(prix, bins=10, alpha=0.7, color='blue', edgecolor='black')

    # Ajouter des lignes pour la moyenne, la médiane et l'écart-type
    plt.axvline(moyenne, color='red', linestyle='dashed', linewidth=2, label='Moyenne')
    plt.axvline(mediane, color='green', linestyle='dashed', linewidth=2, label='Médiane')
    plt.axvline(moyenne + ecart_type, color='orange', linestyle='dotted', linewidth=2, label='Écart-Type (+1)')
    plt.axvline(moyenne - ecart_type, color='orange', linestyle='dotted', linewidth=2, label='Écart-Type (-1)')

    # Ajouter des labels et un titre
    plt.title('Distribution des Prix des Produits')
    plt.xlabel('Prix')
    plt.ylabel('Fréquence')
    plt.legend()
    plt.grid()

    # Afficher le graphique
    plt.show()


def main():
    choix = input("Voulez-vous entrer les prix manuellement (tapez '1') ou depuis un fichier (tapez '2') ? ")

    if choix == '1':
        # Saisie manuelle des prix
        prix_input = input("Entrez les prix des produits, séparés par des espaces : ")
        prix = [float(x) for x in prix_input.split()]

    elif choix == '2':
        # Lecture des prix depuis un fichier
        nom_fichier = 'TP2\\TP2_3\\' + input("Entrez le nom du fichier contenant les prix : ")
        try:
            with open(nom_fichier, 'r') as fichier:
                prix = [float(x) for x in fichier.read().split()]
        except FileNotFoundError:
            print("Le fichier spécifié n'existe pas.")
            return
        except ValueError:
            print("Erreur de format dans le fichier. Assurez-vous que les prix sont des nombres valides.")
            return

    else:
        print("Choix invalide.")
        return

    # Calcul des statistiques
    moyenne, variance, ecart_type, mediane = calculer_statistiques(prix)

    # Affichage des résultats
    print(f"Moyenne des prix : {moyenne:.2f}")
    print(f"Variance des prix : {variance:.2f}")
    print(f"Écart-type des prix : {ecart_type:.2f}")
    print(f"Médiane des prix : {mediane:.2f}")

    # Afficher le graphique
    afficher_graphique(prix, moyenne, mediane, ecart_type)


# Lancer le programme
if __name__ == "__main__":
    main()
