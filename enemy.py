import pygame, display, gamestart
from pygame.locals import *

class Enemy:
    
    car3 = pygame.image.load('Resources/image/car3.png')
    car4 = pygame.image.load('Resources/image/car4.png')
    playerRect = playerImage.get_rect()
    baddieImage = pygame.image.load('Resources/image/car2.png')
    sample = [car3,car4,baddieImage]
    
    def move(self):
        
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)
        
        for b in baddies:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)