customers = open("customers.txt", 'r').read().split('\n')
calls = open("calls.txt", 'r').read().split('\n')

request1 = int(input("Direact(0) or Undirect(1)\n"))
request2 = int(input("Number of calls (0) or Duration (1)\n"))

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


for ch in phoneListSorted:
	i = phoneList.index(ch)
	for ch2 in phoneListSorted:
		j = phoneList.index(ch2)
		if request1 == 0:
			if i != j:
				print(str(i+1)+",", str(j+1)+",", customersMatrix[i][j][request2]) 
		elif request1 == 1 and customersMatrix[i][j][2] == 0 and i != j:
			customersMatrix[j][i][2] = 1
			total = customersMatrix[i][j][request2] + customersMatrix[j][i][request2]
			print(str(i+1)+",", str(j+1)+",", total)

