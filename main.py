import random
from hill_climbing import *
from generate_nxn import *
from test_files import test

def print_board(board):
    for i in board:
        for j in i:
            if (j == 1):
                print("Q",end=" ") 
            else:
                print("-",end=" ") 
        print(end="\n")

def print_moves(case):

    print("Moves for initial state:")
    print_board(case.moves[0])
    for move_i in range(1, len(case.moves)):
        print("Move: ", move_i, "\n")
        print_board(case.moves[move_i])
        print(end="\n")

def print_statistics(cases, print_case_count):
    successes = 0
    failures = 0
    total_failed_steps = 0
    total_successful_steps = 0
    total_successful_sideways = 0
    total_successful_restarts = 0
    if (len(cases) == 1 and
        'y' == input("Would you like to print the path (y/N)?")
        ):
        print_case_count = 1


    for case in cases:
        if (case.IsSuccess()):
            successes += 1
            total_successful_steps += case.steps
            total_successful_sideways += case.sideways
            total_successful_restarts += case.restarts
        else:
            failures += 1
            total_failed_steps += case.steps

        if (print_case_count > 0 and case.IsSuccess()):
            print_case_count -= 1
            print_moves(case)


    print("Rate of success: ", successes / len(cases))
    print("Rate of failure: ", failures / len(cases))

    success_output = "Unkown"
    success_sideways_output = "Unkown"
    success_restarts_output = "Unkown"
    if (successes > 0):
        success_output = total_successful_steps / successes
        success_sideways_output = total_successful_sideways / successes
        success_restarts_output = total_successful_restarts / successes
        
    failure_output = "Unkown"
    if (failures > 0):
        failure_output = total_failed_steps / failures

    print("Average steps for success: ", success_output)
    print("Average steps for failure: ", failure_output)
    if (success_sideways_output > -1):
        print("Average steps for success sideways: ", success_sideways_output)
    if (success_restarts_output > -1):
        print("Average steps for success restarts: ", success_restarts_output)

def run_hill_climbing(amount, size):
    print("Running", amount, "case(s) for hill climbing")
    cases = []
    for i in range(amount):
        cases.append(climb(generate_initial_state(size)))
    print_statistics(cases, 4)

def run_hill_climbing_sideways(amount, sideways_amount, size):
    print("Running", amount, "case(s) for sideways move with", sideways_amount, "steps")
    cases = []
    for i in range(amount):
        cases.append(
            climb_sideways(
                generate_initial_state(size),
                sideways_amount)
            )
    print_statistics(cases, 4)

def run_hill_climbing_random_restart(amount, restarts, size):
    print("Running", amount, "case(s) for random restart move with", restarts, "restarts")
    cases = []
    for i in range(amount):
        cases.append(
            climb_random_restart(
                generate_initial_state(size),
                restarts)
            )
    print_statistics(cases, 0)

def run_hill_climbing_random_restart_sideways(amount, restarts, size):
    print("Running", amount, "case(s) for random restart move with", restarts, "restarts and sideways moves")
    cases = []
    for i in range(amount):
        cases.append(
            climb_random_restart_sideways(
                generate_initial_state(size),
                restarts)
            )
    print_statistics(cases, 0)

def run_evaluation():

    amount = 100
    sideways_amount = 25
    restarts = 25
    board_size = 8
    
    print("Running evaluation for 8-queens problem at,", amount,"unique cases")

    run_hill_climbing(amount, board_size)
    run_hill_climbing_sideways(amount, sideways_amount, board_size)
    run_hill_climbing_random_restart(amount, restarts, board_size)
    run_hill_climbing_random_restart_sideways(amount, restarts, board_size)

def get_size_input():
    size = int(input("What is the size you want to test?:"))
    amount = int(input("How many restarts do you want to have?:"))
    run_hill_climbing_random_restart(1, amount, size)

test.test_all()
print("Test cases passed")

run_input = input("Run evaluation or run a single size (eval/single)?")
if (run_input == 'eval'):
    run_evaluation()
elif (run_input == 'single'): 
    get_size_input()
else:
    print("Nothing will be done, exiting ...")

