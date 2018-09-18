def S1(n) :
	sumnum = (n*(n+1))/2
	print("Sum : ")
	print(int(sumnum))

def S2(n) :
	first = 3
	last = 3 + ((n-1)*2)
	sumnum = ((first+last)*n)/2
	print("Sum : ")
	print(int(sumnum))

def S3(n) :
	sumnum = 0
	numlist = []
	for i in range(1,n+1) :
		numlist.append(i)

	for i in range(1,len(numlist)) :
		#finding perfect square
		if (numlist[i]*numlist[i]) not in numlist :
			sumnum = sumnum + i #adding numbers which are not squares
	print("Sum : ")
	print(int(sumnum))

term = int(input("Enter n : "))
S1(term)
S2(term)
S3(term)


