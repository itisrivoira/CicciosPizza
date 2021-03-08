import pygame, sys
import pygame_menu #libreria di pygame che permette una facile creazione del main menu di gioco
from pygame_menu import sound
import livello_prova

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

from pygame.locals import *

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


def colonnaSonora(volume):
	if(FLAGPAUSE == True):
		pygame.mixer.music.load("Suoni/colonnaSonora.ogg")
		pygame.mixer.music.play(-1)   #play della colonna sonora -1 ---> indica per tempo infinito
		pygame.mixer.music.set_volume(volume)
		pygame.mixer.music.pause()
	else:
		pygame.mixer.music.load("Suoni/colonnaSonora.ogg")
		pygame.mixer.music.play(-1)   #play della colonna sonora -1 ---> indica per tempo infinito
		pygame.mixer.music.set_volume(volume)		
	

def regola_volume(valor, indice):
	value, indice= valor  #value valore del selettore da prelevare al indice passato
	print(value)
	volumer = value[0]  #volumer corrisponde al primo elemento della tupla prelevata dal selettore
	print(volumer)
	num = int(volumer) / 100 #il volume con pygame è settabile da 0 a 1 quindi divido per 100 per avere un intervallo da 0, 0.1, 0.2 ecc
	print(num)
	pygame.mixer.music.set_volume(num)
	global VOLUMESETTATO
	VOLUMESETTATO = num


    	


def settaClick(menu): #serve per metterre il suono quando si clicca
	eventoDelClick = sound.Sound()
	eventoDelClick.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, 'Suoni/click.wav')
	menu.set_sound(eventoDelClick, recursive=True)
	return menu
    
def cambia_modalita(value, difficulty):
    # Do the job here !
	print(difficulty)
	pass

def start_the_game():
	print(FLAGPAUSE)
	flag = livello_prova.main(FLAGPAUSE, VOLUMESETTATO)
	if ( flag == 1):
		pygame.quit()
		sys.exit() #SENZA QUESTO DA ERRORE PERCHE' RIPROVEREBBE A DISEGNARE SULLO SCHERMO CAUSANDO UN ERRORE
	print(VOLUMESETTATO)
	colonnaSonora(VOLUMESETTATO)
		
      
#da implementare nel prossimo sprint
      
def cambia_background(valor, indice):
	global PATH_IMMAGINE_BG
	
	value, indice= valor  #value valore del selettore da prelevare al indice passato
	backName = value[0]
	print(backName)
    
	if backName == 'BACKGROUND GRIGIO':
		PATH_IMMAGINE_BG = "Immagini_Gioco/background_menu/background.png" 
	elif backName == "BACKGROUND MATTONI":
		PATH_IMMAGINE_BG = "Immagini_Gioco/background_menu/blu.jpg" 
	elif backName == 'BACKGROUND AZZURRO':
		PATH_IMMAGINE_BG = "Immagini_Gioco/background_menu/x.jpg" 
    

def Imposta(menuPrinc):
	temaImpostazioni = pygame_menu.themes.THEME_DARK.copy() #prendo il tema di default della libreria pygame_menu
	temaImpostazioni.widget_font = pygame_menu.font.FONT_NEVIS #FONT DELLE OPZIONI
	temaImpostazioni.title_font = pygame_menu.font.FONT_8BIT  #FONT TITOLO IMPOSTAZIONI
	temaImpostazioni.title_offset = (5, -2)
	temaImpostazioni.widget_offset = (0, 0.14)
	imgPizza = pygame_menu.baseimage.BaseImage(image_path = PATH_IMMAGINE_BG,
                                               drawing_mode = pygame_menu.baseimage.IMAGE_MODE_FILL) #imgPizza mi permette di creare la mia immagine di sfondo come background
	temaImpostazioni.background_color = imgPizza
	temaImpostazioni.widget_font = fontMenu
	temaImpostazioni.widget_font_color = (0,108,50)
	menuImpostazioni = pygame_menu.Menu(
		height=919,
		theme=temaImpostazioni,
		title='IMPOSTAZIONI',
		width=1279
	)
	menuImpostazioni = settaClick(menuImpostazioni)
    #select = pygame_menu.widgets.Selector('VOLUME DI GIOCO :', [('0', 1), ('10', 2), ('20', 3), ('30', 4), ('40', 5), ('50', 6) ,('60', 7), ('70', 8) ,('80', 9), ('90', 10), ('100', 11)], selection_color = (0,0,255))
	menuImpostazioni.add_selector('VOLUME DI GIOCO :', [('0', 1), ('10', 2), ('20', 3), ('30', 4), ('40', 5), ('50', 6) ,('60', 7), ('70', 8) ,('80', 9), ('90', 10), ('100', 11)], onchange = regola_volume,  selection_color = (0,0,255))
	menuImpostazioni.add_vertical_margin(100)
	menuImpostazioni.add_selector('BACKGROUND MENU :', [('BACKGROUND GRIGIO', 1), ('BACKGROUND AZZURRO', 2), ('BACKGROUND MATTONI', 3)], onchange = cambia_background,  selection_color = (0,0,255))
	menuImpostazioni.add_vertical_margin(100)
    #selettoreVolume.change(regola_volume(selettoreVolume.get_value()))
	menuImpostazioni.add_button('RITORNA AL MENU PRINCIPALE', pygame_menu.events.BACK, selection_color = (0,0,255))
	return menuImpostazioni
    #for m in ABOUT:
    #    about_menu.add.label(m, margin=(0, 0))
    #about_menu.add.label('')
    #about_menu.add.button('Return to Menu', pygame_menu.events.BACK)

def creazione_menuGioco():
	global PATH_IMMAGINE_BG
	print(PATH_IMMAGINE_BG)
	i=0;
	i = i+1
	print(i)
	temaPizzeria = pygame_menu.themes.THEME_ORANGE.copy()  #Prendo uno dei temi di default della libreria pygame_menu e lo modifico per le mie esigenze

	imgPizza = pygame_menu.baseimage.BaseImage(image_path = PATH_IMMAGINE_BG,
                                               drawing_mode = pygame_menu.baseimage.IMAGE_MODE_FILL) #imgPizza mi permette di creare la mia immagine di sfondo come background

                                                        
	temaPizzeria.background_color = imgPizza #mette l'immagine come background
	temaPizzeria.widget_font = fontMenu
	temaPizzeria.title_font_size = 54
	temaPizzeria.title_font_color = (255,117,20)
	temaPizzeria.title_font = fontMenu
	temaPizzeria.widget_font_color = (0,127,255)

	menuGioco = pygame_menu.Menu(919, 1279, 'Ciccios Pizza',
                           theme=temaPizzeria)
	menuGioco = settaClick(menuGioco)

	menuGioco.add_vertical_margin(50)
	menuGioco.add_image(PATH_LOGO)
	menuGioco.add_vertical_margin(50)
	menuGioco.add_button('INIZIA PARTITA', start_the_game, selection_color = (0,0,255))
	menuGioco.add_vertical_margin(50)
	menuGioco.add_selector('MODALITA DI GIOCO :', [('CARRIERA', 1), ('GIRO PIZZA', 2)], onchange=cambia_modalita, selection_color = (0,0,255))
	menuGioco.add_vertical_margin(50)
	menuGioco.add_button('IMPOSTAZIONI', Imposta(menuGioco), selection_color = (0,0,255))
	menuGioco.add_vertical_margin(50)
	menuGioco.add_button('ESCI DAL GIOCO', pygame_menu.events.EXIT, selection_color = (0,0,255))
	menuGioco.add_vertical_margin(50)
   

	return menuGioco
   
    
   

#inizio programma
pygame.init()
screen = pygame.display.set_mode((1280, 920)) #CREAZIONE SCHERMO DI GIOCO
main_menu = None
PATH_IMMAGINE_BG = "Immagini_Gioco/background_menu/blu.jpg" #PATH (percorso della mia immagine da mettere come sfondo)
PATH_VOLUME = "Immagini_Gioco/volumeAttivo.png"
PATH_MUTO = "Immagini_Gioco/muto.png"
PATH_LOGO = "Immagini_Gioco/logo.png"
DONE = True
DEFAULT_VOLUME = 0.5
FLAGPAUSE = False
VOLUMESETTATO = 1
colonnaSonora(DEFAULT_VOLUME)
fontMenu = pygame_menu.font.FONT_8BIT
#colonnaSonora(DEFAULT_VOLUME) #faccio partire la colonna sonora



#main_menu = creazione_menuGioco()

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
main_menu = creazione_menuGioco()
muto = pygame_menu.baseimage.BaseImage(PATH_MUTO)
suono = pygame_menu.baseimage.BaseImage(PATH_VOLUME)
main_menu.add_image(PATH_VOLUME, image_id="1234", align = pygame_menu.locals.ALIGN_LEFT)
#rect_imgSuono = main_menu.get_widget("1234").get_rect()
pygame.display.flip()
flagMuto = 0;

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

while DONE:

	#main_menu = creazione_menuGioco()
	events = pygame.event.get() #lista eventi di una finestra
	for event in events:
		if event.type == pygame.QUIT:
			pygame.quit()

        #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
		
		elif event.type == MOUSEBUTTONDOWN:
			click = event.pos
			print(PATH_IMMAGINE_BG)
			if main_menu.get_widget("1234").get_rect(inflate = (0, 30)).collidepoint(click) and event.button==1 and flagMuto == 0:
				#print(main_menu.get_widget("1234").get_rect().y)
				#print(main_menu.get_widget("1234").get_position())
				pygame.mixer.music.pause()
				FLAGPAUSE = True
				main_menu.get_widget("1234").set_image(muto)
				#rect_imgSuono = main_menu.get_widget("1234").get_rect()
				pygame.display.flip()
				flagMuto = 1
				
			elif main_menu.get_widget("1234").get_rect(inflate = (0, 30)).collidepoint(click) and event.button==1 and flagMuto == 1:
				pygame.mixer.music.unpause()
				FLAGPAUSE = False
				main_menu.get_widget("1234").set_image(suono)
				#rect_imgSuono = main_menu.get_widget("1234").get_rect()
				pygame.display.flip()
				flagMuto = 0				

        #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

            

	if main_menu.is_enabled():
        #print("abilitato")
		main_menu.update(events)
		main_menu.draw(screen)
		pygame.display.update()
	else:
       # print("disabilitato")
		pygame.quit()

