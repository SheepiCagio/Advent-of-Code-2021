import numpy as np

raw = open("inputs/13.txt","r").readlines()
input_array= [i.replace("\n", "") for i in raw]
test_raw = open("inputs/13_test.txt","r").readlines()
test_array= [i.replace('\n', '') for i in test_raw]

def foldInput(paperMatrix, fold):
	if 'y' in fold[0]: #horizontal fold
		foldLine = int(fold[1])
		for z in range(1, len(paperMatrix) - foldLine):
			paperMatrix[foldLine + z - (len(paperMatrix)- foldLine)] += paperMatrix[-z]
		paperMatrix = paperMatrix[:-(foldLine+1)]	
		return paperMatrix
	else: #vertical fold
		foldLine = int(fold[1])
		for line in range(0,len(paperMatrix)):
			for q in range(1, len(paperMatrix[line]) - foldLine):
				paperMatrix[line][foldLine + q - (len(paperMatrix[line])-foldLine)] += paperMatrix[line][-q]
		paperMatrix = paperMatrix[:,:-(foldLine+1)]
		return paperMatrix
		
def findCode(inputArray):
	dots = []
	instructions = []
	for x in inputArray:
		instructions = [x.split('=') for x in inputArray if 'fold' in x]
		dots = [x for x in inputArray if ',' in x]
	dots = [i.split(',') for i in dots]
	dots = [[int(s) for s in row] for row in dots]
	xMax, yMax = np.max(dots,axis=0)
	transparantPaper = np.zeros([yMax +2,xMax+1])
	for y in dots:
		transparantPaper[int(y[1])][int(y[0])] = 1
	for fold in instructions:
		transparantPaper = foldInput(transparantPaper,fold)
		print('There are', sum(sum(transparantPaper>0)),'dots visible')
	print(np.where(transparantPaper>0 , '#', ' '))

findCode(test_array)
findCode(input_array)