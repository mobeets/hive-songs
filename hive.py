LOCATIONS = ['/*', '|*', '\*', '*\\', '*|', '*/', '=*']
LOCATION_NAMES = {'/*': 'NW', '|*': 'W', '\*': 'SW', '*\\': 'NE', '*|': 'E', '*/': 'SE', '=*': 'TOP'}
PLAYERS = ['w', 'b']
PIECE_TYPES = ['Q', 'A', 'B', 'G', 'S']
PIECE_NOS = {'Q': 1, 'A': 3, 'B': 2, 'G': 3, 'S': 2}

def all_pieces():
    pcs = []
    for p in PLAYERS:
        for pt, no in PIECE_NOS.iteritems():
            for i in range(no):
                pcs.append(Piece(p, pt, i+1))
    return pcs

class Location(object):
    def __init__(self, key, name, index):
        self.key = key
        self.name = name
        self.index = index

    def write(self):
        return self.key

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'Location({0}, {1}, {2})'.format(self.key, self.name, self.index)

class Piece(object):
    def __init__(self, player, piece_type, piece_no):
        self.raw = player + piece_type + str(piece_no)
        self.player = player
        self.piece_type = piece_type
        self.piece_no = piece_no

    def write(self):
        return self.player + self.piece_type + str(self.piece_no)

    def __ne__(self, other):
        return not self == other

    def __eq__(self, other):
        return self.raw == other.raw

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'Piece({0}, {1}, {2}, {3})'.format(self.raw, self.player, self.piece_type, self.piece_no)

class Move(object):
    def __init__(self, piece_from, loc, piece_to):
        self.piece_from = piece_from
        self.loc = loc
        self.piece_to = piece_to

    def write(self):
        tail = ''
        if self.loc and self.piece_to:
            tail = self.loc.write() + self.piece_to.write()
        return self.piece_from.write() + tail

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'Move({0}, {1}, {2})'.format(self.piece_from, self.loc, self.piece_to)
