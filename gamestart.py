import pygame, random, sys ,os,time
from pygame.locals import *

class GameStart:
    
    def __init__(self, quit, color):
        self.terminate = quit
        self.tekscolor = color
        
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
        textobj = font.render(text, 1, self.tekscolor)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)