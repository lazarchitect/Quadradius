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