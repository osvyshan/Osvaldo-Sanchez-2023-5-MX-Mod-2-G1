import pygame
from pygame.sprite import Sprite

class BasicBullet(Sprite):
    def __init__(self, location, sprite):
        self.image = pygame.transform.scale(sprite, (30, 40))
        self.rect = self.image.get_rect()
        self.speed = 35
        self.speed_enemy = 30
        self.rect.center = location

    def update(self):
        self.rect.y -= self.speed #Actualiza la posición de la bala arriba eje Y

    def update_enemy(self):
        self.rect.y += self.speed_enemy #Actualiza la posición de la bala enemiga abajo eje Y.

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def collides_with_enemy(self, enemy):
        return self.rect.colliderect(enemy.rect)   
