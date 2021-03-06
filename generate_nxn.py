# n = int(input("enter the matrix size: "))
# arr = []

# 0 for not queen
# 1 for queen

import copy
import random
import numpy as np

def generate_initial_state(n_queens):
    board = []
    for i in range(n_queens):
        queen_place = random.randint(0,n_queens-1)
        temp = []
        counter = 0
        while counter<n_queens:
            if(counter==queen_place):
                temp.append(1)
            else:
                temp.append(0)
            counter+=1

        board.append(temp)
        return_board = []
        for i in np.rot90(board):
            return_board.append(list(i))

    return return_board

def generate_successors(state):
    successors = []
    for i in range(len(state)):
        for j in range(len(state)):
            local_state = copy.deepcopy(state)
            for l in range(len(state)):
                local_state[l][i] = 0
                
            local_state[j][i] = 1
            if (local_state != state):
                successors.append(local_state)
    return successors

def generate_sideways_successors(state):
    successors = []
    for i in range(len(state) - 1):
        for j in range(i, len(state)):
            # Don't need to swap two columns that are equal
            if (i == j): continue; 

            temp_state = copy.deepcopy(state)
            for k in range(len(state)):
                temp = temp_state[k][i]
                temp_state[k][i] = temp_state[k][j]
                temp_state[k][j] = temp

            successors.append(temp_state)
    return successors