#Other powers: raise tile, lower tile, wall, trench, teach, swap, snake tunneling, scramble, relocate, refurb, purify, pilfer, orbic rehash, multiply, learn, kamikaze, invert, beneficiary, dredge, destroy, bombs, smart bombs, acidic

#Theres also switcheroo, centerpult, and power dump, which im thinking about implementing.
#Not entirely sure what network bridge does but i think its cool. power plant is a mystery. dont want recursive. OP.

import powers
from random import choice, randint

class Torus():

	def __init__(self, team, x, y, b):
		
		self.team = team #gonna be 0 or 1
		self.x = x
		self.y = y
		#note that being next to a wall or edge (unless you have climb or f2s) will limit this list. or ally presence
		self.board = b
	
		self.powerList = [] #ideally will be a list of Power objects
		self.abilities = {
			"moveDiagonal":False, 
			"climb": False, 
			"jumpProof":False, 
			"flatToSphere":False, 
			"inhibited":False,
			"invisible":False, #???
			"moveAgain":False,
			"parasite":False,
			"host":False,
			"networkBridge": False, #????
			"scavenger":False,
			"spyware":False,
			"growQuadradius": 0
		}
		
		
	def validMove(self, targetX, targetY):
		
		if(targetX < 0 or targetX > 7 or targetY<0 or targetY>7) and self.abilities["flatToSphere"] == False:
			return False #Out of bounds
		
		if (board[targetX][targetY].elevation - board[self.x][self.y].elevation > 1) and self.abilities["climb"]==False:
			return False #Too High
		
		if board[targetX][targetY] != None and board[targetX][targetY].item.__name__ == "Torus" and board[targetX][targetY].item.team == self.team:
			return False #Allies there
		
		if board[targetX][targetY].destroyed == True:
			return False #destroyed by bombs or acid
		
		return True		
		   	
	def generateValidMoveList(self):
		
		retval = []
		if validMove(self, self.x, self.y+1):
			retval.append((self.x, self.y+1))
		if validMove(self, self.x+1, self.y):
			retval.append((self.x+1, self.y))
		if validMove(self, self.x-1, self.y):
			retval.append((self.x-1, self.y))
		if validMove(self, self.x, self.y-1):
			retval.append((self.x, self.y-1))
		
		if(self.abilities["moveDiagonal"]==True):
			if validMove(self, self.x-1, self.y+1):
				retval.append((self.x-1, self.y+1))
			if validMove(self, self.x+1, self.y+1):
				retval.append((self.x+1, self.y+1))
			if validMove(self, self.x-1, self.y-1):
				retval.append((self.x-1, self.y-1))
			if validMove(self, self.x+1, self.y-1):
				retval.append((self.x+1, self.y-1))				
		
		return retval
	
	def move(self, destX, destY):
		validMoveList = GenerateValidMoveList()
		if (destX, destY) in validMoveList:
			self.x = destX
			self.y = destY
			

	def activatePower(self, power):
		pass
		#removeFromPowerList()
		#GainAbility()
		#note that f2s, move diagonal, and climb affect validMoves
		
	def __str__(self):
		return str(self.team)	




class Power():
	def __init__(self, name):
		self.name = name
		self.func = powers.powerList[name]
		
	def __str__(self):
		return self.name	
	
class Orb():
	def __init__(self, x, y, b):
		self.power = Power(choice(list(powers.powerList.keys())))
		self.x = x
		self.y = y
		self.board = b
		
	def __str__(self):
		return str(self.x) +", " + str(self.y) +": " + str(self.power)	
		
class Tile():
	def __init__(self, x, y):
		self.item = None
		self.x = x#location never gets changed but keeping a reference seems useful...
		self.y = y
		self.hasTorus = False #gets modified when tori initialized or when a piece moves here (or relocate)
		self.hasOrb = False
		self.elevation = 2
		self.destroyed = False
		self.mods = {
			"bankrupt":False, 
			"hotspot":False,
			"orbSpy":False,
			"tripwire":False
		}
	def __str__(self):
		if self.item==None: return " "
		return str(self.item)	

class Board():
	def __init__(self):
		self.grid = []
		for i in range(8):
			self.grid.append([])
			for j in range(8):
				self.grid[i].append(Tile(i, j))
				if(i==0 or i==1):
					self.grid[i][j].item = Torus(0, i, j, self)
				elif(i==6 or i == 7):
					self.grid[i][j].item = Torus(1, i, j, self)
					
	def __str__(self):
		retval = ""
		for i in self.grid:
			for j in i:
				retval+=str(j)+", "
			retval+="\n"
		return retval	

	def printcoords(self):
		for i in self.grid:
			for j in i:
				print(j.x,j.y," ", end = "")
			print()
			

if __name__ == "__main__":
	
	x = randint(0, 7)
	y = randint(0, 7)
	
	o = Orb(x,y)
	print(o)
