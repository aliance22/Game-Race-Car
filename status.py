class Status:
    
    def score(self):
        return('Score: %s' % (score), font, windowSurface, 128, 0)

    def Tops_core(self):
        return('Top Score: %s' % (topScore), font, windowSurface,128, 20)
        
    def Rest_life(self):
        return('Rest Life: %s' % (count), font, windowSurface,128, 40)
        
            windowSurface.blit(playerImage, playerRect)

        
        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()