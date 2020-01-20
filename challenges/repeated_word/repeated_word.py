def first_repeated_word(string):
    """
    Function that returns that first repeated word in a string
    In: String
    out: String
    """

    word_split = string.lower().split(' ')
    word_list = []

    for word in word_split:
        if word in word_list:
            return word
        word_list.append(word)
    
    return None

def most_repeated_word(string):
    """
    Function that returns that most repeated word in a string
    In: String
    out: String
    """

    word_list = string.lower().split(' ')
    dictionary = {}
    most_repeated_value = 0
    most_repeated_key = ''

    i = 0
    for word in word_list:
        if word_list[i] in dictionary:
            dictionary[word_list[i]] += 1
        
        else:
            dictionary[word_list[i]] = 1
        i += 1

    j = 0
    for key in dictionary:
        current_val = dictionary.get(key)
        if current_val:
            if current_val > most_repeated_value:
                most_repeated_value = current_val
                most_repeated_key = key
        j += 1
    
    return most_repeated_key