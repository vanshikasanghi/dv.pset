i = 0 #first fibonacci number
j = 1 #second fibonacci number
evensum = 0 

while ((i+j)<4*(10**6)) : #only runs till four million
	k = i + j #next in fibonacci series
	if (k%2==0) :
		evensum = evensum + k #adding the sum of even numbers
	i = j
	j = k
print("The sum of the even valued terms are : ")
print(evensum)