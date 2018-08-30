num = 2**1000
print(num)

sumnum = 0
while num>0:
	lastdigit = int(num)%10
	sumnum = sumnum + lastdigit
	num = num/10
print("The sum is : ")
print(sumnum)