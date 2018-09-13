def isPrime(num) : #to check if a number is prime or not
	
	if num < 2 : #for negative numbers and 0 and 1
		return False
	else :
		root = num**0.5
		root1 = int(root)
		prime = True
		for x in range(2,root1+1) :
			if(num%x==0) :
				prime = False
		if(prime==True) :
			return True
		else :
			return False

maximum = 0 #to store maximum primes 

for a in range(-1001,1000) : 
	for b in range(-1001,1000) : 

		if isPrime(b):
			counter = 0
			n = 0
			while isPrime((n*n)+(a*n)+b) :
				counter = counter + 1
				n = n + 1

			if counter > maximum :
				maximum = counter
				A = a
				B = b
				
print("The product of the coefficients a and b, that produce the maximum number of primes for consecutive values of n is : ")
print(A*B)


