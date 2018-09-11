def findSumOfDigits(x) :
	sumdig = 0
	for i in range (0,len(str(x))) : 
		last = x % 10 #finding last digit
		sumdig = sumdig + last
		x = int(x / 10)
	print("Sum of Digits : ")
	print(sumdig)

num = int(input("Enter a number : "))
findSumOfDigits(num)