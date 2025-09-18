from stats import get_word_count
from stats import get_letter_count

def get_book_text(relative_path:str):
    """ Prend en parametre <relative_path:str> un chemin relatif et retourne le contenu du fichier. """
    file_text = str()
    with open(relative_path) as f:
        file_text = f.read()

    return file_text
def main():
    print(get_letter_count(get_book_text("./books/frankenstein.txt")))


main()
