import pygame 
from entity import Entity

class Character(Entity):
    def __init__(self, game, width, height, x, y, speed, image_path, dead_image_path):
        super().__init__(game, width, height, x, y, speed, image_path)
        self.dead = False
        self.dead_image = pygame.image.load(dead_image_path)

    def collide(self, other):
        return self.rect.colliderect(other.rect)

    def collide_with_opponent(self):
        self.dead = True

    def collide_with_player(self):
        self.dead = True
        pygame.time.set_timer(pygame.USEREVENT, 2000)

    def die(self):
        self.dead = True

    def render(self):
        if self.dead:
            self.game.screen.blit(self.dead_image, (self.x, self.y))
        else:
            super().render()

    def __str__(self):
        return super().__str__() + ' (CHARACTER)'
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return super().__eq__(other)
    
    def __hash__(self):
        return super().__hash__()