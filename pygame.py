import pygame
from pygame.locals import *
from classes import *

def main():
	pygame.init()
	windowX = 300
	windowY = 400
	size = (windowX, windowY)
	screen = pygame.display.set_mode(size)
	

	# Event loop
	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return


if __name__ == '__main__': main()