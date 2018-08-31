A = 50*(10**6) #country A
B = 70*(10**6) #country B
counter = 0

while True :
    A = A + ((3/100)*A)
    B = B + ((2/100)*B)
    counter = counter + 1
    if(A>B) :
    	break
print("The number of years that A will take to surpass B are : ")
print(counter)