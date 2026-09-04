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

    def build_rect(self) -> Rect:
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        return self.rect

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)