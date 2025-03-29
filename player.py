import pygame
from character import Character

class Player(Character):
    def __init__(self, game):
        width = int(game.width * 0.05)
        height = int(game.height * 0.05)
        x = game.width // 2 - width // 2
        y = game.height - height
        speed = 5
        image_path = 'assets/bueno.png'
        dead_image_path = 'assets/bueno_muerto.png'
        super().__init__(game, width, height, x, y, speed, image_path, dead_image_path)
        self.lives = 3

    def update(self, keys):
        if not self.dead:
            if keys[pygame.K_LEFT] and self.x > 0:
                self.x -= self.speed
            if keys[pygame.K_RIGHT] and self.x < self.game.width - self.width:
                self.x += self.speed
            if keys[pygame.K_SPACE]:
                self.game.shoot(self)

    def die(self):
        super().die()
        self.lives -= 1
        if self.lives == 0:
            self.game.game_over()
        else:
            self.x = self.game.width // 2 - self.width // 2
            self.y = self.game.height - self.height
        
    def __str__(self):
        return super().__str__() + ' (PLAYER)'