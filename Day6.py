import numpy as np

raw = open("inputs/6.txt","r").readline()
raw = raw[:-1]
input_array= [int(i) for i in np.asarray(raw.split(","))]
#input_array = [3,4,3,1,2]

def PartOne_Naive(day_count):
	for i in range(1,day_count):
		for x, fish in enumerate(input_array):
			input_array[x]= fish -1
			if input_array[x] < 0 :
				input_array[x] = 6
				input_array.append(9)
	print("Na", day_count, "dagen zijn er",len(input_array), "vissen")

def PartOneTwo(day_count):
	fish_count = [0,0,0,0,0,0,0,0,0]
	temp_fish_count = [0,0,0,0,0,0,0,0,0]
	for i in range(0,9):
		fish_count[i]  = input_array.count(i)
	for x in range(0,day_count):
		temp_fish_count = fish_count[:]
		for j in range(0,9):
			if j==6 :
				fish_count[j] = temp_fish_count[j+1]+temp_fish_count[0]
			elif j==8:
				fish_count[j] = temp_fish_count[0]
			else:
				fish_count[j] = temp_fish_count[j+1]
	print("Na", day_count, "dagen zijn er",sum(fish_count), "vissen")

PartOneTwo(80)
PartOneTwo(256)