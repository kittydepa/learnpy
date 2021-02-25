class Numbers:

    def convert_number(self, s):
        try:
            return int(s)
        except ValueError:
            return None


class UserInput:

    lexicon = {
        'directions': ['north', 'south', 'east', 'west'],
        'verbs': ['go', 'stop', 'kill', 'eat'],
        'stops': ['the', 'in', 'of', 'from', 'at', 'it'],
        'nouns': ['door', 'bear', 'princess', 'cabinet'],
        'numbers': Numbers(),
    }

