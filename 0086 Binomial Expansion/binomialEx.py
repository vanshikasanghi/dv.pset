#getting the expanion
elements = [1] 
n = int(input("Input : "))

for x in range(0,n) :
	tripattern = []
	tripattern.append(1) #starting term
	
	for i in range(0,len(elements)-1) :
		tripattern.append(elements[i]+elements[i+1])

	tripattern.append(1) #ending term
	elements = tripattern #storing the value of the sequence in elements 

#printing the binomial expansion
i = 0
x = n #for coefficients
y = 0
print("Output : ")
print("(x+y)"+str(n)+" = ",end='')
while (x>=0) :
	
	if (y==0) :
		if (elements[i]!=1) :
			coeff = elements[i]
		else :
			coeff = ""
		print(str(coeff)+"x^"+str(x)+" + ",end ='')
	
	elif (x==0) :
		if(elements[i]!=1) :
			coeff = elements[i]
		else :
			coeff = ""
		print(str(coeff)+"y^"+str(y))
	
	else :
		if(elements[i]!=1) :
			coeff = elements[i]
		else :
			coeff = ""
		print(str(coeff)+"x^"+str(x)+"y^"+str(y)+" + ",end='')
	i = i+1	
	x = x-1
	y = y+1