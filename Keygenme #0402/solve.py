import random

listKey = []

inputs = int(input("How many Serial Key you want?: "))
for i in range(0,inputs):
	listAlpha = ["B","C","D","F","H","I","J","K","L","N","O","P","Q","T","U","V","X","Z"]
	random.shuffle(listAlpha)
	strkey = "".join(listAlpha[0:4])+"-"+"".join(listAlpha[4:8])+"-"+"".join(listAlpha[8:12])+"-"+"".join(listAlpha[12:16])
	if strkey not in listKey:
		listKey.append(strkey)

for i in range(0,len(listKey)):
	print("Serial "+str(i+1)+" : "+listKey[i])
