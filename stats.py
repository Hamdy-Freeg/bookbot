def get_number_of_words(list_of_words):

    cnt = 0

    for word in list_of_words :
        cnt +=1
    
    return cnt

def characters_count(txt_file) :
    char_count = {}
    for char in txt_file :
        lower_char = char.lower()
        if lower_char.isalpha():
            if lower_char in char_count:
                char_count[lower_char] += 1
            else : 
                char_count[lower_char] = 1
    sorted_dict = dict(sorted(char_count.items()))

    return sorted_dict
