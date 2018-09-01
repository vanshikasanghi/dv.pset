number = []
found = False
for i in range(0,10) :
	num = input("Enter Number "+str(i+1)+" : ")
	number.append(num)

search = input("Enter search element : ")
length = len(number) #here 10

for x in range(0,length) :
	if(search==number[x]) :
		found = True
if(found == True) :
	print("Element Found!")
else :
	print("Element Not Found!")
		