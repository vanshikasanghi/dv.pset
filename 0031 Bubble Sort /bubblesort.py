#bubble sort

numbers = [] #to store the elements 
i = 0
while i<10 :
	num = int(input("Enter Number "+str(i+1)+" : "))
	numbers.append(num)
	i = i + 1
#bubble sotring 
for i in range(0,10) : #since there are 10 elements in numbers
	for j in range(0,10-i-1) :
		if numbers[j] > numbers [j+1] :
			temp = numbers[j] #temporary variable to store value
			numbers[j] = numbers[j+1]
			numbers[j+1] = temp

for num in numbers : #printing sorted elements
	print (num)