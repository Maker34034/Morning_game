import pygame
import sys
import pygame_menu
from pygame_menu import *

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((918, 630))
pygame.display.set_caption("Keys_test")

def sn_close():
    
    background = pygame.image.load('img/Locations/Close.jpg').convert()

    player_seed = 7
    keys_x = 1
    keys_y = 1
    keys_pos = [4 // 2, 4 // 2] 

    player_anim_count = 0
    
    sur_tast = pygame.Surface((70, 40))
    sur_tast.fill('Red')        
    
    key = pygame.image.load('img/Original_keys.png')

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_7]:
                key = pygame.image.load('img/1967_keys.png')
            else:
                key = pygame.image.load('img/Original_keys.png')

            # Проверка нажатия кнопки мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if sur_tast.get_rect(topleft=(350, 450)).collidepoint(mouse_x, mouse_y):
                    sn_open()  # Переход на следующую сцену

        screen.blit(background, (0, 0)) 
        key_rect = key.get_rect(topleft=(100, 100))
        
        # Рисуем красный квадрат (кнопку)
        screen.blit(sur_tast, (350, 450))
        
        # Отображаем ключи (или курсор)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(key, (mouse_x // 1.1, mouse_y // 1.1))
        
        pygame.display.update()
        clock.tick(60)


def sn_open():
    
    background = pygame.image.load('img/Locations/Open.jpg').convert()

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()     
                
        screen.blit(background, (0, 0))

        pygame.display.update()
        clock.tick(15)


def game():
    while True:
        sn_close()  # Начинаем с первой сцены
        sn_open()  # Затем переходим ко второй сцене


font = pygame_menu.font.FONT_MUNRO
menubar = pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL

mytheme = Theme(background_color=(0, 0, 0, 0),
                title_background_color=(4, 47, 126), 
                widget_font=font,
                title_bar_style=menubar)

menu = pygame_menu.Menu('Welcome', 918, 630, 
                        theme=mytheme)

menu.add.text_input('', default='Morning_game') 
menu.add.button('Play', game) 
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)