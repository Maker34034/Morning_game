import pygame
import sys

# Инициализация Pygame
pygame.init()
clock = pygame.time.Clock()

# Функция первой сцены
def sn1():
    screen = pygame.display.set_mode((918, 630))  # 1818, 1362 or 918, 662

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
    bacraund1 = pygame.image.load('img/Locations/№1 .jpg').convert()

    player_seed = 7
    player_x = 100
    player_y = 400

    player_anim_count = 0

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Завершение программы
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:  # Нажмите "2", чтобы перейти к сцене 2
                    return  # Завершить эту функцию и перейти к следующей сцене
                if event.key == pygame.K_2:  
                    return  
                if event.key == pygame.K_4:  
                    return                 

        screen.blit(bacraund1, (0, 0))
        player_rect = player_walk_left[0].get_rect(topleft=(player_x, player_y))

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

# Функция второй сцены
def sn2():
    screen = pygame.display.set_mode((918, 630))  # 1818, 1362 or 918, 662

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

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Завершение программы
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # Нажмите "1", чтобы перейти к сцене 1
                    return  # Завершить эту функцию и перейти к следующей сцене
                if event.key == pygame.K_3:  
                    return                
                if event.key == pygame.K_4:  
                    return                 

        screen.blit(bacraund2, (0, 0))
        player_rect = player_walk_left[0].get_rect(topleft=(player_x, player_y))

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
    screen = pygame.display.set_mode((918, 630))  # 1818, 1362 or 918, 662

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
                if event.key == pygame.K_4:  
                    return                 
                

        screen.blit(bacraund2, (0, 0))
        player_rect = player_walk_left[0].get_rect(topleft=(player_x, player_y))

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


def sn4():
    screen = pygame.display.set_mode((918, 630))  # 1818, 1362 or 918, 662

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
                if event.key == pygame.K_3:  
                    return                 
                

        screen.blit(bacraund2, (0, 0))
        player_rect = player_walk_left[0].get_rect(topleft=(player_x, player_y))

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
        
# Основной цикл программы
while True:
    sn1()  # Начинаем с первой сцены
    sn2()  # Затем переходим ко второй сцене
    sn3()
    sn4()