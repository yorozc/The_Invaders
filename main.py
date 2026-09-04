import pygame
import os
import random
import time
import sys
from entities.player import Player

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
x = WINDOW_WIDTH / 2
y = WINDOW_HEIGHT / 2 
p1 = Player(x, y, SIZE, SIZE, (255,255,255), 100, 5)

# main game loop
while True:
    # check for and handle events
    for event in pygame.event.get():
        # click close, quit pygame and program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # do any "per frame" actions
    keys = pygame.key.get_pressed()
    dx, dy= 0,0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]: dx += -1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]: dx += 1
    if keys[pygame.K_UP] or keys[pygame.K_w]: dy += -1
    if keys[pygame.K_DOWN] or keys[pygame.K_s]: dy += 1

    p1.move(dx, dy)

    #clear window every tick
    window.fill(BLACK)

    # draw all window elements
    p1.draw(window)

    # keep rect in bounds
    p1.rect.clamp_ip(surf_window)

    # update window
    pygame.display.update()

    clock.tick(FPS)