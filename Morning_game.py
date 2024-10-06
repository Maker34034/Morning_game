import pygame
import sys
import pygame_menu
from pygame_menu import *
import imageio

pygame.init()       # Инициализация Pygame
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((918, 630))

menu_music = 'song/Music/Clam.mp3'                       # Загрузка музыки
game_music = 'song/Music/Morring city.mp3'  
v_3_music = 'song/Music/V_3.mp3'

icon = pygame.image.load('img/Main_icon.png')           # Загрузка изображения для значка
pygame.display.set_icon(icon)                           # Устанавливаем значок
pygame.display.set_caption("This_is_The_Morning_game 30.09.2024.20:08")

def sn1(player_x, player_y): # Функция первой сцены

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
        
        transition_1 = sur_tast.get_rect(topleft=(863, 500))
        
        if player_rect.colliderect(transition_1):
            sn2(100, 400)
        
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
        
def sn2(player_x, player_y):

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
            video_2()
        elif player_rect.colliderect(transition_2):
            sn1(800, 500)            

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


def video_2():
 
        video_path = 'V_2_out.mp4'                      # Загрузка видео 
        video_reader = imageio.get_reader(video_path)
        
        running = True                                  # Основной цикл
        for frame in video_reader:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            frame_surface = pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], "RGB")
        
            screen.blit(frame_surface, (0, 0))         # Отображение кадра на экране
            pygame.display.flip()
            
            pygame.time.delay(int(1000 / 30))          # Задержка для соответствия FPS видео (пример: 30 FPS)
        
        game_2()      


def sn3(player_x, player_y):
    
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
        
        transition_1 = sur_tast.get_rect(topleft=(863, 400))
        transition_2 = sur_tast.get_rect(topleft=(9, 400))        
        
        if player_rect.colliderect(transition_2):
            sn2(800, 400)
        elif player_rect.colliderect(transition_1):
            sn_close()

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

def game_1():
    while True:
        sn1(100, 500)  # Начинаем с первой сцены
        sn2(100, 400)  # Затем переходим ко второй сцене
        
        
def game_2():
    while True:
        sn3(100, 400)
        sn_close()  
        sn_open()        


def video_1():
    
        pygame.mixer.music.stop()                       # Остановим музыку меню
        pygame.mixer.music.load(game_music)             # Запуск музыки игры
        pygame.mixer.music.play(-1    )                 # Включите зацикливание музыки  
    
        video_path = 'V_1_out.mp4'                      # Загрузка видео 
        video_reader = imageio.get_reader(video_path)
        
        running = True                                  # Основной цикл
        for frame in video_reader:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            frame_surface = pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], "RGB")
        
            screen.blit(frame_surface, (0, 0))         # Отображение кадра на экране
            pygame.display.flip()
            
            pygame.time.delay(int(1000 / 30))          # Задержка для соответствия FPS видео (пример: 30 FPS)
        
        game_1()            

def sn_close():

    player_seed = 7
    keys_x = 1
    keys_y = 1
    keys_pos = [4 // 2, 4 // 2] 

    player_anim_count = 0
    
    sur_tast = pygame.Surface((70, 40))
    sur_tast.fill('Red')        
    
    background = pygame.image.load('img/Locations/Close.jpg').convert()
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
                
            if event.type == pygame.MOUSEBUTTONDOWN:         # Проверка нажатия кнопки мыши
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if sur_tast.get_rect(topleft=(350, 450)).collidepoint(mouse_x, mouse_y):
                    sn_open()  # Переход на следующую сцену

        screen.blit(background, (0, 0)) 
        key_rect = key.get_rect(topleft=(100, 100))
        
        mouse_x, mouse_y = pygame.mouse.get_pos()      # Отображаем ключи
        screen.blit(key, (mouse_x // 1.1, mouse_y // 1.1))
        
        pygame.display.update()
        clock.tick(60)


def video_3():
    
    pygame.mixer.music.stop()
    pygame.mixer.music.load(v_3_music)
    pygame.mixer.music.play()  
    
    video_path = 'V_3.mp4'    # Загрузка видео
    video_reader = imageio.get_reader(video_path)
    
    
    running = True  # Основной цикл
    for frame in video_reader:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        frame_surface = pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], "RGB") 
    
        screen.blit(frame_surface, (0, 0)) # Отображение кадра на экране
        pygame.display.flip()
        pygame.time.delay(int(1000 / 100)) # Задержка для соответствия FPS видео
    
    menu()
    
    
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
        video_3()


def menu():
    
    pygame.mixer.music.stop()                          # Остановка музыки игры
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
    
    
    menu = pygame_menu.Menu('Welcome to the alpha 30.09.2024.20:08', 918, 630, 
                            theme=mytheme)
    
    menu.add.text_input('', default='Morning_game') 
    menu.add.button('Play', video_1) 
    menu.add.button('Quit', pygame_menu.events.EXIT)
    
    menu.mainloop(screen)
    menu.update(pygame.event.get())
    menu.draw(screen)
menu()