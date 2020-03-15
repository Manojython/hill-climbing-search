n = int(input("enter the matrix size: "))
arr = []

for i in range(n):
	temp = []
	counter = 0
	while counter<n:
		temp.append("_")
		counter+=1

	arr.append(temp)


print(arr)
