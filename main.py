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

screen = pygame.display.set_mode(size)

draw_tiles(width, height, screen)

populate(width, screen)

#Gameplay loop
while 1:
	for event in pygame.event.get():
		if(pygame.mouse.get_pressed()[0]):

			unHighlightAll(b, screen)

			location = pygame.mouse.get_pos()
			# print(location)
			x = int(location[0]/100)
			y = int(location[1]/100)

			choiceTile = b.grid[y][x]
			if type(choiceTile.item).__name__ == "Torus":
				#THEY HAVE CLICKED ON A TORUS
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

				NEXT BIG STEP: GET THE TILES TO ACTUALLY MOVE

				# highlight(b, screen, x-1, y)

		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4):
			exit()



#Game Over loop
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4):
			exit()