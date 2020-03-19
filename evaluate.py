# Determine how many attacks there are from all of the queens placed
# on the board.
def evaluate(board): 
    attacks = 0
    for y in range(0, len(board) - 1):
        for x in range(0, len(board) - 1):
            if (board[y][x] == 1):
                attacks += horizontalAttacks(x, y, board)
                attacks += verticalAttacks(x, y, board)
                attacks += diagonalAttacks(x, y, board)
                attacks += reverseDiagonalAttacks(x, y, board)
    return attacks

# Checks for all attacks that occur in the horizontal direction:
# 
# 0 0 0 0
# 1 1 1 1
# 0 0 0 0
# 0 0 0 0
# 
# Should produce 3 attacks for x,y position 1,2.
def horizontalAttacks(x, y, board):
    attacks = 0
    for i in range(1, len(board)):
        if (board[y][(x + i) % len(board)] == 1):
            attacks += 1
    return attacks

# Checks for all attacks that occur in the vertical direction:
# 
# 0 1 0 0
# 0 1 0 0
# 0 1 0 0
# 0 1 0 0
# 
# Should produce 3 attacks for x,y position 2,1.
def verticalAttacks(x, y, board):
    attacks = 0
    for i in range(1, len(board)):
        if (board[(y + i) % len(board)][x] == 1):
            attacks += 1
    return attacks

# Checks for all attacks that occur in the diagonal direction:
# 
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1
# 0 0 0 0
# 
# Should produce 2 attacks for x,y position 2,1.
def diagonalAttacks(x, y, board):
    attacks = 0
    # Move the checks in the right starting position
    checkX = x
    checkY = y
    while checkX > 0 and checkY > 0:
        checkX -= 1
        checkY -= 1

    while (    
        checkY < len(board)
        and checkX < len(board)
    ):
        if (    
            checkX != x
            and checkY != y
            and board[checkY][checkX] == 1
        ):
            attacks += 1
        checkX += 1
        checkY += 1
    return attacks

# Checks for all attacks that occur in the reverse diagonal direction:
# 
# 0 0 0 0
# 0 0 0 1
# 0 0 1 0
# 0 1 0 0
# 
# Should produce 2 attacks for x,y position 1,3.
def reverseDiagonalAttacks(x, y, board):
    attacks = 0
    # Move the checks in the right starting position
    checkX = x
    checkY = y
    while checkX > 0 and checkY < len(board) - 1:
        checkX -= 1
        checkY += 1

    while (
        checkY > -1
        and checkX < len(board)
    ):
        if (
            checkX != x
            and checkY != y
            and board[checkY][checkX] == 1
        ):
            attacks += 1
        checkX += 1
        checkY -= 1
    return attacks
