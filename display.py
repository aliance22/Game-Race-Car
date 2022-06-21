import pygame
from gamestart import GameStart
from pygame.locals import *

WINDOWHEIGHT = 600
WINDOWWIDTH = 800

class Display(GameStart):
    
    def __init__(self, mainClock, windowSurface, font):
        self.mainClock = mainClock
        self.windowSurface = windowSurface
        self.font = font
    
    def show_display(self):
        pygame.init()
        
    def waktu(self):
        self.mainClock = pygame.time.Clock()
        
    def windows(self):
        self.windowSurface = pygame.display.set_mode(WINDOWHEIGHT, WINDOWWIDTH)
        pygame.display.set_caption('car race')
        
    def text(self):
        self.font = pygame.font.SysFont(None, 30)
    
    def control(self):
        return pygame.mouse.set_visible(False)
    
    def sound(self):
        return pygame.mixer.music.load('Resources/music/music_car.wav')
    laugh = pygame.mixer.Sound('Resources/music/music_laugh.wav')