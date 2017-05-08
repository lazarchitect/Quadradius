#really self-explanatory. Powers have a name and a use. 
#They are a class hat is only used in other classes: They don't have a repesentation on the board. However, their effects do.

class Power():
	def __init__(self, name):
		self.name = name
		self.func = powers.powerList[name]
		
	def __str__(self):
		return self.name