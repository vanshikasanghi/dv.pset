import random
m = int(input("Enter a number : "))
mrange = random.randint(1,(m+1)) #generating random number
#print(mrange)
counter = 0
while True:
    guess = int(input("Make a guess : "))
    if (guess > mrange) :
        print("High")
        counter = counter+1
    if(guess < mrange):
        print("Low")
        counter = counter+1
    elif (guess == mrange):
        print("Correct")
        counter = counter+1
        break
print("Number of attempts taken : " +str(counter))