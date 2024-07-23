"""
Analyse de la fréquence des lettres d'un texte
"""

from unidecode import unidecode


def input_sentence():
    """
    Demande à l’utilisateur de rentrer une phrase
    :return: La phrase
    """

    user_input = input("Enter sentence :")
    return user_input


def normalize_sentence(string):
    """
    Normalise une phrase en la convertissant en minuscules et en supprimant les accents.
    :param string:Chaine de caractère
    :return: La phrase en minuscule et sans accent
    """
    string = string.lower()
    string = unidecode(string)
    return string
