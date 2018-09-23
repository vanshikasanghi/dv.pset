#recursive solution as function is being called within itself repeatedly
def Hanoi(d, start, middle, last) :
	if d == 1 :
		print("Move disk 1 from "+start+" to "+last)
		return 0
	
	Hanoi(d-1,start,last,middle) #changing positions and calling function again, middle and last were switched
	
	print("Move disk "+str(d)+" from "+start+" to "+last) #printing the move
	
	Hanoi(d-1,middle,start,last) #changing positions again middle becomes start, start becomes middle and last remains last

d = int(input("Enter number of disks : "))
Hanoi(d,'A','B','C')