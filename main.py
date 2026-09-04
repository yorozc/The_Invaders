import pygame
import os
import random
import time

import pygame
from pygame import Rect
import sys

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
player_rect = pygame.Rect(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, SIZE, SIZE)

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
    if keys[pygame.K_LEFT] or keys[pygame.K_a]: player_rect.x -= SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]: player_rect.x += SPEED
    if keys[pygame.K_UP] or keys[pygame.K_w]: player_rect.y -= SPEED
    if keys[pygame.K_DOWN] or keys[pygame.K_s]: player_rect.y += SPEED 

    #clear window every tick
    window.fill(BLACK)

    # draw all window elements
    pygame.draw.rect(window, (255,255,255), player_rect)

    # keep rect in bounds
    player_rect.clamp_ip(surf_window)

    # update window
    pygame.display.update()

    clock.tick(FPS)