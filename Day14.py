import numpy as np
import re

raw = open("inputs/14.txt","r").readlines()
input_array= [i.replace("\n", "") for i in raw]
test_raw = open("inputs/14_test.txt","r").readlines()
test_array= [i.replace('\n', '') for i in test_raw]

def occurrences(text, sub):
        return len(re.findall('(?={0})'.format(re.escape(sub)), text))

def polymerization(inputArray, steps):
	polTemplate = inputArray[0].strip()
	instructions = np.asarray([x.split(' -> ') for x in inputArray[2:]])
	unique_chars = np.unique(instructions[:,1])
	counts = [0] * (len(instructions))
	for x in range(0,len(instructions)):	
		countAdd = occurrences(polTemplate,instructions[x][0])
		counts[x] = countAdd

	for i in range(0,steps):
		tempCounts = [0] * (len(instructions))
		for x in range(0,len(instructions)):
			if counts[x] > 0:
				#print(np.where(instructions[:,0] == str(instructions[x][0][0] + instructions[x][1]))[0][0])
				tempCounts[np.where(instructions[:,0] == str(instructions[x][0][0] + instructions[x][1]))[0][0]] += counts[x]
				tempCounts[np.where(instructions[:,0] == str(instructions[x][1] + instructions[x][0][1]))[0][0]] += counts[x]
		counts = tempCounts[:]
		#print(sum(counts)+1, counts)
	scores = [0] * len(unique_chars)
	for y in range(0, len(unique_chars)):
		if polTemplate[-1] == unique_chars[y]:
			scores[y] += 1
		for x in range(0,len(instructions)):
			if instructions[x][0][0] == unique_chars[y]:
				scores[y] += counts[x]
	print('The answer is', max(scores)-min(scores))

polymerization(test_array, 10)
polymerization(input_array, 10)
polymerization(test_array, 40)
polymerization(input_array, 40)