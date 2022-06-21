class time:
    
pygame.mixer.music.stop()
    count=count-1
        gameOverSound.play()
    time.sleep(1)
    if (count==0):
        laugh.play()
        drawText('Game over', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
        drawText('Press any key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 30)
    pygame.display.update()
    time.sleep(2)
    waitForPlayerToPressKey()
    count=3
    gameOverSound.stop()