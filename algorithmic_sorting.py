list_1 = [2, 1, 10,-1, 0]
n = len(list_1) #5
#iterate by going through each term and seeing if the next term is less then the current term
for i in range(0, n):
		#another for loop nested inside... important
	for j in range( 0, n - i - 1):
		if (list_1[j] > list_1[j+1]):
			temp=list_1[j]
			list_1[j] = list_1[j+1]
			list_1[j+1] = temp
			print(list_1)
	
		