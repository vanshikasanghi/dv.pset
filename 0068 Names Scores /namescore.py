f = open("nameslist.py","r+")
from nameslist import nameslist 

length = len(nameslist)

#sorting in ascending order
for i in range(0,(length-1)) :
	for j in range(0,length-i-1) :
		if(nameslist[j]>nameslist[j+1]) :
			temp = nameslist[j]
			nameslist[j] = nameslist[j+1]
			nameslist[j+1] = temp
#finding score
sumscore = 0 #total score of all names

for x in range(length) :
	sumname = 0 #sum of all letters in the name
	namescore = 0
	name = nameslist[x]
	namelength = len(name)
	
	for y in range(namelength) :
		char = ord(name[y]) #finding ASCII value to find number score
		char = char - 64 #since all letters are in uppercase
		sumname = sumname + char
	namepos = x + 1 #position of name in sorted array
	namescore = sumname * namepos #score of each name
	sumscore = sumscore + namescore

print("Total of all name scores is : ")
print(sumscore)





