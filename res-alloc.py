import collections
from configs import instances, cpu_dict, hours, price, min_capacity

#method to calculate min cost and elements selected and it returns a list
def MinKnapsack(value, weight, W, N):
	K = [[[0,[]] for x in range(W+1)] for x in range(N+1)]
	for i in range(N+1):
		for w in range(W+1):
			if(w <= 0):
				K[i][w][0] = 0
			elif ((i<=0) and w>0):
				#set cost as infinity item 0, so that min does not return 0
				K[i][w][0] = float('inf')
			elif ((i>0) and (w>0)):
				if ((weight[i-1]<=w) and (value[i-1]+K[i][w-weight[i-1]][0] <= K[i-1][w][0])):
					K[i][w][0] = value[i-1]+K[i][w-weight[i-1]][0]
					K[i][w][1] = K[i][w-weight[i-1]][1][:]
					#append items chosen into list 
					K[i][w][1].append(weight[i-1])
				else:
					K[i][w][0] = K[i-1][w][0]
					K[i][w][1] = K[i-1][w][1][:]
	return K[N][W]

#method to calculate cost, region and servers available - sorted according to total cost
def get_costs(instances, hours, cpus, price):
	final_result = []
	for key,val in instances.iteritems():
		value, weight, count_keys = ([] for i in range(3))
		info = {}

		#append cost of each server to values list
		for i in val.values():
			value.append(i)
		
		#weight for available set of servers in a particular region
		weight = [cpu_dict[x] for x in list(set(val.keys()) & set(cpu_dict.keys()))]
		
		result = MinKnapsack(value, weight, min_capacity, len(weight))		
		
		#calculate occurance of each server in result 
		count_dict = collections.Counter(result[1])
		
		for ki in count_dict.keys():
			for k,v in cpu_dict.iteritems():
				if(ki == v):
					count_keys.append(k)
		count_values = [value for value in count_dict.values()]
		
		info = {'region' : key,
				'total_cost' : format(result[0]*hours,'.2f'),
			    'servers' : zip(count_keys, count_values)}
		
		final_result.append(info)
	return sorted(final_result, key=lambda k:k['total_cost'])
				
print "#############--FINAL RESULT--###############"
print get_costs(instances, hours, min_capacity, price)