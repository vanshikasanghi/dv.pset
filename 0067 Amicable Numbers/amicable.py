'''a = 220 #since first pair
b = 284
sumnum = 0
for a in range (1,10000) :
	for b in range (1, 10000) :
		asumdiv = 0
		bsumdiv = 0
		
		acheck = (a/2) + 1
		bcheck = (b/2) + 1

		for x in range(2,int(acheck)) :
			adiv = 0
			if a%x==0 :
				adiv = a/x
				asumdiv = asumdiv + adiv
		
		for x in range(2,int(bcheck))	:
			bdiv = 0
			if b%x == 0 :
				bdiv = b/x
				bsumdiv = bsumdiv + bdiv
		
		if(asumdiv == b) and (bsumdiv == a) and (a!=b) :
			sumnum = sumnum + asumdiv + bsumdiv
print("Sum of all amicable numbers under 10000 is : ")
print(sumnum)''' 
#ABOVE SOLUTION TOO LONG, TOOK OVER TEN MINUTES

#DECIDED TO OPTIMISE AND USE FUNCTIONS INSTEAD

sumnum = 0
def divisorSum(num) :
	numcheck = num/2
	sumdiv = 1 #since 1 is also a factor
	for x in range (2,int(numcheck)+1) :
		numdiv = 0
		if num%x == 0 :
			numdiv = num/x
			sumdiv = sumdiv + numdiv
	return sumdiv

for a in range (100,10000) :
	b = divisorSum(a)
	if (a < b) :
		c = divisorSum(b)
		if (c == a) :
			#print(a)
			#print(b)
			sumnum = sumnum + a + b
print("Sum of all amicable numbers under 10000 is : ")
print(sumnum)



