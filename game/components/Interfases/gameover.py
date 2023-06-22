import pygame
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.enemies.enemy_handler import EnemyHandler

class GameOverScreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.enemy_handler = EnemyHandler(self)
        self.score = 0

    def update_go_screen(self):
        self.score = self.enemy_handler.score
        image = pygame.image.load("E:/INDEX/PROGRAMACION/Osvaldo-Sanchez-2023-5-MX-Mod-2-G1/game/assets/Other/GAMEOVER.png")
        image_rect = image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)) # crea un rectangulo y lo posisiona en el centro
        self.screen.blit(image, image_rect) # Muestra la imagen en el centro
    
        font = pygame.font.Font(None, 36)
        #score_text = font.render("Score: " + str(self.enemy_handler.score), True, (255, 255, 255))
        #score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        #self.screen.blit(score_text, score_rect)
    
        continue_text = font.render("Press Enter to Restart", True, (255, 255, 255))
        continue_rect = continue_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        self.screen.blit(continue_text, continue_rect)
    
        pygame.display.flip()
    
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False   