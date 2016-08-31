from pandas import *

def KnapsackMax(value, weight, W, N):
	K = [[0 for x in range(W+1)] for x in range(N+1)]

	for i in range(N+1):
		for w in range(W+1):
			if(i==0 or w==0):
				K[i][w] = 0
			elif (weight[i-1] <= w):
				K[i][w] = max(value[i-1]+K[i-1][w-weight[i-1]], K[i-1][w])
			else: 
				K[i][w] = K[i-1][w]
	
	#print DataFrame(K)
	return K[N][W], getItems(K, value, weight, W, N)

def KnapsackMin(value, weight, W, N):
	K = [[0 for x in range(W+1)] for x in range(N+1)]
	for i in range(N+1):
		for w in range(W+1):
			if(w <= 0):
				K[i][w] = 0
			elif ((i<=0) and w>0):
				K[i][w] = float('inf')
			elif ((i>0) and (w>0)):
				K[i][w] = min(value[i-1]+K[i][w-weight[i-1]], K[i-1][w])
	#print DataFrame(K)
	return K[N][W], getItems(K, value, weight, W, N)

def getItems(K, value, weight, w, n):
	bag = []
	while(w > 0):
		if (K[n][w] != K[n-1][w]):
			bag.append(n)
			n = n - 1
			w = w - weight[n]
		else:
			n = n - 1
	return bag

value = [6, 10, 12]
weight = [1, 2, 3]
W = 5
N = len(weight)

print "#######################---MAX---#########################"
print KnapsackMax(value, weight, W, N)
print "#######################---MIN---#########################"
print KnapsackMin(value, weight, W, N)
