import pygame
import sys
import pygame_menu
from pygame_menu import *
import imageio

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((918, 630))

menu_music = 'song/Music/Clam.mp3'                       # Загрузка музыки

icon = pygame.image.load('img/Main_icon.png')           # Загрузка изображения для значка

pygame.display.set_icon(icon)                           # Устанавливаем значок окна
pygame.display.set_caption("Menu_test")
    
def menu2():
    
    pygame.mixer.music.load(menu_music)
    pygame.mixer.music.play(-1)                        # Зацикливание музыки
    
    background_image = pygame.image.load('img/Menu_fon.jpg') # Загрузка фонового изображения
        
    button_background_color = (144, 238, 144)           # Цвет фона кнопок
    button_hover_background_color = (0, 250, 154)       # Цвет фона кнопок при наведении
    button_text_color = (255, 255, 255)                 # Белый цвет текста
    button_hover_color = (0, 0, 0)                      # Цвет текста при наведении
    
    font = pygame_menu.font.FONT_MUNRO
    menubar = pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL
    
    # Загрузка фонового изображения
    myimage = pygame_menu.baseimage.BaseImage(
        image_path='img/Menu_fon.jpg',  
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
    )
    
    mytheme = Theme(background_color=myimage,
                    title_background_color=(4, 47, 126), 
                    widget_font=font,
                    widget_font_color=button_text_color,
                    title_bar_style=menubar,
                    widget_background_color=button_background_color,
                    widget_margin=(10, 10))

    def set_difficulty(value, difficulty):
        pass    
    
    menu = pygame_menu.Menu('Welcome', 918, 630, 
                            theme=mytheme) 
    
    menu.add.text_input('', default='Morning_game') 
    menu.add.selector('Difficulty :', [('Chapter 1', 1), ('Chapter 2', 2)], onchange=set_difficulty)
    menu.add.button('Play',) 
    menu.add.button('Quit', pygame_menu.events.EXIT)
    
    menu.mainloop(screen)
    menu.update(pygame.event.get())
    menu.draw(screen)    
    
    
def menu():
    
    pygame.mixer.music.load(menu_music)
    pygame.mixer.music.play(-1)                        # Зацикливание музыки
    
    background_image = pygame.image.load('img/Menu_fon.jpg') # Загрузка фонового изображения
        
    button_background_color = (144, 238, 144)           # Цвет фона кнопок
    button_hover_background_color = (0, 250, 154)       # Цвет фона кнопок при наведении
    button_text_color = (255, 255, 255)                 # Белый цвет текста
    button_hover_color = (0, 0, 0)                      # Цвет текста при наведении
    
    font = pygame_menu.font.FONT_MUNRO
    menubar = pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL
    
    # Загрузка фонового изображения
    myimage = pygame_menu.baseimage.BaseImage(
        image_path='img/Menu_fon.jpg',  
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
    )
    
    mytheme = Theme(background_color=myimage,
                    title_background_color=(4, 47, 126), 
                    widget_font=font,
                    widget_font_color=button_text_color,
                    title_bar_style=menubar,
                    widget_background_color=button_background_color,
                    widget_margin=(10, 10))

    def set_difficulty(value, difficulty):
        pass    
    
    menu = pygame_menu.Menu('Welcome', 918, 630, 
                            theme=mytheme) 
    
    menu.add.text_input('', default='Morning_game') 
    menu.add.button('Play', menu2) 
    menu.add.button('Quit', pygame_menu.events.EXIT)
    
    menu.mainloop(screen)
    menu.update(pygame.event.get())
    menu.draw(screen)
menu()

