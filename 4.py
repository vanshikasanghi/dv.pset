import random #to generate a random number

num = random.randint(1,100)
print("Chosen a word. Time to guess!")
counter = 0

x = True
while x :
	g = int(input("Guess : "))
	
	if g<num :
		print("LOW")
		counter = counter + 1

	elif g>num :
		print("HIGH")
		counter = counter + 1
	
	else :
		counter = counter + 1
		x = False


print("Congrats! That's correct. You took "+str(counter)+" steps.")