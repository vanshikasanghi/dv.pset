import datetime #to find the time

name = input("Enter your name : ")
dt = datetime.datetime.now()
time_hour = dt.hour

if time_hour <=12 :
	print("Good Morning, "+name+"!")

elif (time_hour>12 and time_hour<=17) :
	print("Good Afternoon, "+name+"!")

else :
	print("Good Night, "+name+"!")
