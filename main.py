def get_book_text(relative_path:str):
    """ Prend en parametre <relative_path:str> un chemin relatif et retourne le contenu du fichier. """
    file_text = str()
    with open(relative_path) as f:
        file_text = f.read()
    return file_text

def get_word_count(text:str):
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count
    

def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    wc = get_word_count(text)
    print(f"{wc} words found in the document")


main()
