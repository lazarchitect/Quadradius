import pygame

def draw_tiles(width, height, screen):
	# retval = []
	for x in range(width):
		for y in range(height):
			img = pygame.image.load("Tile3.png")
			img = pygame.transform.scale(img, (100, 100))
			screen.blit(img, (x*100, y*100))
	pygame.display.flip()
	# return retval

#Draws the initial tori onto the screen.
def populate(width, screen):
	for x in range(width):
		for y in range(2):
			img = pygame.image.load("RedTorus.png")
			img = pygame.transform.scale(img, (100, 100))
			screen.blit(img, (x*100, y*100))
	for x in range(width):
		for y in range(6,8):
			img = pygame.image.load("BlueTorus.png")
			img = pygame.transform.scale(img, (100, 100))
			screen.blit(img, (x*100, y*100))
	pygame.display.flip()		

def blitToScreen(b, screen, item, x, y):
	className = type(item).__name__
	# print(className)
	if(className == "Orb"):
		img = pygame.image.load("Orb.png")
		img = pygame.transform.scale(img, (100, 100))
	if(className == "Torus"):
		if(item.team == 0):
			img = pygame.image.load("RedTorus.png")
			img = pygame.transform.scale(img, (100, 100))
		else:
			img = pygame.image.load("BlueTorus.png")
			img = pygame.transform.scale(img, (100, 100))
	screen.blit(img, (x*100, y*100))
	# pygame.display.update(pygame.Rect(x*100, y*100, 100, 100))
			

#Given a tile's coordinates, makes it glow yellow
def	highlight(b, screen, x, y):
	img = pygame.image.load("Tile3Glow.png")
	img = pygame.transform.scale(img, (100, 100))
	screen.blit(img, (x*100, y*100))
	
	thing = b.grid[y][x].item
	# print(thing)
	if(thing != None):
		blitToScreen(b, screen, thing, x, y)
	pygame.display.update(pygame.Rect(x*100, y*100, 100, 100))
	b.grid[y][x].isHighlighted = True

#Shuts off all glowing tiles, wherever they might be. Might be more efficient to keep track of any highlited tiles instead of checking all
def unHighlightAll(b, screen):
	for y in range(8):
		for x in range(10):
			if(b.grid[y][x].isHighlighted == True):
				img = pygame.image.load("Tile3.png")
				img = pygame.transform.scale(img, (100, 100))
				screen.blit(img, (x*100, y*100))
				thing = b.grid[y][x].item
				if(thing != None):
					blitToScreen(b, screen, thing, x, y)
				pygame.display.update(pygame.Rect(x*100, y*100, 100, 100))
				b.grid[y][x].isHighlighted = False

#Checks if a move is valid... blegh im tired
def validMove(srcTile, destTile):
	#What makes a move valid?
	#What makes a move INVALID?
	#Cant jump on teammate.
	#Cant jump off screen (handled already.... hopefully. wait, cant click there anyway)
	#Thats about it haha

	if(destTile.item != None and type(destTile.item).__name__ == "Torus"):
		if(srcTile.item.team == destTile.item.team):
			return False
		return True
	#Other checks later. height, acidic, etc
	return True		












