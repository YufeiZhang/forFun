commend = str(input()).split()

if "f" in commend:
	if commend[0] == "f":
		print(commend[1])
		print (float(commend[1]) * 25, "cm")
	else:
		print (float(commend[0]) * 25, "cm")

elif "p" in commend:
	if commend[0] == "p":
		print (float(commend[1]) * 0.453592 * 2, "斤")
	else:
		print (float(commend[0]) * 0.453592 * 2, "斤")
else:
	print("f - feet -> cm\np - pound -> 斤")

# 178.308 cm & 113斤