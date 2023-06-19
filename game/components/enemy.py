import pygame, random

from pygame.sprite import Sprite

from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy(Sprite):
    def __init__ (self):
        self.width = 40
        self.height = 50
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH-self.width)
        self.rect.y = 0
        self.speed = 10

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def motion_vertical(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -self.height
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.width)

    def update(self):
        self.motion_vertical()