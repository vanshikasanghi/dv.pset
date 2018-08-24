word = input("Enter a word : ")

newword = list(word)
length = len(newword)

for x in range(0,length) :
	for y in range(0,x+1) :
		print(newword[y],end="")
	print("")
