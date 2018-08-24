def celsius(f):
    fah = f
    cel = (5*(fah-32))/9
    print("The celsius conversion is :")
    print(cel)
def fahrenheit(c):
    cels = c
    faher = ((9*cels)+160)/5
    print("The fahrenheit conversion is :")
    print(faher)

temp = input("Enter a temperature :")
task = input("Do you want to convert it to\n1. Celsius\n2.Fahrenheit.\nInput 1 or 2 : ")

if(task == '1') :
	celsius(float(temp))
elif(task == '2') :
	fahrenheit(float(temp))
else :
	print("Enter valid input!")

