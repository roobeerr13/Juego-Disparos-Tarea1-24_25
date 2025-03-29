import pygame
import os
from entity import Entity

class Character(Entity):
    def __init__(self, game, width, height, x, y, speed, image_path, dead_image_path):
        super().__init__(game, width, height, x, y, speed, image_path)
        # Cargamos la imagen de "muerto" usando rutas absolutas
        self.dead_image = pygame.image.load(dead_image_path)
    def render(self):
        if self.dead:
            self.game.screen.blit(self.dead_image, (self.x, self.y))
        else:
            super().draw()