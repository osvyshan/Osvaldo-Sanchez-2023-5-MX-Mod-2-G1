import pygame
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.components.spaceship import Spaceship
from game.components.interfases.gameover import GameOverScreen
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.interfases.sounds import SoundPlayer


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10 # el numero de pixeles que el "objeto / imagen" se mueve en patalla
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.spaceship = Spaceship()
        self.enemy_handler = EnemyHandler(self.spaceship)
        self.soundplayer = SoundPlayer()
        self.gameoverscreen = GameOverScreen()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing and self.enemy_handler.lose_game():
            self.handle_events()
            self.update()
            self.draw()
            
        pygame.display.quit()
        pygame.quit()

    def handle_events(self):
        # pygame.event.get() es un iterable (lista)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #el QUIT event es el click en el icono que cierra ventana
                self.playing = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.enemy_handler.shoot()
                    self.spaceship.shoot()
                    self.soundplayer.play_sound()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    pass

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.enemy_handler.remove_shield()
                    print("se apreto la Q")

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    print("se desapreto la Q")    
            

    def update(self):
        events = pygame.key.get_pressed()
        self.spaceship.update(events)
        self.enemy_handler.update()
       

    def draw(self):
        self.clock.tick(FPS) # configuro cuantos frames per second voy a dibujar
        if not self.enemy_handler.lose_game():
                self.gameoverscreen.update_go_screen()
                self.spaceship.num_collisions = 0
                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                waiting = False
                                self.enemy_handler = EnemyHandler(self.spaceship)  # Reiniciar los enemigos
                                self.playing = True
        self.screen.fill((255, 255, 255)) # lleno el screen de color BLANCO???? 255, 255, 255 es el codigo RGB
        
        self.draw_background()
     
        self.spaceship.draw(self.screen)
        self.enemy_handler.draw(self.screen)

        pygame.display.update() # esto hace que el dibujo se actualice en el display de pygame
        pygame.display.flip()  # hace el cambio

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()# alto de la imagen
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg)) # blit "dibuja"
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed     