import random
from game.components.spaceship import Spaceship

class Shield:
    def __init__(self):
        self.inventory = []
        
        self.spaceship = Spaceship()

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
        if 'shield' in self.inventory:
            self.inventory.remove('shield')
            print ("Inventory:", self.inventory)
            self.spaceship.use_shield()

   #def update(self, keyboard_events):
       # if keyboard_events[pygame.K_q]:
        #    self.remove_shield()
       #     print ("q")
            
    
