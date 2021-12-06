
import numpy as np

raw = open("inputs/1.txt","r").readlines()
input_array = np.asarray([int(string[:-1]) for string in raw])

def partOne(input):
	input_previous = input[:-1]
	input_new= input[1:]
	count = sum((input_new-input_previous)>0)
	print(count)

def partTwo(input):
	input_previous = input[:-3]+input[1:-2]+input[2:-1]
	input_new= input[1:-2]+input[2:-1]+input[3:]
	count = sum((input_new-input_previous)>0)
	print(count)

partOne(input_array)
partTwo(input_array)
