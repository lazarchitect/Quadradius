#A Board class. exactly 1 is instatiated per game. All tiles and Tori have references to it.
#Top left is (0, 0). Moving down increases the first value. Moving right increases the second.

from Torus import Torus
from Tile import Tile

class Board():
	def __init__(self):
		self.grid = []
		for i in range(8):
			self.grid.append([])
			for j in range(10):
				self.grid[i].append(Tile(i, j, self))
				if(i == 0 or i==1):
					self.grid[i][j].item = Torus(0, i, j, self)
				elif(i==6 or i==7):
					self.grid[i][j].item = Torus(1, i, j, self)
					
	# def __str__(self):
	# 	retval = ""
	# 	for i in self.grid:
	# 		for j in i:
	# 			retval+=str(j)+", "
	# 		retval+="\n"
	# 	return retval	


	# #Handy little method to show how the coordinate system works.
	# def printcoords(self):
	# 	for i in self.grid:
	# 		for j in i:
	# 			print(j.x,j.y," ", end = "")
	# 		print()			