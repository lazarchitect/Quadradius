#really self-explanatory. Powers have a name and a use. 
#They are a class hat is only used in other classes: They don't have a repesentation on the board. However, their effects do.

class Power():
	def __init__(self, func):
		self.func = func
		self.name = func.__name__
		
	def __str__(self):
		return self.name