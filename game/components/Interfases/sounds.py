import pygame.mixer

class SoundPlayer:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('E:/INDEX/PROGRAMACION/Osvaldo-Sanchez-2023-5-MX-Mod-2-G1/game/assets/Sounds/Explosion.mp3')

    def play_sound(self):
        pygame.mixer.music.play(1)
