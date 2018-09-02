'''i = 1
num = 1000 #assumming starting point 
while num<1000000000 : 
	for i in range (1,21) :
		rem = num%i
		if(rem == 0) :
			counter = counter + 1
	if counter == 20 :
		print(num)
		break
	num = num - 1
	counter = 0 '''
#TRIED THE ABOVE WAY BUT TOO LONG ^

num = 1
while ((num%2 != 0) or (num%3 != 0) or (num%4 != 0) or (num%5 != 0) or (num%6 != 0) or (num%7 != 0) or (num%8 != 0) or (num%9 != 0) or (num%10 != 0) or (num%11 != 0) or (num%12 != 0) or (num%13 != 0) or (num%14!= 0) or (num%15 != 0) or (num%16 != 0) or (num%17 != 0) or (num%18 != 0) or (num%19 != 0) or (num%20 != 0)) :
	num = num + 1
print(num)