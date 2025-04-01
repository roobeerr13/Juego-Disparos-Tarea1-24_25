from opponent import Opponent
import pygame

class Boss(Opponent):
    def __init__(self, game):
        super().__init__(game)
        self.speed *= 2  # El jefe se mueve el doble de rápido
        self.image = pygame.image.load('assets/jefe.png')
        self.dead_image = pygame.image.load('assets/jefe_muerto.png')