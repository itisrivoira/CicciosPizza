import pygame
import pygame_menu #libreria di pygame che permette una facile creazione del main menu di gioco
from pygame_menu import sound
from pygame.locals import *


import time, datetime


def victory(schermo, counter):
    pygame.mixer.music.load("Suoni/level_complete.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    fontVittoria = pygame.font.SysFont("Verdana", 34, italic=True)
    surf_text = fontVittoria.render("LIVELLO COMPLETATO !!!", True, (255, 255, 0))
    x=450
    y= 350
    schermo.blit(surf_text, (x,y))

    if(counter >= 40):
        print("tre stelle")
    elif (counter < 40 and counter >= 20):
        print("due stelle")
    elif (counter < 20):
        print("una stella")

#dobbiamo mettere a posto la finestra quando si clicca su inizia partita,
#coordinate immagini,
#grandezza immagini,
#timer

def main():
    # pygame.init()#inizio programma non necessario perchè il programma iniza dal menu quindi richiamarco è inutile
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1280, 920)) #CREAZIONE SCHERMO DI GIOCO
    pygame.display.set_caption("LIVELLO 1 CICCIO'S PIZZA ")
    surf_background = pygame.image.load("Immagini_Gioco/background_menu/sfondo.jpg").convert()
    screen.blit(surf_background, (0, 0))


    surf_ordine = pygame.image.load("Immagini_Gioco/Immagini_Livello/ordinazione.png")
    screen.blit(surf_ordine, (20, 0))

    fontOrdine = pygame.font.SysFont("Verdana", 34, italic=True)
    text = ["PIZZA MARGHERITA","CLICCA IN QUESTO ORDINE:","1)POMODORO","2)MOZZARELLA"]
    descriptioncounter = 0
    for x in text:
            descriptioncounter += 0.5
            screen.blit((pygame.font.SysFont('constantia',18).render(x, True,(255, 0, 0))),(100,100+100*descriptioncounter))
    descriptioncounter = 0

            
    #surf_ordine = fontOrdine.render("ORDINE ---> MARGHERITA\n Clicca gli ingredienti nel sequente ordine \n 1)POMODORO\n2)MOZZARELLA", True, (255, 255, 0))
    #screen.blit(surf_ordine, (50,50))

    surf_pizzaVuota=pygame.image.load('Immagini_Gioco/Immagini_Livello/impasto.png')
    rect_pizzaVuota = surf_pizzaVuota.get_rect()
    x=475  #coordinata centro
    y=500  #coordinata centro
    rect_pizzaVuota.move_ip(x, y)
    screen.blit(surf_pizzaVuota, (x,y))

    surf_pomodoro=pygame.image.load('Immagini_Gioco/Immagini_Livello/pomodoro.png')
    rect_pomodoro = surf_pomodoro.get_rect()
    x=400  #coordinata in alto a sinistra/destra
    y=50  #coordinata in alto a sinistra/destra
    rect_pomodoro.move_ip(x, y) #MOVE IP MUOVE IL RECT NELLE CORDINATE DECISE DA UTENTE
    screen.blit(surf_pomodoro, (x,y))

    surf_mozzarella=pygame.image.load('Immagini_Gioco/Immagini_Livello/mozzarella.png')
    rect_mozzarella = surf_pomodoro.get_rect()
    x=850  #coordinata in alto a sinistra/destra sotto pomodoro
    y=50  #coordinata in alto a sinistra/destra sotto pomodoro
    rect_mozzarella.move_ip(x, y)
    screen.blit(surf_mozzarella, (x,y))

    surf_tornahome= pygame.image.load("Immagini_Gioco/Immagini_Livello/menu.png")
    rect_tornahome = surf_tornahome.get_rect()
    x=1000  #coordinata centro
    y=700  #coordinata centro
    rect_tornahome.move_ip(x, y)
    screen.blit(surf_tornahome, (x,y))

    pygame.display.flip()


    flag=0
    ritornoMenu = 0

    timer_stop = datetime.datetime.utcnow() +datetime.timedelta(seconds=30)
    #start_ticks=pygame.time.get_ticks() #starter tick
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)
    counter, text = 60, '60'
    poz = font.render(text, True, (0, 0, 0), (255, 255, 0))

    done = False
    while not done:
        #seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
        #if seconds>10: # if more than 10 seconds close the game
        #    break
       # print (seconds) #print how many seconds
        for ev in pygame.event.get():
            #if datetime.datetime.utcnow() > timer_stop:
            #    print ("timer complete")
            #    break
            # se l'evento e' la fine del programma esce
            if ev.type == pygame.QUIT:
                #pygame.quit()
                ritornoMenu = 1
                done = True
            # se l'evento e' un click ... (vedi sotto)
            elif ev.type == MOUSEBUTTONDOWN:
                click = ev.pos
                if rect_pomodoro.collidepoint(click) and ev.button==1 and flag == 0:
                    surf_pizzaVuota=pygame.image.load('Immagini_Gioco/Immagini_Livello/marinara.png')
                    rect_pizzaVuota = surf_pizzaVuota.get_rect()
                    x=475  #coordinata centro
                    y=500  #coordinata centro
                    screen.blit(surf_pizzaVuota, (x,y))
                    pygame.display.flip()
                    flag=1

                if rect_mozzarella.collidepoint(click) and ev.button==1 and flag==1:
                    surf_pizzaVuota=pygame.image.load('Immagini_Gioco/Immagini_Livello/pizzaMargherita.png')
                    rect_pizzaVuota = surf_pizzaVuota.get_rect()
                    x=475  #coordinata centro
                    y=500  #coordinata centro
                    screen.blit(surf_pizzaVuota, (x,y))
                    victory(screen, counter)
                    flag = 2
                    pygame.display.flip()

                if rect_tornahome.collidepoint(click) and ev.button==1 :
                    done = True
            if ev.type == pygame.USEREVENT: 
                counter -= 1
                text = str(counter)
                
        if(flag != 2):
            poz.fill((255, 255, 255))#serve per cancellare il contenuto della surface in modo da fare il timer decrescente
            poz = font.render(text, True, (0, 0, 0), (255, 255, 0))
            screen.blit(poz, (650, 418))
            pygame.display.flip()
            clock.tick(60)
                    
    return ritornoMenu
                    



