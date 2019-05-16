import random
import sys
import math

if len(sys.argv) == 1:
	print("Incorrect noise type argument")
	sys.exit()

# Params

if sys.argv[1].lower() == "blue_noise".lower():

	start = 0
	end = 20
	cellSize = 1
	points = 0
	normalize = 1
	showBox = 1
	
	# Generate grid
	
	length = end - start
	grid = []
	
	for x in range(start, end):
		for y in range(start, end):
			x *= cellSize
			y *= cellSize
			randX = random.random() * cellSize + x
			randY = random.random() * cellSize + y
			grid.append([ randX, randY])
			
	if points == 0:
		points = length * length
			
	randomized = random.sample(grid, points)
			
	import matplotlib.pyplot as plt
	from matplotlib.patches import Rectangle
	
	for xy in randomized:
	
		cellX = math.floor(xy[0] / cellSize)
		cellY = math.floor(xy[1] / cellSize)
	
		if normalize:
			xy[0] = (xy[0] - start) / length
			xy[1] = (xy[1] - start) / length
			
		plt.plot(xy[0], xy[1], 'ro')
		
		if showBox:
			if normalize:
				plt.gca().add_patch(Rectangle((cellX * cellSize / length, cellY * cellSize / length), cellSize / length, cellSize / length, edgecolor='black'));
			else:
				plt.gca().add_patch(Rectangle((cellX * cellSize, cellY * cellSize), cellSize, cellSize, edgecolor='black'));
		
		
	if normalize:
		plt.axis([0, 1, 0, 1])
	else:
		plt.axis([start, end, start, end])
		
	plt.show()
	
else:
	print("Incorrect noise type argument: blue_noise/white_noise/poisson")
	sys.exit()