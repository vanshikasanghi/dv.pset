num1 = int(input("Numerator 1 : "))
deno1 = int(input("Denominator 1 : "))

num2 = int(input("Numerator 2 : "))
deno2 = int(input("Denominator 2 : "))

print(str(num1)+"/"+str(deno1)+" + "+str(num2)+"/"+str(deno2),end=" ")

if deno1==deno2 : #if denominators are same
	addfrac = num1+num2 #added numerator
	denofinal = deno1
else :
	denofinal = deno1*deno2 #multiplying denominators
	addfrac = (num1*deno2) + (num2*deno1) 
print(" = "+str(addfrac)+"/"+str(denofinal))
