import pygame

from Power import Power
from Torus import Torus
from Board import Board
from Tile import Tile
from Orb import Orb

from consts import *
from functs import *

pygame.init()
b = Board()

screen = pygame.display.set_mode(screensize)

ARIAL = pygame.font.SysFont("arial", 30)

#initialize the board state
draw_tiles(boardWidth, boardHeight, screen)
populate(boardWidth, screen)

#Intialize the "info zone"
drawInfoZone(b, screen)

currentTeam = 0 # 0 is red, 1 is blue
gameOver = False

#Gameplay loop
while 1:

	updateInfoZone(b, screen, currentTeam)

	for event in pygame.event.get():
		if(pygame.mouse.get_pressed()[0]):

			unHighlightAll(b, screen)

			location = pygame.mouse.get_pos()
			# print(location)
			x = int(location[0]/tileWidth)
			y = int(location[1]/tileHeight)

			if x >= boardWidth: 
				break

			choiceTile = b.grid[y][x]
			if type(choiceTile.item).__name__ == "Torus" and choiceTile.item.team == currentTeam:
				#THEY HAVE CLICKED ON A (their own!) TORUS
				if y != 0: 
					upTile = b.grid[y-1][x]
					if(validMove(choiceTile, upTile)):
						highlight(b, screen, x, y-1)
				if x != 0: 
					leftTile = b.grid[y][x-1]
					if(validMove(choiceTile, leftTile)):
						highlight(b, screen, x-1, y)
				if x != 9: 
					rightTile = b.grid[y][x+1]
					if(validMove(choiceTile, rightTile)):
						highlight(b, screen, x+1, y)
				if y != 7: 
					downTile = b.grid[y+1][x]
					if(validMove(choiceTile, downTile)):
						highlight(b, screen, x, y+1)

				result = move(b, screen, choiceTile, currentTeam)
				
				if result:
					currentTeam = abs(1 - currentTeam)
					if endCheck():
						gameOver = True

		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4):
			exit()

	if(gameOver):
		break

#Game Over loop
displayResults(b, screen)
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4):
			exit()