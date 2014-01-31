"""
INSTRUMENTS
    Queen = wind
    Beetle = bass
    Spider = horns
    Grasshopper = strings
    Ant = synth
RHYTHMS
    Queen 1 = whole note
    Beetle 1 = half note + half rest
    Beetle 2 = half rest + half note
    Spider 1 = triplet starts measure
    Spider 2 = triplet ends measure
    Ant 1 = quarter rest + quarter note + quarter note + quarter rest
    Ant 2 = quarter note + quarter note + quarter note + quarter rest
    Ant 3 = quarter note + quarter note + quarter note + quarter note
    Grasshopper 1 = quarter note + quarter rest + quarter note + quarter note
    Grasshopper 2 = quarter note + quarter note + quarter rest + quarter note
    Grasshopper 3 = quarter note + quarter rest + quarter note + quarter rest
"""

from hive import all_pieces

QUARTER_NOTE = 24
HALF_NOTE = QUARTER_NOTE*2
WHOLE_NOTE = QUARTER_NOTE*4
C_MAJOR = [261.63, 293.66, 329.63, 349.23, 392, 440, 493.88]

class SongParams:
    def __init__(self, bpm, scale):
        self.bpm = bpm
        self.scale = scale

    def get_freq_from_index(self, index, octave):
        return self.scale[index]*octave

RTHM_LOOKUP = {
    ('Q', 1): [(1, WHOLE_NOTE)],
    ('B', 1): [(1, HALF_NOTE), (0, HALF_NOTE)],
    ('B', 2): [(0, HALF_NOTE), (1, HALF_NOTE)],
    ('S', 1): [(1, EIGTH_NOTE), (1, EIGTH_NOTE), (1, EIGTH_NOTE), (0, 3*QUARTER_NOTE)],
    ('S', 2): [(0, 3*QUARTER_NOTE), (1, EIGTH_NOTE), (1, EIGTH_NOTE), (1, EIGTH_NOTE)],
    ('A', 1): [(0, QUARTER_NOTE), (1, QUARTER_NOTE), (1, QUARTER_NOTE), (0, QUARTER_NOTE)],
    ('A', 2): [(1, QUARTER_NOTE), (1, QUARTER_NOTE), (1, QUARTER_NOTE), (0, QUARTER_NOTE)],
    ('A', 3): [(1, QUARTER_NOTE), (1, QUARTER_NOTE), (1, QUARTER_NOTE), (1, QUARTER_NOTE)],
    ('G', 1): [(1, QUARTER_NOTE), (0, QUARTER_NOTE), (1, QUARTER_NOTE), (1, QUARTER_NOTE)],
    ('G', 2): [(1, QUARTER_NOTE), (1, QUARTER_NOTE), (0, QUARTER_NOTE), (1, QUARTER_NOTE)],
    ('G', 3): [(1, QUARTER_NOTE), (0, QUARTER_NOTE), (1, QUARTER_NOTE), (0, QUARTER_NOTE)],
}
INST_LOOKUP = {
    'Q': 'wind',
    'B': 'bass',
    'S': 'horns',
    'A': 'strings',
    'G': 'synth',
}

class Rhythm:
    def __init__(self, notes):
        self.notes = notes # [(ON/OFF, DURATION), ...]

class Instrument:
    def __init__(self, piece):
        self.piece = piece
        self.pan = -1 if piece.player == 'w' else 1
        self.rthm = Rhythm(RTHM_LOOKUP[(piece.piece_type, piece.piece_no)])
        self.name = INST_LOOKUP[(piece.piece_type, piece.piece_no)]

def all_instruments():
    return dict((piece, Instrument(piece)) for piece in all_pieces())

def load_settings(infile):
    params = SongParams(120, C_MAJOR)
    drums = None
    insts = all_instruments()
    return params, drums, insts
