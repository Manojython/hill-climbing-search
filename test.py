from evaluate import *
from generate_nxn import *
import sys
import numpy as np

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


def test_generate_initial_state():
    size = 8
    matrix =  generate_initial_state(size)
    matrix = np.rot90(matrix,axes=(1,0))
    assert len(matrix) == size, "Expected number of rows are not {}".format(size)
    for i in matrix:
        assert len(i) == size, "Expected number of columns are not {}".format(size)
        assert list(i).count(1) == 1, "Expected number of 1's is not one"

def test_generate_successors():
    initial_state = [
        [0,1,0,0],
        [0,0,0,1],
        [1,0,1,0],
        [0,0,0,0]
    ];

    successors = generate_successors(initial_state);

    assert len(successors) == 12, "For a 4x4 board there should be 12 successors";

    # column 1 states
    assert successors.count([
        [1,1,0,0],
        [0,0,0,1],
        [0,0,1,0],
        [0,0,0,0]
    ]) == 1, "Expected the successor for the 1st column of the 1st iteration to be included"

    assert successors.count([
        [0,1,0,0],
        [1,0,0,1],
        [0,0,1,0],
        [0,0,0,0]
    ]) == 1, "Expected the successor for the 2nd column of the 1st iteration to be included"

    assert successors.count([
        [0,1,0,0],
        [0,0,0,1],
        [0,0,1,0],
        [1,0,0,0]
    ]) == 1, "Expected the successor for the 3rd column of the 1st iteration to be included"

    # column 2 states
    assert successors.count([
        [0,0,0,0],
        [0,1,0,1],
        [1,0,1,0],
        [0,0,0,0]
    ]) == 1, "Expected the successor for the 2nd column of the 1st iteration to be included"

    assert successors.count([
        [0,0,0,0],  
        [0,0,0,1],  
        [1,1,1,0],  
        [0,0,0,0]
    ]) == 1, "Expected the successor for the 2nd column of the 2nd iteration to be included"  

    assert successors.count([
        [0,0,0,0],
        [0,0,0,1],
        [1,0,1,0],
        [0,1,0,0]
    ]) == 1, "Expected the successor for the 2nd column of the 3rd iteration to be included"
    
    # column 3 states
    assert successors.count([
        [0,1,1,0],
        [0,0,0,1],
        [1,0,0,0],
        [0,0,0,0]
    ]) == 1, "Expected the successor for the 3rd column of the 1st iteration to be included"

    assert successors.count([
        [0,1,0,0],
        [0,0,1,1],
        [1,0,0,0],
        [0,0,0,0]
    ]) == 1, "Expected the successor for the 3rd column of the 2nd iteration to be included"

    assert successors.count([
        [0,1,0,0],
        [0,0,0,1],
        [1,0,0,0],
        [0,0,1,0]
    ]) == 1, "Expected the successor for the 3rd column of the 3rd iteration to be included"
    
    # column 4 states
    assert successors.count([
        [0,1,0,1],
        [0,0,0,0],
        [1,0,1,0],
        [0,0,0,0]
    ]) == 1, "Expected the successor for the 4th column of the 1st iteration to be included"

    assert successors.count([
        [0,1,0,0],
        [0,0,0,0],
        [1,0,1,1],
        [0,0,0,0]
    ]) == 1, "Expected the successor for the 4th column of the 2nd iteration to be included"

    assert successors.count([
        [0,1,0,0],
        [0,0,0,0],
        [1,0,1,0],
        [0,0,0,1]
    ]) == 1, "Expected the successor for the 4th column of the 3rd iteration to be included"

def test():
    test_horizontalAttacks();
    test_verticalAttacks();
    test_diagonalAttacks();
    test_reverseDiagonalAttacks();
    test_evaluate();
    test_generate_initial_state();
    test_generate_successors();


matrix  = generate_initial_state(8)
for i in matrix:
    print(i,end="\n")

try:
    test();
    print("Test cases passed")
except:

    print("Test cases did not pass")
    sys.exit(0)



