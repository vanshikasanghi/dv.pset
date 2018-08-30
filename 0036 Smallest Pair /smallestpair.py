i = 1
numbers = []
while i<11 :
	num = int(input("Enter Number "+str(i)+" : ")) 
	numbers.append(num)
	i = i+1

fsmall = numbers[0]#storing first smallest
secsmall = numbers[0] #storing second smallest

x = 9
while x>=0 :
	if(numbers[x]<fsmall) :
		secsmall = fsmall
		fsmall = numbers[x]
	elif(numbers[x]<secsmall) :
		secsmall = numbers[x]
	x = x-1
print("The pair is : ")
print(str(fsmall)+" "+str(secsmall))

