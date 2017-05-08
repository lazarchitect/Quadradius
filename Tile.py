#A class representing a tile on the board. 
#Mostly a way to keep track of data. Tiles don't do anything, per se. They just have things happen to them.

class Tile():
	def __init__(self, x, y, b):
		self.item = None
		self.x = x#location never gets changed but keeping a reference seems useful...
		self.y = y
		self.board = b
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