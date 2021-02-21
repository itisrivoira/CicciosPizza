import pygame
import pygame_menu #libreria di pygame che permette una facile creazione del main menu di gioco
from pygame_menu import sound
from pygame.locals import *

import time, datetime


#dobbiamo mettere a posto la finestra quando si clicca su inizia partita,
#coordinate immagini,
#grandezza immagini,
#timer

pygame.init()#inizio programma
screen = pygame.display.set_mode((1280, 920)) #CREAZIONE SCHERMO DI GIOCO

surf_pizzaVuota=pygame.image.load('Immagini_Gioco/Immagini_Livello/impasto.png')
rect_pizzaVuota = surf_pizzaVuota.get_rect()
x=450  #coordinata centro
y=550  #coordinata centro
rect_pizzaVuota.move_ip(x, y)
screen.blit(surf_pizzaVuota, (x,y))

surf_pomodoro=pygame.image.load('Immagini_Gioco/Immagini_Livello/pomodoro4.png')
rect_pomodoro = surf_pomodoro.get_rect()
x=400  #coordinata in alto a sinistra/destra
y=50  #coordinata in alto a sinistra/destra
rect_pomodoro.move_ip(x, y) #MOVE IP MUOVE IL RECT NELLE CORDINATE DECISE DA UTENTE
screen.blit(surf_pomodoro, (x,y))

surf_mozzarella=pygame.image.load('Immagini_Gioco/Immagini_Livello/formaggio.png')
rect_mozzarella = surf_pomodoro.get_rect()
x=850  #coordinata in alto a sinistra/destra sotto pomodoro
y=50  #coordinata in alto a sinistra/destra sotto pomodoro
rect_mozzarella.move_ip(x, y)
screen.blit(surf_mozzarella, (x,y))

pygame.display.flip()


flag=0

timer_stop = datetime.datetime.utcnow() +datetime.timedelta(seconds=30)

done = False
while not done:
    for ev in pygame.event.get():
        #if datetime.datetime.utcnow() > timer_stop:
        #    print ("timer complete")
        #    break
        # se l'evento e' la fine del programma esce
        if ev.type == pygame.QUIT:
            pygame.quit()
            done = True
        # se l'evento e' un click ... (vedi sotto)
        elif ev.type == MOUSEBUTTONDOWN:
            click = ev.pos
            if rect_pomodoro.collidepoint(click) and ev.button==1:
                surf_pizzaVuota=pygame.image.load('Immagini_Gioco/Immagini_Livello/pizzaPomodoro.png')
                rect_pizzaVuota = surf_pizzaVuota.get_rect()
                x=450  #coordinata centro
                y=550  #coordinata centro
                screen.blit(surf_pizzaVuota, (x,y))
                pygame.display.flip()
                flag=1

            if rect_mozzarella.collidepoint(click) and ev.button==1 and flag==1:
                surf_pizzaVuota=pygame.image.load('Immagini_Gioco/Immagini_Livello/margherita.png')
                rect_pizzaVuota = surf_pizzaVuota.get_rect()
                x=450  #coordinata centro
                y=550  #coordinata centro
                screen.blit(surf_pizzaVuota, (x,y))
                pygame.display.flip()
