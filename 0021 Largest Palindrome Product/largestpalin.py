def isPalindrome(num) : #to check if a number is palindrome or not
	
	reverse = ''
	length = len(num)
	for i in range(length-1,-1,-1): #checking in reverse
		reverse = reverse + num[i]

	if num == reverse : 
		return True
	else :
		return False

largest = 0

for x in range(100,1000) : #checking for all three digit numbers
	for y in range(100,1000) :
		number = x * y #finding the product
		if (isPalindrome(str(number)) == True) and (number > largest) :
			largest = number

print("The largest Palindrome made from the product of two 3-digit numbers :")
print(largest)