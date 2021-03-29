# Scanner will take a string of raw input from a user
# It will return a sentence that is composed of a list of tuples with the (TOKEN, WORD) pairing.
# If a word is NOT part of lexicon, it should still return WORD but set the TOKEN to an error. 
    ## This error token will tell the user they messed up

"""
# Base stuff

stuff = input('> ')
words = stuff.split()


# Lexicon Tuples

first_word = ('verb', 'go')
second _word = ('direction', 'north')
third_word = ('direction', 'west')


"""
class Numbers:

    def convert_number(self, s):
        try:
            return int(s)
        except ValueError:
            return None



class UserInput(Numbers):
    
    def __init__(self):
       self.lexicon = dict()
    
    lexicon = {
            'directions': ['north', 'south', 'east', 'west'],
                'verbs': ['go', 'stop', 'kill', 'eat'],
                'stops': ['the', 'in', 'of', 'from', 'at', 'it'],
                'nouns': ['door', 'bear', 'princess', 'cabinet'],
                'numbers': Numbers(),
        }

    def scan(self, input):
        self.input = input()

        if UserInput in input:
            #return[LEXICON THING_ THINK OF THE PASSPORT EXAMPLE WITH DICTS!]
            print("This shit worked!")
    
    # def scan(self, stuff, words): # Not sure what to call the latter
    #     stuff = input("> ")
    #     words = stuff.split()    



# def scan(input):
#     if input == "go":
#         return [('verb', 'go')]
#lexicon = UserInput()

