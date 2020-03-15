# n = int(input("enter the matrix size: "))
# arr = []

def generate():
	board= []
	n = int(input("enter the matrix size: "))
	for i in range(n):
		temp = []
		counter = 0
		while counter<n:
			temp.append("_")
			counter+=1

		board.append(temp)

	return board


# print(arr)
