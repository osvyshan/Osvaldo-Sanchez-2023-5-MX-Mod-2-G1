import pygame
import random

from game.components.enemies.enemy import Enemy
from game.components.bullet.basic_bullet import BasicBullet
from game.utils.constants import ENEMY_1, BULLET

class EnemyShip(Enemy):
    WIDTH = 40
    HEIGHT = 60
    
    def __init__(self):
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)

    def shoot(self):
        if self.shoot_interval <= 0:
            self.enemy_bullet = BasicBullet(self.rect.center, BULLET)
            self.shoot_interval = random.randint(10, 50 )  # Intervalo de tiempo aleatorio entre disparos
        else:
            self.shoot_interval -= 1 