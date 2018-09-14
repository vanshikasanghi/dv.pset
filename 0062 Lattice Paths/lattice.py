#For a 20x20 matrix
n = 40 #20 Down as well as 40 Right moves
fact1 = 1
for i in range(n,0,-1) :
	fact1 = fact1 * i

d_r = 20 #for similar down and right moves
fact2 = 1
for x in range(d_r,0,-1) :
	fact2 = fact2 * x

path = fact1/(fact2*fact2)
print("Total number of paths : ")
print(int(path))