# n = int(input("enter the matrix size: "))
# arr = []

# 0 for not queen
# 1 for queen

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

def get_next(row):
    possible_states=[]
    possible_states.append(row)
    mat =[0]*len(row)
    for j in range(len(row)):
        mat[j] = 1
        temp = mat[:]
        if(temp not in possible_states):
            possible_states.append(temp)
        mat[j]=0
    return possible_states

def generate_successors(state):

    matrix_len = len(state)
    # n_successors = (matrix_len*matrix_len) - matrix_len
    state = (np.rot90(state,axes=(1,0)))
    # print(state)
    solution_list = []
    for i in range(matrix_len):
        row_name=(state[i]).tolist()
        # print(row_name)
        
        
            # random.shuffle(row_name)
        row_state = get_next(row_name)

        for j in range(len(row_state)):
            state[i] = row_state[j]
            state = np.rot90(state)
            solution_list.append(state.tolist())

    return solution_list


def generate(n_queens):
    board= []
    
    for i in range(n_queens):
        temp = []
        counter = 0
        while counter<n_queens:
            temp.append("_")
            counter+=1

        board.append(temp)

    return board


# print(arr)
