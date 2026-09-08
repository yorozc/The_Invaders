import pygame
import os
import random
import time
import sys
from entities.player import Player
from entities.enemy import Enemy

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

# initialize variables 

SIZE = 30 # char size
MAX_WIDTH = WINDOW_WIDTH - SIZE
MAX_HEIGHT = WINDOW_HEIGHT - SIZE
x = WINDOW_WIDTH / 2 - SIZE
y = WINDOW_HEIGHT * 0.75

# =====Player init=====
p1 = Player(x, 400, SIZE, SIZE, (255,255,255), 100, 5)

# =====Enemy inits=====
bullets = []
enemies_basic = [Enemy(x, 60, SIZE, SIZE, (0, 255, 0), 100, 1, bullets), Enemy(x - 60, 80, SIZE, SIZE, (0, 255, 0), 100, 1, bullets), Enemy(x + 60 , 80, SIZE, SIZE, (0, 255, 0), 100, 1, bullets)]


# main game loop
while True:
    # check for and handle events
    for event in pygame.event.get():
        # click close, quit pygame and program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                p1.add_bullet()
    
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

    p1.move(dx, dy) # updates player movement

    # gets rid of enemy if they go past the screen
    enemies_basic = [enemy for enemy in enemies_basic if enemy.rect.top < WINDOW_HEIGHT]    

    #clear window every tick
    window.fill(BLACK)

    # player bullet
    p1.shoot(window)

    # ===enemy functions===
    for enemy in enemies_basic:
        enemy.draw(window)
        enemy.shoot(window, WINDOW_HEIGHT)

    # draw all window elements
    p1.draw(window)
    
    # keep player in bounds
    p1.rect.clamp_ip(surf_window)
    p1.check_bounds()

    # update window
    pygame.display.update()

    clock.tick(FPS)