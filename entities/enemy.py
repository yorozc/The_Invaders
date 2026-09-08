import pygame
import time
from entities.entity import Entity
class Enemy(Entity):

    def __init__(self,  x, y, width, height, color, health, move_speed, bullets):
        super().__init__(x, y, width, height, color, health, move_speed)
        self.projectile_speed = 2
        self.shoot_cooldown = 2000
        self.last_shot_time = 0
        self.start_time_move = 0
        self.bullets = bullets

    def update(self):
        pass
        
    def move(self):
        duration = 5
        
        if self.rect.y != 200 :
            self.start_time_move = time.time()
            self.rect.y += self.move_speed

        if time.time() - self.start_time_move >= duration:
            self.rect.y += self.move_speed

    def add_bullet(self):
        self.last_shot_time = pygame.time.get_ticks()
        bullet = pygame.Rect(self.rect.centerx, self.rect.centery, 10, 10)
        self.bullets.append(bullet)

    def update_bullet(self, surface, window_height):
        if pygame.time.get_ticks() - self.last_shot_time >= self.shoot_cooldown:
            self.add_bullet()

        for bullet in self.bullets:
            bullet.y += self.projectile_speed
            pygame.draw.ellipse(surface, (0, 0, 255), bullet)
            if bullet.y > window_height:
                self.bullets.remove(bullet)

        print(self.bullets)

        