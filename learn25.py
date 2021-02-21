def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words  #Just calling words, once you defined what it is, will split  it up.

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word) #popping off means getting rid of it. Always OVERRIDES the new word list with it popped off.

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word) # same as previos f(x), but with the last word in the list.

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of a sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


# TIP if you run this in a terminal and do help(filename), it will show you all the functions,
# And that you have wrote in the comments! :)
