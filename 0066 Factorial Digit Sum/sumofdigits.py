number = 100
fact = 1
for x in range(1,(int(number)+1)): 
	fact = fact*x #to find 100!
print("Factorial : ")
print(fact)

sumdig = 0 #to find the sum of the digits
while(fact>0) :
	newnumber = int(fact)%10 #finding the last digit
	fact = int(fact)/10
	sumdig = sumdig+newnumber 
print("Sum of Digits : ")
print(sumdig)
