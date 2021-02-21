import pygame
import pygame_menu #libreria di pygame che permette una facile creazione del main menu di gioco
from pygame_menu import sound

import time, datetime


#dobbiamo mettere a posto la finestra quando si clicca su inizia partita,
#coordinate immagini,
#grandezza immagini,
#timer


pizzaVuota=pygame.image.load('Immagini_Gioco/pizzaVuota.png')
rect_pizzaVuota = surf_pizzaVuota.get_rect()
x=50  #coordinata centro
y=50  #coordinata centro
screen.blit(pizzaVuota, (x,y))

pomodoro=pygame.image.load('Immagini_Gioco/pomodoro.png')
rect_pomodoro = surf_pomodoro.get_rect()
xp=50  #coordinata in alto a sinistra/destra
yp=50  #coordinata in alto a sinistra/destra
screen.blit(pomodoro, (xp,yp))

mozzarella=pygame.image.load('Immagini_Gioco/mozzarella.png')
rect_mozzarella = surf_pomodoro.get_rect()
x=50  #coordinata in alto a sinistra/destra sotto pomodoro
y=50  #coordinata in alto a sinistra/destra sotto pomodoro
screen.blit(mozzarella, (x,y))

pygame.display.flip()


flag=0

timer_stop = datetime.datetime.utcnow() +datetime.timedelta(seconds=30)

done = False
while not done:
    for ev in pygame.event.get():
        if datetime.datetime.utcnow() > timer_stop:
            print "timer complete"
            break
        # se l'evento e' la fine del programma esce
        if ev.type == QUIT:
            done = True
        # se l'evento e' un click ... (vedi sotto)
        elif ev.type == MOUSEBUTTONDOWN:
            click = ev.pos
            if rect_pomodoro.collidepoint(click) and ev.button==1:
                pizzaPomodoro=pygame.image.load('Immagini_Gioco/pizzaPomodoro.png')
                rect_pizzaPomodoro = surf_pizzaPomodoro.get_rect()
                x=50  #coordinata centro
                y=50  #coordinata centro
                screen.blit(pizzaPomodoro, (x,y))
                pygame.display.flip()
                flag=1

            if rect_mozzarella.collidepoint(click) and ev.button==1 and flag==1:
                margherita=pygame.image.load('Immagini_Gioco/pizzaMargherita.png')
                rect_margherita = surf_margherita.get_rect()
                x=50  #coordinata centro
                y=50  #coordinata centro
                screen.blit(margherita, (x,y))
                pygame.display.flip()