number = 13 #to check for the series
counterfinal = 0
finalnum = 0
while number < 1000000 :
	counter = 0
	num = number #for the sequence, to check for each number
	while num > 1 : #finding one sequence
		if (num%2==0) :
			num = num/2
			counter = counter + 1
		else :
			num = (3*num)+1
			counter = counter + 1
	
	if (counter > counterfinal) : #checking for the longest sequence
		counterfinal = counter
		finalnum = number
	number = number + 1
print("Longest Collatz Sequence starts with : ")
print(finalnum)



