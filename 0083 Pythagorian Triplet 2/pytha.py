num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

if ((num1>num2) and (num1>num3)) : #if first number is the biggest
	pytha = num2**2 + num3**2 
	if(pytha == (num1**2)) :
		print("True")
	else :
		print("False")
elif((num2>num1) and (num2>num3)) : #if second number is the biggest
	pytha = num1**2 + num3**2
	if(pytha == (num2**2)) :
		print("True")
	else :
		print("False")
elif((num3>num2) and (num3>num1)) : #if third number is the biggest
	pytha = num2**2 + num1**2
	if(pytha == (num3**2)) :
		print("True")
	else :
		print("False")
else :
	print("False")