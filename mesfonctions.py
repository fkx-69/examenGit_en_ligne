"""Collection de fonctions generees avec l'aide d'une IA.

Ce module regroupe 10 fonctions independantes et faciles a tester.
"""


def addition(a, b):
    """Retourne la somme de deux nombres."""
    return a + b


def soustraction(a, b):
    """Retourne la difference entre deux nombres."""
    return a - b


def multiplication(a, b):
    """Retourne le produit de deux nombres."""
    return a * b


def division(a, b):
    """Retourne le quotient de deux nombres."""
    if b == 0:
        raise ValueError("La division par zero est impossible.")
    return a / b


def est_pair(nombre):
    """Indique si un nombre entier est pair."""
    return nombre % 2 == 0


def factorielle(nombre):
    """Calcule la factorielle d'un entier positif ou nul."""
    if nombre < 0:
        raise ValueError("La factorielle n'existe pas pour un nombre negatif.")

    resultat = 1
    for valeur in range(2, nombre + 1):
        resultat *= valeur
    return resultat


def inverser_chaine(texte):
    """Inverse les caracteres d'une chaine."""
    return texte[::-1]


def compter_voyelles(texte):
    """Compte les voyelles dans une chaine."""
    voyelles = "aeiouyAEIOUY"
    return sum(1 for caractere in texte if caractere in voyelles)


def maximum_liste(nombres):
    """Retourne le plus grand nombre d'une liste non vide."""
    if not nombres:
        raise ValueError("La liste ne doit pas etre vide.")
    return max(nombres)


def moyenne(nombres):
    """Retourne la moyenne d'une liste non vide de nombres."""
    if not nombres:
        raise ValueError("La liste ne doit pas etre vide.")
    return sum(nombres) / len(nombres)
