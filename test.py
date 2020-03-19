from evaluate import *

# test the evaluate function, ensure that
# all the valid solutions are 0 and all
# invalid solutions are greater than 0
def test_evaluate():

    assert evaluate([
        [0,1,0,0],
        [0,0,0,1],
        [1,0,0,0],
        [0,0,1,0]
    ]) == 0, "Valid solution is marked as away from 0"

    assert evaluate([
        [0,0,1,0],
        [0,0,0,1],
        [1,0,0,0],
        [0,0,1,0]
    ]) != 0, "Invalid solution does not represent non-zero evaluation"

def test_horizontalAttacks():
    assert horizontalAttacks(2, 1, [
        [0,0,0,0],
        [0,1,1,1],
        [0,0,0,0],
        [0,0,0,0]
    ]) == 2, "There should be a total of 2 horizontal attacks"

def test_verticalAttacks():
    assert verticalAttacks(1,0, [
        [0,1,0,0],
        [0,1,0,0],
        [0,1,0,0],
        [0,1,0,0]
    ]) == 3, "There should be a total of 3 vertical attacks"
    
    assert verticalAttacks(2,1, [
        [0,0,0,0],
        [0,0,1,0],
        [0,0,1,0],
        [0,0,1,0]
    ]) == 2, "There should be a total of 2 vertical attacks"

def test_diagonalAttacks():
    assert diagonalAttacks(0,0,[
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,1]
    ]) == 3, "Total of 3 diagonal attacks"

    assert diagonalAttacks(0,1,[
        [0,0,0,0],
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,0]
    ]) == 2, "Total of 2 diagonal attacks"

    assert diagonalAttacks(2,0,[
        [0,0,1,0],
        [0,0,0,1],
        [0,0,0,0],
        [0,0,0,0]
    ]) == 1, "Total of 1 diagonal attack"

def test_reverseDiagonalAttacks():
    assert reverseDiagonalAttacks(0, 3, [
        [0,0,0,1],
        [0,0,1,0],
        [0,1,0,0],
        [1,0,0,0]
    ]) == 3, "Total of 3 reverse diagonal attacks"

    assert reverseDiagonalAttacks(1, 3, [
        [0,0,0,0],
        [0,0,0,1],
        [0,0,1,0],
        [0,1,0,0]
    ]) == 2, "Total of 2 reverse diagonal attacks"

    assert reverseDiagonalAttacks(0, 1, [
        [0,1,0,0],
        [1,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]) == 1, "Total of 1 reverse diagonal attack"


def test():
    test_horizontalAttacks();
    test_verticalAttacks();
    test_diagonalAttacks();
    test_reverseDiagonalAttacks();
    test_evaluate();

test();