import numpy as np

raw = open("inputs/8.txt","r").readlines()
input_array= [np.asarray(i.replace("\n","").split('|')) for i in raw]
test_raw = open("inputs/8_test.txt","r").readlines()
test_array= [np.asarray(i.replace("\n","").split('|')) for i in test_raw]

def partOne(input):
	counter = 0 
	answer = 0
	after = []
	while counter < len(input):	
		after = after + input[counter][1].split()
		counter += 1
	
	for i in after:
		if len(i) == 2 or len(i) == 3  or len(i) == 4 or len(i) == 7: 
			answer += 1
	print('The answer to part one is:',answer)

def checkString(findString, searchArray):
	letterFound = 0
	for a in searchArray:
		if a in findString:	
			letterFound +=1
	return letterFound	

def partTwo(input):
	counter = 0 
	answer = ''
	after = []
	before = []
	config = [0,0,0,0,0,0,0,0,0,0]
	answer_array = []
	while counter < len(input):	
		before.append(input[counter][0].split())	
		after.append(input[counter][1].split())
		counter += 1
	#Determine the config to identify each number.
	for iteration in range(0,len(before)): 
		a = before[iteration]
		length_array = np.asarray([len(x) for x in a])
		config[1] = ''.join(sorted(a[int(np.where(length_array ==2)[0])]))
		config[4] = ''.join(sorted(a[int(np.where(length_array ==4)[0])]))
		config[7] = ''.join(sorted(a[int(np.where(length_array ==3)[0])]))
		config[8] = ''.join(sorted(a[int(np.where(length_array ==7)[0])]))
		for b in np.where(length_array == 6)[0]:
			if checkString(a[int(b)],list(config[1])) == 1:
				config[6] = ''.join(sorted(a[int(b)]))
			elif checkString(a[int(b)],list(config[4])) == 4:
				config[9] = ''.join(sorted(a[int(b)]))
			else: config[0] = ''.join(sorted(a[int(b)]))
		for b in np.where(length_array == 5)[0]:
			if checkString(a[int(b)],list(config[7])) == 3:
				config[3] = ''.join(sorted(a[int(b)]))
			elif checkString(a[int(b)],set(list(config[8])).difference(list(config[9]))) == 0:
				config[5] = ''.join(sorted(a[int(b)]))
			else: config[2] = ''.join(sorted(a[int(b)]))
		#decode the output values	
		for x in after[iteration]:
			answer += str(config.index(str(''.join(sorted(x)))))
		answer_array.append(int(answer))
		answer = '' 
	print('The answer to part two is:',sum(answer_array))

#partOne(test_array)
partOne(input_array)
#partTwo(test_array)
partTwo(input_array)

