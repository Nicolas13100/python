# -*-coding:Latin-1 -*

def start():
    while True:
        try:
            # Demander un entier positif ? l'utilisateur
            N = int(input("Entrez un entier positif inferieur a 1000: "))
            if N < 0 or N >= 1000:  # Correction here: should be "N < 0 or N >= 1000"
                print("Veuillez entrer un entier positif inf?rieur ? 1000.")
                continue

            somme = 0
            produit = 1
            nombres_pairs = []

            # Calcul de la somme et du produit des nombres pairs jusqu'? N
            for i in range(2, N + 1, 2):
                somme += i
                produit *= i
                nombres_pairs.append(i)

            # Afficher la somme
            print(f"Somme: {' + '.join(map(str, nombres_pairs))} = {somme}")

            # Afficher le produit
            print(f"Produit: {' * '.join(map(str, nombres_pairs))} = {produit}")

            # Demander ? l'utilisateur s'il veut recommencer
            recommencer = input("Voulez-vous recommencer? (oui/non): ").strip().lower()
            if recommencer not in ['oui', 'o']:
                print("Merci d'avoir utilis? le programme!")
                break

        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

# Ex?cution du programme
if __name__ == "__main__":
    start()
