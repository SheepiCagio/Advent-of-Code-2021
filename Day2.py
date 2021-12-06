import numpy as np

raw = open("inputs/2.txt","r").readlines()
input_array = np.asarray([string[:-1].split(' ') for string in raw])
horizontalPosition = 0
depthMeasurement = 0
aim = 0

def partOne(input,horPos, depMeas):
	for instruction in input:
		if instruction[0] == 'forward':
			horPos += int(instruction[1])
		elif instruction[0] == 'down':
			depMeas += int(instruction[1])
		elif instruction[0] == 'up':
			depMeas -= int(instruction[1])
	print(horPos*depMeas)
		
def partTwo(input, horPos, depMeas, aimValue):
	for instruction in input:
		if instruction[0] == 'forward':
			horPos += int(instruction[1])
			depMeas += int(instruction[1])*aimValue
		elif instruction[0] == 'down':
			aimValue += int(instruction[1])
		elif instruction[0] == 'up':
			aimValue -= int(instruction[1])
	print(horPos*depMeas)

partOne(input_array, horizontalPosition, depthMeasurement)
partTwo(input_array, horizontalPosition, depthMeasurement, aim)