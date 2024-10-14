import statistics
import matplotlib.pyplot as plt
import os


def calculer_statistiques(prix):
    """Calcul des statistiques pour une liste de prix."""
    moyenne = sum(prix) / len(prix)
    variance = sum((x - moyenne) ** 2 for x in prix) / len(prix)
    ecart_type = variance ** 0.5
    mediane = statistics.median(prix)
    return moyenne, variance, ecart_type, mediane


def afficher_graphique(prix, moyenne, mediane, ecart_type):
    """Affiche un histogramme des prix avec des lignes pour les statistiques."""
    plt.figure(figsize=(10, 6))
    plt.hist(prix, bins=10, alpha=0.7, color='blue', edgecolor='black')

    plt.axvline(moyenne, color='red', linestyle='dashed', linewidth=2, label='Moyenne')
    plt.axvline(mediane, color='green', linestyle='dashed', linewidth=2, label='Médiane')
    plt.axvline(moyenne + ecart_type, color='orange', linestyle='dotted', linewidth=2, label='Écart-Type (+1)')
    plt.axvline(moyenne - ecart_type, color='orange', linestyle='dotted', linewidth=2, label='Écart-Type (-1)')

    plt.title('Distribution des Prix des Produits')
    plt.xlabel('Prix')
    plt.ylabel('Fréquence')
    plt.legend()
    plt.grid(axis='y', alpha=0.75)

    plt.show()


def main():
    choix = input("Voulez-vous entrer les prix manuellement (tapez '1') ou depuis un fichier (tapez '2') ? ")

    prix = []

    if choix == '1':
        # Saisie manuelle des prix
        prix_input = input("Entrez les prix des produits, séparés par des espaces : ")
        try:
            prix = [float(x) for x in prix_input.split()]
        except ValueError:
            print("Erreur : Veuillez entrer uniquement des nombres valides.")
            return

    elif choix == '2':
        # Get the current script directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Lecture des prix depuis un fichier
        nom_fichier = current_dir + '\\' +input("Entrez le nom du fichier contenant les prix : ")

        try:
            with open(nom_fichier, 'r') as fichier:
                prix = [float(x) for x in fichier.read().split()]
        except FileNotFoundError:
            print(f"Le fichier {nom_fichier} est introuvable.")
            return
        except ValueError:
            print("Erreur de format dans le fichier. Assurez-vous que les prix sont des nombres valides.")
            return

    else:
        print("Choix invalide.")
        return

    if not prix:
        print("Erreur : Aucune donnée de prix valide n'a été fournie.")
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
