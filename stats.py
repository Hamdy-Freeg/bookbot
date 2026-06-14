def get_book_text(filebath):
    with open(filebath, "r", encoding="utf-8") as file:
        book_data = file.read() 
    return book_data

def get_num_words(filebath) :
    book_data = get_book_text(filebath)
    return f"Found {len(book_data.split())} total words"

def sort_on(text: tuple[str, int]) -> int:
    return text[1]
    
def count_chars(filebath) :
    char_count = {}
    book_data = get_book_text(filebath).lower()
    for char in book_data : 
        if char in char_count:
            char_count[char] += 1
        else :
            char_count[char] = 1
    sorted_items = sorted(char_count.items(), key=sort_on, reverse=True)
    return dict(sorted_items)