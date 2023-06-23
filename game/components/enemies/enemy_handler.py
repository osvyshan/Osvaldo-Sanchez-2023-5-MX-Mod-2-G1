import pygame
import random
from game.components.enemies.enemy_ship import EnemyShip
from game.components.interfases.sounds import SoundPlayer
from game.components.spaceship import Spaceship
from game.components.bullet.basic_bullet import BasicBullet
from game.utils.constants import BULLET
from game.utils.constants import ENEMY_1

class EnemyHandler:
    MAX_ENEMIES = 4

    def __init__(self, player):
        self.enemies = []
        self.enemies.append(EnemyShip())
        self.player = player
        self.bullet = None
        self.image = ENEMY_1
        self.rect = self.image.get_rect()
        self.shoot_interval = 0
        self.score = 0
        self.sound_player = SoundPlayer()
        self.spaceship = Spaceship() 
        self.invulnerable = False
        self.shield_durability = 3
        self.inventory = []



    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update()
            if not enemy.is_alive:
                self.remove_enemy(enemy)
            
            if self.player.bullet is not None:   #si la bala existe 
                if self.player.bullet.collides_with_enemy(enemy):
                    enemy.is_alive = False
                    self.shield_spawn()
                    print("Enemy Colition")
                    self.sound_player.play_sound()
                    self.player.bullet = None  
                    self.score += 100
                    print("Score:",self.score)

            if enemy.enemy_bullet is not None:
                enemy.enemy_bullet.update_enemy()

                if enemy.enemy_bullet.rect.colliderect(self.player.rect) and self.invulnerable == True:
                    print("colition Bloked")
                    enemy.enemy_bullet = None 
                    self.player.num_collisions += 0
                    self.shield_durability -= 1
                    print(self.player.num_collisions)
                    enemy.enemy_bullet = None

                elif enemy.enemy_bullet.rect.colliderect(self.player.rect) and self.invulnerable == False:
                    print("Spaceship Colition")
                    enemy.enemy_bullet = None  
                    self.player.num_collisions += 1
                    print(self.player.num_collisions)
                    enemy.enemy_bullet = None

        if self.shield_durability == 0:
            self.invulnerable = False
            self.shield_durability +=3
                

        if self.player.num_collisions >= 3:
            self.playing = False    

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
            if enemy.enemy_bullet is not None:
                enemy.enemy_bullet.draw(screen)
            
    def use_shield(self):
        self.invulnerable = True  
        print("Eres invulnerable")
        print(self.invulnerable)

    def add_enemy(self):
        if len(self.enemies) < self.MAX_ENEMIES:
            self.enemies.append(EnemyShip())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def lose_game(self):
        if self.player.num_collisions >= 3:
            return False
        else:
            return True 

    def shoot(self):
        if self.shoot_interval <= 0:
            self.enemy_bullet = BasicBullet(self.rect.center, BULLET)
            self.shoot_interval = random.randint(10, 50 )  # Intervalo de tiempo aleatorio entre disparos
        else:
            self.shoot_interval -= 1

    def shield_spawn(self):                 #Se encarga de dropear el item shield
        numero = random.randint(1,10)
        if numero % 2 == 0:
            self.inventory.append('shield')
            print (numero)
            print("powerup droped")
            print(self.inventory)
        else:
            print("nothing here")

    def remove_shield(self):
            print ("Inventory:", self.inventory)
            self.use_shield()