import pygame
import pygame_menu #libreria di pygame che permette una facile creazione del main menu di gioco
from pygame_menu import sound


def colonnaSonora(volume):
    pygame.mixer.music.load("Suoni/colonnaSonora.mp3")
    pygame.mixer.music.play(-1)   #play della colonna sonora -1 ---> indica per tempo infinito
    pygame.mixer.music.set_volume(volume)

def regola_volume(valor, indice):
    value, indice= valor
    print(value)
    volumer = value[0]
    print(volumer)
    num = int(volumer) / 100
    print(num)
    pygame.mixer.music.set_volume(num)


def settaClick(menu):
    eventoDelClick = sound.Sound()
    eventoDelClick.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, 'Suoni/click.wav')
    menu.set_sound(eventoDelClick, recursive=True)
    return menu
    
def cambia_modalita(value, difficulty):
    # Do the job here !
    print(difficulty)
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
    selettoreVolume = menuImpostazioni.add_selector('VOLUME DI GIOCO :', [('0', 1), ('10', 2), ('20', 3), ('30', 4), ('40', 5), ('50', 6) ,('60', 7), ('70', 8) ,('80', 9), ('90', 10), ('100', 11)], onchange = regola_volume,  selection_color = (0,0,255))
    #selettoreVolume.change(regola_volume(selettoreVolume.get_value()))
    menuImpostazioni.add_button('RITORNA AL MENU PRINCIPALE', pygame_menu.events.BACK, selection_color = (0,0,255))
    return menuImpostazioni
    #for m in ABOUT:
    #    about_menu.add.label(m, margin=(0, 0))
    #about_menu.add.label('')
    #about_menu.add.button('Return to Menu', pygame_menu.events.BACK)

def cambia():
    print("ciao")

def creazione_menuGioco():
    temaPizzeria = pygame_menu.themes.THEME_ORANGE.copy()  #Prendo uno dei temi di default della libreria pygame_menu e lo modifico per le mie esigenze

    imgPizza = pygame_menu.baseimage.BaseImage(image_path = PATH_IMMAGINE_BG,
                                               drawing_mode = pygame_menu.baseimage.IMAGE_MODE_FILL) #imgPizza mi permette di creare la mia immagine di sfondo come background

                                                        
    temaPizzeria.background_color = imgPizza
    temaPizzeria.widget_font = fontMenu
    temaPizzeria.title_font_size = 54
    temaPizzeria.title_font_color = (0,108,50)
    temaPizzeria.title_font = fontMenu
    temaPizzeria.widget_font_color = (0,108,50)

    menuGioco = pygame_menu.Menu(919, 1279, 'Ciccios Pizza',
                           theme=temaPizzeria)
    menuGioco = settaClick(menuGioco)

    menuGioco.add_vertical_margin(50)
    imgLogo =  menuGioco.add_image(PATH_LOGO)
    menuGioco.add_vertical_margin(150)
    bottoneInizia = menuGioco.add_button('INIZIA PARTITA', start_the_game, selection_color = (0,0,255))
    menuGioco.add_vertical_margin(50)
    selettoreModalita = menuGioco.add_selector('MODALITA DI GIOCO :', [('CARRIERA', 1), ('GIRO PIZZA', 2)], onchange=cambia_modalita, selection_color = (0,0,255))
    menuGioco.add_vertical_margin(50)
    bottoneImpostazioni = menuGioco.add_button('IMPOSTAZIONI', Imposta(), selection_color = (0,0,255))
    menuGioco.add_vertical_margin(50)
    bottoneEsci = menuGioco.add_button('ESCI DAL GIOCO', pygame_menu.events.EXIT, selection_color = (0,0,255))
    menuGioco.add_vertical_margin(150)
    muto = pygame_menu.widgets.Image(PATH_MUTO)
    imgSuonoAttivo =  menuGioco.add_image(PATH_VOLUME, align = pygame_menu.locals.ALIGN_LEFT)
    a = imgSuonoAttivo.get_position()
    print(a)
    menuGioco.mainloop(surface)

pygame.init()#inizio programma
surface = pygame.display.set_mode((1280, 920)) #CREAZIONE SCHERMO DI GIOCO
PATH_IMMAGINE_BG = "Immagini_Gioco/background_menu/background.png" #PATH (percorso della mia immagine da mettere come sfondo)
PATH_VOLUME = "Immagini_Gioco/volumeAttivo.png"
PATH_MUTO = "Immagini_Gioco/muto.png"
PATH_LOGO = "Immagini_Gioco/logo.png"
DEFAULT_VOLUME = 0.5
fontMenu = pygame_menu.font.FONT_8BIT
colonnaSonora(DEFAULT_VOLUME) #faccio partire la colonna sonora

creazione_menuGioco()

