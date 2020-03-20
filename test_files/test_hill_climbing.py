import sys
import os
import numpy as np
sys.path.append(os.path.abspath("../"))
from hill_climbing import *

def test_best_successor():
    assert type(find_best_successor([])) == Node, "The return is a node"
    assert find_best_successor([
            [
                [0,1,0,0],
                [0,0,0,1],
                [1,0,0,0],
                [0,0,1,0]
            ],
            [
                [0,1,0,0],
                [0,1,0,0],
                [1,0,0,0],
                [0,0,1,0]
            ]
        ]).cost == 0, "The node with the lowest score (0) should be picked"

def test_climb():
    assert climb([
        [0,1,0,0],
        [0,0,0,1],
        [1,0,0,0],
        [0,0,1,0]
    ]) == [
        [0,1,0,0],
        [0,0,0,1],
        [1,0,0,0],
        [0,0,1,0]
    ], "The best successor is simply the current node since it is the goal"