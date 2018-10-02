n = int(input("Input : "))

for i in range(0,n+1) :
	for j in range(0,i) :
		print("*",end=" ")
	print()

for i in range(0,n) :
	for j in range(n-1,i,-1) :
		print("*",end=" ")
	print()
