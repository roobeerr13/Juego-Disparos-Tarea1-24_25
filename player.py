import pygame
import os
from character import Character

class Player(Character):
    def __init__(self, game):
        width = int(game.width * 0.05)
        height = int(game.height * 0.05)
        x = game.width // 2 - width // 2
        y = game.height - height
        speed = 5
        image_path = os.path.join(os.getcwd(), 'assets/bueno.png')
        dead_image_path = os.path.join(os.getcwd(), 'assets/bueno_muerto.png')
        super().__init__(game, width, height, x, y, speed, image_path, dead_image_path)

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < self.game.width - self.width:
            self.x += self.speed
        self.rect.topleft = (self.x, self.y)