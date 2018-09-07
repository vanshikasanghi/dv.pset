counter = 0
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

number = 2

while counter < 10001 :
	check = isPrime(number)
	
	if check != 0 :
		counter = counter + 1
	
	if counter == 10001 :	
		print("The 10001st Prime Number : ")
		print(check)
	number = number + 1
