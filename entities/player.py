import pygame
from entities.entity import Entity
class Player(Entity):

    def __init__(self,  x, y, width, height, color, health, move_speed):
        super().__init__(x, y, width, height, color, health, move_speed)
        self.inventory = {}
        self.build_rect()

    def move(self, dx, dy):
        self.rect.x += dx * self.move_speed
        self.rect.y += dy * self.move_speed

    def add_to_inv(self):
        pass

    def view_inv(self):
        pass
        