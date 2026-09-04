import pygame
from entities.entity import Entity
class Enemy(Entity):

    def __init__(self,  x, y, width, height, color, health, move_speed):
        super().__init__(x, y, width, height, color, health, move_speed)