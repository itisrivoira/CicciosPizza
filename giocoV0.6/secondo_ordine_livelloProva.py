import pygame
import pygame_menu #libreria di pygame che permette una facile creazione del main menu di gioco
from pygame_menu import sound
from pygame.locals import *
import menu_pausa as pause


import time, datetime

counterS = 0
textS = " "

def colonnaSonora(volume,  FLAGPAUSE):
	if(FLAGPAUSE == True):
		pygame.mixer.music.load("Suoni/colonnaSonora.ogg")
		pygame.mixer.music.play(-1)   #play della colonna sonora -1 ---> indica per tempo infinito
		pygame.mixer.music.set_volume(volume)
		pygame.mixer.music.pause()
	else:
		pygame.mixer.music.load("Suoni/colonnaSonora.ogg")
		pygame.mixer.music.play(-1)   #play della colonna sonora -1 ---> indica per tempo infinito
		pygame.mixer.music.set_volume(volume)		
	

def setValoriPunteggio(counter, text):
	global counterS
	global textS
	counterS = counter
	textS = text
	
def getValoreNum():
	global counterS
	return counterS
	
def getValoreTxt():
	global textS
	return textS

def crea_livello(screen, flag, dragPomodoro, eliminaPomodoro, dragMozzarella, eliminaMozzarella, dragSalame, eliminaSalame):
	print("eee")
		
	surf_background = pygame.image.load("Immagini_Gioco/background_menu/rossa2.jpg").convert()
	screen.blit(surf_background, (0, 0))
		
	surf_ordine = pygame.image.load("Immagini_Gioco/Immagini_Livello/funza.png")
	screen.blit(surf_ordine, (20, 0))
		
	#fontOrdine = pygame.font.SysFont("Verdana", 34, italic=True)
	#text = ["PIZZA AL PROSCIUTTO ","CLICCA IN QUESTO ORDINE:","1)POMODORO","2)MOZZARELLA", "3)SALAME"]
	#distanza = 0
	#for x in text:
	#	distanza += 1
	#	screen.blit((pygame.font.SysFont('constantia',18).render(x, True,(255, 0, 0))),(100,100+100*distanza))
	#distanza = 0
		
	surf_tagliere=pygame.image.load('Immagini_Gioco/Immagini_Livello/tagliere.png')
	x=450  
	y=0
	screen.blit(surf_tagliere, (x,y))
		
	surf_contenitore=pygame.image.load('Immagini_Gioco/Immagini_Livello/contenitore.png')
	x=310
	y=340  
	screen.blit(surf_contenitore, (x,y))
		
	if(flag == 0):  
		surf_pizzaVuota=pygame.image.load('Immagini_Gioco/Immagini_Livello/impasto.png')
		rect_pizzaVuota = surf_pizzaVuota.get_rect()
		x=475  
		y=500  
		rect_pizzaVuota.move_ip(x, y)
		screen.blit(surf_pizzaVuota, (x,y))
	elif (flag == 1):
		surf_pizzaVuota=pygame.image.load('Immagini_Gioco/Immagini_Livello/marinara.png')
		rect_pizzaVuota = surf_pizzaVuota.get_rect()
		x=475  #coordinata centro
		y=500  #coordinata centro
		screen.blit(surf_pizzaVuota, (x,y))
		#pygame.display.flip()	
	elif (flag == 2):
		print("fatto")
		surf_pizzaVuota=pygame.image.load('Immagini_Gioco/Immagini_Livello/pizzaMargherita.png')
		rect_pizzaVuota = surf_pizzaVuota.get_rect()
		x=475  #coordinata centro		
		y=500  #coordinata centro
		screen.blit(surf_pizzaVuota, (x,y))
	elif (flag == 3):
		print("fatto")
		surf_pizzaVuota=pygame.image.load('Immagini_Gioco/Immagini_Livello/pizzaSalame.png')
		rect_pizzaVuota = surf_pizzaVuota.get_rect()
		x=475  #coordinata centro		
		y=500  #coordinata centro
		screen.blit(surf_pizzaVuota, (x,y))
	
	if dragPomodoro == False and eliminaPomodoro == False :	
		surf_pomodoro=pygame.image.load('Immagini_Gioco/Immagini_Livello/pomodoro.png')
		rect_pomodoro = surf_pomodoro.get_rect()
		x=550 
		y=150 
		rect_pomodoro.move_ip(x, y) #MOVE IP MUOVE IL RECT NELLE CORDINATE DECISE DA UTENTE
		screen.blit(surf_pomodoro, (x,y))
	if dragMozzarella == False and eliminaMozzarella == False:	
		surf_mozzarella=pygame.image.load('Immagini_Gioco/Immagini_Livello/mozzarella.png')
		rect_mozzarella = surf_mozzarella.get_rect()
		x=850 
		y=150
		rect_mozzarella.move_ip(x, y)
		screen.blit(surf_mozzarella, (x,y))
	if dragSalame == False and eliminaSalame == False:	
		surf_salame = pygame.image.load('Immagini_Gioco/Immagini_Livello/salame2.png')
		rect_salame = surf_salame.get_rect()
		x=700
		y=150
		rect_salame.move_ip(x, y)
		screen.blit(surf_salame, (x,y))
		
	surf_pause= pygame.image.load("Immagini_Gioco/Immagini_Livello/pausa4.png")
	rect_pause = surf_pause.get_rect()
	x=1050
	y=700
	rect_pause.move_ip(x, y)
	screen.blit(surf_pause, (x,y))
		
	surf_orologio= pygame.image.load("Immagini_Gioco/Immagini_Livello/orologio.png")
	rect_orologio = surf_orologio.get_rect()
	x=1000
	y=450  
	rect_orologio.move_ip(x, y)
	screen.blit(surf_orologio, (x,y))



def main(counter, text, FLAGPAUSE, VOLUMESETTATO): #parametri da ricevere flag / tempo a cui si è arrivati 
	
	pygame.init()
	clock = pygame.time.Clock()
	FPS = 30
	screen = pygame.display.set_mode((1280, 920)) #CREAZIONE SCHERMO DI GIOCO
	pygame.display.set_caption("ORDINE 2 CICCIO'S PIZZA ")
		
	surf_background = pygame.image.load("Immagini_Gioco/background_menu/rossa2.jpg").convert()
	screen.blit(surf_background, (0, 0))
		
	surf_ordine = pygame.image.load("Immagini_Gioco/Immagini_Livello/funza.png")
	screen.blit(surf_ordine, (20, 0))
		
	#fontOrdine = pygame.font.SysFont("Verdana", 34, italic=True)
	#textO = ["PIZZA AL PROSCIUTTO ","CLICCA IN QUESTO ORDINE:","1)POMODORO","2)MOZZARELLA", "3)SALAME"]
	#distanza = 0
	#for x in textO:
	#	distanza += 1
	#	screen.blit((pygame.font.SysFont('constantia',18).render(x, True,(255, 0, 0))),(100,100+100*distanza))
	#distanza = 0
		
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
	xPom=550 
	yPom=150 
	rect_pomodoro.move_ip(xPom, yPom) #MOVE IP MUOVE IL RECT NELLE CORDINATE DECISE DA UTENTE
	screen.blit(surf_pomodoro, (xPom,yPom))
	
	surf_mozzarella=pygame.image.load('Immagini_Gioco/Immagini_Livello/mozzarella.png')
	rect_mozzarella = surf_mozzarella.get_rect()
	xMoz=850 
	yMoz=150
	rect_mozzarella.move_ip(xMoz, yMoz)
	screen.blit(surf_mozzarella, (xMoz,yMoz))
	
	surf_salame = pygame.image.load('Immagini_Gioco/Immagini_Livello/salame2.png')
	rect_salame = surf_salame.get_rect()
	xSal=700
	ySal=150
	rect_salame.move_ip(xSal, ySal)
	screen.blit(surf_salame, (xSal,ySal))
		
	surf_pause= pygame.image.load("Immagini_Gioco/Immagini_Livello/pausa4.png")
	rect_pause = surf_pause.get_rect()
	x=1050
	y=700
	rect_pause.move_ip(x, y)
	screen.blit(surf_pause, (x,y))
		
	surf_orologio= pygame.image.load("Immagini_Gioco/Immagini_Livello/orologio.png")
	rect_orologio = surf_orologio.get_rect()
	x=1000
	y=450  
	rect_orologio.move_ip(x, y)
	screen.blit(surf_orologio, (x,y))
		
	pygame.display.flip() 
	
	pygame.time.set_timer(pygame.USEREVENT, 1000)
	font = pygame.font.SysFont('Consolas', 30)
	counter2 = counter + 3 #tempo a cui si è arrivati
	text2 =  str(counter2).rjust(3)
	poz = font.render(text2, True, (0, 0, 0), (255, 255, 0))
	 
	
	done = False
	dragPomodoro = False
	dragSalame = False
	dragMozzarella = False
	ifYouHaveDrag = False
	flag = 0
	eliminaSalame = False
	eliminaMozzarella = False
	eliminaPomodoro = False
	flagPerso = 0 
	flagVinto = 0
	ritornoMenu = 0
	
	while not done:
		print(text)
		print(counter)
		for ev in pygame.event.get():
		
			if ev.type == pygame.QUIT:
				
				ritornoMenu = 1
				done = True
			
			if ev.type == MOUSEBUTTONDOWN:
				click = ev.pos
				
				if rect_pomodoro.collidepoint(click) and ev.button==1:
					dragPomodoro = True
					mouse_x1, mouse_y1 = ev.pos
					offset_x1 = rect_pomodoro.x - mouse_x1
					offset_y1 = rect_pomodoro.y - mouse_y1
				
				if rect_mozzarella.collidepoint(click) and ev.button==1:
					dragMozzarella = True
					mouse_x2, mouse_y2 = ev.pos
					offset_x2 = rect_mozzarella.x - mouse_x2
					offset_y2 = rect_mozzarella.y - mouse_y2
					
				if rect_salame.collidepoint(click) and ev.button==1:
					dragSalame = True
					mouse_x3, mouse_y3 = ev.pos
					offset_x3 = rect_salame.x - mouse_x3
					offset_y3 = rect_salame.y - mouse_y3
					
				if rect_pause.collidepoint(click) and ev.button==1 and flag != 3:
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

							if pause.get_menu() == 1:
								DONE = False
								done = True
								ritornoMenu = 2
								pause.resetTorna()

						pygame.display.update()
					print("chiuso")
					crea_livello(screen, flag,  dragPomodoro, eliminaPomodoro, dragMozzarella, eliminaMozzarella, dragSalame, eliminaSalame)	
					
			if ev.type == pygame.USEREVENT:
				if (flagPerso == 0 and flag != 3):
					app = counter2 -1 
					if( app == 0 and flagPerso != 1):
						flagPerso = 1
						flag = 4
					else:
						counter2 -= 1
						text2 = str(counter2).rjust(3)
							
			if ev.type == pygame.MOUSEBUTTONUP:
				if ev.button == 1:
					if rect_pomodoro.colliderect(rect_pizzaVuota) and flagVinto == 0 and flag != 4:
						eliminaPomodoro = True
						surf_pizzaVuota=pygame.image.load('Immagini_Gioco/Immagini_Livello/marinara.png')
						rect_pizzaVuota = surf_pizzaVuota.get_rect()
						x=475  #coordinata centro
						y=500  #coordinata centro
						screen.blit(surf_pizzaVuota, (x,y))
						rect_pizzaVuota.move_ip(x, y)
						flag=1
					if dragPomodoro:
						print(eliminaPomodoro)
						dragPomodoro = False
						print(xPom, yPom)
						rect_pomodoro.x = xPom
						rect_pomodoro.y = yPom
						crea_livello(screen, flag, dragPomodoro, eliminaPomodoro, dragMozzarella, eliminaMozzarella, dragSalame, eliminaSalame)
					if rect_mozzarella.colliderect(rect_pizzaVuota) and flagVinto == 0 and flag < 2:
						if(flag == 1):
							print("eaeae")
							eliminaMozzarella = True
							surf_pizzaVuota= pygame.image.load('Immagini_Gioco/Immagini_Livello/pizzaMargherita.png')
							rect_pizzaVuota = surf_pizzaVuota.get_rect()
							x=475
							y=500
							screen.blit(surf_pizzaVuota, (x,y))
							rect_pizzaVuota.move_ip(x, y)				   						    				
							pygame.display.flip()						    										    				    			
							flag = 2
						else:
							suonoErrore = False
							pygame.mixer.music.load("Suoni/erroreSelezione.ogg")
							pygame.mixer.music.set_volume(0.5)
							pygame.mixer.music.play()
							pygame.time.wait(500)
							colonnaSonora(VOLUMESETTATO, FLAGPAUSE)	
							
					if dragMozzarella:
						dragMozzarella = False
						rect_mozzarella.x = xMoz
						rect_mozzarella.y = yMoz
						crea_livello(screen, flag,  dragPomodoro, eliminaPomodoro, dragMozzarella, eliminaMozzarella, dragSalame, eliminaSalame)
							
						
					if rect_salame.colliderect(rect_pizzaVuota) and flagVinto == 0 and flag != 4:
						print("ciao")
						if(flag == 2):
							print("eaeae")
							eliminaSalame = True
							surf_pizzaVuota= pygame.image.load('Immagini_Gioco/Immagini_Livello/pizzaSalame.png')
							rect_pizzaVuota = surf_pizzaVuota.get_rect()
							x=475
							y=500
							screen.blit(surf_pizzaVuota, (x,y))
							rect_pizzaVuota.move_ip(x, y)
							poz.fill((255, 255, 255))#serve per cancellare il contenuto della surface in modo da fare il timer decrescente
							poz = font.render(text2, True, (0, 0, 0), (255, 255, 255))
							screen.blit(poz, (1058, 542))
			   						    				
							pygame.display.flip()						    										    				    			
							flag = 3
							setValoriPunteggio(counter2, text2)
							done = True
						else:
							suonoErrore = False
							pygame.mixer.music.load("Suoni/erroreSelezione.ogg")
							pygame.mixer.music.set_volume(0.5)
							pygame.mixer.music.play()
							pygame.time.wait(500)
							colonnaSonora(VOLUMESETTATO, FLAGPAUSE)
					if dragSalame:
						dragSalame = False
						rect_salame.x = xSal
						rect_salame.y = ySal
						crea_livello(screen, flag,  dragPomodoro, eliminaPomodoro, dragMozzarella, eliminaMozzarella, dragSalame, eliminaSalame)							
					
			if ev.type == pygame.MOUSEMOTION:
				if dragPomodoro: 
					print("ciao")
					mouse_x1, mouse_y1 = ev.pos
					rect_pomodoro.x = mouse_x1 + offset_x1
					rect_pomodoro.y = mouse_y1 + offset_y1
					ifYouHaveDrag = True
                     
				if dragMozzarella:
					print(flag)
					mouse_x2, mouse_y2 = ev.pos
					rect_mozzarella.x = mouse_x2 + offset_x2
					rect_mozzarella.y = mouse_y2 + offset_y2
					ifYouHaveDrag = True
						
				if dragSalame:
					print(flag)
					mouse_x3, mouse_y3 = ev.pos
					rect_salame.x = mouse_x3 + offset_x3
					rect_salame.y = mouse_y3 + offset_y3
					ifYouHaveDrag = True
#if rect_pomodoro.colliderect(rect_pizzaVuota) and flagVinto == 0:
#eliminaPomodoro = True
#surf_pizzaVuota=pygame.image.load('Immagini_Gioco/Immagini_Livello/marinara.png')
#rect_pizzaVuota = surf_pizzaVuota.get_rect()
#x=475  #coordinata centro
#y=500  #coordinata centro
#screen.blit(surf_pizzaVuota, (x,y))
#rect_pizzaVuota.move_ip(x, y)
#flag=1				

		#if rect_pomodoro.colliderect(rect_pizzaVuota) and flagVinto == 0 and flag != 4:
		#	eliminaPomodoro = True
		#	surf_pizzaVuota=pygame.image.load('Immagini_Gioco/Immagini_Livello/marinara.png')
		#	rect_pizzaVuota = surf_pizzaVuota.get_rect()
		#	x=475  #coordinata centro
		#	y=500  #coordinata centro
		#	screen.blit(surf_pizzaVuota, (x,y))
		#	rect_pizzaVuota.move_ip(x, y)
		#	flag=1
			
			
		#if rect_mozzarella.colliderect(rect_pizzaVuota) and flagVinto == 0 and flag != 4:
		#	print("gay")
		#	if(flag == 1):
		#		print("eaeae")
		#		eliminaMozzarella = True
		#		surf_pizzaVuota= pygame.image.load('Immagini_Gioco/Immagini_Livello/pizzaMargherita.png')
		#		rect_pizzaVuota = surf_pizzaVuota.get_rect()
		#		x=475
		#		y=500
		#		screen.blit(surf_pizzaVuota, (x,y))
		#		rect_pizzaVuota.move_ip(x, y)				   						    				
		#		pygame.display.flip()						    										    				    			
		#		flag = 2
			#else:
			#	suonoErrore = False
			#	pygame.mixer.music.load("Suoni/erroreSelezione.ogg")
			#	pygame.mixer.music.set_volume(0.5)
			#	pygame.mixer.music.play()
			#	pygame.time.wait(500)
			#	colonnaSonora(VOLUMESETTATO, FLAGPAUSE)						
			
	#	if rect_salame.colliderect(rect_pizzaVuota) and flagVinto == 0 and flag != 4:
		#	print("gay")
		#	if(flag == 2):
		#		print("eaeae")
		#		eliminaSalame = True
			#	surf_pizzaVuota= pygame.image.load('Immagini_Gioco/Immagini_Livello/pizzaSalame.png')
			#	rect_pizzaVuota = surf_pizzaVuota.get_rect()
			#	x=475
			#	y=500
			#	screen.blit(surf_pizzaVuota, (x,y))
			#	rect_pizzaVuota.move_ip(x, y)				   						    				
			#	pygame.display.flip()						    										    				    			
			#	flag = 3
			#	setValoriPunteggio(counter2, text2)
			#	done = True
			#else:
			#	suonoErrore = False
			#	pygame.mixer.music.load("Suoni/erroreSelezione.ogg")
			#	pygame.mixer.music.set_volume(0.5)
			#	pygame.mixer.music.play()
			#	pygame.time.wait(500)
			#	colonnaSonora(VOLUMESETTATO, FLAGPAUSE)				
				
		if(ritornoMenu != 1):
			poz.fill((255, 255, 255))#serve per cancellare il contenuto della surface in modo da fare il timer decrescente
			poz = font.render(text2, True, (0, 0, 0), (255, 255, 255))
			screen.blit(poz, (1058, 542))
			pygame.display.flip()
			clock.tick(60)
					
							
		if ifYouHaveDrag:
			#print("hey")
			#crea_livello(screen,flag, dragPomodoro, eliminaPomodoro, dragMozzarella, eliminaMozzarella, dragSalame, eliminaSalame)
			#pygame.display.flip()
			#print("cia")
			clock.tick(60)
			crea_livello(screen, flag, dragPomodoro, eliminaPomodoro, dragMozzarella, eliminaMozzarella, dragSalame, eliminaSalame)
			#if flag == 3:
			#	poz.fill((255, 255, 255))#serve per cancellare il contenuto della surface in modo da fare il timer decrescente
			#	poz = font.render(text2, True, (0, 0, 0), (255, 255, 255))
			#	screen.blit(poz, (1058, 542))
			#	pygame.display.flip()
			#	done = True				
			#surf_background = pygame.image.load("Immagini_Gioco/background_menu/rossa2.jpg").convert()
			#screen.blit(surf_background, (0, 0))
	
			
		ifYouHaveDrag = False
		if(eliminaPomodoro == False):
			#print("dad")
			screen.blit(surf_pomodoro, rect_pomodoro)
		if(eliminaMozzarella == False):
			screen.blit(surf_mozzarella, rect_mozzarella)
		if(eliminaSalame == False):
			screen.blit(surf_salame, rect_salame)
		pygame.display.flip()	
		
		if(flag == 4):
			done = True
		
	clock.tick(60)
	if ritornoMenu == 1:
		return -1
	elif ritornoMenu == 2:
		return -2
	else:
		return flag
	
	
	
#if __name__ == "__main__":
#	main()
