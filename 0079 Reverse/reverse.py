def reverseNumber(x) :
	reverse = ''
	for i in range(len(str(x))-1,-1,-1) :
		reverse = reverse + str(x)[i]
	print("Reverse : ",end='')
	print(reverse)

num1 = int(input("Enter Number : "))
reverseNumber(num1)