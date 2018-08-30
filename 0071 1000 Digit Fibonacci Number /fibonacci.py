fibolist = [] #list to store fibonacci numbers for index
i = 0 #first fibonacci number
j = 1 #second fibonacci number
fibolist.append(i)
fibolist.append(j)

counter = 2 

while (counter<5000) : #assuming term to contain 1000 digits is within 5000 mumbers 
	k = i+j
	fibolist.append(k) #adding fibonacci numbers to list
	i = j
	j = k
	counter = counter+1
#to find the first term of 1000 digits 
newcounter = 0
while (newcounter<5000) :
	length = len(str(fibolist[newcounter]))
	if(length == 1000) :
		break
	newcounter = newcounter+1
print("The index of the first term to contain 1000 digits is : ")
print(newcounter)





