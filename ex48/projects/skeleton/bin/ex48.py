"""
# Base stuff

stuff = input('> ')
words = stuff.split()


# Lexicon Tuples

first_word = ('verbä', 'go')
second _word = ('direction', 'north')
third_word = ('direction', 'west')


"""


class Numbers:

    def convert_number(self, s):
        try:
            return int(s)
        except ValueError:
            return None


class UserInput:

    def lexicon(self):
        x_lexicon = {
                'directions': ['north', 'south', 'east', 'west'],
                'verbs': ['go', 'stop', 'kill', 'eat'],
                'stops': ['the', 'in', 'of', 'from', 'at', 'it'],
                'nouns': ['door', 'bear', 'princess', 'cabinet'],
                'numbers': Numbers(),
            }
        #return x_lexicon
        print(x_lexicon)
    
    def scan(self, words):
        return self

# NEED TO DEFINE SCAN SOMEWHERE!

x = UserInput()
x.lexicon() 