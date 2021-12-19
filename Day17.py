import numpy as np
minX = 206
maxX = 250
minY = -57
maxY = -105
distance = 0
speed = []
xarray = []
heightarray = []

def partOne():
	j = abs(maxY)-1
	tempheight = []
	height = 0
	count = 0

	while height > maxY:
		height += (j + count * -1)
		count += 1
		tempheight.append(height)
	print(max(tempheight), 'is the max height')

partOne()

def partTwo():

	for x in range(1,maxX+1):
		if (x+1)*x/2 < maxX and (x+	1)*x/2 > minX:
			speed.append(x)
	print(speed)
	for x in range(1, max(speed)+1):
		for j in range(1, maxX +1):
			if x * j - (x*(x-1)/2) >= minX and x*j- (x*(x-1)/2) <= maxX:
				if x in speed and j in speed:
					xarray.append([1000000,j])
				else:
					xarray.append([x,j])
	for i in xarray:
		for j in range(maxY-100, abs(maxY)+100):
			height = 0
			count = 0
			while height >= maxY and count < int(i[0]):
				height += (j + count * -1)
				count += 1
				if height >= maxY and height <= minY:
			 		if count == int(i[0]) or (int(i[0]) == 1000000 and count >= min(speed)):
						 heightarray.append(str(i[1]) + "," + str(j))
	print(len(np.unique(heightarray)))

partTwo()
