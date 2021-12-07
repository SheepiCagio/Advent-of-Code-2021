import numpy as np

raw = open("inputs/7.txt","r").readline()
input_array= [int(i) for i in np.asarray(raw.split(","))]
test_array = [16,1,2,0,4,2,7,1,2,14]

def alignCrabsPartOne(input):
	result_array=[]
	for i in range(min(input), max(input)+1):
		result_array.append(sum([abs((horizontalPos-i)) for horizontalPos in input]))	
	print("The crabs align on",''.join(map(str,np.where(result_array == np.amin(result_array))[0])),"and spend", np.amin(result_array), "fuel")

def alignCrabsPartTwo(input):
	result_array=[]
	for i in range(min(input), max(input)+1):
		result_array.append(sum([(abs(horizontalPos-i)+1)/2*(abs(horizontalPos -i)) for horizontalPos in input]))	
	#	print([(abs(horizontalPos-i)+1)/2*(abs(horizontalPos -i)) for horizontalPos in input])
	print("The crabs align on",''.join(map(str,np.where(result_array == np.amin(result_array))[0])),"and spend", np.amin(result_array), "fuel")


alignCrabsPartOne(test_array)
alignCrabsPartOne(input_array)
alignCrabsPartTwo(test_array)
alignCrabsPartTwo(input_array)