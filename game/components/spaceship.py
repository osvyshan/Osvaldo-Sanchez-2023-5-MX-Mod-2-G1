import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH


class Spaceship(Sprite):
    def __init__(self):
        self.width = 40
        self.height = 50
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = pygame.rect
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y =  SCREEN_HEIGHT - self.height
        self.speed = 10

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move_left(self, keyboard_events):   
        if keyboard_events[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed

    def move_right(self, keyboard_events):
        if keyboard_events[pygame.K_d] and self.rect.x < SCREEN_WIDTH - self.width:
            self.rect.x += self.speed
    
    def move_up(self, keyboard_events):
        if keyboard_events[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

    def move_down(self, keyboard_events):
        if keyboard_events[pygame.K_s] and self.rect.y < SCREEN_HEIGHT - self.height:
            self.rect.y += self.speed

    def update(self, keyboard_events):
        self.move_left(keyboard_events)
        self.move_right(keyboard_events)
        self.move_up(keyboard_events)
        self.move_down(keyboard_events)