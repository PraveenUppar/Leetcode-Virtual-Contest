def maxDistance(moves: str) -> int:
    x = moves.count('R') - moves.count('L')
    y = moves.count('U') - moves.count('D')
    blanks = moves.count('_')
    return abs(x) + abs(y) + blanks

print(maxDistance("L_D_"))  


# You are given a string moves consisting of the characters 'U', 'D', 'L', 'R', and '_'.

# Starting from the origin (0, 0), each character represents one move on a 2D plane:

# 'U': Move up by 1 unit.
# 'D': Move down by 1 unit.
# 'L': Move left by 1 unit.
# 'R': Move right by 1 unit.
# '_': Can be independently replaced with any one of 'U', 'D', 'L', or 'R'.
# Return the maximum Manhattan distance from the origin that can be achieved after all moves have been performed.