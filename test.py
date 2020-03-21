import sys
import os

# from test_files import test
from generate_nxn import generate_successors

initial_state = [
        [0,1,0,0],
        [0,0,0,1],
        [1,0,1,0],
        [0,0,0,0]
    ]

output = generate_successors(initial_state)
ind = 0 
for i in output:
    for j in i:
        print(j,end="\n")
    print("----------")
    ind+=1
print(ind)
# test.test_all()
# print("Test cases passed")
