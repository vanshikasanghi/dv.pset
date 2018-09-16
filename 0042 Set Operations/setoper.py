def union(P,Q) :
	R = []
	for i in range(0,len(P)) :
		R.insert(i,P[i])

	length = len(str(R))
	
	for j in range(0,len(Q)) :
		if Q[j] not in R :
			R.insert(length,Q[j])
			length = length + 1
	return R

def difference(P,Q) : #elements of P which are not in Q
	R = [] #R = P - Q

	for i in range(0,len(P)) :
		
		if P[i] not in Q :
			R.insert(i,P[i])
	return R

def is_subset(P,Q) :
	check = True #to check if P is a subset of Q

	for i in range(0,len(P)) :
		if P[i] not in Q :
			check = False

	return check

def powerset(P) :
	R = []
	length = len(P)
	lenpow = 2**length #total number of powersets
	counter = 0
	i = 0
	for counter in range(0,lenpow) :
		print("[",end="")
		for i in range(0,length) :
			if ((counter & (1 << i))>0) :
				print(P[i],end=",",)
		print("]")

def symmetric_difference(P,Q) :
	R = [] #symmetric difference (P-Q union Q-P) 
	G = [] #P-Q
	S = [] #Q-P
	
	if len(Q) > len(P) :
		for i in range(0,len(P)) :
			
			if P[i] not in Q :
				G.insert(i,P[i])
				R.insert(i,P[i]) #first inserting P-Q

		for i in range(0,len(Q)) :
			if Q[i] not in P :
				S.insert(i,Q[i])

		length = len(R)
		length = length + len(S)

		for i in range(len(S)-1,length) :
			R.insert(i,S[i-len(S)]) #inserting Q-P

		return R

	elif len(P) > len(Q) :
		for i in range(0,len(Q)) :
			
			if Q[i] not in P :
				S.insert(i,Q[i])
				R.insert(i,Q[i]) #first inserting P-Q

		for i in range(0,len(P)) :
			if P[i] not in Q :
				G.insert(i,P[i])

		length = len(R)
		length = length + len(G)

		for i in range(len(G),length) :
			R.insert(i,G[i-len(G-1)]) #inserting Q-P

		return R

	else : 
		length = len(P)*2
		for i in range(0,len(P)) :
			if P[i] not in Q :
				R.insert(i,P[i])

		for i in range(len(P),length) :
			if Q[i-len(Q)] not in P :
				R.insert(i,Q[i-len(Q)])

		return R

Set1 = []
Set2 = []

S1 = input("Enter Set 1 : ")
Set1 = S1.split()

S2 =  input("Enter Set 2 : ")
Set2 = S2.split()

print("Set 1 : ",end ="")
print(Set1)
print("Set 2 : ",end="")
print(Set2)

union = union(Set1,Set2)
print("\nUnion : ",end='')
print(union)

diff = difference(Set1,Set2)
print("\nP - Q : ",end='')
print(diff)

value = is_subset(Set1, Set2)
if (value == True) :
	print("\nP is a subset of Q")
else :
	print("\nP is not a subset of Q")

print("\nPowerset of P : ")
powerset(Set1)

symdif = symmetric_difference(Set1,Set2) 
print("\nSymmteric Difference : ",end='')
print(symdif)
