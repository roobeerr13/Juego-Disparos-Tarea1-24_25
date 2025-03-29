import pygame
from opponent import Opponent

class Boss(Opponent):
    def __init__(self, game):
        super().__init__(game)
        self.speed *= 2 
        self.image = pygame.image.load('assets/jefe.png')
        self.dead_image = pygame.image.load('assets/jefe_muerto.png')

    def update(self):
        super().update()
        if self.rect.right < 0:
            self.kill()
            self.game.game_over()
    
    def __str__(self):
        return super().__str__() + ' (BOSS)'