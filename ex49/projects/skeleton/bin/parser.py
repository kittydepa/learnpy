# Starting with the exception we need for a parsing error:

class ParserError(Exception):
    pass


class Sentence:

    def __init__(self, subject, verb, object):
        # remember, we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1] # why [1] for these?
        # Just make simple classes here!

# ------------- End of Sentence() class -------------- #



# Are functions that make up the parser

def peek(word_list): # to make decisions about what kind of setnence we're dealing with, based on the next word...
                         # then call another function to consume that word and carry on- see the next funct
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


# skip words that are not useful, the 'stop words'
# This will skip not JUST 1 word, but skip over all stop words
def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)


def parse_verb(word_list):
    skip(word_list, 'stop') #We skip any stop words, then peek to see if the next work is a verb.

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(word_list): # Here we handle both a noun and directions
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")


def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")



# Finally, where the magic happens
def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
