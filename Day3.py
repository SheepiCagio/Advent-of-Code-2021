import numpy as np

#raw = open("inputs/3.txt","r").readlines()
input_array= np.asarray([string[:-1] for string in  open("inputs/3.txt","r").readlines()])
test_array= np.asarray([string[:-1] for string in  open("inputs/3_test.txt","r").readlines()])


def partOne(input):
#	for i in range(0,len(input)):
#		while i < len(input[0]):
#			for charBin in input:
	input.count()				

partOne(test_array)