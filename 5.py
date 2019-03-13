word = input("Enter string : ")

length = len(word)

for i in range(0, length+1) :
	
	for j in range(0,i) :
		print(word[j], end = "")
	print()



