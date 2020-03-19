# Determine how many attacks there are
# from all of the queens.
def evaluate(solution): 
    attacks = 0
    for y in range(0, len(solution) - 1):
        for x in range(0, len(solution) - 1):
            if (solution[y][x] == 1):
                attacks += horizontalAttacks(x, y, solution)
                attacks += verticalAttacks(x, y, solution)
                attacks += diagonalAttacks(x, y, solution)
                attacks += reverseDiagonalAttacks(x, y, solution)
    return attacks

# Checks for all attacks that occur in the horizontal direction:
# 
# 0 0 0 0
# 1 1 1 1
# 0 0 0 0
# 0 0 0 0
# 
# Should produce 3 attacks for x,y position 1,2.
def horizontalAttacks(x, y, solution):
    attacks = 0
    for i in range(1, len(solution)):
        if (solution[y][(x + i) % len(solution)] == 1):
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
def verticalAttacks(x, y, solution):
    attacks = 0
    for i in range(1, len(solution)):
        if (solution[(y + i) % len(solution)][x] == 1):
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
def diagonalAttacks(x, y, solution):
    attacks = 0
    # Move the checks in the right starting position
    checkX = x
    checkY = y
    while checkX > 0 and checkY > 0:
        checkX -= 1
        checkY -= 1

    while (    
        checkY < len(solution)
        and checkX < len(solution)
    ):
        if (    
            checkX != x
            and checkY != y
            and solution[checkY][checkX] == 1
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
def reverseDiagonalAttacks(x, y, solution):
    attacks = 0
    # Move the checks in the right starting position
    checkX = x
    checkY = y
    while checkX > 0 and checkY < len(solution) - 1:
        checkX -= 1
        checkY += 1

    while (
        checkY > -1
        and checkX < len(solution)
    ):
        if (
            checkX != x
            and checkY != y
            and solution[checkY][checkX] == 1
        ):
            attacks += 1
        checkX += 1
        checkY -= 1
    return attacks
