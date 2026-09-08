import pygame
from entities.entity import Entity
class Player(Entity):

    def __init__(self,  x, y, width, height, color, health, move_speed):
        super().__init__(x, y, width, height, color, health, move_speed)
        self.projectile_speed = 5
        self.inventory = {}
        self.bullets = [] 

    def update(self, dx, dy, surface, bullet_list):
        self.move(dx, dy)
        self.update_bullet()
        self.enemy_bullet_collision(bullet_list)
        print(self.health)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        for bullet in self.bullets:
            pygame.draw.ellipse(surface, (255, 0, 0), bullet)

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

    def update_bullet(self):
        for bullet in self.bullets[:]:
            bullet.y -= self.projectile_speed
            if bullet.y < 0:
                self.bullets.remove(bullet)

    def enemy_bullet_collision(self, bullet_list):
        if self.rect.collidelistall(bullet_list):
            self.health -= 5

    def add_to_inv(self):
        pass

    def view_inv(self):
        pass
        