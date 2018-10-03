array = []
for i in range(0,10) :
	num = float(input("Enter Number "+str(i+1)+" : "))
	array.append(num)

sumnum = 0
for i in range(0,10) :
	sumnum = sumnum + array[i]

average = sumnum/10
print("Average of 10 floating point value is : "+str(average))

