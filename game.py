"""
Notation via https://github.com/jclopes/hive
"""
from hive import Location, Piece, Move
from hive import LOCATIONS, LOCATION_NAMES, PLAYERS, PIECE_TYPES, PIECE_NOS

HEADER_LINE = '+++++'
PIECE_STR_LEN = 3
LOC_STR_LEN = 2

def parse_header_and_content(lines):
    head_lines = []
    for i, line in enumerate(lines):
        if HEADER_LINE in line:
            return lines[:i], lines[i+1:]

def read(infile):
    with open(infile) as f:
        return parse_header_and_content(f.readlines())

def write(moves, outfile, head_lines=None):
    with open(outfile, 'w') as f:
        if head_lines:
            f.write('\n'.join(head_lines) + '\n')
        f.write(HEADER_LINE + '\n')
        for move in moves:
            f.write(move.write() + '\n')

def parse_location(loc_str):
    if len(loc_str) != LOC_STR_LEN:
        return None
    assert loc_str in LOCATIONS
    loc_name = LOCATION_NAMES[loc_str]
    loc_index = LOCATIONS.index(loc_str)
    return Location(loc_str, loc_name, loc_index)

def parse_piece(piece_str):
    if len(piece_str) != PIECE_STR_LEN:
        return None
    player = piece_str[0].lower()
    piece_type = piece_str[1].upper()
    assert piece_str[2].isdigit()
    piece_no = int(piece_str[2])

    assert player in PLAYERS
    assert piece_type in PIECE_TYPES
    assert piece_type in PIECE_NOS
    assert piece_no <= PIECE_NOS[piece_type]

    return Piece(player, piece_type, piece_no)

def parse_move(line):
    piece_from = line[:PIECE_STR_LEN]
    loc = line[PIECE_STR_LEN:PIECE_STR_LEN+LOC_STR_LEN]
    piece_to = line[PIECE_STR_LEN+LOC_STR_LEN:PIECE_STR_LEN+LOC_STR_LEN+PIECE_STR_LEN]
    assert len(piece_from) == PIECE_STR_LEN
    return Move(parse_piece(piece_from), parse_location(loc), parse_piece(piece_to))

def parse(head_lines, game_lines):
    return [parse_move(line) for line in game_lines]

def load_game(infile):
    return parse(*read(infile))

if __name__ == '__main__':
    infile = 'game.hive'
    outfile = 'game2.hive'
    moves = load_game(infile)
    print '\n'.join([str(x) for x in moves])
    write(moves, outfile)
