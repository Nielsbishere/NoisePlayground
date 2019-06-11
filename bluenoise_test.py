from matplotlib.image import imread
import random
import math

# constants
kernelSize = 5 
points = 16
marker = [ "ro", "bo", "mo", "co", "yo" ]		# Center, sample0, sample1, sample2, sample3

# image
img = imread('noise.png')
width = len(img)
height = len(img[0])

def generate(img, width, height, kernelSize, points, marker):

	# random point
	x = random.randint(kernelSize, width - kernelSize - 1)
	y = random.randint(kernelSize, height - kernelSize - 1)
	
	# kernel, sort by distance
	values = [ [], [], [], [] ]
	
	for i in range(-kernelSize, kernelSize):
		for j in range(-kernelSize, kernelSize):
			px = (i + x) % width
			py = (j + y) % height
			value = img[height - 1 - py][px][0]
			ii = i + .5
			jj = j + .5
			sqrDist = ii * ii + jj * jj
			t = math.floor(value * 4)
			
			if i == 0 and j == 0:
				values[0].append((px + py * width, 0, 0, value))
				values[1].append((px + py * width, 0, 0, value))
				values[2].append((px + py * width, 0, 0, value))
				values[3].append((px + py * width, 0, 0, value))
			else:
				values[t].append((px + py * width, sqrDist, random.random(), value))
		
	import matplotlib.pyplot as plt
	
	k = 1
	plt.plot(x, y, marker[0])
	
	print("static const float2 samples[4][", points ,"] = {")
	
	for value in values:
		value = sorted(value, key=lambda v: v[1] + v[2])
		value = value[0:points];
	
		print("\t{")
		
		index = 0
	
		for v in value:
			i = v[0] % width
			j = math.floor(v[0] / width)
			plt.plot(i + .5, j + .5, marker[k])
			
			if index % 4 == 0:
				print("\t\t", end="")
			
			if index == len(value) - 1:
				print("float2(", i - x, ", ", j - y, ")")
			else:
				print("float2(", i - x, ", ", j - y, "),", end =" ")
				
			if index % 4 == 3:
				print("")
				
			index += 1

		if k == len(values):
			print("\t}")
		else:
			print("\t},")
			
		k += 1
		
	print("};")
	
	plt.imshow(img, extent=(0, width, 0, height))
	plt.axis([x - kernelSize, x + kernelSize, y - kernelSize, y + kernelSize])
	
	def press(event):
		if event.key == 'x':
			plt.close()
			generate(img, width, height, kernelSize, points, marker)

	plt.connect('key_press_event', press)
	plt.show()

generate(img, width, height, kernelSize, points, marker)