import pygame
import os
from character import Character

class Opponent(Character):
    def __init__(self, game):
        width = int(game.width * 0.05)
        height = int(game.height * 0.05)
        x = game.width // 2 - width // 2
        y = 0
        speed = 3
        image_path = os.path.join(os.getcwd(), 'assets/malo.png')
        dead_image_path = os.path.join(os.getcwd(), 'assets/malo_muerto.png')
        super().__init__(game, width, height, x, y, speed, image_path, dead_image_path)

    def update(self):
        self.y += self.speed
        if self.y > self.game.height:
            self.y = 0
        self.rect.topleft = (self.x, self.y)