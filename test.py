from stats import get_letter_count
from stats import get_word_count
from stats import get_letter_count

alphabet ={
 'a': 0, 'b': 8, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0,
 't': 0, 'u': 0, 'v': 3, 'w': 0, 'x': 1, 'y': 56, 'z': 0
}


def get_book_text(relative_path:str):
    """ Prend en parametre <relative_path:str> un chemin relatif et retourne le contenu du fichier. """
    file_text = str()
    with open(relative_path) as f:
        file_text = f.read()

    return file_text





def main():
    entree = get_letter_count(get_book_text("./books/frankenstein.txt"))
    word_list = []
    for a in entree:
        word_list.append({"char":a,
                             "num":entree[a]})
        
       
    print(word_list)

main()
    
    

