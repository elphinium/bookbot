

def get_word_count(text:str):
    """ Prend en paramètre un texte <text> et retourne le nombre de mot """
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count