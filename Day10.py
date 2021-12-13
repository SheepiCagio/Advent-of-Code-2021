import numpy as np

raw = open("inputs/10.txt","r").readlines()
input_array= [np.asarray(i.replace("\n","").split()) for i in raw]
test_raw = open("inputs/10_test.txt","r").readlines()
test_array= [np.asarray(i.replace("\n","").split()) for i in test_raw]

def checkLine(stringInput):
	openingTags = np.array(['[','(', '{', '<'])
	closingTags = np.array([']',')', '}', '>'])
	points = np.array([57,3,1197,25137])
	checkChunk = []
	temp = list(stringInput)
	for i in range(0, len(temp)):
		if temp[i] in openingTags:
			checkChunk.append(temp[i])
		if temp[i] in closingTags:
			if np.where(closingTags == temp[i])[0][0] == np.where(openingTags == checkChunk[-1])[0][0]:
				checkChunk = checkChunk[:-1]
			else: 
				#print('Corrupted', temp[i], temp, checkChunk)
				return points[np.where(closingTags == temp[i])[0][0]]
	if len(checkChunk) > 0:
		#print('Incomplete', temp, checkChunk)
		return 0
	else:  
		#print('Valid', temp, checkChunk)
		return 0

def autoCompleteLine(stringInput):
	openingTags = np.array(['[','(', '{', '<'])
	closingTags = np.array([']',')', '}', '>'])
	points = np.array([2,1,3,4])
	score = 0
	checkChunk = []
	temp = list(stringInput)
	for i in range(0, len(temp)):
		if temp[i] in openingTags:
			checkChunk.append(temp[i])
		if temp[i] in closingTags:
			if np.where(closingTags == temp[i])[0][0] == np.where(openingTags == checkChunk[-1])[0][0]:
				checkChunk = checkChunk[:-1]
			else: 
				#print('Corrupted')
				return None			
	if len(checkChunk) > 0:
		#print('Incomplete')
		score = np.int64(0)
		for x in range(1, len(checkChunk)+1):
				score = score * 5 + points[np.where(openingTags == checkChunk[-x])[0][0]]
		return score
	else:  
		#print('Valid')
		return None

def SyntaxSorting(inputArray):
	result = []
	for i in inputArray:
		res = checkLine(i[0])
		result.append(res)
	print('The syntax error score =', sum(result))

def SyntaxCompleting(inputArray):
	result = []
	for i in inputArray:
		res = autoCompleteLine(i[0])
		if not res == None:
			result.append(res)
	print('The autocomplete score =', np.sort(result)[round(len(result)/2)])

SyntaxSorting(test_array)
SyntaxSorting(input_array)
SyntaxCompleting(test_array)
SyntaxCompleting(input_array)