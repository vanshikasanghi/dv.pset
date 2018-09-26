def starPattern(n) :
	for i in range(n,0,-1) :
		for j in range(0,i) :
			print("*",end=' ')
		print()

n1 = input("n : ")
starPattern(int(n1))
