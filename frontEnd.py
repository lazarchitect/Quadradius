import pygame
from classes import *

pygame.init()

windowX = 800
windowY = 800
size = (windowX, windowY)

#COLORS
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
TEAL =  (  0, 128, 128)
GRAY1 = ( 80,  80,  80)
GRAY2 = (100, 100, 100)
GRAY3 = (130, 130, 130)
GRAY4 = (160, 160, 160)
GRAY5 = (180, 180, 180)

screen = pygame.display.set_mode(size)
# screen.fill(BLACK)	

def draw_tiles():
	for i in range(8):
		for j in range(8):
			pygame.draw.rect(screen, GRAY3, pygame.Rect(i*100, j*100, 100, 100), 0)
			pygame.draw.rect(screen, BLACK, pygame.Rect(i*100, j*100, 100, 100), 5)

def populate():
	for i in range(8):
		

draw_tiles()

pygame.display.update()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4):
			exit()