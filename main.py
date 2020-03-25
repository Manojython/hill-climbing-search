from hill_climbing import *
from generate_nxn import *
from test_files import test

def print_statistics(cases):
    successes = 0
    failures = 0
    total_failed_steps = 0
    total_successful_steps = 0
    for case in cases:
        if (case.IsSuccess()):
            successes += 1
            total_successful_steps += case.steps
        else:
            failures += 1
            total_failed_steps += case.steps

    print("Rate of success: ", successes / len(cases))
    print("Rate of failure: ", failures / len(cases))

    success_output = "Unkown"
    if (successes > 0):
        success_output = total_successful_steps / successes
        
    failure_output = "Unkown"
    if (failures > 0):
        failure_output = total_failed_steps / failures

    print("Average steps for success: ", success_output)
    print("Average steps for failure: ", failure_output)

def run_hill_climbing(amount):
    print("Running", amount, "cases for hill climbing")
    cases = []
    for i in range(amount):
        cases.append(climb(generate_initial_state(8)))
    print_statistics(cases)

def run_hill_climbing_sideways(amount, sideways_amount):
    print("Running", amount, "cases for sideways move with", sideways_amount, "steps")
    cases = []
    for i in range(amount):
        cases.append(
            climb_sideways(
                generate_initial_state(8),
                sideways_amount)
            )
    print_statistics(cases)

def run_hill_climbing_random_restart(amount, restarts):
    print("Running", amount, "cases for random restart move with", restarts, "restarts")
    cases = []
    for i in range(amount):
        cases.append(
            climb_random_restart(
                generate_initial_state(8),
                restarts)
            )
    print_statistics(cases)

test.test_all()
print("Test cases passed")

run_hill_climbing(500)
run_hill_climbing_sideways(100, 100)
run_hill_climbing_random_restart(100, 100)