distinct = []
for a in range(2,101) :
	for b in range (2,101) :
		num = a**b
		distinct.append(num)

counter = 0
for x in range(0,len(distinct)) :
	for y in range(x+1,len(distinct)) :
		if distinct[x] == distinct[y] :
			distinct[y] = 0

for z in range(0,len(distinct)) :
	if distinct[z] != 0 :
		counter = counter + 1
	
print(counter)
	
