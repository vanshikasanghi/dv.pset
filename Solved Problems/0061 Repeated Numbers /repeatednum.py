numbers = [] #to store the inputted numbers
i = 0 #for storing in list
while(i<10) :
	digit = int(input("Enter Number "+str(i+1)+" : "))
	numbers.append(digit) #inserting digits in the list
	i = i+1

x = 0 #choose single number one at a time
j = 0 #finding if the numbers are repeating

for x in range(0,10) :
	for j in range((x+1),10) :
		if(numbers[x] == numbers[j]) :
			print(str(numbers[x]),end=' ') #printing the repeated numbers
		j = j + 1
	x = x + 1
