lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'west': 'direction',
    'down':'direction',
    'up':'direction',
    'left':'direction',
    'right':'direction',
    'go': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'door':'noun',
    'bear': 'noun',
    'princess': 'noun',
    'dollar': 'money',
    'pound': 'money',
    'kronor': 'money',
    'miles': 'distance',
    'km': 'distance',
    'meter': 'distance',
}

def scan(sentence):
    sentence = sentence.split()
    result = []
    """ sentence got its value from scan('input').
        Then it splits it up in parts and will be values 
        for word in the loop.
        For each loop word compare its value(part) 
        to the content in lexicon."""
    for word in sentence:
        wordtype = lexicon.get(word, 'error')
        pair = (wordtype, word)

        """If there is a match it will append the wordtype + word to result. """
        if word in lexicon:
            result.append(pair)

            """ Then it look if it is a number(str). 
            If so it convert it with function convert_int to a integer. 
            Then pair adds 'number + the integer to a."""
        elif word not in lexicon:
            number = convert_number(word)
            if number:
                pair = ('number', number)
                
                """If neither of the two previous condition is met, 
                it sets pair to wordtype with its default value (error)"""
            elif word not in lexicon and not number:
                pair = (wordtype, word)

            result.append(pair) # This append from conditions #2 and #3

    print (result)  # For humans
    return result # For python
    
# This function is used in condition #2
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

if __name__ == '__main__':
    sentence = input('write something:> ')
    sentence = sentence.lower()

    scan(sentence)


# NOT MY CODE
# COPIED FROM https://forum.learncodethehardway.com/t/pytest-for-ex48-for-python3/2418
# ON GIT: https://raw.githubusercontent.com/ulfsjodin/ex48/master/lexicon2.py