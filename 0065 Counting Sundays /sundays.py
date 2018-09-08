def months(year) :
	leap = [31,29,31,30,31,30,31,31,30,31,30,31]
	nonleap = [31,28,31,30,31,30,31,31,30,31,30,31]

	if (year%4 == 0) and (year%400 == 0) and (year%100 != 0) : 
		return leap
	else :
		return nonleap

counter = 0
day = 2 #since 1 Jan 1900 was a monday, next year it will be a tuesday as 1901 is a non leap year

for x in range(1901,2001) : #check for all years to find the months
	length = months(x)
	for y in range(0,12) : #for one month, finding first sundays
		if(day == 0) :
			counter = counter + 1
		day = (day + length[y]) % 7 #finding days of the week

print("No. of Sundays that fell on the first of the month during twentieth century :")
print(counter)
