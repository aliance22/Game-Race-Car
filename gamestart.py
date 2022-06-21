import pygame, sys
from pygame.locals import *

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 40
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 8
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 6
PLAYERMOVERATE = 5
count=3

class GameStart:
    
    def __init__(self, quit, color):
        self.terminate = quit
        self.TEXTCOLOR = color
        
    def terminate(self):
        pygame.quit()
        sys.exit()
        
    def waitForPlayerToPressKey(self):
        while True:
            for event in pygame.event.get(self):
                if event.type == QUIT:
                    self.terminate()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE: #escape quits
                        self.terminate()
                    return
    
    def playerHasHitBaddie(self, playerRect, baddies):
        for b in baddies:
            if playerRect.colliderect(b['rect']):
                return True
        return False
    
    def drawText(self, text, font, surface, x, y):
        textobj = font.render(text, 1, self.TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)