numbers = [] #to store numbers
i = 0
while i <5 :
	num = input("Enter number "+str(i+1)+" : ")
	numbers.append(int(num))
	i = i + 1

j = 4
ascending = 1 #to check for ascending
descending = 1 #to check for descending

for j in range(4,0,-1) :
	if (numbers[j] > numbers[j-1]) :
		ascending = ascending +1
	elif(numbers[j] < numbers[j-1]) :
		descending = descending +1
	
if (ascending == 5) :
	print("Ascending")
elif(descending == 5) :
	print("Descending")
else :
	print("None")
