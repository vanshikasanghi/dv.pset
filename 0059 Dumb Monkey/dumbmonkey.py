P = int(input("Enter Length of the Pillar : "))

if (P<3) :
	print("NO")
else : 
	newP = P-3
	newP = newP%2
	if newP == 0 : 
		print("YES")
	else : 
		print("NO")


