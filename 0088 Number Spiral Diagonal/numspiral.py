x = 1001 #the matrix is 1001 x 1001
n = int((x - 1)/2)
sumdiag = 1 #1 for the center element, which is 1

for i in range(1,n+1) : 
	sumdiag = sumdiag + 4*((4*(i**2))+i+1)
print("Sum of Diagonals of a 1001x1001 matrix is : ")
print(sumdiag)


