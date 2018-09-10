sumnum = 0
for x in range(1,1000) : 
	if (x%5==0) or (x%3==0) : 
		sumnum = sumnum + x
print("The sum of all multiples of 3 or 5 below 1000 : ")
print(sumnum)