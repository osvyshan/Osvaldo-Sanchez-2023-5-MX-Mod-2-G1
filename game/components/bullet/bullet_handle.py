import pygame
from game.components.spaceship import Spaceship

class shoting:
    
    def __init__(self) -> None:
           self.spaceship = Spaceship() 
    
    def shoot(self, keyboard_event):
        if keyboard_event[pygame.K_SPACE] == True:
            self.spaceship.shoot()

        elif keyboard_event[pygame.K_SPACE] == False:
             pass
