num = int(input("Enter number to check if palindrome : "))

newnum = num #to perform operations
check = 0 #to check for palindrome

while newnum != 0 :
	
	last = newnum % 10 #finding the last digit
	check = (check * 10) + last
	newnum = newnum // 10

if num == check :
	print("Palindrome Number")
else :
	print("Not a Palindrome Number")

