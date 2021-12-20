import numpy as np

raw = open("inputs/20.txt","r").readlines()
input_array= [(i.replace('\n', '').replace('.','0').replace('#', '1')) for i in raw]
test_raw = open("inputs/20_test.txt","r").readlines()
test_array= [(i.replace('\n', '').replace('.','0').replace('#', '1')) for i in test_raw]

def addLayerZero(grid):
#if sum(np.asarray(grid)[:,0]) > 0: 
	grid = np.hstack((np.zeros(len(grid), dtype=int)[:, np.newaxis],grid))
#if sum(np.asarray(grid)[0,:]) > 0:
	grid = np.vstack((np.zeros(len(grid[0]), dtype=int)[np.newaxis,:],grid))
# if sum(np.asarray(grid)[:,-1]) > 0: 
	grid = np.hstack((grid,np.zeros(len(grid), dtype=int)[:, np.newaxis]))
# if sum(np.asarray(grid)[-1,:]) > 0:
	grid = np.vstack((grid, np.zeros(len(grid[0]), dtype=int)[np.newaxis,:]))
	return grid

def pictureEnhancer(input_array):
	splitvalue = False
	index_string = ''
	grid = []
	for i in input_array:
		if i == '':
			splitvalue = True
			continue
		if not splitvalue:
			index_string += i
		else: 
			grid.append(list(i))
	grid = [[int(i) for i in row] for row in grid]
	
	grid = enhancer(grid, index_string)
	grid = enhancer(grid, index_string)
	print('The number of lit pixels is:', sum(sum(grid)))
	

def enhancer(grid, index_string):	
	grid = addLayerZero(grid)
	output_grid = np.zeros((len(grid),len(grid[0])),dtype=int)
	grid = addLayerZero(grid)
	print(len(grid), len(grid[0]))
	for i in range(1,len(grid)-1): 
		for j in range(1, len(grid[i])-1):
			binStr = ''
			for k in range(-1,2):
				for l in range(-1,2):
					binStr += str(grid[i+k][j+l])
			output_grid[i-1][j-1] = index_string[int(binStr,2)]
	return output_grid

pictureEnhancer(test_array)
pictureEnhancer(input_array)
