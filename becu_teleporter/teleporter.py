def destinations(teleporters, die_sides, start_pos, last_square):
    teleporter_dict = {int(from_square): int(to_square) for from_square, to_square in (pair.split(',') for pair in teleporters)}
    visited_destinations = set()

    for roll in range(1, die_sides + 1):
        square = start_pos + roll
        if square <= last_square:
            destination = teleporter_dict.get(square, square)
            visited_destinations.add(destination)

    return sorted(visited_destinations)


def destinations_orig(teleporter, die_sides, start_pos, last_square):
    visited_destinations = set()
    teleporters = {int(pair.split(',')[0]): int(pair.split(',')[1]) for pair in teleporter}

    squares = range(last_square + 1)
    for square in squares[start_pos + 1: start_pos + die_sides + 1]:
        if square in teleporters:
            visited_destinations.add(teleporters.get(square))
        else:
            visited_destinations.add(square)

    return visited_destinations


# We are developing a new board game, Thrilling Teleporters.

# The board consists of consecutive squares from 0 to last_square, some of the spaces also contain Teleporters, which are given as comma delimited strings "from,to".

# The game is played as follows:
#   1. Each turn, the player rolls a die numbered from 1 to die_sides.
#   2. The player moves forward the rolled number of squares.
#   3. The player stops at last_square if they reach it.
#   4. If the player finishes on a square with a teleporter, they are moved to where the teleporter points.

# Note: Only one teleporter is followed per turn.

# A sample board with last_square 20 the following teleporters might look like this conceptually.
# teleporters1 = ["3,1", "4,2", "5,10"]

#    +-----+
#    v     |
# 0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20
#       ^     |  |               ^
#       +-----+  +---------------+

# Write a function that returns a collection of the possible squares a player can move to in a single turn, given the following inputs:
# - A collection of teleporter strings
# - The number of sides on the die
# - The square the player starts on
# - The last square on the board

# Example:
# With a 6-sided die, starting at square 0 with a board ending at square 20 (as pictured above)

# Rolling a 1, 2 or 6 have no teleporters so they end at that square.
# Rolling a 3 goes to 1, rolling a 4 goes to 2, rolling a 5 goes to 10.
# The possible outcomes are, in order of die roll, are [1, 2, 1, 2, 10, 6].
# If we remove the duplicates, the answer is [1, 2, 10, 6]
# destinations(teleporters1, 6, 0, 20) => [1, 2, 10, 6]

# Additional Inputs:
# teleporters2 = ["5,10", "6,22", "39,40", "40,49", "47,29"]
# teleporters3 = ["6,18", "36,26", "41,21", "49,55", "54,52",
#                 "71,58", "74,77", "78,76", "80,73", "92,85"]
# teleporters4 = ["97,93", "99,81", "36,33", "92,59", "17,3",
#                 "82,75", "4,1", "84,79", "54,4", "88,53",
#                 "91,37", "60,57", "61,7", "62,51", "31,19"]
# teleporters5 = ["3,8", "8,9", "9,3"]

# Complexity Variable:
# B = size of the board
# Note: The number of teleporters, T, and the size of the die, D, are bounded by B.

# All Test Cases:
# (output can be in any order)
#                            die  start  last
#                           sides, pos, square
# destinations(teleporters1,  6,    0,    20)  => [1, 2, 10, 6]
# destinations(teleporters2,  6,   46,   100)  => [48, 49, 50, 51, 52, 29]
# destinations(teleporters2, 10,    0,    50)  => [1, 2, 3, 4, 7, 8, 9, 10, 22]
# destinations(teleporters3, 10,   95,   100)  => [96, 97, 98, 99, 100]
# destinations(teleporters3, 10,   70,   100)  => [72, 73, 75, 76, 77, 79, 58]
# destinations(teleporters4,  6,    0,   100)  => [1, 2, 3, 5, 6]
# destinations(teleporters5,  6,    0,    20)  => [1, 2, 4, 5, 6, 8]
