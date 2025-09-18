

def get_word_count(text:str):
    """ Prend en paramètre un texte <text> et retourne le nombre de mot """
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def get_letter_count(text:str):
    alphabet ={
 'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0,
 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
}
    for letter in text:
        low_letter = letter.lower()
        if low_letter in alphabet:
            alphabet[low_letter] += 1
        else:
            alphabet[low_letter] = 1
    return alphabet
    