import pygame, sys
import pygame_menu #libreria di pygame che permette una facile creazione del main menu di gioco
from pygame_menu import sound


#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

from pygame.locals import *

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


def reset_flag():
	global FLAG
	FLAG = 0

def set_flag():
	global FLAG 
	FLAG= 1
	
def get_flag():
	global FLAG
	return FLAG

def creazione_menu_pausa():
	
	temaPausa =  pygame_menu.themes.THEME_SOLARIZED.copy()
	
	imgBack = pygame_menu.baseimage.BaseImage(image_path = PATH_IMMAGINE_BG, drawing_mode = pygame_menu.baseimage.IMAGE_MODE_FILL)
	
	temaPausa.background_color= imgBack
	
	temaPausa.widget_font = fontMenu
	temaPausa.title_font_size = 54
	temaPausa.title_font_color = (255,117,20)
	temaPausa.title_font = fontMenu
	temaPausa.widget_font_color = (0,127,255)
	menuPausa = pygame_menu.Menu(919, 1279, 'PAUSA', theme=temaPausa)
	menuPausa.add_button('xxx', None,  selection_color = (0,0,255))
	menuPausa.add_button('ESCI DAL MENU', set_flag, selection_color = (0,0,255))
    
	return menuPausa
    

fontMenu = pygame_menu.font.FONT_8BIT
PATH_IMMAGINE_BG = "Immagini_Gioco/background_menu/background.png"
FLAG= 0
