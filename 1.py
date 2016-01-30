import math

customers = open("customers.txt", 'r').read().split('\n')
calls = open("calls.txt", 'r').read().split('\n')


customersList, phoneList = [], []
for i in range(len(customers)-1):
	customersLine = customers[i].split(';')
	customersLine.append(0) # number of call
	customersLine.append(0) # duration in s
	customersLine.append(0) # due = minutes * rate
	customersList.append(customersLine)
	phoneList.append(customersLine[0])
print(phoneList)


for j in range(len(calls)-1):
	sampleCalls = calls[j]
	callerData = sampleCalls.split(';')
	for ch in customersList:
		if callerData[1] in ch:
			ch[3] += 1
			minutes = math.ceil(float(callerData[3]) / 60)
			ch[4] += float(callerData[3])
			ch[5] += minutes * float(callerData[4])

