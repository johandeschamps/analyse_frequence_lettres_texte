"""
Analyse de la fréquence des lettres d'un texte
"""
import unicodedata


def input_sentence():
    """
    Demande à l’utilisateur l’entrée d’une phrase
    :return: La phrase
    """

    user_input = input("Enter sentence :")
    return user_input


def normalize_sentence(string):
    """
    Normalise une phrase en la convertissant en minuscules et en supprimant les accents.
    :param input_str:Chaine de caractère
    :return: La phrase en minuscule et sans accent
    """
    string = string.lower()
    string = unicodedata.normalize('NFKD', string)
    chaine = ''.join([c for c in string if not unicodedata.combining(c)])
    return string