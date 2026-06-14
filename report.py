from stats import get_num_words, count_chars

def format(filepath):
    message = get_num_words(filepath)
    char_list = count_chars(filepath)
    

    print("============ BOOKBOT ============")
    print("Analyzing book found at ", filepath, "...")
    print("----------- Word Count ----------")
    print(message)
    print("--------- Character Count -------")
    for key in char_list : 
        if key.isalpha() :
            print(key, ": ", char_list[key])
            
    print("============= END ===============")