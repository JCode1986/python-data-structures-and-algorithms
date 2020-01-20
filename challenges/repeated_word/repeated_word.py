def repeated_word(string):
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