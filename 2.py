customers = open("customers.txt", 'r').read().split('\n')
calls = open("calls.txt", 'r').read().split('\n')

request1 = 1 # for testing
request2 = 1 # 0 -> number of call, 1 -> number of dration

customersMatrix = []
for i in range(len(customers)-1):
	customersMatrix.append([])
	for j in range((len(customers)-1)):
		customersMatrix[i].append([])
		customersMatrix[i][j].append(0) #
		customersMatrix[i][j].append(0) # 
		customersMatrix[i][j].append(0) # flag


