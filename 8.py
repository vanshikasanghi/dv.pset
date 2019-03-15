i = 1
numbers = []
while i < 11 :
	num = int(input("Enter Number "+str(i)+" : ")) 
	numbers.append(num)
	i = i + 1

#setting counter variables
neg = 0
pos = 0
zer = 0

for i in range (0,10) :
	if numbers[i] < 0 :
		neg = neg + 1

	elif numbers[i] > 0:
		pos = pos + 1

	else :
		zer = zer + 1

	i = i + 1

print("Zeros : "+str(zer)+", Positive : "+str(pos)+", Negative : "+str(neg))