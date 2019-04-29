from data_preprocess import *
import pickle
import glob

def extract_notes(verbose=False):

    """ Get all the notes and chords from the midi files in the ./input_music directory """

    notes=[]
    for file in glob.glob("input_music/*.mid"):
        midi = converter.parse(file)
        notes_to_parse = None
        if (verbose):
            print("Parsing file :  %s" % file)
        try:  # file has instrument parts
            s2 = instrument.partitionByInstrument(midi)
            notes_to_parse = s2.parts[0].recurse()
        except:  # file has notes in a flat structure
            notes_to_parse = midi.flat.notes
        for nt in notes_to_parse:
            if isinstance(nt, note.Note):
                notes.append(str(nt.pitch))
            elif isinstance(nt, chord.Chord):
                notes.append('.'.join(str(n) for n in nt.normalOrder))
    with open('notes', 'wb') as filepath:
        pickle.dump(notes, filepath)

    return notes

#execute:
extract_notes(True)