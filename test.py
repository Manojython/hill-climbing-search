from hill_climbing import *

# test generate_random_solution
generate_random_solution()

# test the evaluate function, ensure that
# all the valid solutions are 0 and all
# invalid solutions are greater than 0
def test_evaluate():
    valid_solution = [
        [0,1,0,0],
        [0,0,0,1],
        [1,0,0,0],
        [0,0,1,0]
    ]

    assert evaluate(valid_solution) == 0