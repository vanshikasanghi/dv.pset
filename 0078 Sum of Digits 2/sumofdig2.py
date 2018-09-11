def findSumOfDigits(x) :
	sumdig = 0
	for i in range (0,len(str(x))) : 
		last = x % 10 #finding last digit
		sumdig = sumdig + last
		x = int(x / 10)
	return sumdig 

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

if (findSumOfDigits(num1) == findSumOfDigits(num2)) : 
	print("1")
else :
	print("0")
