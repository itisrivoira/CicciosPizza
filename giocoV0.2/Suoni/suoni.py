import pygame
from pygame.locals import *

pygame.init()

pygame.mixer.music.load("Suoni/colonnaSonora.mp3")
pygame.mixer.music.play(-1)   #play della colonna sonora
pygame.mixer.music.set_volume(0.6)

#creo suono click
sound1 = pygame.mixer.Sound("Suoni/click.wav")

#aggiorno lo schermo
pygame.display.flip()

#ciclo while che si chiude quando l'utente chiude il programma
done = False
while not done:
    for ev in pygame.event.get():
        if ev.type == QUIT:                       # chiusura del programma
            done = True
        elif ev.type == MOUSEBUTTONDOWN:          # click del mouse
            click=ev.pos
            tastoMouse=ev.button
            if tastoMouse==1:
                sound1.play()                     #play suono click
           # if ButtonMuto.collidepoint(click) and tastoMouse==1:
             #   pygame.mixer.music.fadeout(5000)    #si ferma la colonna sonora








        










