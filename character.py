import pygame 
from entity import Entity

class Character(Entity):
    def __init__(self, game, width, height, x, y, speed, image_path, dead_image_path, lives=3):
        super().__init__(game, width, height, x, y, speed, image_path)
        self.dead = False
        self.dead_image = pygame.image.load(dead_image_path)
        self.lives = lives
        self.is_alive = self.lives > 0

    def move(self, dx=0, dy=0):
        if self.is_alive:
            super().move(dx, dy)

    def shoot(self):
        print(f"{self} disparó un proyectil.")

    def collide(self, other):
        return self.rect.colliderect(other.rect)

    def collide_with_opponent(self):
        self.die()

    def collide_with_player(self):
        self.die()
        pygame.time.set_timer(pygame.USEREVENT, 2000)

    def die(self):
        self.lives -= 1
        self.is_alive = self.lives > 0
        if not self.is_alive:
            self.dead = True

    def render(self):
        if self.dead:
            self.game.screen.blit(self.dead_image, (self.x, self.y))
        else:
            super().draw()

    def __str__(self):
        return super().__str__() + f' (CHARACTER, Lives: {self.lives})'
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return super().__eq__(other)
    
    def __hash__(self):
        return super().__hash__()