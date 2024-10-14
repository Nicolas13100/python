import os

import matplotlib.pyplot as plt

def lire_notes_depuis_fichier(nom_fichier):
    """Lit les notes depuis un fichier et les retourne sous forme de liste."""
    try:
        # Get the current script directory
        current_dir = os.path.dirname(os.path.abspath(__file__))

        with open(current_dir + '\\' + nom_fichier, 'r') as fichier:
            contenu = fichier.read()
            notes = list(map(float, contenu.split()))
            return notes
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} est introuvable.")
        return []
    except ValueError:
        print("Erreur dans le format des notes dans le fichier.")
        return []

def entrer_notes():
    """Demande à l'utilisateur d'entrer des notes séparées par des espaces."""
    notes_input = input("Entrez les notes des étudiants, séparées par des espaces : ")
    return list(map(float, notes_input.split()))

def calculer_moyenne(notes):
    """Calcule la moyenne des notes."""
    return sum(notes) / len(notes) if notes else 0

def calculer_mediane(notes):
    """Calcule la médiane des notes."""
    notes_triees = sorted(notes)
    n = len(notes_triees)
    if n == 0:
        return 0
    elif n % 2 == 1:
        return notes_triees[n // 2]
    else:
        return (notes_triees[n // 2 - 1] + notes_triees[n // 2]) / 2

def afficher_histogramme(notes):
    """Affiche un histogramme des notes."""
    plt.figure(figsize=(10, 6))
    plt.hist(notes, bins=10, alpha=0.7, color='blue', edgecolor='black')
    plt.title('Histogramme des Notes des Étudiants')
    plt.xlabel('Notes')
    plt.ylabel('Nombre d\'Étudiants')
    plt.axvline(calculer_moyenne(notes), color='red', linestyle='dashed', linewidth=1, label='Moyenne')
    plt.axvline(calculer_mediane(notes), color='green', linestyle='dashed', linewidth=1, label='Médiane')
    plt.legend()
    plt.grid(axis='y', alpha=0.75)
    plt.show()

def afficher_boite_a_moustaches(notes):
    """Affiche une boîte à moustaches des notes."""
    plt.figure(figsize=(8, 5))
    plt.boxplot(notes, vert=False)
    plt.title('Boîte à Moustaches des Notes des Étudiants')
    plt.xlabel('Notes')
    plt.grid(axis='x', alpha=0.75)
    plt.show()

def main():
    """Fonction principale pour exécuter le programme."""
    choix = input("Voulez-vous entrer les notes manuellement (M) ou à partir d'un fichier (F) ? ").strip().upper()
    if choix == 'F':
        nom_fichier = input("Entrez le nom du fichier : ")
        notes = lire_notes_depuis_fichier(nom_fichier)
    elif choix == 'M':
        notes = entrer_notes()
    else:
        print("Choix invalide.")
        return

    if not notes:
        print("Aucune note valide n'a été entrée.")
        return

    moyenne = calculer_moyenne(notes)
    mediane = calculer_mediane(notes)

    print(f"La moyenne des notes est : {moyenne:.2f}")
    print(f"La médiane des notes est : {mediane:.2f}")

    afficher_histogramme(notes)
    afficher_boite_a_moustaches(notes)

if __name__ == "__main__":
    main()
