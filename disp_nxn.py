from generate_nxn import generate

board = generate()

for i in board:
	for j in i:
		print(j,end=" ") 
	print(end="\n")