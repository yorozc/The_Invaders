import pygame
import os
import random
import time
import sys
from entities.player import Player
from entities.enemy import Enemy
from menus.start_menu import Start_Menu
from menus.button import Button

# define constants
BLACK = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 60
SPEED = 5

# initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
surf_window = window.get_rect()
clock = pygame.time.Clock()

# load assets
# 279x126
start_img = pygame.image.load('assets/start_btn.png').convert_alpha()
# 240x126
exit_img = pygame.image.load('assets/exit_btn.png').convert_alpha()

# initialize variables 

SIZE = 30 # char size
MAX_WIDTH = WINDOW_WIDTH - SIZE
MAX_HEIGHT = WINDOW_HEIGHT - SIZE
x = WINDOW_WIDTH / 2 - SIZE
y = WINDOW_HEIGHT * 0.75
FONT = pygame.font.SysFont("arialblack", 40)
GAME_STATE = "start_menu"
start_menu = Start_Menu()
start_button = Button((640-279) / 2, 100, start_img, 1)
exit_btn = Button((640-240) / 2, 250, exit_img, 1)

# =====Player init=====
p1 = Player(x, 400, SIZE, SIZE, (255,255,255), 100, 5)

# =====Enemy inits=====
enemy_bullets = []
enemies_basic = [Enemy(x, 60, SIZE, SIZE, (0, 255, 0), 100, 1, enemy_bullets), Enemy(x - 60, 80, SIZE, SIZE, (0, 255, 0), 100, 1, enemy_bullets), Enemy(x + 60 , 80, SIZE, SIZE, (0, 255, 0), 100, 1, enemy_bullets)]


# main game loop
while True:
    # check for and handle events
    for event in pygame.event.get():
        # click close, quit pygame and program
        if event.type == pygame.QUIT or GAME_STATE == "quit":
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                p1.add_bullet()

            elif event.key == pygame.K_ESCAPE:
                GAME_STATE = "start_menu"

    if GAME_STATE == "start_menu":
        window.fill(BLACK)

        start_menu.draw_text("The Invaders", FONT, (255, 255, 255), 160, 25, window)

        if start_button.draw(window):
            GAME_STATE = "game"

        if exit_btn.draw(window):
            GAME_STATE = "quit"

    elif GAME_STATE == "game":

        # do any "per frame" actions
        keys = pygame.key.get_pressed()
        dx, dy= 0,0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: dx += -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: dx += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]: dy += -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: dy += 1

        # ===movement===
        for enemy in enemies_basic:
            enemy.move()

        p1.update(dx, dy, window, enemy_bullets) # updates player movement

        # gets rid of enemy if they go past the screen
        enemies_basic = [enemy for enemy in enemies_basic if enemy.rect.top < WINDOW_HEIGHT]    

        #clear window every tick
        window.fill(BLACK)

        # ===enemy functions===
        for enemy in enemies_basic:
            enemy.draw(window)
            enemy.update_bullet(window, WINDOW_HEIGHT) # temp

        # draw all window elements
        p1.draw(window)
        
        # keep player in bounds
        p1.rect.clamp_ip(surf_window)
        p1.check_bounds()

        # update window
    pygame.display.update()

    clock.tick(FPS)