text = input("Enter String : ")
word1 = input("Enter word you want to replace : ")
word2 = input("Enter the word you want to replace the previous word with : ")

if word1 in text :
	print(text.replace(word1,word2))

else :
	print("word not found in string")
