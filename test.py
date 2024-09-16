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
    
    bacraund = pygame.image.load('img/Locations/Close.jpg').convert()

    player_seed = 7
    keys_x = 1
    keys_y = 1
    keys_pos = [4 // 2, 4 // 2] 

    player_anim_count = 0
    
    sur_tast = pygame.Surface((50, 20))
    sur_tast.fill('Red')        
    
    keys = pygame.image.load('img/1726509240830.png')

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
                
        screen.blit(bacraund, (0, 0))
        #screen.blit(keys, (0, 0))
        keys_rect = keys.get_rect(topleft=(keys_x, keys_y))
        
        #transition_2 = sur_tast.get_rect(topleft=(9, 400))
        #if keys_rect.colliderect(transition_2):
        #    sn_open()        

        mouse_x, mouse_y = pygame.mouse.get_pos() #pygame.mouse.get_pressed()
        #pos = pygame.mouse.get_pos()
        
       
        screen.blit(keys, (mouse_x // 1.1, mouse_y // 1.1))
        
        #if mouse[0]:
        #    keys_x = pos
        #    keys_y = pos
        #    screen.blit(keys, (keys_x, keys_y))
            
        #if player_anim_count == 3:
        #    player_anim_count = 0
        #else:
        #    player_anim_count += 1

        pygame.display.update()
        clock.tick(60) 
        
        
def sn_open():
    
    bacraund = pygame.image.load('img/Locations/Open.jpg').convert()

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()     
                
        screen.blit(bacraund, (0, 0))
 
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