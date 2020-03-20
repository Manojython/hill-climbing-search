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
	return np.rot90(board)


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
