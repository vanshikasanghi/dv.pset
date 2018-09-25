def add(x,y):
    a = x + y
    return a
 
def subtract(x,y):
    s = x - y
    return s
 
def multiply(x,y):
    m = x * y
    return m

def divide(x,y):
    d = x / y
    return d
 
x = int(input("Number 1 : "))
y = int(input("Number 2 : "))

print("\nCalculator : ")

add = add(x,y)
print("\nAddition : "+str(add))

sub = subtract(x,y)
print("\nSubtraction : "+str(sub))

mul = multiply(x,y)
print("\nMultiplication : "+str(mul))

div = divide(x,y)
print("\nDivision : "+str(div))