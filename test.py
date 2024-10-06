import pygame
import sys
import pygame_menu
from pygame_menu import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((918, 630))
icon = pygame.image.load('img/Main_icon.png')           # Загрузка изображения для значка
pygame.display.set_icon(icon)                           # Устанавливаем значок окна
pygame.display.set_caption("Player_test")

player_x = 100                                          # Глобальные переменные для положения игрока
player_y = 500
player_seed = 7
player_anim_count = 0

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


def player():
    global player_x, player_y, player_anim_count  # Используем глобальные переменные

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and player_x > 10: # Обработка движения игрока
        player_x -= player_seed
        player_anim_count = (player_anim_count + 1) % len(player_walk_left)  # Идем налево
        screen.blit(player_walk_left[player_anim_count], (player_x, player_y))

    elif keys[pygame.K_RIGHT] and player_x < 860:
        player_x += player_seed
        player_anim_count = (player_anim_count + 1) % len(player_walk_right)  # Идем направо
        screen.blit(player_walk_right[player_anim_count], (player_x, player_y))

    else:
        screen.blit(player_stay, (player_x, player_y))  # Показываем стоящее положение


def sn1(): 
    bacraund2 = pygame.image.load('img/Locations/№2 .jpg').convert()

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()                        

        screen.blit(bacraund2, (0, 0))
        player()  # Вызов функции игрока

        pygame.display.update()
        clock.tick(15)


def game():
    while True:
        sn1()


def menu():    
    background_image = pygame.image.load('img/Menu_fon.jpg')  # Загрузка фонового изображения
    button_background_color = (144, 238, 144)  # Цвет фона кнопок
    button_text_color = (255, 255, 255)  # Белый цвет текста

    font = pygame_menu.font.FONT_MUNRO
    menubar = pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL

    myimage = pygame_menu.baseimage.BaseImage(
        image_path='img/Menu_fon.jpg',  
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
    )

    mytheme = Theme(background_color=myimage,
                    title_background_color=(4, 47, 126), 
                    widget_font=font,
                    widget_font_color=button_text_color,
                    title_bar_style=menubar,
                    widget_background_color=button_background_color)

    menu = pygame_menu.Menu('Welcome to the alpha', 918, 630, theme=mytheme)

    menu.add.text_input('', default='Morning_game') 
    menu.add.button('Play', game) 
    menu.add.button('Quit', pygame_menu.events.EXIT)
    
    menu.mainloop(screen)

menu()