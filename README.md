HIVE SONG
----------
The song represents the notation of the game, from beginning to end.
Each player's own unique drum beat plays as long as he is alive.
Each measure encodes a move in the game.

HOW
----
In each measure, two instruments will play, one representing the piece being moved, the second representing the piece the first piece is moved to.
The instrument for the origin piece (the one being moved) will play in the bass clef.
The instrument for the destination piece will play in the tenor clef.

QUESTIONS
----------
What is the key of the song?

MAPPINGS
---------
player = L pan / R pan
origin/destination = bass clef / tenor clef
piece type = instrument
piece count = rhythm pattern
destination location = note/pitch

    INSTRUMENTS
    ------------
    Queen = wind
    Beetle = bass
    Spider = horns
    Grasshopper = strings
    Ant = synth

    RHYTHMS
    --------
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

    PITCHES (w.r.t. key)
    ---------------------
    N = 1
    NE = 2
    SE = 3
    S = 4
    SW = 5
    NW = 6
    OVER = 7

NOTATION (via https://github.com/jclopes/hive)
----------
Assuming one {MOVE} per line.
No validation done--assuming game is legal.
Header information above ++++++ line.
First move will just be {PIECE_MOVING}

    {MOVE} = {PIECE_MOVING}{POINT_OF_CONTACT}{PIECE_TARGET}

        {PIECE_*} = {PLAYER}{PIECE_TYPE}{PIECE_COUNT}
            {PLAYER} = {b|w}
            {PIECE_TYPE} = {A|B|G|Q|S}
            {PIECE_COUNT} = {1|2|3}

        {POINT_OF_CONTACT}
            /* = NW
            |* = W
            \* = SW
            *\ = NE
            *| = E
            */ = SE
            =* = OVER

TO DO
------
USER PARAMS
    TEMPO
    KEY
    SCALE
    DRUM BEAT
    INSTRUMENT TONES
INTERNAL PARAMS
    PAN
    OCTAVE
    INSTRUMENT TYPE
    RHYTHM
    SCALE INDEX
