length = 0 #length of recurring value

for i in range(1000,0,-1) : #denominator values, starting from 1000

	if length >= i :
		break;
	
	remainder = [0]*i #array to store the length of remainder
	x = 1 #for the values
	d = 0 #for the denominator 
	
	#finding the rvalues
	while (x != 0) and (remainder[x]==0) :
		remainder[x] = d
		x = x * 10
		x = x % i
		d = d + 1

	if ((d - remainder[x]) > length) :
		length = d - remainder[x]

print("The value of d<1000 for which 1/d has the longest recurring cycle is : ")
print(d)
