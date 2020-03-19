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

def horizontalAttacks(x, y, solution):
    attacks = 0
    for i in range(1, len(solution)):
        if (solution[y][(x + i) % len(solution)] == 1):
            attacks += 1
    return attacks

def verticalAttacks(x, y, solution):
    attacks = 0
    for i in range(1, len(solution)):
        if (solution[(y + i) % len(solution)][x] == 1):
            attacks += 1
    return attacks

def diagonalAttacks(x, y, solution):
    attacks = 0
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

def reverseDiagonalAttacks(x, y, solution):
    attacks = 0
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
