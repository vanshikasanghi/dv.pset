i = 0
x = True
trinum = 0
trinumbers = [] #to store which triange number it is
while x == True :
	i = i + 1
	trinum = trinum + i
	trinumbers.append(trinum)
	
	checkfac = trinum
	counter = 1
	for y in range(2,checkfac+1) :
		if checkfac%y == 0 :
			counter = counter + 1
		
		if counter == 500 :
			x = False
			break;
	
	if counter == 500 :
		ind = trinumbers.index(trinum)
		print("The Triangle Number containing over 500 divisors is : ")
		print(str(ind+1))
		print(trinum)
