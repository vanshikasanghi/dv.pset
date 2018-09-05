finalsum = 0
def abundant(num) :
	numcheck = num/2
	sumdiv = 1 #since 1 is also a factor
	for x in range (2,int(numcheck)+1) :
		numdiv = 0
		if num%x == 0 :
			numdiv = num/x
			sumdiv = sumdiv + numdiv
	if sumdiv > num :
		return num #returns an abundant number
	else : 
		return 0
numlist = []
for i in range(1,28124) :
	numlist.append(i) #storing all intergers to check later

for y in range (1,28124) :
	for z in range(1,28124) :
		number1 = abundant(y)
		number2 = abundant(z)
		sumnum = number1 + number2
		
		'''if sumnum not in numlist :
			finalsum = finalsum + sumnum
			print(finalsum)'''
		if sumnum in numlist : 
			ind = numlist.index(sumnum)
			numlist.pop(ind)

for z in range(0,len(numlist)) :
	finalsum = finalsum + numlist[z]

print("The sum is : ")
print(finalsum)