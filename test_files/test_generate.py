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
