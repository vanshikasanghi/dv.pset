elements = [1]
N = int(input("Enter number of lines : "))

emp = (2*N)-2 #for empty spaces
for x in range(0,N) :
	for y in range(0,emp) :
		print(" ",end='')
	emp = emp - 1
	print(*elements) #to print array in the same line
	print()

	tripattern = []
	tripattern.append(1) #starting 1
	
	for i in range(0,len(elements)-1) : #getting each element of one line
		tripattern.append(elements[i]+elements[i+1])

	tripattern.append(1) #ending 1
	elements = tripattern #storing the value of the sequence in elements 
