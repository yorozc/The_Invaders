import pygame
from pygame import Rect

class Entity:

    def __init__(self, x, y, width, height, color, health, move_speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.health = health
        self.move_speed = move_speed
        self.build_rect()

    def build_rect(self) -> Rect:
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)

    def is_alive(self):
        return self.health > 0