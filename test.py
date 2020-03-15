from evaluate import *

# test generate_random_solution
# generate_random_solution()

# test the evaluate function, ensure that
# all the valid solutions are 0 and all
# invalid solutions are greater than 0
def test_evaluate():

    assert evaluate([
        [0,1,0,0],
        [0,0,0,1],
        [1,0,0,0],
        [0,0,1,0]
    ]) == 0

    assert evaluate([
        [0,0,1,0],
        [0,0,0,1],
        [1,0,0,0],
        [0,0,1,0]
    ]) != 0

test_evaluate();