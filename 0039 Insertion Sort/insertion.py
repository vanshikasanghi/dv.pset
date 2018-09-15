numbers = []
for x in range(0,10) :
	num = int(input("Enter element "+str(x+1)+" : "))
	numbers.append(num) #inserting elements to the list

for i in range(1,10) : #since 10 is the length of the list
	
	index = numbers[i] 
	j = i - 1 #checking elements before the current one
	
	while numbers[j]>index and j>=0 : 
		numbers[j+1] = numbers[j] #if smaller, it's location is changed
		j = j - 1
	
	numbers[j+1] = index #current element placed how it would be in the sorted list

print("Sorted List : ")
for x in range(0,10) :
	print(numbers[x]) #printing list


