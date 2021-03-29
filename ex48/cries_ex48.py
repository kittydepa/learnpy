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
    sentence = sentence.split() # Split it up into different words
    result = [] # Start empty, so we can fill it later upon return

    for word in sentance:
        wordtype = lexicon.get(word, 'error') # get with a dict will give the key, and second argument is just want we want to print when the input is not valid..Here get the words from the lexicon dict
        pair = (wordtype, word) # we want them with the words, the key and what the user input

        if for in lexicon:
            result.append(pair) # If user input is valid, then make it a pair!
        elif word not in lexicon:
            number = convert_number(word) # convert string to into
            if number:
                pair = ('number', number) # return the result similar to if it were a words
        elif word not in lexicon and not number:
            pair = (wordtype, word) # otherwise, just this, already address the error. This helps us see WHICH word was the error exactly

            result.append(pair) #put condition 2 and 3 together

    print(result) # For humans
    return result

# The equation for str to int conversion, used above
def convert_number(s):
    try: #used for user input, catching errors
        return int(s)
    except ValueError:
        return None


if __name__ == '__main__':
    sentence = input('write something> ')
    sentence - sentence.lower() # cuz the dict lexicon is in lower

    scan(sentence) # Run the user input with our functions!
