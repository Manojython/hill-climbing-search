from test_evaluate import *
from test_generate import *
from test_hill_climbing import *

def test_all():
    test_horizontalAttacks();
    test_verticalAttacks();
    test_diagonalAttacks();
    test_reverseDiagonalAttacks();
    test_evaluate();
    test_best_successor();
    test_climb();
    test_generate_initial_state();
    test_generate_successors();

test_all();