# def findPermutation(n) : 

# 	res = [] 

# 	# Initial numbers to be pushed to result 
# 	en, on = 2, 1

# 	# If n is even 
# 	if (n % 2 == 0) : 
# 		for i in range(n) : 
# 			if (i % 2 == 0) : 
# 				res.append(en) 
# 				en += 2
# 			else : 
# 				res.append(on) 
# 				on += 2
		

# 	# If n is odd 
# 	else : 
# 		for i in range(n-2) : 
# 			if (i % 2 == 0) : 
# 				res.append(en) 
# 				en += 2
# 			else : 
# 				res.append(on) 
# 				on += 2
			
		
# 		res.append(n) 
# 		res.append(n - 2) 
	

# 	# Print result 
# 	for i in range(n) : 
# 		print(res[i] ,end = " ")	 
# 	print() 

# def findHack(key, l):
# 	for i in range()

# t = int(input())
# for _ in range(t):
#     key = input()
#     l = len(key)
#     findHack(key, l+1) 

import itertools

t = int(input())
for _ in range(t):
    key = input()
    l = len(key)
    arr = range(1, l+2)
    b = list(itertools.permutations(arr))
	for ele in  range(len(b)):
		