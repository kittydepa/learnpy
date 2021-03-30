# https://betterprogramming.pub/how-to-learn-guitar-with-python-978a1896a47?fbclid=IwAR1dMg6yxfgASXhz-pyyyfwW_cbOJC3FfXzRnbRs1F_ElYduxjW-QtzRY_I&gi=53f4904528e7

# Using the intervals of a given scale as indexes.
# Two octaves worth of notes
whole_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G',
                    'G#', 'A', 'A#', 'B'] * 3
# # Example, index where element 'B' is located.
# root = whole_notes.index('B')
#
# # Starting from this index, slice 12 elements
# B = whole_notes[root:root + 12]
#
# # print(B) # B Chromatic scale
#
# # Using the major scale intervals to retrive the B major scale
# major_scale = [0, 2, 4, 5, 7, 9, 11]
#
# notes = [B[i] for i in major_scale]
# print("B major scale:", notes)
#
# # Notes contained in another scale,
# another_scale = [0, 2, 5, 10, 11]
# notes = [B[i] for i in another_scale]
# print('Some scale: ', notes)

## STEP 1
# A function that summarises the above code, to retrieve any major_scale
def get_notes(key, intervals):
    """Given any key C, C#...B
        and intervals z.B Tone Tone Semitone"""

    whole_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G',
                    'G#', 'A', 'A#', 'B'] * 3 # A long seq. of notes to slice from

    root = whole_notes.index(key) # Finding start of slice
    octave = whole_notes[root:root + 13] # taking 12 consecutive elements
    return [octave[i] for i in intervals] # accessing indexes specified by 'intervals' to retrive notes

## STEP 2
# Creating a dict with commone musical scales!
scales = {
    "major" : [0, 2, 4, 5, 7, 9, 11],
    "minor" : [0, 2, 3, 5, 7, 10, 11],
    "dorian" : [0, 2, 3, 4, 7, 9, 10, 12],
    "phrygian" : [0, 1, 3, 5, 7, 8, 10, 12],
    "minor_pentatonic" : [0, 3, 5, 7, 10],
    "major_pentatonic" : [0, 2, 4, 7, 9],
    "harmonic_minor" : [0, 2, 3, 5, 7, 8, 10, 12],
    "mixolydian" : [0, 2, 4, 5, 7, 9, 10],
    "minor_blues" : [0, 3, 5, 6, 7, 10],
    "locrian" : [0, 1, 3, 5, 6, 8, 10, 12],
    "lydian" : [0, 2, 4, 6, 7, 9, 11, 12],
}

# Now, we have an easy way of accessing the notes of any scale, start at any root!
#print("A minor scale: ", get_notes('A', scales['minor']))
print("Test: ", get_notes('E', scales['minor_blues']))


## STEP 3 MAKING THE GUITAR
# making a dict with the name of the strings as its keys
strings = {i:0 for i in 'EADGB'}
for i in strings.keys():
    start = whole_notes.index(i)
    strings[i] = whole_notes[start:start + 20] # Shows up in ErrorLens, but runs without error?

print(strings.keys())
print("Notes on the E string: ", strings['E'])