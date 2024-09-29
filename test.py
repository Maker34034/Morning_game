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
game_music = 'song/Music/Morring city.mp3'  
v_3_music = 'song/Music/V_3.mp3'

icon = pygame.image.load('img/Main_icon.png')           # Загрузка изображения для значка

pygame.display.set_icon(icon)                           # Устанавливаем значок окна
pygame.display.set_caption("Menu_test")
   
    
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


def video_2():
    
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
    
        frame_surface = pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], "RGB") # Конвертация кадра в формат, понятный Pygame
    
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
        video_2()


def game():
      
    while True:
        sn_close()  
        sn_open()  
        
        
def video():
    
        pygame.mixer.music.stop()                       # Остановим музыку меню
        pygame.mixer.music.load(game_music)             # Запуск музыки игры
        pygame.mixer.music.play(-1    )                 # Включите зацикливание музыки  
    
        video_path = 'V_2_out.mp4'                      # Загрузка видео 
        video_reader = imageio.get_reader(video_path)
        
        running = True                                  # Основной цикл
        for frame in video_reader:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            frame_surface = pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], "RGB") # Конвертация кадра в формат, понятный Pygame
        
            screen.blit(frame_surface, (0, 0))         # Отображение кадра на экране
            pygame.display.flip()
        
            
            pygame.time.delay(int(1000 / 30))          # Задержка для соответствия FPS видео (пример: 30 FPS)
        
        game()                                         # Вызываем функцию после завершения видео


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
    
    
    menu = pygame_menu.Menu('Welcome', 918, 630, 
                            theme=mytheme)
    
    menu.add.text_input('', default='Morning_game') 
    menu.add.button('Play', video) 
    menu.add.button('Quit', pygame_menu.events.EXIT)
    
    menu.mainloop(screen)
    menu.update(pygame.event.get())
    menu.draw(screen)
menu()