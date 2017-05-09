import pygame
#This file defines some variables for use in the main program. 

#Tile dimensions, in pixels
tileWidth = 90
tileHeight = 90
tilesize = (tileWidth, tileHeight)

#Board space dimensions, in Tiles
boardWidth = 10
boardHeight = 8

#Screen dimensions, in pixels
screenWidth = tileWidth*boardWidth + 400
screenHeight = tileHeight*boardHeight
screensize = (screenWidth, screenHeight)

infoZoneLeft = tileWidth * boardWidth
infoZoneTop = 0
infoZoneWidth = 400
infoZoneHeight = screenHeight

infoZoneRect = pygame.Rect(infoZoneLeft, infoZoneTop, infoZoneWidth, infoZoneHeight)

#COLORS
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
TEAL =  (  0, 128, 128)
# GRAY1 = ( 80,  80,  80)
# GRAY2 = (100, 100, 100)
# GRAY3 = (130, 130, 130)
# GRAY4 = (160, 160, 160)
# GRAY5 = (180, 180, 180)