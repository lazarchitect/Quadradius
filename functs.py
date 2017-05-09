import pygame
from consts import *

def draw_tiles(width, height, screen):
	# retval = []
	for x in range(width):
		for y in range(height):
			img = pygame.image.load("Tile3.png")
			img = pygame.transform.scale(img, (tileWidth, tileHeight))
			screen.blit(img, (x*tileWidth, y*tileHeight))
	pygame.display.flip()
	# return retval

#Draws the initial tori onto the screen.
def populate(width, screen):
	for x in range(width):
		for y in range(2):
			img = pygame.image.load("RedTorus.png")
			img = pygame.transform.scale(img, (tileWidth, tileHeight))
			screen.blit(img, (x*tileWidth, y*tileHeight))
	for x in range(width):
		for y in range(6,8):
			img = pygame.image.load("BlueTorus.png")
			img = pygame.transform.scale(img, (tileWidth, tileHeight))
			screen.blit(img, (x*tileWidth, y*tileHeight))
	pygame.display.flip()		

def drawInfoZone(b, screen):
	pygame.draw.rect(screen, WHITE, infoZoneRect, 0)
	pygame.display.update(infoZoneRect)

def blitToScreen(b, screen, item, x, y):
	className = type(item).__name__
	if(className == "Orb"):
		img = pygame.image.load("Orb.png")
		img = pygame.transform.scale(img, (tileWidth, tileHeight))
		screen.blit(img, (x*tileWidth, y*tileHeight))
	if(className == "Torus"):
		if(item.team == 0):
			img = pygame.image.load("RedTorus.png")
			img = pygame.transform.scale(img, (tileWidth, tileHeight))
			screen.blit(img, (x*tileWidth, y*tileHeight))
		else:
			img = pygame.image.load("BlueTorus.png")
			img = pygame.transform.scale(img, (tileWidth, tileHeight))
			screen.blit(img, (x*tileWidth, y*tileHeight))

#Given a tile's coordinates, makes it glow yellow
def	highlight(b, screen, x, y):
	img = pygame.image.load("Tile3Glow.png")
	img = pygame.transform.scale(img, (tileWidth, tileHeight))
	screen.blit(img, (x*tileWidth, y*tileHeight))
	
	thing = b.grid[y][x].item
	if(thing != None):
		blitToScreen(b, screen, thing, x, y)
	pygame.display.update(pygame.Rect(x*tileWidth, y*tileHeight, tileWidth, tileHeight))
	b.grid[y][x].isHighlighted = True

#Shuts off all glowing tiles, wherever they might be. Might be more efficient to keep track of any highlited tiles instead of checking all
def unHighlightAll(b, screen):
	for y in range(8):
		for x in range(10):
			if(b.grid[y][x].isHighlighted == True):
				img = pygame.image.load("Tile3.png")
				img = pygame.transform.scale(img, (tileWidth, tileHeight))
				screen.blit(img, (x*tileWidth, y*tileHeight))
				thing = b.grid[y][x].item
				if(thing != None):
					blitToScreen(b, screen, thing, x, y)
				pygame.display.update(pygame.Rect(x*tileWidth, y*tileHeight, tileWidth, tileHeight))
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

#Moves a torus from its current location to a desired adjacent Tile, GIVEN THAT THE DEST TILE IS VALID(HIGHLIGHTED). 
#Returns true if the move happened. False if not.
def move(b, screen, choiceTile, team):
	#take new input. if THAT is on a highlighted tile, move the torus there, unhighlight all, return true. else, unhighlight all and return False
	while 1:
		for event in pygame.event.get():
			
			if(pygame.mouse.get_pressed()[0]):
			
				location = pygame.mouse.get_pos()
				x = int(location[0]/tileWidth)
				y = int(location[1]/tileHeight)

				if x >= boardWidth: 
					unHighlightAll(b, screen)
					return False

				destTile = b.grid[y][x]
				if(destTile.isHighlighted == True):
					
					if type(destTile.item).__name__ == "Torus":
						print("BOOM!")

					destTile.item = choiceTile.item
					blitToScreen(b, screen, destTile.item, destTile.y, destTile.x) #WHY IS IT Y THEN X? THIS IS BANANAS
					choiceTile.item = None
					img = pygame.image.load("Tile3.png")
					img = pygame.transform.scale(img, (tileWidth, tileHeight))
					screen.blit(img, (choiceTile.y*tileWidth, choiceTile.x*tileHeight)) #WTFFFF
					pygame.display.flip()

					unHighlightAll(b, screen)
					return True

				else:
					unHighlightAll(b, screen)
					return False

			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4):
				exit()

#Each turn, tell the player that its their turn.
#Other tasks: display available powers, chatbox, FF button
def updateInfoZone(b, screen):
	pass


#Should notify the winner if they destroyed all enemy pieces. A tie is also possible.
#returns true if the game is over, and false if not.
#if this returns true, break the game loop.
def endCheck(b):
	pass







