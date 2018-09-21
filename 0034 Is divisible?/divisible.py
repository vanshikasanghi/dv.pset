n = int(input("Enter Number : "))

counter = 0
for i in range(1,(n+1)) :
	if (i % 7 == 0) : 
		counter = counter + 1

print(counter)
