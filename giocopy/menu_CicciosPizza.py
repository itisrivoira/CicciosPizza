import pygame
import pygame_menu #libreria di pygame che permette una facile creazione del main menu di gioco
from pygame_menu import sound
def colonnaSonora(volume):
    pygame.mixer.music.load("Suoni/colonnaSonora.wav")
    pygame.mixer.music.play(-1)   #play della colonna sonora -1 ---> indica per tempo infinito
    pygame.mixer.music.set_volume(volume)

def settaClick(menu):
    eventoDelClick = sound.Sound()
    eventoDelClick.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, 'Suoni/click.wav')
    menu.set_sound(eventoDelClick, recursive=True)
    return menu
    
def cambia_modalita(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

def Imposta():
    temaImpostazioni = pygame_menu.themes.THEME_DARK.copy() #prendo il tema di default della libreria pygame_menu
    temaImpostazioni.widget_font = pygame_menu.font.FONT_NEVIS #FONT DELLE OPZIONI
    temaImpostazioni.title_font = pygame_menu.font.FONT_8BIT  #FONT TITOLO IMPOSTAZIONI
    temaImpostazioni.title_offset = (5, -2)
    temaImpostazioni.widget_offset = (0, 0.14)
    imgPizza = pygame_menu.baseimage.BaseImage(image_path = PATH_IMMAGINE_BG,
                                               drawing_mode = pygame_menu.baseimage.IMAGE_MODE_FILL) #imgPizza mi permette di creare la mia immagine di sfondo come background
    temaImpostazioni.background_color = imgPizza
    menuImpostazioni = pygame_menu.Menu(
        height=919,
        theme=temaImpostazioni,
        title='IMPOSTAZIONI',
        width=1279
    )
    menuImpostazioni = settaClick(menuImpostazioni)
    menuImpostazioni.add_text_input('VOLUME :', default='0.5')
    menuImpostazioni.add_button('RITORNA AL MENU PRINCIPALE', pygame_menu.events.BACK)
    
    return menuImpostazioni
    #for m in ABOUT:
    #    about_menu.add.label(m, margin=(0, 0))
    #about_menu.add.label('')
    #about_menu.add.button('Return to Menu', pygame_menu.events.BACK)

def creazione_menuGioco():
    menuPizzeria = pygame_menu.themes.THEME_ORANGE.copy()  #Prendo uno dei temi di default della libreria pygame_menu e lo modifico per le mie esigenze

    imgPizza = pygame_menu.baseimage.BaseImage(image_path = PATH_IMMAGINE_BG,
                                               drawing_mode = pygame_menu.baseimage.IMAGE_MODE_FILL) #imgPizza mi permette di creare la mia immagine di sfondo come background
    
    menuPizzeria.background_color = imgPizza
    fontMenu = pygame_menu.font.FONT_8BIT
    menuPizzeria.widget_font = fontMenu
    menuPizzeria.title_font_size = 34
    menuPizzeria.title_font_color = (0,255,0)
    menuPizzeria.title_font = fontMenu
    menuPizzeria.widget_font_color = (0,108,50)

    menuGioco = pygame_menu.Menu(919, 1279, 'Ciccios Pizza',
                           theme=menuPizzeria)
    menuGioco = settaClick(menuGioco)
    bottoneInizia = menuGioco.add_button('INIZIA PARTITA', start_the_game, selection_color = (0,0,255))
    selettoreModalita = menuGioco.add_selector('MODALITA DI GIOCO :', [('CARRIERA', 1), ('GIRO PIZZA', 2)], onchange=cambia_modalita, selection_color = (0,0,255))
    bottoneImpostazioni = menuGioco.add_button('IMPOSTAZIONI', Imposta(), selection_color = (0,0,255))
    bottoneEsci = menuGioco.add_button('ESCI DAL GIOCO', pygame_menu.events.EXIT, selection_color = (0,0,255))


    menuGioco.mainloop(surface)

pygame.init()#inizio programma
surface = pygame.display.set_mode((1280, 920)) #CREAZIONE SCHERMO DI GIOCO
PATH_IMMAGINE_BG = "Immagini_Gioco/background_menu/sfondoPizza.png" #PATH (percorso della mia immagine da mettere come sfondo)
DEFAULT_VOLUME = 0.5
colonnaSonora(DEFAULT_VOLUME) #faccio partire la colonna sonora

creazione_menuGioco()

