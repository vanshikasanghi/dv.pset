numbers = []
for x in range(0,10) :
	num = int(input("Enter Number "+str(x+1)+" : "))
	numbers.append(num)

diff = numbers[0] - numbers[1]
#finding the pair of numbers with least difference 
pair1 = 0
pair2 = 0
for y in range(0,9) :
	if (numbers[y]<numbers[y+1]) < diff :
		diff = numbers[y] - numbers [y+1]
		pair1 = numbers[y]
		pair2 = numbers[y+1]

print("The pairs with least difference are : ")
print(str(pair1)+" "+str(pair2))