import numpy as np

raw = open("inputs/16.txt","r").readlines()
input_string= [i.replace("\n", "") for i in raw][0]

#input_string = 'CE00C43D881120'
packets = []
binaryString = bin(int(input_string, base=16))[2:].zfill(len(input_string)*4)

def typeBin(inputBin):
	if not int(inputBin,2) == 0:
		temp = [int(inputBin[0:3],2), int(inputBin[3:6],2),inputBin[6:]]
		packets.append(temp)
		value = ''
		if temp[1] == 4: #unpack literal value
			remainBin = "0"
			while temp[2][0] == '1':
				value += temp[2][1:5]
				temp[2] = temp[2][5:]
			value += temp[2][1:5]
			value = int(value,2)
			remainBin = temp[2][5:]
			return remainBin, value
		else: #unpack operator value
			if temp[2][0] == '0':
				lenSubPack = int(temp[2][1:16],2)
				typePacket = temp[1]
				remainBin = temp[2][16+lenSubPack:]
				tempSubPacket = runUnpack(temp[2][16:16+ lenSubPack])
				value = executeOperator(typePacket, tempSubPacket)
				return remainBin, value
			else:
				numSubPack = int(temp[2][1:12],2)
				counter = numSubPack
				tempSubPacket =[]
				remainBin = temp[2][12:]
				value = 0
				while counter > 0:
					remainBin, value = typeBin(remainBin)
					tempSubPacket.append(value)
					counter -= 1
				value = executeOperator(temp[1], tempSubPacket)
				return remainBin, value
	else:
		remainBin = '0'
		value =  0
	return remainBin, value
		
def executeOperator(type, values):
	if type == 0:
		return sum(values)
	elif type == 1:
		return np.product(values)
	elif type == 2:
		return min(values)
	elif type == 3: 
		return max(values)
	elif type == 5: 
		return values[0] > values[1]
	elif type == 6: 
		return values[0] < values[1]
	elif type == 7: 
		return values[0] == values[1]

def runUnpack(inputBin):
	tempSubPacket = []
	while len(inputBin) > 1:
		inputBin, value = typeBin(inputBin)
		tempSubPacket.append(value)
	return tempSubPacket

answer = runUnpack(binaryString)

typeVersion = [[int(i) for i in row] for row in np.asarray(packets)[:,0:2]]
sumVersion = sum(np.asarray(typeVersion)[:,0])

print('The sum of the versions:',sumVersion)
print('The expression of the transmission:', answer[0])