#5 unique random numbers
import random
counter = 1 #to stop running after five numbers
while (True) :
	number = random.randint(1,100)
	number2 = random.randint(1,100)
	if(number!=number2):
		if(counter==3):
			print(number)
			break
		else :
			print(number)
			print(number2)
		counter=counter+1
