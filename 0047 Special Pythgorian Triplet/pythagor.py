a = 1
b = 1
c = 1
for a in range(1,1001):
	for b in range(1,1001):
		for c in range(1,1001):
			multi = (a**2) + (b**2)
			if (multi == (c**2)) :
				if ((a+b+c) == 1000) :
					print("The triplet is : ")
					print(a)
					print(b)
					print(c)
					print("The product is : ")
					print(a*b*c)
		            break
					break
					break		


	
