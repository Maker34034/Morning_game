import pygame
import sys
import pygame_menu
from pygame_menu import *

# Инициализация Pygame
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((918, 630))
pygame.display.set_caption("This_is_The_Morning_game")

def sn1(): # Функция первой сцены

    player_walk_right = [
        pygame.image.load('pl_ra/player_1.png'),
        pygame.image.load('pl_ra/player_2.png'),
        pygame.image.load('pl_ra/player_3.png'),
        pygame.image.load('pl_ra/player_4.png')
    ]

    player_walk_left = [
        pygame.image.load('pl_le/player_1.png'),
        pygame.image.load('pl_le/player_2.png'),
        pygame.image.load('pl_le/player_3.png'),
        pygame.image.load('pl_le/player_4.png')
    ]

    player_stay = pygame.image.load('pl_ra/player_1.png')
    bacraund2 = pygame.image.load('img/Locations/№2 .jpg').convert()

    player_seed = 7
    player_x = 100
    player_y = 400

    player_anim_count = 0
    
    sur_tast = pygame.Surface((50, 20))
    sur_tast.fill('Red')    

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Завершение программы
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:  # Нажмите "2", чтобы перейти к сцене 2
                    return  # Завершить эту функцию и перейти к следующей сцене
                if event.key == pygame.K_3:  
                    return                             

        screen.blit(bacraund2, (0, 0))
        player_rect = player_walk_left[0].get_rect(topleft=(player_x, player_y))
        
        transition_1 = sur_tast.get_rect(topleft=(863, 400))
        transition_2 = sur_tast.get_rect(topleft=(9, 400))
        
        
        if player_rect.colliderect(transition_1):
            sn2()
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            screen.blit(player_walk_left[player_anim_count], (player_x, player_y))
        elif keys[pygame.K_RIGHT]:
            screen.blit(player_walk_right[player_anim_count], (player_x, player_y))
        else:
            screen.blit(player_stay, (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x > 10:
            player_x -= player_seed
        elif keys[pygame.K_RIGHT] and player_x < 860:
            player_x += player_seed

        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        pygame.display.update()
        clock.tick(15)
        
def sn2():

    player_walk_right = [
        pygame.image.load('pl_ra/player_1.png'),
        pygame.image.load('pl_ra/player_2.png'),
        pygame.image.load('pl_ra/player_3.png'),
        pygame.image.load('pl_ra/player_4.png')
    ]

    player_walk_left = [
        pygame.image.load('pl_le/player_1.png'),
        pygame.image.load('pl_le/player_2.png'),
        pygame.image.load('pl_le/player_3.png'),
        pygame.image.load('pl_le/player_4.png')
    ]

    player_stay = pygame.image.load('pl_ra/player_1.png')
    bacraund2 = pygame.image.load('img/Locations/№3 .jpg').convert()

    player_seed = 7
    player_x = 100
    player_y = 400

    player_anim_count = 0
    
    sur_tast = pygame.Surface((50, 20))
    sur_tast.fill('Red')    

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Завершение программы
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # Нажмите "3", чтобы перейти к сцене 3
                    return  # Завершить эту функцию и перейти к следующей сцене  
                if event.key == pygame.K_3:  
                    return
                 
        screen.blit(bacraund2, (0, 0))
        player_rect = player_walk_left[0].get_rect(topleft=(player_x, player_y))
        
        transition_1 = sur_tast.get_rect(topleft=(863, 400))
        transition_2 = sur_tast.get_rect(topleft=(9, 400))        
        
        if player_rect.colliderect(transition_1):
            sn3()
        elif player_rect.colliderect(transition_2):
            sn1()            

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            screen.blit(player_walk_left[player_anim_count], (player_x, player_y))
        elif keys[pygame.K_RIGHT]:
            screen.blit(player_walk_right[player_anim_count], (player_x, player_y))
        else:
            screen.blit(player_stay, (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x > 10:
            player_x -= player_seed
        elif keys[pygame.K_RIGHT] and player_x < 860:
            player_x += player_seed

        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        pygame.display.update()
        clock.tick(15)

def sn3():
    
    player_walk_right = [
        pygame.image.load('pl_ra/player_1.png'),
        pygame.image.load('pl_ra/player_2.png'),
        pygame.image.load('pl_ra/player_3.png'),
        pygame.image.load('pl_ra/player_4.png')
    ]

    player_walk_left = [
        pygame.image.load('pl_le/player_1.png'),
        pygame.image.load('pl_le/player_2.png'),
        pygame.image.load('pl_le/player_3.png'),
        pygame.image.load('pl_le/player_4.png')
    ]

    player_stay = pygame.image.load('pl_ra/player_1.png')
    bacraund2 = pygame.image.load('img/Locations/№4 .jpg').convert()

    player_seed = 7
    player_x = 100
    player_y = 400

    player_anim_count = 0
    
    sur_tast = pygame.Surface((50, 20))
    sur_tast.fill('Red')        

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Завершение программы
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # Нажмите "3", чтобы перейти к сцене 3
                    return  # Завершить эту функцию и перейти к следующей сцене  
                if event.key == pygame.K_2:  
                    return          
                
        screen.blit(bacraund2, (0, 0))
        player_rect = player_walk_left[0].get_rect(topleft=(player_x, player_y))
        
        transition_2 = sur_tast.get_rect(topleft=(9, 400))
        
        if player_rect.colliderect(transition_2):
            sn2()        

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            screen.blit(player_walk_left[player_anim_count], (player_x, player_y))
        elif keys[pygame.K_RIGHT]:
            screen.blit(player_walk_right[player_anim_count], (player_x, player_y))
        else:
            screen.blit(player_stay, (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x > 10:
            player_x -= player_seed
        elif keys[pygame.K_RIGHT] and player_x < 860:
            player_x += player_seed

        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        pygame.display.update()
        clock.tick(15)

def game():
    sound1 = pygame.mixer.Sound('song/Music/Morring city.mp3')
    sound1.set_volume(0.1)
    sound1.play()
    
    while True:
        sn1()  # Начинаем с первой сцены
        sn2()  # Затем переходим ко второй сцене
        sn3()


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