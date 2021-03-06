import pygame
import pygame_menu #libreria di pygame che permette una facile creazione del main menu di gioco
from pygame_menu import sound
from pygame.locals import *
import menu_pausa as pause


import time, datetime

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

def colonnaSonora(volume, FLAGPAUSE):
	if(FLAGPAUSE == True):  #SE LA MUSICA DI SOTTOFONDO E' DISATTIVATA NEL MENU PRINCIPALE NON LA FACCIO RIPARTIRE MA I SUONI DEL GIOCO FUNZIONANO COMUNQUE
		pygame.mixer.music.load("Suoni/colonnaSonora.ogg")
		pygame.mixer.music.play(-1)   #play della colonna sonora -1 ---> indica per tempo infinito
		pygame.mixer.music.set_volume(volume)
		pygame.mixer.music.pause()
	else:
		pygame.mixer.music.load("Suoni/colonnaSonora.ogg")
		pygame.mixer.music.play(-1)   #play della colonna sonora -1 ---> indica per tempo infinito
		pygame.mixer.music.set_volume(volume)

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


def victory(schermo, counter):
    pygame.mixer.music.load("Suoni/level_complete.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    fontVittoria = pygame.font.SysFont("Verdana", 34, italic=True)
    surf_text = fontVittoria.render("LIVELLO COMPLETATO !!!", True, (255, 255, 0))
    x=450
    y= 350
    schermo.blit(surf_text, (x,y))
    
    if(counter >= 40):
    	print("tre stelle")
    	surf_stelle=pygame.image.load('Immagini_Gioco/stelle/stelle3.png')
    	rect_stelle = surf_stelle.get_rect()
    	x=65  
    	y=500  
    	rect_stelle.move_ip(x, y)
    	schermo.blit(surf_stelle, (x,y))
    elif (counter < 40 and counter >= 20):
    	print("due stelle")
    	surf_stelle=pygame.image.load('Immagini_Gioco/stelle/stelle2.png')
    	rect_stelle = surf_stelle.get_rect()
    	x=65  
    	y=500  
    	rect_stelle.move_ip(x, y)
    	schermo.blit(surf_stelle, (x,y))
    elif (counter < 20):
    	surf_stelle=pygame.image.load('Immagini_Gioco/stelle/stelle1.png')
    	rect_stelle = surf_stelle.get_rect()
    	x=65  
    	y=500  
    	rect_stelle.move_ip(x, y)
    	schermo.blit(surf_stelle, (x,y))
    	print("una stella")
    	

def crea_livello(screen, flagPomodoro):

	surf_background = pygame.image.load("Immagini_Gioco/background_menu/rossa2.jpg").convert()
	screen.blit(surf_background, (0, 0))


	surf_ordine = pygame.image.load("Immagini_Gioco/Immagini_Livello/ordinazione.png")
	screen.blit(surf_ordine, (20, 0))

	fontOrdine = pygame.font.SysFont("Verdana", 34, italic=True)
	text = ["PIZZA MARGHERITA","CLICCA IN QUESTO ORDINE:","1)POMODORO","2)MOZZARELLA"]
	distanza = 0
	for x in text:
		distanza += 0.5
		screen.blit((pygame.font.SysFont('constantia',18).render(x, True,(255, 0, 0))),(100,100+100*distanza))
	distanza = 0
	
	surf_tagliere=pygame.image.load('Immagini_Gioco/Immagini_Livello/tagliere.png')
	x=450  
	y=0  
	screen.blit(surf_tagliere, (x,y))
	
	surf_contenitore=pygame.image.load('Immagini_Gioco/Immagini_Livello/contenitore.png')
	x=310
	y=340  
	screen.blit(surf_contenitore, (x,y))

	if(flagPomodoro == 0):  
		surf_pizzaVuota=pygame.image.load('Immagini_Gioco/Immagini_Livello/impasto.png')
		rect_pizzaVuota = surf_pizzaVuota.get_rect()
		x=475  
		y=500  
		rect_pizzaVuota.move_ip(x, y)
		screen.blit(surf_pizzaVuota, (x,y))
	elif (flagPomodoro == 1):
		surf_pizzaVuota=pygame.image.load('Immagini_Gioco/Immagini_Livello/marinara.png')
		rect_pizzaVuota = surf_pizzaVuota.get_rect()
		x=475  #coordinata centro
		y=500  #coordinata centro
		screen.blit(surf_pizzaVuota, (x,y))
		pygame.display.flip()		

	surf_pomodoro=pygame.image.load('Immagini_Gioco/Immagini_Livello/pomodoro.png')
	rect_pomodoro = surf_pomodoro.get_rect()
	x=550  
	y=150   
	rect_pomodoro.move_ip(x, y) #MOVE IP MUOVE IL RECT NELLE CORDINATE DECISE DA UTENTE
	screen.blit(surf_pomodoro, (x,y))

	surf_mozzarella=pygame.image.load('Immagini_Gioco/Immagini_Livello/mozzarella.png')
	rect_mozzarella = surf_pomodoro.get_rect()
	x=850  
	y=150 
	rect_mozzarella.move_ip(x, y)
	screen.blit(surf_mozzarella, (x,y))

	surf_tornahome= pygame.image.load("Immagini_Gioco/Immagini_Livello/menu.png")
	rect_tornahome = surf_tornahome.get_rect()
	x=1000  
	y=700  
	rect_tornahome.move_ip(x, y)
	screen.blit(surf_tornahome, (x,y))

    #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

	surf_orologio= pygame.image.load("Immagini_Gioco/Immagini_Livello/orologio.png")
	rect_orologio = surf_orologio.get_rect()
	x=1000
	y=450  
	rect_orologio.move_ip(x, y)
	screen.blit(surf_orologio, (x,y))

	surf_pause= pygame.image.load("Immagini_Gioco/Immagini_Livello/Pause2.png")
	rect_pause = surf_pause.get_rect()
	x=40
	y=700  
	rect_pause.move_ip(x, y)
	screen.blit(surf_pause, (x,y))

    #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

	pygame.display.flip()


def main(FLAGPAUSE, VOLUMESETTATO):
    # pygame.init()#inizio programma non necessario perchè il programma iniza dal menu quindi richiamarlo è inutile
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((1280, 920)) #CREAZIONE SCHERMO DI GIOCO
	pygame.display.set_caption("LIVELLO 1 CICCIO'S PIZZA ")

	surf_background = pygame.image.load("Immagini_Gioco/background_menu/rossa2.jpg").convert()
	screen.blit(surf_background, (0, 0))


	surf_ordine = pygame.image.load("Immagini_Gioco/Immagini_Livello/ordinazione.png")
	screen.blit(surf_ordine, (20, 0))

	fontOrdine = pygame.font.SysFont("Verdana", 34, italic=True)
	text = ["PIZZA MARGHERITA","CLICCA IN QUESTO ORDINE:","1)POMODORO","2)MOZZARELLA"]
	distanza = 0
	for x in text:
		distanza += 0.5
		screen.blit((pygame.font.SysFont('constantia',18).render(x, True,(255, 0, 0))),(100,100+100*distanza))
	distanza = 0
	
	surf_tagliere=pygame.image.load('Immagini_Gioco/Immagini_Livello/tagliere.png')
	x=450
	y=0  
	screen.blit(surf_tagliere, (x,y))
	
	surf_contenitore=pygame.image.load('Immagini_Gioco/Immagini_Livello/contenitore.png')
	x=310
	y=340  
	screen.blit(surf_contenitore, (x,y))
    
	surf_pizzaVuota=pygame.image.load('Immagini_Gioco/Immagini_Livello/impasto.png')
	rect_pizzaVuota = surf_pizzaVuota.get_rect()
	x=475  
	y=500  
	rect_pizzaVuota.move_ip(x, y)
	screen.blit(surf_pizzaVuota, (x,y))

	surf_pomodoro=pygame.image.load('Immagini_Gioco/Immagini_Livello/pomodoro.png')
	rect_pomodoro = surf_pomodoro.get_rect()
	x=550  
	y=150  
	rect_pomodoro.move_ip(x, y) #MOVE IP MUOVE IL RECT NELLE CORDINATE DECISE DA UTENTE
	screen.blit(surf_pomodoro, (x,y))

	surf_mozzarella=pygame.image.load('Immagini_Gioco/Immagini_Livello/mozzarella.png')
	rect_mozzarella = surf_pomodoro.get_rect()
	x=850  
	y=150  
	rect_mozzarella.move_ip(x, y)
	screen.blit(surf_mozzarella, (x,y))

	surf_tornahome= pygame.image.load("Immagini_Gioco/Immagini_Livello/menu.png")
	rect_tornahome = surf_tornahome.get_rect()
	x=1000  
	y=700  
	rect_tornahome.move_ip(x, y)
	screen.blit(surf_tornahome, (x,y))

    #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

	surf_orologio= pygame.image.load("Immagini_Gioco/Immagini_Livello/orologio.png")
	rect_orologio = surf_orologio.get_rect()
	x=1000
	y=450  
	rect_orologio.move_ip(x, y)
	screen.blit(surf_orologio, (x,y))

	surf_pause= pygame.image.load("Immagini_Gioco/Immagini_Livello/Pause2.png")
	rect_pause = surf_pause.get_rect()
	x=40
	y=700  
	rect_pause.move_ip(x, y)
	screen.blit(surf_pause, (x,y))

    #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

	pygame.display.flip()
	
	
	flag=0
	ritornoMenu = 0

    #timer_stop = datetime.datetime.utcnow() +datetime.timedelta(seconds=30)
    #start_ticks=pygame.time.get_ticks() #starter tick
	pygame.time.set_timer(pygame.USEREVENT, 1000)
	font = pygame.font.SysFont('Consolas', 30)
	counter, text = 60, '60'.rjust(3)
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

                #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

				if flag==0 and ev.button==1 and rect_mozzarella.collidepoint(click):
					pygame.mixer.music.load("Suoni/erroreSelezione.ogg")  
					pygame.mixer.music.set_volume(0.5)  
					pygame.mixer.music.play()  #fa partire suono errore
					pygame.time.wait(500)  #aspetta mezzo secondo 
					colonnaSonora(VOLUMESETTATO, FLAGPAUSE)  #riparte colonna sonora

                #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

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

				if rect_pause.collidepoint(click) and ev.button==1 and flag != 2:
					DONE = True
					print("ciao")
					menu_pausa = pause.creazione_menu_pausa()
					print(menu_pausa)
                	#menu_pausa.mainloop(screen)
					while DONE:

						x= pause.get_flag()
						print(x)

						events = pygame.event.get()
						for event in events:
							if event.type == pygame.QUIT:
								exit()

						if menu_pausa.is_enabled():
							menu_pausa.update(events)
							menu_pausa.draw(screen)
							
						if pause.get_flag() == 1:
							pause.reset_flag()
							DONE = False

						pygame.display.update()
					print("chiuso")
					crea_livello(screen, flag)				

                    
				if rect_tornahome.collidepoint(click) and ev.button==1 :
					done = True
                
                
			if ev.type == pygame.USEREVENT: 
				app = counter -1 
				if( app == 0):
					done = True
				else:
					counter -= 1
					text = str(counter).rjust(3) 
                
		if(flag != 2):
			poz.fill((255, 255, 255))#serve per cancellare il contenuto della surface in modo da fare il timer decrescente
			poz = font.render(text, True, (0, 0, 0), (255, 255, 255))
			screen.blit(poz, (1058, 542))
			pygame.display.flip()
			clock.tick(60)
                    
	return ritornoMenu
                    



