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

def generate_successors(state):
	matrix_len = len(state)
	n_successors = (matrix_len*matrix_len) - matrix_len
	state = np.rot90(state,axes=(1,0))
	solution_list = []
	for i in range(matrix_len):
		row_name=state[i]
		counter = 0
		row_state=[]
		while counter < len(row_name):
			if(row_name not in row_state):
				row_state.append(row_name)
				counter+=1
			random.shuffle(row_name)

		for j in range(row_state):
			state[i] = row_state[j]
			state = np.rot90(state)
			solution_list.append(state)

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
