from stats import get_word_count
from stats import get_letter_count
from stats import format_dic

def get_book_text(relative_path:str):
    """ Prend en parametre <relative_path:str> un chemin relatif et retourne le contenu du fichier. """
    file_text = str()
    with open(relative_path) as f:
        file_text = f.read()

    return file_text

def main():
    relative_path = "./books/frankenstein.txt"
    book = get_book_text(relative_path)

    letter_count = get_letter_count(book)
    sorted_dict = (format_dic(letter_count))
    word_count = get_word_count(book)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {relative_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for i in range(0,len(sorted_dict)):
        print(f"{sorted_dict[i]["char"]}: {sorted_dict[i]["num"]}")
    print("============= END ===============")
    

main()
