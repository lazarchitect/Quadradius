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

pygame.display.update()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4):
			exit()