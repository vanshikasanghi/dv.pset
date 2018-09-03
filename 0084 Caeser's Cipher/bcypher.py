text = input("Encrypted Message : ")
key = int(input("Enter Caeser's Key (1-26) : "))
counter = 1
oldmessage = "" #to find the actual message
length = len(text)

for counter in range(length) :
	char = ord(text[counter]) #finding the ASCII values
	if ((char>=65) and (char<=90)) or (char>=97) and (char<=122)  :
		#for rotation
		if (char <= 65+(key-1)) :
			rotnum = (65 + (key-1)) - char
			oldmessage = oldmessage + chr(90-rotnum)
		elif ((char <= 97+(key-1)) and (char>90)) :
			rotnum = (97 + (key-1)) - char
			oldmessage = oldmessage + chr(122-rotnum)
		else :
			char = char - key
			oldmessage = oldmessage + chr(char)
	else :
		oldmessage = oldmessage + chr(char)
print("Decrypted Message : ")
print(oldmessage)
