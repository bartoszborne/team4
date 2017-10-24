import time

grid_x = []
grid_y = []
grid_c = []

def anim():
	for i in range(1000):
		frame()
		time.sleep(0.1)

def frame():
	width = 79
	height = 24
	for j in range(height):
		lineout = ""
		for i in range(width):
			match = False
			for k in range(len(grid_x)):
				if (grid_x[k] == i) and (grid_y[k] == j):
					match = grid_c[k]
					break
			if match:
				lineout += grid_c[k]
			else:
				lineout += str(" ")
		print(lineout)


def rect(x,y,width,height,char,fill=False):
	for i in range(x, x+width):
		if fill:
			for j in range(y, y+height):
				grid_x.append(i)
				grid_y.append(j)
				grid_c.append(char)
		else:
			grid_x.append(i)
			grid_y.append(y)
			grid_c.append(char)
			grid_x.append(i)
			grid_y.append(y+height-1)
			grid_c.append(char)
	if not fill:
		for j in range(y+1, y+height):
			grid_x.append(x)
			grid_y.append(j)
			grid_c.append(char)
			grid_x.append(x+width-1)
			grid_y.append(j)
			grid_c.append(char)

def clear():
	grid_x=[]
	grid_y=[]
	grid_c=[]

rect(5,5,5,5,"#",True)
rect(12,6,5,5,"#",False)
frame()
