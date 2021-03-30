whole_notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']*3


def get_notes(key, intervals):
    # a sufficiently long sequence of notes to slice from
    whole_notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']*3
    # finding start of slice
    root = whole_notes.index(key)
    # taking 12 consecutive elements
    octave = whole_notes[root:root+13]
    # accesing indexes specified by `intervals` to retrieve notes
    return [octave[i] for i in intervals]

scales = {
    "major" : [0, 2, 4, 5, 7, 9, 11],
    "minor" : [0, 2 , 3, 5, 7, 10, 11],
    "dorian" : [0,  2,  3,  5,  7,  9, 10, 12],
    "phrygian" : [0, 1, 3, 5, 7, 8, 10, 12],
    "minor_pentatonic" : [0, 3, 5, 7, 10],
    "major_pentatonic" : [0, 2, 4, 7, 9],
    "harmonic_minor" : [0, 2, 3, 5, 7, 8, 10, 12],
    "mixolydian": [0, 2, 4, 5, 7, 9, 10],
    "minor_blues" : [0, 3, 5, 6, 7, 10],
    "locrian" : [0, 1, 3, 5, 6, 8, 10, 12],
    "lydian" :[0, 2, 4, 6, 7, 9, 11, 12],
}
# print('Notes of C major scale:\n{}'.format(get_notes('C', scales['major'])))
# print('Notes of B minor scale:\n{}'.format(get_notes('B', scales['minor'])))
# print('Notes of F# locrian scale:\n{}'.format(get_notes('F#', scales['locrian'])))


## Step 2 bruh
# Creating strings of guitar
start_strings = []
strings = {i:0 for i in 'EADGB'}
for i in strings.keys():
    start = whole_notes.index(i)
    strings[i] = whole_notes[start:start+20]
print(strings.keys())

## setting up for the function
# print('Notes in the E string: ', strings['E'])
# print('Notes in the D string: ', strings['D'])


## the real fucnc
def find_notes(my_scale):
    notes_strings = {i:0 for i in "EADGB"}
    # for every string 
    for key in strings.keys():
        # we create an empty list of indexes
        indexes = []
        for note in my_scale.notes:
            # append index where note of the scale is found in
            ind = strings[key].index(note)
            indexes.append(ind)
            # because there are 20 frets, there are duplicate notes in the string
            if ind <= 7:
                # we must also append these to indexes
                indexes.append(ind+12)
        notes_strings[key] = indexes
    return notes_strings
    
# printing with the prev. func. 
# finding notes in a scale:
C_minor_blues = get_notes('C', scales['minor_blues'])
# finding positions of these notes in the guitar, as a dict
positions = find_notes(C_minor_blues)

print('Position of C minor blues in the guitar:')
for i in positions.keys():
    print('Notes in the {} string {}'.format(i, positions[i]))