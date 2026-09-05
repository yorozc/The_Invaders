import pygame
from entities.entity import Entity
class Player(Entity):

    def __init__(self,  x, y, width, height, color, health, move_speed):
        super().__init__(x, y, width, height, color, health, move_speed)
        self.projectile_speed = 5
        self.inventory = {}
        self.bullets = []
        self.build_rect()


    def check_bounds(self):
        max_player_height = 400
        if self.rect.y >= max_player_height:
            self.rect.y = max_player_height 

    def move(self, dx, dy):
        self.rect.x += dx * self.move_speed
        self.rect.y += dy * self.move_speed

    def add_bullet(self):
        bullet = pygame.Rect(self.rect.center[0], self.rect.center[1], 10, 10)
        self.bullets.append(bullet)

    def shoot(self, surface):
        for bullet in self.bullets:
            bullet.y -= self.projectile_speed
            pygame.draw.ellipse(surface, (255, 0, 0), bullet)
            if bullet.y < 0:
                self.bullets.remove(bullet)

    def add_to_inv(self):
        pass

    def view_inv(self):
        pass
        