text = input("Enter Message : ")
key = int(input("Enter Caeser's Key (1-26) : "))
counter = 1
newmessage = ""
length = len(text) #to find the length of text

for counter in range(length) :
	char = ord(text[counter]) #finding ASCII value of each letter
	if ((char>=65) and (char<=90)) or (char>=97) and (char<=122)  : #lowercase and uppercase
		#if and elif to check for end letters and rotating it back
		if(char >= 90-(key-1)) and (char<92)  :
			rotnum = char - (90 - (key-1))
			newmessage = newmessage + chr(65+rotnum)
		elif(char >= 122 - (key-1)) and (char<124) :
			rotnum = char - (122- (key-1))
			newmessage = newmessage + chr(97+rotnum)
		else :
			char = char + key
			newmessage = newmessage + chr(char) #converting ASCII to character 
	else :
		newmessage = newmessage + chr(char) #for spaces and numbers

print("Encrypted Message : ")
print(newmessage)