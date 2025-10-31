import sys
from stats import get_number_of_words, characters_count

def get_book_text(filepath) :
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def get_list_of_words(txt_file):
    words = txt_file.split()
    return words

    

def main(): 
    sysArg = sys.argv

    if len(sysArg) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    book_text = get_book_text(filepath)

    words = get_list_of_words(book_text)

    word_number = get_number_of_words(words)

    char_count_list = characters_count(book_text)

    print("=================== BOOKBOT ===================\n")
    print(f"Analyzing book found at {filepath} \n")
    print("------------------ Word count -----------------\n")
    print(f" Found {word_number} total words\n")

    print("--------------- Character Count ---------------\n")

    for char , count in char_count_list.items() :
        print(f"{char} : {count}")



if __name__ == "__main__":
    main()

