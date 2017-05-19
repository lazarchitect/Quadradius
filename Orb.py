#Orbs spawn into locatons on the board, given by x and y coords.
#Each has a Power. When a Torus steps on an orb, it gets the power and the orb is destroyed.

from Power import Power
from random import choice
from powers import *

class Orb():
	def __init__(self, x, y, b):
		self.power = Power(choice(powerList))
		self.x = x
		self.y = y
		self.board = b
		
	def __str__(self):
		return str(self.x) +", " + str(self.y) +": " + str(self.power)	