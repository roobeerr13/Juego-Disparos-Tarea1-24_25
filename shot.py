import pygame
from entity import Entity
from player import Player

class Shot(Entity):
    def __init__(self, game, character):
        width = int(game.width * 0.015)
        height = int(game.height * 0.015)
        x = character.x + character.width // 2 - width // 2
        y = character.y
        speed = 10
        image_path = 'assets/shot1.png' if isinstance(character, Player) else 'assets/shot2.png'
        super().__init__(game, width, height, x, y, speed, image_path)

    def move(self):
        if isinstance(self.game.player, Player):
            self.y -= self.speed 
        else:
            self.y += self.speed
        self.rect.topleft = (self.x, self.y)

    def hit_target(self, target):
        if self.rect.colliderect(target.rect):
            target.die() 
            if isinstance(self.game.player, Player):
                self.game.player_shots.remove(self) 
            else:
                self.game.opponent_shots.remove(self) 

    def update(self):
        self.move() 
        if self.y < 0 or self.y > self.game.height:
            if isinstance(self.game.player, Player):
                self.game.player_shots.remove(self)
            else:
                self.game.opponent_shots.remove(self)

    def __str__(self):
        return super().__str__() + ' (SHOT)'