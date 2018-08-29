i = 100
sumsq = 0
square = 0
while(i>0):
	sumsq = sumsq + (i**2)  #sum of the squares 
	square = square + i #finding the sum of all numbers
	i = i - 1
squaresum = square**2 #finding square of the sum
difference = squaresum - sumsq #finding the difference
print("The difference is : ")
print(difference)