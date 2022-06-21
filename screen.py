import pygame, os
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

class Screen:
    
    def draw(self):
        drawText('Press any key to start the game.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3))
        drawText('And Enjoy', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3)+30)
        pygame.display.update()
        waitForPlayerToPressKey()
        zero=0
        if not os.path.exists("data/save.dat"):
            f=open("data/save.dat",'w')
        f.write(str(zero))
        f.close()   
    v=open("data/save.dat",'r')
    topScore = int(v.readline()) 
    v.close()
    while (count>0):
    # start of the game
        baddies = []
        score = 0
        playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
        moveLeft = moveRight = moveUp = moveDown = False
        reverseCheat = slowCheat = False
        baddieAddCounter = 0
        pygame.mixer.music.play(-1, 0.0)