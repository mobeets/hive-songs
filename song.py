from game import load_game
from settings import load_params

"""
http://www.html5rocks.com/en/tutorials/webaudio/intro/
http://blog.teamtreehouse.com/building-a-synthesizer-with-the-web-audio-api
"""

class SongPart:
    def __init__(self, inst):
        self.inst = inst
        self.measures = {}

    def play(self, i, pitch):
        self.measures[i] = pitch

class Song:
    def __init__(self, params, drums, insts):
        """
        pan represents player
        inst represents piece_type
        rthm represents piece_number
        octave represents whether piece is source or target
        pitch_index represents location of piece being moved, w.r.t. the target piece
        """
        self.params = params # bpm, key, scale
        self.drums = drums # instrument for drum beat
        self.insts = insts # instruments for both players
        self.measure_index = 0

    def begin(self):
        self.parts = dict((inst, SongPart(inst)) for inst in self.insts)
        self.parts[self.drums] = SongPart(self.drums)
        self.measure_index = 0

    def get_pitch(self, octave, pitch_index):
        return 440*octave

    def play_inst(self, inst, ind, octave, pitch_index):
        """
        single instrument playing a single pitch at a given rhythm, for one measure, at given pan
        """
        pitch = self.params.get_freq_from_index(pitch_index, octave)
        self.parts[inst].play(ind, pitch)

    def play_drums(self, ind):
        self.parts[self.drums].play(ind, None)

    def play(self, move):
        """
        plays next measure of song using move
            each measure includes a melody for drum beat, moving piece, and target piece
        """
        self.measure_index += 1
        self.play_drums(self.measure_index)
        self.play_inst(inst=self.insts[move.piece_from], ind=self.measure_index, octave=1, pitch_index=1)
        if move.piece_to:
            self.play_inst(inst=self.insts[move.piece_to], ind=self.measure_index, octave=2, pitch_index=move.loc.index)

    def play_all(self, moves):
        return [self.play(move) for move in moves]

def main(gamefile, paramsfile, outfile):
    params, drums, insts = load_settings(paramsfile)
    song = Song(params, drums, insts)
    moves = load_game(gamefile)
    song.play_all(moves)

if __name__ == '__main__':
    gamefile = 'game.hive'
    paramsfile = 'default.hive-params'
    outfile = 'game.wav'
    main(gamefile, paramsfile, outfile)
