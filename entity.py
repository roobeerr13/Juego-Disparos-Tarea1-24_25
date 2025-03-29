import pygame

class Entity:
    def __init__(self, game, width, height, x, y, speed, image_path):
        self.game = game
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))