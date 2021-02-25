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


class UserInput:
    
    def lexicon(self):
        lexicon = {
            'directions': ['north', 'south', 'east', 'west'],
            'verbs': ['go', 'stop', 'kill', 'eat'],
            'stops': ['the', 'in', 'of', 'from', 'at', 'it'],
            'nouns': ['door', 'bear', 'princess', 'cabinet'],
            'numbers': Numbers(),
        }
        print(lexicon)

    def scan(self, stuff, words): # Not sure what to call the latter
        stuff = input('> ')
        words = stuff.split()
    
    

# NEED TO DEFINE SCAN SOMEWHERE!

x = UserInput()
x.lexicon() 