import pygame
import time
from entities.entity import Entity
class Enemy(Entity):

    def __init__(self,  x, y, width, height, color, health, move_speed):
        super().__init__(x, y, width, height, color, health, move_speed)
        self.start_time = 0

    def move(self, window_height):
        duration = 5
        
        if self.rect.y != 200 :
            self.start_time = time.time()
            self.rect.y += self.move_speed

        if time.time() - self.start_time >= duration:
            self.rect.y += self.move_speed

        self.attack()

    def attack(self):
        print('Enemy shoot')