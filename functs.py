import pygame

from Tile import Tile

def draw_tiles(width, height, screen):
	# retval = []
	for x in range(width):
		for y in range(height):
			# retval.append(Tile(x, y, b))
			img = pygame.image.load("Tile3.png")
			img = pygame.transform.scale(img, (100, 100))
			screen.blit(img, (x*100, y*100))

	# return retval

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