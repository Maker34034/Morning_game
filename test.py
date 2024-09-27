import pygame
import sys
import pygame_menu
from pygame_menu import *
import imageio

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((918, 630))

# Загрузка музыки
menu_music = 'song/Music/Clam.mp3'  # Замените на путь к вашей музыке для меню
game_music = 'song/Music/Morring city.mp3'  # Замените на путь к вашей музыке для игры

# Загрузка изображения для значка
icon = pygame.image.load('img/Main_icon.png')

# Устанавливаем значок окна
pygame.display.set_icon(icon)
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


def video_2():
    pygame.mixer.music.stop()
    # Загрузка видео
    video_path = 'V_3.mp4'  # Укажите путь к вашему видео файлу
    video_reader = imageio.get_reader(video_path)
    
    # Основной цикл
    running = True
    for frame in video_reader:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        # Конвертация кадра в формат, понятный Pygame
        frame_surface = pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], "RGB")
    
        # Отображение кадра на экране
        screen.blit(frame_surface, (0, 0))
        pygame.display.flip()
    
        # Задержка для соответствия FPS видео (пример: 30 FPS)
        pygame.time.delay(int(1000 / 60))
    
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
        sn_close()  # Начинаем с первой сцены
        sn_open()  # Затем переходим ко второй сцене
        
        
def video():
    # Остановим музыку меню
        pygame.mixer.music.stop()
        
        # Запуск музыки игры
        pygame.mixer.music.load(game_music)
        pygame.mixer.music.play(-1    )  # Включите зацикливание музыки  
    
        # Загрузка видео
        video_path = 'V_2_out.mp4'  # Укажите путь к вашему видео файлу
        video_reader = imageio.get_reader(video_path)
        
        # Основной цикл
        running = True
        for frame in video_reader:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
            # Конвертация кадра в формат, понятный Pygame
            frame_surface = pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], "RGB")
        
            # Отображение кадра на экране
            screen.blit(frame_surface, (0, 0))
            pygame.display.flip()
        
            # Задержка для соответствия FPS видео (пример: 30 FPS)
            pygame.time.delay(int(1000 / 30))
        
        # Вызываем функцию после завершения видео
        game()


def menu():
    pygame.mixer.music.stop()  # Остановка музыки игры
    pygame.mixer.music.load(menu_music)
    pygame.mixer.music.play(-1)  # Включите зацикливание музыки
    
    # Настройка музыки меню
    pygame.mixer.music.load(menu_music)
    pygame.mixer.music.play(-1)  # Включите зацикливание музыки меню    
    
    # Загрузка фонового изображения
    background_image = pygame.image.load('img/Menu_fon.jpg')
        
    # Функция для отрисовки фонового изображения
    def draw_background():
        screen.blit(background_image, (0, 0))
        
    
    # Задание цветов
    button_background_color = (144, 238, 144)  # Цвет фона кнопок
    button_hover_background_color = (0, 250, 154) # Цвет фона кнопок при наведении
    button_text_color = (255, 255, 255)  # Белый цвет текста
    button_hover_color = (0, 0, 0)   # Цвет текста при наведении
    
    font = pygame_menu.font.FONT_MUNRO
    menubar = pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL
    
    # Загрузка фонового изображения
    myimage = pygame_menu.baseimage.BaseImage(
        image_path='img/Menu_fon.jpg',  
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
    )
    
    mytheme = Theme(background_color=myimage, #(0, 0, 0, 0)
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