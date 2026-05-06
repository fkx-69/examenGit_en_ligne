"""Petit jeu de devinette genere avec l'aide d'une IA."""

import random

from mesfonctions import est_pair


def generer_nombre_secret(minimum=1, maximum=100):
    """Genere le nombre a deviner."""
    if minimum > maximum:
        raise ValueError("Le minimum doit etre inferieur ou egal au maximum.")
    return random.randint(minimum, maximum)


def analyser_proposition(proposition, secret):
    """Compare la proposition du joueur avec le nombre secret."""
    if proposition < secret:
        return "trop petit"
    if proposition > secret:
        return "trop grand"
    return "gagne"


def demander_entier(message):
    """Demande un entier au joueur jusqu'a obtenir une saisie valide."""
    while True:
        saisie = input(message)
        try:
            return int(saisie)
        except ValueError:
            print("Veuillez entrer un nombre entier.")


def jouer():
    """Lance une partie interactive."""
    minimum = 1
    maximum = 100
    essais_max = 7
    secret = generer_nombre_secret(minimum, maximum)

    print("=== Jeu de devinette ===")
    print(f"Devinez le nombre secret entre {minimum} et {maximum}.")
    print(f"Vous avez {essais_max} essais.")
    print("Indice: le nombre secret est pair." if est_pair(secret) else "Indice: le nombre secret est impair.")

    for essai in range(1, essais_max + 1):
        proposition = demander_entier(f"Essai {essai}/{essais_max} - Votre proposition: ")
        resultat = analyser_proposition(proposition, secret)

        if resultat == "gagne":
            print(f"Bravo, vous avez gagne en {essai} essai(s) !")
            return True

        print(f"C'est {resultat}.")

    print(f"Perdu ! Le nombre secret etait {secret}.")
    return False


if __name__ == "__main__":
    jouer()
