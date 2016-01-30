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


custList, phoneList, phoneListSorted = [], [], []
for i in range(len(customers)-1):
	custList.append(customers[i].split(";"))
	phoneList.append(customers[i].split(";")[0])
phoneListSorted = sorted(phoneList)


for i in range(len(calls)-1):
	callsList = calls[i].split(";")
	caller  = phoneList.index(callsList[1])
	resever = phoneList.index(callsList[2])
	customersMatrix[caller][resever][0] += 1
	customersMatrix[caller][resever][1] += int(callsList[3])


