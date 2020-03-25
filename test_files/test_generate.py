import sys
import os
import numpy as np
sys.path.append(os.path.abspath("../"))
from generate_nxn import *

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

def test_generate_sideways_successors():
    initial_state = [
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,1]
    ];

    successors = generate_sideways_successors(initial_state);

    assert len(successors) == 6, "For a 4x4 board there should be 6 sideways successors from the current successor";

    # 1 with 2
    assert successors.count([
        [0,1,0,0],
        [1,0,0,0],
        [0,0,1,0],
        [0,0,0,1]
    ]) == 1, "The sideways successors list should contain a swap of column 1 with column 2"

    # 1 with 3
    assert successors.count([
        [0,0,1,0],
        [0,1,0,0],
        [1,0,0,0],
        [0,0,0,1]
    ]) == 1, "The sideways successors list should contain a swap of column 1 with column 3"

    # 1 with 4
    assert successors.count([
        [0,0,0,1],
        [0,1,0,0],
        [0,0,1,0],
        [1,0,0,0]
    ]) == 1, "The sideways successors list should contain a swap of column 1 with column 4"

    # 2 with 3
    assert successors.count([
        [1,0,0,0],
        [0,0,1,0],
        [0,1,0,0],
        [0,0,0,1]
    ]) == 1, "The sideways successors list should contain a swap of column 2 with column 3"

    # 2 with 4
    assert successors.count([
        [1,0,0,0],
        [0,0,0,1],
        [0,0,1,0],
        [0,1,0,0]
    ]) == 1, "The sideways successors list should contain a swap of column 2 with column 4"

    # 3 with 4
    assert successors.count([
        [1,0,0,0],
        [0,1,0,0],
        [0,0,0,1],
        [0,0,1,0]
    ]) == 1, "The sideways successors list should contain a swap of column 3 with column 4"
