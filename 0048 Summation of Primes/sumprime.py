def isPrime(num) : #to check if a number is prime or not
	root = num**0.5
	prime = True
	for x in range(2,int(root)+1) :
		if(num%x==0) :
			prime = False
	if(prime==True) :
		return True
	else :
		return False

sumnum = 0
for i in range (2,2000000) : 
	if (isPrime(i) == True) : 
		sumnum = sumnum + i
		
print("Sum of all prime numbers below two million : ")
print(sumnum)