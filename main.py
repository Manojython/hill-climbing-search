from hill_climbing import *
from generate_nxn import *
from test_files import test
test.test_all()
print("Test cases passed")

print("Running 500 cases")
cases = []
for i in range(500):
    cases.append(climb(generate_initial_state(8)))

successes = 0
failures = 0
total_failed_steps = 0
total_successful_steps = 0
for case in cases:
    if (case.IsSuccess()):
        successes += 1
        total_failed_steps += case.steps
    else:
        failures += 1
        total_successful_steps += case.steps

print("Rate of failure: ", failures / len(cases))
print("Rate of success: ", successes / len(cases))
print("Average steps for success: ", total_successful_steps / successes)
print("Average steps for failure: ", total_failed_steps / failures)