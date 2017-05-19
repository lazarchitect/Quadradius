import pygame
from consts import *
from random import randint
from Orb import Orb

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
		b.grid[y][x].item = Orb(x, y, b)
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

	TIQ = b.grid[y][x] #tile in question
	elev = TIQ.elevation

	img = pygame.image.load("Tile"+str(elev)+"Glow.png")
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
				
				TIQ = b.grid[y][x] #tile in question
				elev = TIQ.elevation

				img = pygame.image.load("Tile"+str(elev)+".png")

				img = pygame.transform.scale(img, (tileWidth, tileHeight))
				screen.blit(img, (x*tileWidth, y*tileHeight))
				thing = b.grid[y][x].item
				if(thing != None):
					blitToScreen(b, screen, thing, x, y)
				pygame.display.update(pygame.Rect(x*tileWidth, y*tileHeight, tileWidth, tileHeight))
				b.grid[y][x].isHighlighted = False


#This method triggers when a torus is moved, altering all relevant variables.
def updateValues(b, screen):
	global moveCount, nCheck, n, torusCount, low, high
	moveCount+=1
	nCheck += 1

	if nCheck >= n:
		nCheck = 0
		spawnOrbs(b, screen)

	tempCount = 0
	for i in b.grid:
		for j in i:
			if type(j.item).__name__ == "Torus":
				tempCount += 1
	torusCount = tempCount
	
	if torusCount < 21: n = 3
	else: n = 7

	low = int((40 - torusCount)/3)+2
	high = low + 1


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

	global player1Score
	global player2Score

	toMove = choiceTile.item

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
					
					if type(destTile.item).__name__ == "Torus": #If the detination contains a torus, (definitely an enemy)
						if(destTile.item.team == 0): player1Score -= 1
						else: player2Score -= 1


					if type(destTile.item).__name__ == "Orb":
						choiceTile.item.powerList.append(destTile.item.power)
						print(destTile.item.power)

					choiceTile.item.x = destTile.x ####ehhh???? The purpose of this is for easy access to row and col for abilities. not sure if it works yet
					choiceTile.item.y = destTile.y

					#Also, not sure if changing Tile references here is good...

					destTile.item = choiceTile.item
					blitToScreen(b, screen, destTile.item, destTile.y, destTile.x) #WHY IS IT Y THEN X? THIS IS BANANAS
					choiceTile.item = None
					img = pygame.image.load("Tile3.png")
					img = pygame.transform.scale(img, (tileWidth, tileHeight))
					screen.blit(img, (choiceTile.y*tileWidth, choiceTile.x*tileHeight)) #WTFFFF
					pygame.display.flip()

					unHighlightAll(b, screen)
					updateValues(b, screen)
					return True

				else:
					unHighlightAll(b, screen)
					return False

			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4):
				exit()

def spawnOrbs(b, screen):
	num = randint(low, high)
	for i in range(num):
		while 1:
			x = randint(0, boardWidth-1)
			y = randint(0, boardHeight-1)
			if b.grid[y][x].item == None:
				b.grid[y][x].item = Orb(x,y,b)
				blitToScreen(b, screen, b.grid[y][x].item, x, y)
				break

#Each turn, tell the player that its their turn.
#Other tasks: display available powers, chatbox, FF button
def updateInfoZone(b, screen, currentTeam):

	global player1Score
	global player2Score

	pygame.draw.rect(screen, WHITE, infoZoneRect)
	screen.blit(ARIAL.render("Player " + str(currentTeam + 1) + ", Your Turn", 0, BLACK), (infoZoneLeft+35, infoZoneTop))

	screen.blit(ARIAL.render("Player 1's Score: " + str(player1Score), 0, BLACK), (infoZoneLeft+35, infoZoneTop + 100))
	screen.blit(ARIAL.render("Player 2's Score: " + str(player2Score), 0, BLACK), (infoZoneLeft+35, infoZoneTop + 130))

	pygame.display.update(infoZoneRect)



#Should notify the winner if they destroyed all enemy pieces. A tie is also possible.
#returns true if the game is over, and false if not.
#if this returns true, break the game loop.
def endCheck():
	
	global player1Score
	global player2Score

	if player2Score == 0 or player1Score == 0:
		return True
	
	return False	


def displayResults(b, screen):
	
	global player1Score
	global player2Score

	pygame.draw.rect(screen, WHITE, infoZoneRect)
	
	if(player1Score == 0 and player2Score == 0):
		screen.blit(ARIAL.render("It's a Tie!", 0, BLACK), (infoZoneLeft+35, infoZoneTop)) #Impossible to get a tie without the Kamikaze or Bombs powers
	elif(player1Score == 0):
		screen.blit(ARIAL.render("Player 2 Wins!", 0, BLACK), (infoZoneLeft+35, infoZoneTop))
	elif(player2Score == 0):
		screen.blit(ARIAL.render("Player 1 Wins!", 0, BLACK), (infoZoneLeft+35, infoZoneTop))

	pygame.display.update(infoZoneRect)

