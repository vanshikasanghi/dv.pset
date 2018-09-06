number = 600851475143
prime = [] #to store all the prime numbers
largest = 0 #to store the largest prime number
def isPrime(num) : #to check if a number is prime or not
	root = num**0.5
	prime = True
	for x in range(2,int(root)+1) :
		if(num%x==0) :
			prime = False
	if(prime==True) :
		return num
	else :
		return 0

for i in range(1,int(number/2) + 1) :
	if number%i == 0 :
		check = isPrime(i)
		
		if (check != 0) :
			prime.append(check) #storing all prime numbers
			
largest = prime[len(prime)-1] #the last element of array will be the largest
print(largest)




