def get_book_text(relative_path:str):
    """ Prend en parametre <relative_path:str> un chemin relatif et retourne le contenu du fichier. """
    file_text = str()
    with open(relative_path) as f:
        file_text = f.read()

    return file_text

def get_word_count(text:str):
    """ Prend en paramètre un texte <text> et retourne le nombre de mot """
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def get_letter_count(text:str):
    """ Prend en paramètre un texte <text> et retourne le nombre d'apparition de chaque lettre """
    alphabet ={
 'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0,
 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
}
    for letter in text:
        low_letter = letter.lower()
        if low_letter.isalpha():
            if low_letter in alphabet:
                alphabet[low_letter] += 1
            else:
                alphabet[low_letter] = 1
        else:
            continue
    return alphabet
    

def format_dic(dict_letter_number):
    """Prend un dictionnaire sous la forme {lettre:nombre}, le transforme sous la forme {"char":lettre,"num":nombre}  et le tri du plus grand nombre vers le plus petit"""
    word_list = []
    for a in dict_letter_number:
        word_list.append({"char":a,
                             "num":dict_letter_number[a]})
    word_list.sort(reverse=True, key=lambda d: d["num"] )
    return word_list

# def sort_letter_by_number_of_appariton(dict_letter_number):