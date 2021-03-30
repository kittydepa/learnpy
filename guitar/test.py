def get_notes(key, intervals):
    # a sufficiently long sequence of notes to slice from
    whole_notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']*3
    # finding start of slice
    root = whole_notes.index(key)
    # taking 12 consecutive elements
    octave = whole_notes[root:root+12]
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
print('Notes of C major scale:\n{}'.format(get_notes('C', scales['major'])))
print('Notes of B minor scale:\n{}'.format(get_notes('B', scales['minor'])))
print('Notes of F# locrian scale:\n{}'.format(get_notes('F#', scales['locrian'])))
