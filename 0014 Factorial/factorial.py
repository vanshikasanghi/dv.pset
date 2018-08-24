number = input("Enter a number to find it's factorial : ")
fact = 1
for x in range(1,(int(number)+1)):
	fact = fact*x
print("Factorial : "+fact)
