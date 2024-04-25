import pygame
from pygame import *
import sys
import random
import math
import time

pygame.mixer.init()

c = pygame.mixer.music.load('звуки/msc.wav')
pygame.mixer.music.play()
clock = pygame.time.Clock()
level_one = pygame.image.load('изображения/fon.png')
level_two = pygame.image.load('изображения/level_two.png')
level_three = pygame.image.load('изображения/level_three.png')
change_levels = pygame.image.load('изображения/change.png')

begin = pygame.image.load('изображения/fon_hi_new.png')
blue = pygame.image.load('изображения/fon_blue_new.png')
yellow = pygame.image.load('изображения/fon_yellow_new.png')
blue_win = pygame.image.load('изображения/fon_blue_win.png')
yellow_win = pygame.image.load('изображения/fon_yellow_win.png')
player_ppl = pygame.image.load('изображения/player_purple.png.')

clock = pygame.time.Clock()


def draw0(screen):
    color2 = pygame.Color(255, 255, 0)
    screen.fill((0, 0, 0))
    screen.blit(begin, (0, 0))

    intro_text = ["                                                     Игра лабиринт", "",
                  "            ",
                  "                    ",
                  "     "]

    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('pink'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                win12(screen)
        pygame.display.flip()
        clock.tick(60)


def win1(screen):
    color2 = pygame.Color(255, 255, 0)
    screen.fill((0, 0, 0))
    screen.blit((yellow), (0, 0))

    c = pygame.mixer.music.load('звуки/msc.wav')
    pygame.mixer.music.play()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                win12(screen)
        pygame.display.flip()
        clock.tick(60)


def win12(screen):
    color2 = pygame.Color(255, 255, 0)
    screen.fill((0, 0, 0))
    screen.blit((change_levels), (0, 0))

    c = pygame.mixer.music.load('звуки/music_change_level.wav')
    pygame.mixer.music.play()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        draw(screen)
    elif keys[pygame.K_2]:
        draw2(screen)
    elif keys[pygame.K_3]:
        draw3(screen)


def win2(screen):
    color2 = pygame.Color(255, 255, 0)
    screen.fill((0, 0, 0))
    screen.blit((blue), (0, 0))
    c = pygame.mixer.music.load('звуки/msc.wav')
    pygame.mixer.music.play()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                win12(screen)
        pygame.display.flip()
        clock.tick(60)


def win3(screen):
    color2 = pygame.Color(255, 255, 0)
    screen.fill((0, 0, 0))
    screen.blit((blue_win), (0, 0))
    pygame.mixer.music.load('звуки/win.wav')
    pygame.mixer.music.play()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                win12(screen)
        pygame.display.flip()
        clock.tick(60)


def win4(screen):
    color2 = pygame.Color(255, 255, 0)
    screen.fill((0, 0, 0))
    screen.blit((yellow_win), (0, 0))
    pygame.mixer.music.load('звуки/win.wav')
    pygame.mixer.music.play()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                win12(screen)
        pygame.display.flip()
        clock.tick(60)


def draw(screen):
    color = pygame.Color(255, 0, 255)
    color2 = pygame.Color(255, 255, 0)
    color3 = pygame.Color(0, 255, 255)
    color4 = pygame.Color(0, 100, 255)
    color42 = pygame.Color(128, 255, 60)
    vb = pygame.image.load("изображения/player_purple.png")

    pygame.mixer.music.load('звуки/flight_new.wav')
    pygame.mixer.music.play()

    a = random.randint(1, 600)
    b = random.randint(1, 600)

    speed = 5
    x = 765
    y = 563
    r = 20
    t = 20
    d = 20
    s = 20
    a = random.randint(1, 600)
    b = random.randint(1, 600)
    a1 = random.randint(1, 600)
    b1 = random.randint(1, 600)
    a2 = random.randint(1, 600)
    b2 = random.randint(1, 600)
    a3 = 50
    b3 = 12

    run = True
    while run:
        pygame.time.delay(75)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            d -= speed
        if keys[pygame.K_d]:
            d += speed
        if keys[pygame.K_w]:
            s -= speed
        if keys[pygame.K_s]:
            s += speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            r -= speed
        if keys[pygame.K_h]:
            r += speed
        if keys[pygame.K_t]:
            t -= speed
        if keys[pygame.K_g]:
            t += speed
        screen.fill((0, 0, 0))
        screen.blit(level_one, (0, 0))
        pygame.display.update()

        man = pygame.draw.rect(screen, color2, (x, y, 12, 12), 10)
        screen.blit((vb), (r, t))
        man2 = pygame.draw.rect(screen, color4, (d, s, 12, 12), 10)
        a1 = pygame.draw.rect(screen, color3, (50, 50, 1, 500), 5)
        a2 = pygame.draw.rect(screen, color3, (750, 550, 1, 50), 5)
        a3 = pygame.draw.rect(screen, color3, (100, 0, 1, 500), 5)
        a4 = pygame.draw.rect(screen, color3, (150, 0, 1, 350), 5)
        a5 = pygame.draw.rect(screen, color3, (150, 400, 1, 100), 5)
        a6 = pygame.draw.rect(screen, color3, (200, 50, 1, 100), 5)
        a7 = pygame.draw.rect(screen, color3, (200, 200, 1, 250), 5)
        a8 = pygame.draw.rect(screen, color3, (250, 200, 1, 50), 5)
        a9 = pygame.draw.rect(screen, color3, (300, 150, 1, 100), 5)
        a10 = pygame.draw.rect(screen, color3, (300, 350, 1, 100), 5)
        a11 = pygame.draw.rect(screen, color3, (350, 50, 1, 100), 5)
        a12 = pygame.draw.rect(screen, color3, (350, 300, 1, 200), 5)
        a13 = pygame.draw.rect(screen, color3, (400, 100, 1, 50), 5)
        a14 = pygame.draw.rect(screen, color3, (400, 250, 1, 200), 5)
        a15 = pygame.draw.rect(screen, color3, (450, 200, 1, 150), 5)
        a16 = pygame.draw.rect(screen, color3, (450, 400, 1, 100), 5)
        a17 = pygame.draw.rect(screen, color3, (500, 150, 1, 150), 5)
        a18 = pygame.draw.rect(screen, color3, (500, 450, 1, 50), 5)
        a19 = pygame.draw.rect(screen, color3, (550, 150, 1, 100), 5)
        a20 = pygame.draw.rect(screen, color3, (550, 300, 1, 50), 5)
        a21 = pygame.draw.rect(screen, color3, (600, 150, 1, 200), 5)
        a22 = pygame.draw.rect(screen, color3, (650, 150, 1, 100), 5)
        a23 = pygame.draw.rect(screen, color3, (650, 400, 1, 100), 5)
        a24 = pygame.draw.rect(screen, color3, (700, 50, 1, 150), 5)
        a25 = pygame.draw.rect(screen, color3, (700, 250, 1, 100), 5)
        a26 = pygame.draw.rect(screen, color3, (750, 100, 1, 50), 5)
        a27 = pygame.draw.rect(screen, color3, (750, 200, 1, 150), 5)

        b1 = pygame.draw.rect(screen, color3, (50, 550, 150, 1), 5)
        b2 = pygame.draw.rect(screen, color3, (250, 550, 500, 1), 5)
        b3 = pygame.draw.rect(screen, color3, (50, 500, 50, 1), 5)
        b4 = pygame.draw.rect(screen, color3, (150, 500, 300, 1), 5)
        b5 = pygame.draw.rect(screen, color3, (500, 500, 300, 1), 5)
        b6 = pygame.draw.rect(screen, color3, (500, 450, 100, 1), 5)
        b7 = pygame.draw.rect(screen, color3, (200, 450, 100, 1), 5)
        b8 = pygame.draw.rect(screen, color3, (450, 400, 200, 1), 5)
        b9 = pygame.draw.rect(screen, color3, (700, 400, 100, 1), 5)
        b10 = pygame.draw.rect(screen, color3, (650, 350, 50, 1), 5)
        b11 = pygame.draw.rect(screen, color3, (550, 350, 50, 1), 5)
        b12 = pygame.draw.rect(screen, color3, (450, 350, 50, 1), 5)
        b13 = pygame.draw.rect(screen, color3, (250, 350, 50, 1), 5)
        b14 = pygame.draw.rect(screen, color3, (200, 300, 150, 1), 5)
        b15 = pygame.draw.rect(screen, color3, (500, 300, 50, 1), 5)
        b16 = pygame.draw.rect(screen, color3, (650, 250, 50, 1), 5)
        b17 = pygame.draw.rect(screen, color3, (300, 250, 100, 1), 5)
        b18 = pygame.draw.rect(screen, color3, (200, 200, 50, 1), 5)
        b19 = pygame.draw.rect(screen, color3, (350, 200, 100, 1), 5)
        b20 = pygame.draw.rect(screen, color3, (700, 200, 50, 1), 5)
        b21 = pygame.draw.rect(screen, color3, (750, 150, 50, 1), 5)
        b22 = pygame.draw.rect(screen, color3, (550, 150, 50, 1), 5)
        b23 = pygame.draw.rect(screen, color3, (400, 150, 100, 1), 5)
        b24 = pygame.draw.rect(screen, color3, (200, 150, 100, 1), 5)
        b25 = pygame.draw.rect(screen, color3, (200, 100, 150, 1), 5)
        b26 = pygame.draw.rect(screen, color3, (400, 100, 300, 1), 5)
        b27 = pygame.draw.rect(screen, color3, (750, 100, 50, 1), 5)
        b28 = pygame.draw.rect(screen, color3, (350, 50, 450, 1), 5)
        b29 = pygame.draw.rect(screen, color3, (200, 50, 50, 1), 5)

        prize = pygame.draw.rect(screen, color42, (419, 117, 20, 20), 5)

        if x >= 800 or x < 0 or y >= 600 or y < 0:
            win1(screen)
        elif d >= 800 or d < 0 or s >= 600 or s < 0:
            win2(screen)
        elif prize.colliderect(man):
            win4(screen)
        elif prize.colliderect(man2):
            win3(screen)
        elif a1.colliderect(man):
            win1(screen)
        elif a2.colliderect(man):
            win1(screen)
        elif a3.colliderect((man)):
            win1(screen)
        elif a4.colliderect((man)):
            win1(screen)
        elif a5.colliderect((man)):
            win1(screen)
        elif a6.colliderect((man)):
            win1(screen)
        elif a7.colliderect((man)):
            win1(screen)
        elif a8.colliderect((man)):
            win1(screen)
        elif a9.colliderect((man)):
            win1(screen)
        elif a10.colliderect((man)):
            win1(screen)
        elif a11.colliderect((man)):
            win1(screen)
        elif a12.colliderect((man)):
            win1(screen)
        elif a13.colliderect((man)):
            win1(screen)
        elif a14.colliderect((man)):
            win1(screen)
        elif a15.colliderect((man)):
            win1(screen)
        elif a16.colliderect((man)):
            win1(screen)
        elif a17.colliderect((man)):
            win1(screen)
        elif a18.colliderect((man)):
            win1(screen)
        elif a19.colliderect((man)):
            win1(screen)
        elif a20.colliderect((man)):
            win1(screen)
        elif a21.colliderect((man)):
            win1(screen)
        elif a22.colliderect((man)):
            win1(screen)
        elif a23.colliderect((man)):
            win1(screen)
        elif a24.colliderect((man)):
            win1(screen)
        elif a25.colliderect((man)):
            win1(screen)
        elif a26.colliderect((man)):
            win1(screen)
        elif a27.colliderect((man)):
            win1(screen)

        elif a1.colliderect(man2):
            win2(screen)
        elif a2.colliderect(man2):
            win2(screen)
        elif a3.colliderect((man2)):
            win2(screen)
        elif a4.colliderect((man2)):
            win2(screen)
        elif a5.colliderect((man2)):
            win2(screen)
        elif a6.colliderect((man2)):
            win2(screen)
        elif a7.colliderect((man2)):
            win2(screen)
        elif a8.colliderect((man2)):
            win2(screen)
        elif a9.colliderect((man2)):
            win2(screen)
        elif a10.colliderect((man2)):
            win2(screen)
        elif a11.colliderect((man2)):
            win2(screen)
        elif a12.colliderect((man2)):
            win2(screen)
        elif a13.colliderect((man2)):
            win2(screen)
        elif a14.colliderect((man2)):
            win2(screen)
        elif a15.colliderect((man2)):
            win2(screen)
        elif a16.colliderect((man2)):
            win2(screen)
        elif a17.colliderect((man2)):
            win2(screen)
        elif a18.colliderect((man2)):
            win2(screen)
        elif a19.colliderect((man2)):
            win2(screen)
        elif a20.colliderect((man2)):
            win2(screen)
        elif a21.colliderect((man2)):
            win2(screen)
        elif a22.colliderect((man2)):
            win2(screen)
        elif a23.colliderect((man2)):
            win2(screen)
        elif a24.colliderect((man2)):
            win2(screen)
        elif a25.colliderect((man2)):
            win2(screen)
        elif a26.colliderect((man2)):
            win2(screen)
        elif a27.colliderect((man2)):
            win2(screen)
        elif b1.colliderect((man)):
            win1(screen)
        elif b2.colliderect((man)):
            win1(screen)
        elif b3.colliderect((man)):
            win1(screen)
        elif b4.colliderect((man)):
            win1(screen)
        elif b5.colliderect((man)):
            win1(screen)
        elif b6.colliderect((man)):
            win1(screen)
        elif b7.colliderect((man)):
            win1(screen)
        elif b8.colliderect((man)):
            win1(screen)
        elif b9.colliderect((man)):
            win1(screen)
        elif b10.colliderect((man)):
            win1(screen)
        elif b11.colliderect((man)):
            win1(screen)
        elif b12.colliderect((man)):
            win1(screen)
        elif b13.colliderect((man)):
            win1(screen)
        elif b14.colliderect((man)):
            win1(screen)
        elif b15.colliderect((man)):
            win1(screen)
        elif b16.colliderect((man)):
            win1(screen)
        elif b17.colliderect((man)):
            win1(screen)
        elif b18.colliderect((man)):
            win1(screen)
        elif b19.colliderect((man)):
            win1(screen)
        elif b20.colliderect((man)):
            win1(screen)
        elif b21.colliderect((man)):
            win1(screen)
        elif b22.colliderect((man)):
            win1(screen)
        elif b23.colliderect((man)):
            win1(screen)
        elif b24.colliderect((man)):
            win1(screen)
        elif b25.colliderect((man)):
            win1(screen)
        elif b26.colliderect((man)):
            win1(screen)
        elif b27.colliderect((man)):
            win1(screen)
        elif b28.colliderect((man)):
            win1(screen)
        elif b29.colliderect((man)):
            win1(screen)
        elif b1.colliderect((man2)):
            win2(screen)
        elif b2.colliderect((man2)):
            win2(screen)
        elif b3.colliderect((man2)):
            win2(screen)
        elif b4.colliderect((man2)):
            win2(screen)
        elif b5.colliderect((man2)):
            win2(screen)
        elif b6.colliderect((man2)):
            win2(screen)
        elif b7.colliderect((man2)):
            win2(screen)
        elif b8.colliderect((man2)):
            win2(screen)
        elif b9.colliderect((man2)):
            win2(screen)
        elif b10.colliderect((man2)):
            win2(screen)
        elif b11.colliderect((man2)):
            win2(screen)
        elif b12.colliderect((man2)):
            win2(screen)
        elif b13.colliderect((man2)):
            win2(screen)
        elif b14.colliderect((man2)):
            win2(screen)
        elif b15.colliderect((man2)):
            win2(screen)
        elif b16.colliderect((man2)):
            win2(screen)
        elif b17.colliderect((man2)):
            win2(screen)
        elif b18.colliderect((man2)):
            win2(screen)
        elif b19.colliderect((man2)):
            win2(screen)
        elif b20.colliderect((man2)):
            win2(screen)
        elif b21.colliderect((man2)):
            win2(screen)
        elif b22.colliderect((man2)):
            win2(screen)
        elif b23.colliderect((man2)):
            win2(screen)
        elif b24.colliderect((man2)):
            win2(screen)
        elif b25.colliderect((man2)):
            win2(screen)
        elif b26.colliderect((man2)):
            win2(screen)
        elif b27.colliderect((man2)):
            win2(screen)
        elif b28.colliderect((man2)):
            win2(screen)
        elif b29.colliderect((man2)):
            win2(screen)

        pygame.display.update()
    pygame.quit()


def draw2(screen):
    color = pygame.Color(255, 0, 255)
    color2 = pygame.Color(255, 255, 0)
    color3 = pygame.Color(0, 255, 255)
    color4 = pygame.Color(0, 100, 255)
    color42 = pygame.Color(128, 255, 60)
    green = pygame.Color(25, 200, 25)
    vb = pygame.image.load("изображения/player_purple.png")

    pygame.mixer.music.load('звуки/flight_new.wav')
    pygame.mixer.music.play()

    a = random.randint(1, 600)
    b = random.randint(1, 600)

    speed = 5
    x = 765
    y = 563
    r = 20
    t = 20
    d = 20
    s = 20
    a = random.randint(1, 600)
    b = random.randint(1, 600)
    a1 = random.randint(1, 600)
    b1 = random.randint(1, 600)
    a2 = random.randint(1, 600)
    b2 = random.randint(1, 600)
    a3 = 50
    b3 = 12

    run = True
    while run:
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            d -= speed
        if keys[pygame.K_d]:
            d += speed
        if keys[pygame.K_w]:
            s -= speed
        if keys[pygame.K_s]:
            s += speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            r -= speed
        if keys[pygame.K_h]:
            r += speed
        if keys[pygame.K_t]:
            t -= speed
        if keys[pygame.K_g]:
            t += speed
        screen.fill((0, 0, 0))
        screen.blit(level_two, (0, 0))
        pygame.display.update()

        man = pygame.draw.rect(screen, color2, (x, y, 12, 12), 10)
        screen.blit((vb), (r, t))
        pr = pygame.draw.rect(screen, green, (190, 575, 15, 15), 5)
        man2 = pygame.draw.rect(screen, color4, (d, s, 12, 12), 10)
        a1 = pygame.draw.rect(screen, color3, (50, 50, 1, 500), 5)
        a2 = pygame.draw.rect(screen, color3, (750, 550, 1, 50), 5)
        a3 = pygame.draw.rect(screen, color3, (100, 0, 1, 500), 5)
        a4 = pygame.draw.rect(screen, color3, (150, 0, 1, 350), 5)
        a5 = pygame.draw.rect(screen, color3, (150, 400, 1, 100), 5)
        a6 = pygame.draw.rect(screen, color3, (200, 50, 1, 100), 5)
        a7 = pygame.draw.rect(screen, color3, (200, 200, 1, 250), 5)
        a8 = pygame.draw.rect(screen, color3, (250, 200, 1, 50), 5)
        a9 = pygame.draw.rect(screen, color3, (300, 150, 1, 100), 5)
        a10 = pygame.draw.rect(screen, color3, (300, 350, 1, 100), 5)
        a11 = pygame.draw.rect(screen, color3, (350, 50, 1, 100), 5)
        a12 = pygame.draw.rect(screen, color3, (350, 300, 1, 200), 5)
        a13 = pygame.draw.rect(screen, color3, (400, 100, 1, 50), 5)
        a14 = pygame.draw.rect(screen, color3, (400, 250, 1, 200), 5)
        a15 = pygame.draw.rect(screen, color3, (450, 200, 1, 150), 5)
        a16 = pygame.draw.rect(screen, color3, (450, 400, 1, 100), 5)
        a17 = pygame.draw.rect(screen, color3, (500, 150, 1, 150), 5)
        a18 = pygame.draw.rect(screen, color3, (500, 450, 1, 50), 5)
        a19 = pygame.draw.rect(screen, color3, (550, 150, 1, 100), 5)
        a20 = pygame.draw.rect(screen, color3, (550, 300, 1, 50), 5)
        a21 = pygame.draw.rect(screen, color3, (600, 150, 1, 200), 5)
        a22 = pygame.draw.rect(screen, color3, (650, 150, 1, 100), 5)
        a23 = pygame.draw.rect(screen, color3, (650, 400, 1, 100), 5)
        a24 = pygame.draw.rect(screen, color3, (700, 50, 1, 150), 5)
        a25 = pygame.draw.rect(screen, color3, (700, 250, 1, 100), 5)
        a26 = pygame.draw.rect(screen, color3, (750, 100, 1, 50), 5)
        a27 = pygame.draw.rect(screen, color3, (750, 200, 1, 150), 5)

        b1 = pygame.draw.rect(screen, color3, (50, 550, 150, 1), 5)
        b2 = pygame.draw.rect(screen, color3, (250, 550, 500, 1), 5)
        b3 = pygame.draw.rect(screen, color3, (50, 500, 50, 1), 5)
        b4 = pygame.draw.rect(screen, color3, (150, 500, 300, 1), 5)
        b5 = pygame.draw.rect(screen, color3, (500, 500, 300, 1), 5)
        b6 = pygame.draw.rect(screen, color3, (500, 450, 100, 1), 5)
        b7 = pygame.draw.rect(screen, color3, (200, 450, 100, 1), 5)
        b8 = pygame.draw.rect(screen, color3, (450, 400, 200, 1), 5)
        b9 = pygame.draw.rect(screen, color3, (700, 400, 100, 1), 5)
        b10 = pygame.draw.rect(screen, color3, (650, 350, 50, 1), 5)
        b11 = pygame.draw.rect(screen, color3, (550, 350, 50, 1), 5)
        b12 = pygame.draw.rect(screen, color3, (450, 350, 50, 1), 5)
        b13 = pygame.draw.rect(screen, color3, (250, 350, 50, 1), 5)
        b14 = pygame.draw.rect(screen, color3, (200, 300, 150, 1), 5)
        b15 = pygame.draw.rect(screen, color3, (500, 300, 50, 1), 5)
        b16 = pygame.draw.rect(screen, color3, (650, 250, 50, 1), 5)
        b17 = pygame.draw.rect(screen, color3, (300, 250, 100, 1), 5)
        b18 = pygame.draw.rect(screen, color3, (200, 200, 50, 1), 5)
        b19 = pygame.draw.rect(screen, color3, (350, 200, 100, 1), 5)
        b20 = pygame.draw.rect(screen, color3, (700, 200, 50, 1), 5)
        b21 = pygame.draw.rect(screen, color3, (750, 150, 50, 1), 5)
        b22 = pygame.draw.rect(screen, color3, (550, 150, 50, 1), 5)
        b23 = pygame.draw.rect(screen, color3, (400, 150, 100, 1), 5)
        b24 = pygame.draw.rect(screen, color3, (200, 150, 100, 1), 5)
        b25 = pygame.draw.rect(screen, color3, (200, 100, 150, 1), 5)
        b26 = pygame.draw.rect(screen, color3, (400, 100, 300, 1), 5)
        b27 = pygame.draw.rect(screen, color3, (750, 100, 50, 1), 5)
        b28 = pygame.draw.rect(screen, color3, (350, 50, 450, 1), 5)
        b29 = pygame.draw.rect(screen, color3, (200, 50, 50, 1), 5)

        prize = pygame.draw.rect(screen, color42, (419, 117, 20, 20), 5)

        q = 0
        e = 0

        if x >= 800 or x < 0 or y >= 600 or y < 0:
            win1(screen)
        elif d >= 800 or d < 0 or s >= 600 or s < 0:
            win2(screen)
        elif pr.colliderect(man2):
            green = pygame.Color(200, 0, 0)
            pf = pygame.mixer.Sound('звуки/money.wav')
            pf.play()
            q = 1
        elif pr.colliderect(man):
            green = pygame.Color(200, 0, 0)
            pf = pygame.mixer.Sound('звуки/money.wav')
            pf.play()
            e = 1

        elif prize.colliderect(man):
            win4(screen)
        elif prize.colliderect(man2):
            win3(screen)
        elif a1.colliderect(man):
            win1(screen)
        elif a2.colliderect(man):
            win1(screen)
        elif a3.colliderect((man)):
            win1(screen)
        elif a4.colliderect((man)):
            win1(screen)
        elif a5.colliderect((man)):
            win1(screen)
        elif a6.colliderect((man)):
            win1(screen)
        elif a7.colliderect((man)):
            win1(screen)
        elif a8.colliderect((man)):
            win1(screen)
        elif a9.colliderect((man)):
            win1(screen)
        elif a10.colliderect((man)):
            win1(screen)
        elif a11.colliderect((man)):
            win1(screen)
        elif a12.colliderect((man)):
            win1(screen)
        elif a13.colliderect((man)):
            win1(screen)
        elif a14.colliderect((man)):
            win1(screen)
        elif a15.colliderect((man)):
            win1(screen)
        elif a16.colliderect((man)):
            win1(screen)
        elif a17.colliderect((man)):
            win1(screen)
        elif a18.colliderect((man)):
            win1(screen)
        elif a19.colliderect((man)):
            win1(screen)
        elif a20.colliderect((man)):
            win1(screen)
        elif a21.colliderect((man)):
            win1(screen)
        elif a22.colliderect((man)):
            win1(screen)
        elif a23.colliderect((man)):
            win1(screen)
        elif a24.colliderect((man)):
            win1(screen)
        elif a25.colliderect((man)):
            win1(screen)
        elif a26.colliderect((man)):
            win1(screen)
        elif a27.colliderect((man)):
            win1(screen)

        elif a1.colliderect(man2):
            win2(screen)
        elif a2.colliderect(man2):
            win2(screen)
        elif a3.colliderect((man2)):
            win2(screen)
        elif a4.colliderect((man2)):
            win2(screen)
        elif a5.colliderect((man2)):
            win2(screen)
        elif a6.colliderect((man2)):
            win2(screen)
        elif a7.colliderect((man2)):
            win2(screen)
        elif a8.colliderect((man2)):
            win2(screen)
        elif a9.colliderect((man2)):
            win2(screen)
        elif a10.colliderect((man2)):
            win2(screen)
        elif a11.colliderect((man2)):
            win2(screen)
        elif a12.colliderect((man2)):
            win2(screen)
        elif a13.colliderect((man2)):
            win2(screen)
        elif a14.colliderect((man2)):
            win2(screen)
        elif a15.colliderect((man2)):
            win2(screen)
        elif a16.colliderect((man2)):
            win2(screen)
        elif a17.colliderect((man2)):
            win2(screen)
        elif a18.colliderect((man2)):
            win2(screen)
        elif a19.colliderect((man2)):
            win2(screen)
        elif a20.colliderect((man2)):
            win2(screen)
        elif a21.colliderect((man2)):
            win2(screen)
        elif a22.colliderect((man2)):
            win2(screen)
        elif a23.colliderect((man2)):
            win2(screen)
        elif a24.colliderect((man2)):
            win2(screen)
        elif a25.colliderect((man2)):
            win2(screen)
        elif a26.colliderect((man2)):
            win2(screen)
        elif a27.colliderect((man2)):
            win2(screen)
        elif b1.colliderect((man)):
            win1(screen)
        elif b2.colliderect((man)):
            win1(screen)
        elif b3.colliderect((man)):
            win1(screen)
        elif b4.colliderect((man)):
            win1(screen)
        elif b5.colliderect((man)):
            win1(screen)
        elif b6.colliderect((man)):
            win1(screen)
        elif b7.colliderect((man)):
            win1(screen)
        elif b8.colliderect((man)):
            win1(screen)
        elif b9.colliderect((man)):
            win1(screen)
        elif b10.colliderect((man)):
            win1(screen)
        elif b11.colliderect((man)):
            win1(screen)
        elif b12.colliderect((man)):
            win1(screen)
        elif b13.colliderect((man)):
            win1(screen)
        elif b14.colliderect((man)):
            win1(screen)
        elif b15.colliderect((man)):
            win1(screen)
        elif b16.colliderect((man)):
            win1(screen)
        elif b17.colliderect((man)):
            win1(screen)
        elif b18.colliderect((man)):
            win1(screen)
        elif b19.colliderect((man)):
            win1(screen)
        elif b20.colliderect((man)):
            win1(screen)
        elif b21.colliderect((man)):
            win1(screen)
        elif b22.colliderect((man)):
            win1(screen)
        elif b23.colliderect((man)):
            win1(screen)
        elif b24.colliderect((man)):
            win1(screen)
        elif b25.colliderect((man)):
            win1(screen)
        elif b26.colliderect((man)):
            win1(screen)
        elif b27.colliderect((man)):
            win1(screen)
        elif b28.colliderect((man)):
            win1(screen)
        elif b29.colliderect((man)):
            win1(screen)
        elif b1.colliderect((man2)):
            win2(screen)
        elif b2.colliderect((man2)):
            win2(screen)
        elif b3.colliderect((man2)):
            win2(screen)
        elif b4.colliderect((man2)):
            win2(screen)
        elif b5.colliderect((man2)):
            win2(screen)
        elif b6.colliderect((man2)):
            win2(screen)
        elif b7.colliderect((man2)):
            win2(screen)
        elif b8.colliderect((man2)):
            win2(screen)
        elif b9.colliderect((man2)):
            win2(screen)
        elif b10.colliderect((man2)):
            win2(screen)
        elif b11.colliderect((man2)):
            win2(screen)
        elif b12.colliderect((man2)):
            win2(screen)
        elif b13.colliderect((man2)):
            win2(screen)
        elif b14.colliderect((man2)):
            win2(screen)
        elif b15.colliderect((man2)):
            win2(screen)
        elif b16.colliderect((man2)):
            win2(screen)
        elif b17.colliderect((man2)):
            win2(screen)
        elif b18.colliderect((man2)):
            win2(screen)
        elif b19.colliderect((man2)):
            win2(screen)
        elif b20.colliderect((man2)):
            win2(screen)
        elif b21.colliderect((man2)):
            win2(screen)
        elif b22.colliderect((man2)):
            win2(screen)
        elif b23.colliderect((man2)):
            win2(screen)
        elif b24.colliderect((man2)):
            win2(screen)
        elif b25.colliderect((man2)):
            win2(screen)
        elif b26.colliderect((man2)):
            win2(screen)
        elif b27.colliderect((man2)):
            win2(screen)
        elif b28.colliderect((man2)):
            win2(screen)
        elif b29.colliderect((man2)):
            win2(screen)

        pygame.display.update()
    pygame.quit()


def draw3(screen):
    color = pygame.Color(255, 0, 255)
    color2 = pygame.Color(255, 255, 0)
    color3 = pygame.Color(0, 255, 255)
    color4 = pygame.Color(0, 100, 255)
    color42 = pygame.Color(128, 255, 60)
    vb = pygame.image.load("изображения/player_purple.png")

    pygame.mixer.music.load('звуки/flight_new.wav')
    pygame.mixer.music.play()

    a = random.randint(1, 600)
    b = random.randint(1, 600)

    speed = 5
    x = 765
    y = 563
    r = 20
    t = 20
    d = 20
    s = 20
    a = random.randint(1, 600)
    b = random.randint(1, 600)
    a1 = random.randint(1, 600)
    b1 = random.randint(1, 600)
    a2 = random.randint(1, 600)
    b2 = random.randint(1, 600)
    a3 = 50
    b3 = 12

    run = True
    while run:
        pygame.time.delay(25)
        clock.tick(25)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            d -= speed
        if keys[pygame.K_d]:
            d += speed
        if keys[pygame.K_w]:
            s -= speed
        if keys[pygame.K_s]:
            s += speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            r -= speed
        if keys[pygame.K_h]:
            r += speed
        if keys[pygame.K_t]:
            t -= speed
        if keys[pygame.K_g]:
            t += speed
        screen.fill((0, 0, 0))
        screen.blit(level_three, (0, 0))

        pygame.display.update()

        man = pygame.draw.rect(screen, color2, (x, y, 12, 12), 10)
        screen.blit((vb), (r, t))
        man2 = pygame.draw.rect(screen, color4, (d, s, 12, 12), 10)
        a1 = pygame.draw.rect(screen, color3, (50, 50, 1, 500), 5)
        a2 = pygame.draw.rect(screen, color3, (750, 550, 1, 50), 5)
        a3 = pygame.draw.rect(screen, color3, (100, 0, 1, 500), 5)
        a4 = pygame.draw.rect(screen, color3, (150, 0, 1, 350), 5)
        a5 = pygame.draw.rect(screen, color3, (150, 400, 1, 100), 5)
        a6 = pygame.draw.rect(screen, color3, (200, 50, 1, 100), 5)
        a7 = pygame.draw.rect(screen, color3, (200, 200, 1, 250), 5)
        a8 = pygame.draw.rect(screen, color3, (250, 200, 1, 50), 5)
        a9 = pygame.draw.rect(screen, color3, (300, 150, 1, 100), 5)
        a10 = pygame.draw.rect(screen, color3, (300, 350, 1, 100), 5)
        a11 = pygame.draw.rect(screen, color3, (350, 50, 1, 100), 5)
        a12 = pygame.draw.rect(screen, color3, (350, 300, 1, 200), 5)
        a13 = pygame.draw.rect(screen, color3, (400, 100, 1, 50), 5)
        a14 = pygame.draw.rect(screen, color3, (400, 250, 1, 200), 5)
        a15 = pygame.draw.rect(screen, color3, (450, 200, 1, 150), 5)
        a16 = pygame.draw.rect(screen, color3, (450, 400, 1, 100), 5)
        a17 = pygame.draw.rect(screen, color3, (500, 150, 1, 150), 5)
        a18 = pygame.draw.rect(screen, color3, (500, 450, 1, 50), 5)
        a19 = pygame.draw.rect(screen, color3, (550, 150, 1, 100), 5)
        a20 = pygame.draw.rect(screen, color3, (550, 300, 1, 50), 5)
        a21 = pygame.draw.rect(screen, color3, (600, 150, 1, 200), 5)
        a22 = pygame.draw.rect(screen, color3, (650, 150, 1, 100), 5)
        a23 = pygame.draw.rect(screen, color3, (650, 400, 1, 100), 5)
        a24 = pygame.draw.rect(screen, color3, (700, 50, 1, 150), 5)
        a25 = pygame.draw.rect(screen, color3, (700, 250, 1, 100), 5)
        a26 = pygame.draw.rect(screen, color3, (750, 100, 1, 50), 5)
        a27 = pygame.draw.rect(screen, color3, (750, 200, 1, 150), 5)

        b1 = pygame.draw.rect(screen, color3, (50, 550, 150, 1), 5)
        b2 = pygame.draw.rect(screen, color3, (250, 550, 500, 1), 5)
        b3 = pygame.draw.rect(screen, color3, (50, 500, 50, 1), 5)
        b4 = pygame.draw.rect(screen, color3, (150, 500, 300, 1), 5)
        b5 = pygame.draw.rect(screen, color3, (500, 500, 300, 1), 5)
        b6 = pygame.draw.rect(screen, color3, (500, 450, 100, 1), 5)
        b7 = pygame.draw.rect(screen, color3, (200, 450, 100, 1), 5)
        b8 = pygame.draw.rect(screen, color3, (450, 400, 200, 1), 5)
        b9 = pygame.draw.rect(screen, color3, (700, 400, 100, 1), 5)
        b10 = pygame.draw.rect(screen, color3, (650, 350, 50, 1), 5)
        b11 = pygame.draw.rect(screen, color3, (550, 350, 50, 1), 5)
        b12 = pygame.draw.rect(screen, color3, (450, 350, 50, 1), 5)
        b13 = pygame.draw.rect(screen, color3, (250, 350, 50, 1), 5)
        b14 = pygame.draw.rect(screen, color3, (200, 300, 150, 1), 5)
        b15 = pygame.draw.rect(screen, color3, (500, 300, 50, 1), 5)
        b16 = pygame.draw.rect(screen, color3, (650, 250, 50, 1), 5)
        b17 = pygame.draw.rect(screen, color3, (300, 250, 100, 1), 5)
        b18 = pygame.draw.rect(screen, color3, (200, 200, 50, 1), 5)
        b19 = pygame.draw.rect(screen, color3, (350, 200, 100, 1), 5)
        b20 = pygame.draw.rect(screen, color3, (700, 200, 50, 1), 5)
        b21 = pygame.draw.rect(screen, color3, (750, 150, 50, 1), 5)
        b22 = pygame.draw.rect(screen, color3, (550, 150, 50, 1), 5)
        b23 = pygame.draw.rect(screen, color3, (400, 150, 100, 1), 5)
        b24 = pygame.draw.rect(screen, color3, (200, 150, 100, 1), 5)
        b25 = pygame.draw.rect(screen, color3, (200, 100, 150, 1), 5)
        b26 = pygame.draw.rect(screen, color3, (400, 100, 300, 1), 5)
        b27 = pygame.draw.rect(screen, color3, (750, 100, 50, 1), 5)
        b28 = pygame.draw.rect(screen, color3, (350, 50, 450, 1), 5)
        b29 = pygame.draw.rect(screen, color3, (200, 50, 50, 1), 5)

        prize = pygame.draw.rect(screen, color42, (419, 117, 20, 20), 5)

        if x >= 800 or x < 0 or y >= 600 or y < 0:
            win1(screen)
        elif d >= 800 or d < 0 or s >= 600 or s < 0:
            win2(screen)
        elif prize.colliderect(man):
            win4(screen)
        elif prize.colliderect(man2):
            win3(screen)
        elif a1.colliderect(man):
            win1(screen)
        elif a2.colliderect(man):
            win1(screen)
        elif a3.colliderect((man)):
            win1(screen)
        elif a4.colliderect((man)):
            win1(screen)
        elif a5.colliderect((man)):
            win1(screen)
        elif a6.colliderect((man)):
            win1(screen)
        elif a7.colliderect((man)):
            win1(screen)
        elif a8.colliderect((man)):
            win1(screen)
        elif a9.colliderect((man)):
            win1(screen)
        elif a10.colliderect((man)):
            win1(screen)
        elif a11.colliderect((man)):
            win1(screen)
        elif a12.colliderect((man)):
            win1(screen)
        elif a13.colliderect((man)):
            win1(screen)
        elif a14.colliderect((man)):
            win1(screen)
        elif a15.colliderect((man)):
            win1(screen)
        elif a16.colliderect((man)):
            win1(screen)
        elif a17.colliderect((man)):
            win1(screen)
        elif a18.colliderect((man)):
            win1(screen)
        elif a19.colliderect((man)):
            win1(screen)
        elif a20.colliderect((man)):
            win1(screen)
        elif a21.colliderect((man)):
            win1(screen)
        elif a22.colliderect((man)):
            win1(screen)
        elif a23.colliderect((man)):
            win1(screen)
        elif a24.colliderect((man)):
            win1(screen)
        elif a25.colliderect((man)):
            win1(screen)
        elif a26.colliderect((man)):
            win1(screen)
        elif a27.colliderect((man)):
            win1(screen)

        elif a1.colliderect(man2):
            win2(screen)
        elif a2.colliderect(man2):
            win2(screen)
        elif a3.colliderect((man2)):
            win2(screen)
        elif a4.colliderect((man2)):
            win2(screen)
        elif a5.colliderect((man2)):
            win2(screen)
        elif a6.colliderect((man2)):
            win2(screen)
        elif a7.colliderect((man2)):
            win2(screen)
        elif a8.colliderect((man2)):
            win2(screen)
        elif a9.colliderect((man2)):
            win2(screen)
        elif a10.colliderect((man2)):
            win2(screen)
        elif a11.colliderect((man2)):
            win2(screen)
        elif a12.colliderect((man2)):
            win2(screen)
        elif a13.colliderect((man2)):
            win2(screen)
        elif a14.colliderect((man2)):
            win2(screen)
        elif a15.colliderect((man2)):
            win2(screen)
        elif a16.colliderect((man2)):
            win2(screen)
        elif a17.colliderect((man2)):
            win2(screen)
        elif a18.colliderect((man2)):
            win2(screen)
        elif a19.colliderect((man2)):
            win2(screen)
        elif a20.colliderect((man2)):
            win2(screen)
        elif a21.colliderect((man2)):
            win2(screen)
        elif a22.colliderect((man2)):
            win2(screen)
        elif a23.colliderect((man2)):
            win2(screen)
        elif a24.colliderect((man2)):
            win2(screen)
        elif a25.colliderect((man2)):
            win2(screen)
        elif a26.colliderect((man2)):
            win2(screen)
        elif a27.colliderect((man2)):
            win2(screen)
        elif b1.colliderect((man)):
            win1(screen)
        elif b2.colliderect((man)):
            win1(screen)
        elif b3.colliderect((man)):
            win1(screen)
        elif b4.colliderect((man)):
            win1(screen)
        elif b5.colliderect((man)):
            win1(screen)
        elif b6.colliderect((man)):
            win1(screen)
        elif b7.colliderect((man)):
            win1(screen)
        elif b8.colliderect((man)):
            win1(screen)
        elif b9.colliderect((man)):
            win1(screen)
        elif b10.colliderect((man)):
            win1(screen)
        elif b11.colliderect((man)):
            win1(screen)
        elif b12.colliderect((man)):
            win1(screen)
        elif b13.colliderect((man)):
            win1(screen)
        elif b14.colliderect((man)):
            win1(screen)
        elif b15.colliderect((man)):
            win1(screen)
        elif b16.colliderect((man)):
            win1(screen)
        elif b17.colliderect((man)):
            win1(screen)
        elif b18.colliderect((man)):
            win1(screen)
        elif b19.colliderect((man)):
            win1(screen)
        elif b20.colliderect((man)):
            win1(screen)
        elif b21.colliderect((man)):
            win1(screen)
        elif b22.colliderect((man)):
            win1(screen)
        elif b23.colliderect((man)):
            win1(screen)
        elif b24.colliderect((man)):
            win1(screen)
        elif b25.colliderect((man)):
            win1(screen)
        elif b26.colliderect((man)):
            win1(screen)
        elif b27.colliderect((man)):
            win1(screen)
        elif b28.colliderect((man)):
            win1(screen)
        elif b29.colliderect((man)):
            win1(screen)
        elif b1.colliderect((man2)):
            win2(screen)
        elif b2.colliderect((man2)):
            win2(screen)
        elif b3.colliderect((man2)):
            win2(screen)
        elif b4.colliderect((man2)):
            win2(screen)
        elif b5.colliderect((man2)):
            win2(screen)
        elif b6.colliderect((man2)):
            win2(screen)
        elif b7.colliderect((man2)):
            win2(screen)
        elif b8.colliderect((man2)):
            win2(screen)
        elif b9.colliderect((man2)):
            win2(screen)
        elif b10.colliderect((man2)):
            win2(screen)
        elif b11.colliderect((man2)):
            win2(screen)
        elif b12.colliderect((man2)):
            win2(screen)
        elif b13.colliderect((man2)):
            win2(screen)
        elif b14.colliderect((man2)):
            win2(screen)
        elif b15.colliderect((man2)):
            win2(screen)
        elif b16.colliderect((man2)):
            win2(screen)
        elif b17.colliderect((man2)):
            win2(screen)
        elif b18.colliderect((man2)):
            win2(screen)
        elif b19.colliderect((man2)):
            win2(screen)
        elif b20.colliderect((man2)):
            win2(screen)
        elif b21.colliderect((man2)):
            win2(screen)
        elif b22.colliderect((man2)):
            win2(screen)
        elif b23.colliderect((man2)):
            win2(screen)
        elif b24.colliderect((man2)):
            win2(screen)
        elif b25.colliderect((man2)):
            win2(screen)
        elif b26.colliderect((man2)):
            win2(screen)
        elif b27.colliderect((man2)):
            win2(screen)
        elif b28.colliderect((man2)):
            win2(screen)
        elif b29.colliderect((man2)):
            win2(screen)

        pygame.display.update()
    pygame.quit()


def main():
    size = width, height = 800, 600
    running = True
    pygame.init()

    pygame.display.set_caption('Игра')
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    draw0(screen)
    draw(screen)
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()


if __name__ == '__main__':
    main()
